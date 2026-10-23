"""Canonical source-to-reader teaching revision. This module removes generic
roadmaps, expands actual arithmetic, and renders one shared practice answer.
"""
from pathlib import Path
from fractions import Fraction as F
import re,json,html,hashlib,copy
from mathml import inline,matrix
from beginner_math import para,display,mat,stage,final,render_nodes,product_nodes,array_expr,serializable,CHECKS,signed_sum,par
from beginner_prose import author_paragraph,transform,key,render_paragraph
from authored_lessons import PRACTICE,CONVERSION,P,S,D,M,A
from learning import answer_map,practice_label,classify,table
from workbook_teaching import SUPPLEMENTS,REPLACEMENTS
from proof_contexts import CONTEXT as PROOF_CONTEXT,FINAL as PROOF_FINAL
ROOT=Path(__file__).resolve().parent.parent
MANUSCRIPT={'schema':2,'paragraphs':{},'practice':{},'exercises':{},'chapter_lessons':{}}
EDITED=json.loads((ROOT/'source/teaching/beginner-content.json').read_text()) if (ROOT/'source/teaching/beginner-content.json').exists() else {}
if EDITED.get('schema')==2:
 MANUSCRIPT['paragraphs']={k:v for k,v in EDITED.get('paragraphs',{}).items() if not re.match(r'^\*\*[A-Z]\d+',v.get('source',''))}
 for id,record in EDITED.get('practice',{}).items():
  if 'nodes' in record:PRACTICE[id]=record['nodes']
 for id,record in EDITED.get('exercises',{}).items():
  if 'supplement' in record:SUPPLEMENTS[id]=record['supplement']
  if 'replacement' in record:REPLACEMENTS[id]=record['replacement']
 if '4.3' in EDITED.get('chapter_lessons',{}):CONVERSION=EDITED['chapter_lessons']['4.3']['nodes']
REPORT={'canonical_practice':{},'exercises':{},'chapters':{},'products':0,'row_entry_checks':0,'unconverted_ids':[]}

def register(raw):
 for rawp in re.split(r'\n\s*\n',raw):
  rawp=rawp.strip()
  if not rawp or rawp.startswith(('#','@','**Step ','Independently derived')) or re.match(r'^\*\*[A-Z]\d+',rawp):continue
  rawp=' '.join(rawp.splitlines());record=author_paragraph(rawp)
  if record and key(rawp) not in MANUSCRIPT['paragraphs']:MANUSCRIPT['paragraphs'][key(rawp)]=record

def source_answers(text):
 text=text.split('# 12. Worked answers to textbook practice\n',1)[1].split('# 13.',1)[0]
 matches=list(re.finditer(r'^\*\*([A-Z]\d+(?: and [A-Z]\d+)?(?:,[^*]*)?\.)\*\*',text,re.M));out={}
 for i,m in enumerate(matches):
  end=matches[i+1].start() if i+1<len(matches) else len(text)
  chunk=text[m.start():end].split('\n## ')[0].strip()
  for id in re.findall(r'[A-Z]\d+',m[1]):out[id]=chunk
 return out

def enrich_products(h,names=None):
 cursor=0;index=0
 while True:
  start=h.find('<p>The product has ',cursor)
  if start<0:break
  endstart=h.find('<p>As a second interpretation, column j of the answer',start)
  if endstart<0:break
  end=h.find('</p>',endstart)+4;old=h[start:end]
  equations=[html.unescape(s) for s in re.findall(r'<annotation encoding="text/plain">(c_\{.*?}</annotation>)',old)] if False else [html.unescape(s) for s in re.findall(r'<annotation encoding="text/plain">(c_\{[^<]*)</annotation>',old)]
  if not equations:cursor=end;continue
  positions=[];pairs=[]
  for e in equations:
   ij=re.match(r'c_\{(\d)(\d)\}',e);terms=re.findall(r'\(([-\d/]+)\)\(([-\d/]+)\)',e)
   if not ij or not terms:break
   positions.append((int(ij[1])-1,int(ij[2])-1));pairs.append(terms)
  else:
   m=max(i for i,j in positions)+1;p=max(j for i,j in positions)+1;n=len(pairs[0]);AA=[[None]*n for _ in range(m)];BB=[[None]*p for _ in range(n)]
   assert len(positions)==m*p
   for (i,j),terms in zip(positions,pairs):
    assert len(terms)==n
    for k,(a,b) in enumerate(terms):
     a,b=F(a),F(b);assert AA[i][k] in (None,a) and BB[k][j] in (None,b);AA[i][k]=a;BB[k][j]=b
   C=[[sum((AA[i][k]*BB[k][j] for k in range(n)),F(0)) for j in range(p)] for i in range(m)]
   native=re.search(r'<div class="math-scroll"[^>]*><math[^>]*data-matrix="([^"]+)" data-duplicate="false".*?</math></div>',old,re.S)
   assert native
   expected=json.loads(html.unescape(native[1]))
   assert [[F(x) for x in r] for r in expected['a']]==C
   factor_names=names[index] if names and index<len(names) else ('L','R')
   nodes=product_nodes(AA,BB,factor_names,columns=True)
   rendered=render_nodes(nodes)
   # Keep every exact original display expression as well as its new arithmetic.
   for (i,j),terms,e in zip(positions,pairs,equations):
    exp=' + '.join(par(a)+par(b) for a,b in terms)
    rendered=rendered.replace(display(exp),display(e),1)
   result_stage=re.search(r'<section class="teaching-stage calculation-step"><h4>Put the entries.*?</section>',rendered,re.S)
   assert result_stage
   revised=result_stage[0].replace(mat(C),native[0],1)
   rendered=rendered[:result_stage.start()]+revised+rendered[result_stage.end():]
   rendered='<div class="product-demonstration">'+para('In this calculation, '+factor_names[0]+' is the left factor and '+factor_names[1]+' is the right factor.')+rendered+'</div>'
   h=h[:start]+rendered+h[end:];cursor=start+len(rendered);index+=1;REPORT['products']+=1;continue
  cursor=end
 return h

def exact_rref(a,n=None):
 a=[[F(x) for x in row] for row in a];n=n if n is not None else len(a[0]);r=0;piv=[]
 for j in range(n):
  k=next((k for k in range(r,len(a)) if a[k][j]),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r];v=a[r][j];a[r]=[x/v for x in a[r]]
  for k in range(len(a)):
   if k!=r:
    v=a[k][j];a[k]=[x-v*y for x,y in zip(a[k],a[r])]
  piv.append(j);r+=1
  if r==len(a):break
 return a,piv

def system_reading(d,purpose='solve'):
 """Read the actual matrix, show parameter choices, and verify the family."""
 n=d.get('bar');a=[[F(v) for v in row] for row in d['a']]
 if n is None or len(a[0])!=n+1:return ''
 rr,piv=exact_rref(a,n);free=[j for j in range(n) if j not in piv];bad=next((r for r in rr if not any(r[:n]) and r[n]),None)
 out=[stage('What does the reduced matrix say?',mat(rr,n)+para(f'There are {len(a)} equations and {n} unknown weights or coordinates. The divider separates the constants from those unknowns.'))]
 if bad:
  out.append(stage('Read the contradictory row',display('0 = '+str(bad[n]))+para('All coefficients on the left are zero. No choice of unknowns can make zero equal this nonzero constant.')))
  out.append(final(para('No solution exists for this target. If the question asks about span or range, the target is outside it.')));return ''.join(out)
 rows=[[f'x_{j+1}', 'Pivot column → basic' if j in piv else 'No pivot → free', 'Determined by its pivot equation' if j in piv else 'Choose an arbitrary real parameter'] for j in range(n)]
 out.append(stage('Separate determined coordinates from free choices',table(['Coordinate','Look at its column','What you may do'],rows)))
 parameters=['s','t','u','v','w','z'];params={j:parameters[i] if i<len(parameters) else 't_'+str(i+1) for i,j in enumerate(free)}
 p=[F(0)]*n;directions=[]
 for i,j in enumerate(piv):p[j]=rr[i][n]
 for f in free:
  v=[F(0)]*n;v[f]=F(1)
  for i,j in enumerate(piv):v[j]=-rr[i][f]
  directions.append(v)
 for i,j in enumerate(piv):
  lhs='x_'+str(j+1)+''.join(' + ('+str(rr[i][f])+')x_'+str(f+1) for f in free if rr[i][f])
  rhs=str(p[j])+''.join(' + ('+str(-rr[i][f])+')'+params[f] for f in free if rr[i][f])
  out.append(stage('Determine x'+str(j+1)+' from its row',display(lhs+' = '+str(rr[i][n]))+''.join(display('x_'+str(f+1)+' = '+params[f]) for f in free)+display('x_'+str(j+1)+' = '+rhs)+para('Subtract each free-variable term from both sides. The pivot coefficient is 1, so no further division is needed.')))
 if free:
  choices=[('All parameters 0',p)]
  for f,v in zip(free,directions):choices.append((params[f]+' = 1; all other parameters 0',[x+y for x,y in zip(p,v)]))
  out.append(stage('See the freedom with actual choices',table(['Independent choice','Resulting solution'],[[label,'('+','.join(str(x) for x in v)+')'] for label,v in choices])+para('Changing a free coordinate changes the input. Each parameter is independent; forcing two parameters to have the same value would wrongly discard solutions.')))
 expression=array_expr([[v] for v in p])+''.join(' + '+params[f]+array_expr([[v] for v in direction]) for f,direction in zip(free,directions))
 out.append(stage('Verify the starting point in every original equation',''.join(display(' + '.join(par(a[i][j])+par(p[j]) for j in range(n))+' = '+signed_sum([a[i][j]*p[j] for j in range(n)])+' = '+str(a[i][n])) for i in range(len(a)))))
 for f,v in zip(free,directions):
  assert all(sum((r[j]*v[j] for j in range(n)),F(0))==0 for r in a)
  out.append(stage('Verify the '+params[f]+' direction produces zero',''.join(display(' + '.join(par(a[i][j])+par(v[j]) for j in range(n))+' = '+signed_sum([a[i][j]*v[j] for j in range(n)])+' = 0') for i in range(len(a)))))
 if free:out.append(stage('Why this is the whole solution set',para('A times the starting point gives the original right side. A times every direction gives zero. Therefore every parameter choice still gives that right side. Conversely, the pivot equations force exactly these coordinates, so no solution is missing.')))
 conclusion=display('x = '+expression)+para('All displayed parameters are arbitrary real numbers.' if free else 'Every coordinate is fixed. There are no free choices, so the solution is unique.')
 if purpose=='independence':conclusion+=para('The weights are not forced to zero: the displayed nonzero direction proves dependence.' if free else 'The only zero-producing input is zero, so the given columns are linearly independent.')
 out.append(final(conclusion));CHECKS.append({'kind':'system-family','matrix':d,'p':p,'directions':directions,'pivots':piv})
 return '<div class="system-interpretation">'+''.join(out)+'</div>'

# Definitions appear where their words are needed, rather than as a generic roadmap.
TERMS=[
 ('coefficient','A coefficient is the number multiplying an unknown. A missing term has coefficient 0.'),
 ('pivot','In a row staircase, a leading entry is the first nonzero entry when reading a nonzero row from left to right. Its position is a pivot position. A pivot coefficient column determines a basic coordinate; a nonpivot coefficient column allows a free coordinate.'),
 ('span','The span is the set of every weighted sum of the supplied vectors. Membership asks whether weights can produce this particular target.'),
 ('independen','Independence means the only weights producing the zero vector are all zero. A nonzero collection of weights producing zero is a dependence relation.'),
 ('homogeneous','Homogeneous means the right side is the zero vector. The zero input always works; nontrivial means a different, nonzero input.'),
 ('inverse','An inverse undoes a square matrix: both multiplication orders must give the identity. The identity has diagonal 1s and all other entries 0.'),
 ('one-to-one','One-to-one means different inputs never give the same output. For a linear map this is equivalent to only the zero input producing zero.'),
 ('onto','Onto means every vector in the stated codomain can be reached. It requires a pivot in every coefficient row.'),
 ('transpose','Transpose turns each row into a column. A transposed product reverses the factors before transposing each one.'),
 ('linear','Linearity means addition and scalar weights are preserved. A scalar is a single real-number multiplier.')]

def exercise_intro(q):
 raw=q['source'];t=q['title'];kind=classify(q)
 data=re.search(r'^@matrix (.*)$',raw,re.M);notes=[];given=''
 if data and 'The starting matrix is:' in raw:
  d=json.loads(data[1]);m=len(d['a']);cols=len(d['a'][0]);bar=d.get('bar')
  if bar is not None:
   notes.append(f'The calculation below starts with {m} rows. Its {bar} columns before the divider record the coefficients; the {cols-bar} column'+('s' if cols-bar!=1 else '')+' after the divider record the right-hand side'+('s.' if cols-bar!=1 else '.'))
   given=display(' + '.join('('+str(v)+')x_'+str(j+1) for j,v in enumerate(d['a'][0][:bar]))+' = '+str(d['a'][0][bar])) if cols-bar==1 else mat([d['a'][0]],bar)
  elif '@eq c_{' not in raw:
   given=mat([d['a'][0]],label='The actual first row of the matrix being reduced.')
   notes.append(f'The starting matrix below has {m} rows and {cols} columns. Its last column is an ordinary matrix column; no augmented divider is declared.')
 # The visible task uses the actual exercise wording, and local numerical data.
 pieces=[para('**Your task.** '+t+'.')]+[para(n) for n in notes]
 if given:pieces.append(stage('Read the actual first row',given))
 chosen=[];hay=(t+' '+re.sub(r'^Independently[^\n]*','',raw,flags=re.M)).lower()
 for needle,definition in TERMS:
  if needle in hay and (needle!='linear' or 'linear' in t.lower()):chosen.append(definition)
 if chosen:pieces.append('<div class="local-vocabulary"><strong>Words used in this question</strong>'+''.join(para(x) for x in chosen[:3])+'</div>')
 if kind=='true-false':pieces.append(para('Read the exact statement above. The verdict below concerns all of its assumptions; the reason or counterexample is part of the answer.'))
 return '<div class="question-specific-start" data-question="'+q['id']+'">'+''.join(pieces)+'</div>'


def verify_product(A,B):
 A=[[F(x) for x in row] for row in A];B=[[F(x) for x in row] for row in B];out=[];C=[]
 for i,row in enumerate(A):
  crow=[]
  for j,col in enumerate(zip(*B)):
   vals=[x*y for x,y in zip(row,col)];v=sum(vals,F(0));crow.append(v)
   out.append('<div class="entry-calculation"><span class="entry-label">'+f'Output row {i+1}, column {j+1}'+'</span>'+display(' + '.join(par(x)+par(y) for x,y in zip(row,col))+' = '+signed_sum(vals)+' = '+str(v))+'</div>')
  C.append(crow)
 CHECKS.append({'kind':'product','A':A,'B':B,'C':C})
 return ''.join(out)+mat(C)

def inverse_reading(d):
 n=d['bar'];AA=[[F(v) for v in row[:n]] for row in d['a']];rr,piv=exact_rref(d['a'],n)
 if len(piv)<n:
  return stage('Why the inverse does not exist',para(f'There are only {len(piv)} coefficient pivots but {n} input coordinates. Row operations cannot turn this coefficient block into the {n} × {n} identity. Some input information is lost.'))+final(para('A is singular. It has no inverse.'))
 inv=[row[n:] for row in rr]
 assert len(inv[0])==n
 return stage('Read the inverse from the right block',mat(rr,n)+para('The left block is now I: each input is selected once, with no mixing. The same reversible operations on the identity created the inverse in the right block.'))+stage('Verify A times the proposed inverse',verify_product(AA,inv))+stage('Verify the inverse times A',verify_product(inv,AA))+final(display('A^(-1) = '+array_expr(inv)))

def first_matrix(raw):
 m=re.search(r'^@matrix (.*)$',raw,re.M)
 return json.loads(m[1]) if m else None

def prepare_practice(chapters):
 c=next(c for c in chapters if c['id']=='practice-answers');old=answer_map(chapters,duplicate=False);sources=source_answers((ROOT/'source/MATH2255-Complete-Beginner-Textbook.md').read_text());seen={}
 for id,body in old.items():
  if body in seen:
   MANUSCRIPT['practice'][id]={'same_as':seen[body]};REPORT['canonical_practice'][id]=seen[body];continue
  seen[body]=id;raw=sources[id];register(raw)
  label=re.search(r'^\*\*(.*?)\*\*',raw)[1]
  if id in PRACTICE:
   nodes=PRACTICE[id];updated=para('**'+label+'**','canonical-answer-title')+render_nodes(nodes)
   record={'nodes':nodes,'source':raw,'mode':'authored'}
  else:
   updated=enrich_products(body, [('A','B'),('B','A')] if id=='O1' else None)
   updated=transform(raw,updated,MANUSCRIPT['paragraphs'])
   # Preserve the first source label for answer association even if its prose
   # becomes a sequence of reasoning units.
   updated=para('**'+label+'**','canonical-answer-title')+updated
   d=first_matrix(raw)
   if d and d.get('bar')==len(d['a'][0])-1:updated+=system_reading(d,'independence' if id=='I2' else 'solve')
   elif id=='N2':updated+=inverse_reading(d)
   elif id=='O1':updated+=final(display('AB = [4,6;1,3]')+display('BA = [2,4;1,5]')+para('The two orders give different matrices, so AB ≠ BA.'))
   record={'source':raw,'mode':'source-calculations-with-entry-arithmetic','html':updated}
  canonical='<div class="canonical-practice-answer" data-answer-key="'+id+'">'+updated+'</div>'
  c['html']=c['html'].replace(body,canonical,1)
  MANUSCRIPT['practice'][id]=record;REPORT['canonical_practice'][id]=id
 # Keep canonical source blocks stable for use by the chapter disclosures.
 return {id:extract_canonical(c['html'],REPORT['canonical_practice'][id]) for id in old}

def extract_canonical(s,id):
 opening='<div class="canonical-practice-answer" data-answer-key="'+id+'">';start=s.index(opening);pos=start;depth=0
 for m in re.finditer(r'</?div\b[^>]*>',s[start:]):
  depth+=-1 if m[0].startswith('</') else 1
  if depth==0:return s[start:start+m.end()]
 raise ValueError('unclosed answer '+id)

def revise(chapters,exercises):
 for c in chapters:
  register(c['source'])
 for q in exercises:register(q['source'])
 canonical=prepare_practice(chapters)
 # Defer normal concept/pivot refinement until the canonical answers exist.
 from learning import refine_chapters
 refine_chapters(chapters,answers={id:h.replace('data-duplicate="false"','data-duplicate="true"') for id,h in canonical.items()})
 for c in chapters:
  if c['id']=='practice-answers':
   REPORT['chapters'][c['id']]={'canonical_answers':len(canonical)};continue
  h=enrich_products(c['html'],[('A','x')] if c['id']=='section-1-4' else [('A','B'),('B','A')] if c['id']=='section-2-1' else None)
  h=transform(c['source'],h,MANUSCRIPT['paragraphs'])
  h=h.replace('<span class="component-label">THE COMPLETE EXPLANATION</span>','').replace('class="precise-explanation"','class="reading-explanation"')
  if c['id']=='section-1-4':
   lessonid='4-3-one-problem-three-equivalent-languages';opening='<section class="lesson concept-section-root" id="'+lessonid+'"><h2>'
   start=h.index(opening);hend=h.index('</h2>',start)+5;nextlesson=h.index('<section class="lesson concept-section-root"',hend)
   oldbody=h[hend:nextlesson];solution_start=oldbody.find('<p>Each coefficient column')
   # Retain the former complete solve as explicitly optional further study.
   # Conversion itself does not ask the student to solve a system.
   original_work=c['html'][c['html'].index(opening):];original_work=original_work[:original_work.index('<section class="lesson concept-section-root"',len(opening))] if '<section class="lesson concept-section-root"' in original_work[len(opening):] else original_work
   calcstart=original_work.find('<p>Each coefficient column')
   extra=original_work[calcstart:] if calcstart>=0 else ''
   if extra.endswith('</div></section>'):extra=extra[:-16]
   elif extra.endswith('</section>'):extra=extra[:-10]
   extra=transform(c['source'],extra,MANUSCRIPT['paragraphs'])
   new=render_nodes(CONVERSION)+'<details class="proof-detail optional-further-study"><summary>Optional further study: solve this system after converting it</summary>'+extra+'</details>'
   h=h[:hend]+new+'</section>'+h[nextlesson:];MANUSCRIPT['chapter_lessons']['4.3']={'nodes':CONVERSION,'purpose':'Convert only; original full solution retained as optional further study.'}
  c['html']=h;REPORT['chapters'][c['id']]={'teaching_units':h.count('data-prose-key='),'arithmetic_entries':h.count('class="entry-calculation"')}
 for q in exercises:
  if q['status']!='solved':REPORT['exercises'][q['id']]={'status':'original-truncation'};continue
  id=q['id']
  factor_names=[('C','D')] if id=='2.1.1' else [('C','B')] if id=='2.1.2' else [('A','x')] if q['section']=='1.4' else [('A','B'),('A','C')] if id=='2.1.10' else [('A','A^(-1)'),('A^(-1)','A')] if id in ['2.2.1','2.2.2','2.2.3','2.2.4','2.2.5','2.2.6'] else [('A','B')]
  h=enrich_products(q['solution'],factor_names)
  h=transform(q['source'],h,MANUSCRIPT['paragraphs'])
  if q['id']=='2.1.3':
   correction='Subtracting 3I₂ and multiplying by 3I₂ are different operations: the first changes only the matching diagonal entries by subtraction, while the second scales every entry.'
   rec=MANUSCRIPT['paragraphs'].get(key(correction))
   old=render_paragraph(rec) if rec else para(correction)
   h=h.replace(old,stage('Keep subtraction and multiplication distinct',para('For 3I₂ − A, a diagonal entry becomes 3 minus that A entry. An off-diagonal entry becomes 0 minus that A entry, so its sign reverses. For (3I₂)A, every entry of A is multiplied by 3.')))

  first=h.find('</p>')+4
  if id in REPLACEMENTS:h=h[:first]+render_nodes(REPLACEMENTS[id])
  if id in SUPPLEMENTS:h=h[:first]+render_nodes(SUPPLEMENTS[id])+h[first:]
  h=h[:first]+exercise_intro(q)+h[first:]
  if id in PROOF_CONTEXT:
   given,idea=PROOF_CONTEXT[id]
   first=h.find('</p>')+4
   if id in ['2.1.37','2.1.38','2.1.41']:idea+=' Here i names an output row, j an output column, and k the matching inner-entry position. The symbol Σ means add the term for every allowed k. An entry aᵢⱼ is the number in row i, column j.'
   frame=stage('Given',para(given),'proof-given')+stage('What must be shown',para(q['title']),'proof-claim')+stage('Main idea',para(idea),'proof-idea')+'<h3 class="proof-steps-heading">Proof steps and justification</h3>'
   # Place the precise proof context after the short local vocabulary.
   h=h[:first]+frame+h[first:]
  d=first_matrix(q['source']);kind=classify(q)
  # Numerical system families are computed from the actual original augmented
  # data, not inferred from the source's last displayed verification vector.
  if d and d.get('bar')==len(d['a'][0])-1 and q['id'] not in ['2.1.25','2.2.45','2.2.46']:
   if 'without solving' in q['title'].lower():
    rr,pivs=exact_rref(d['a'],d['bar']);bad=any(not any(row[:d['bar']]) and row[d['bar']] for row in rr)
    h+=final(para('The system is inconsistent: a reduced row states zero equals a nonzero constant.' if bad else 'The system is consistent: no reduced row states zero equals a nonzero constant. A consistency decision is all this question requests.'))
   else:h+=system_reading(d,'independence' if q['section']=='1.7' else 'solve')
  elif id in ['2.2.39','2.2.40','2.2.41','2.2.42'] and d:
   h+=inverse_reading(d)
  elif id in ['2.2.1','2.2.2','2.2.3','2.2.4']:
   from questions import Q
   original=first_matrix(Q[id]['text']);AA=[[F(x) for x in row] for row in original['a']];a,b=AA[0];c,dv=AA[1];det=a*dv-b*c;inv=[[dv/det,-b/det],[-c/det,a/det]]
   h+=stage('Check the reverse product as well',verify_product(inv,AA))+final(display('A^(-1) = '+array_expr(inv)))
  elif id=='2.2.45':h+=final(para('The third inverse column is')+mat([[3],[-6],[4]]))
  elif id=='2.2.46':h+=final(para('The second inverse column is')+mat([['3/2'],['-433/6'],['68/3']])+para('The third inverse column is')+mat([['-9/2'],['439/2'],[-69]]))
  elif id in ['2.1.1','2.1.2','2.1.3','2.1.4','1.3.1','1.3.2']:
   results={
    '2.1.1':[display('-2A = [-4,0,2;-8,6,-4]'),display('B-2A = [3,-5,3;-7,2,-7]'),para('AC is undefined.'),display('CD = [1,13;-7,-6]')],
    '2.1.2':[display('A+2B = [16,-10,1;6,-11,-4]'),para('3C − E and EB are undefined.'),display('CB = [9,-13,-5;-13,6,-5]')],
    '2.1.3':[display('3I_2 - A = [-1,1;-5,5]'),display('(3I_2)A = [12,-3;15,-6]')],
    '2.1.4':[display('A - 5I_3 = [4,-1,3;-8,2,-3;-4,1,3]'),display('(5I_3)A = [45,-5,15;-40,35,-15;-20,5,40]')],
    '1.3.1':[display('u+v = [-4;5]'),display('u-2v = [5;-4]')],
    '1.3.2':[display('u+v = [5;5]'),display('u-2v = [-1;-4]')]}
   h+=final(''.join(results[id]))
  elif id in ['1.9.17','1.9.18','1.9.19','1.9.20']:
   matrices=re.findall(r'^@matrix (.*)$',q['source'],re.M)
   h+=final((mat(json.loads(matrices[-1])) if matrices else '')+para('For every input x, this matrix gives Ax = T(x). Therefore T is linear.'))
  elif id in PROOF_FINAL and 'class="final-answer"' not in h:h+=final(''.join(para(x) for x in PROOF_FINAL[id]))
  elif kind=='true-false':
   verdict=re.search(r'\*\*(True|False)\.\*\*',q['source'])
   if verdict:h+=final(para('**'+verdict[1]+'.** '+q['title'].split(':',1)[-1].strip()))
  elif 'class="final-answer"' not in h:
   # Preserve the actual final mathematical conclusion; a verdict alone is
   # never invented for a proof or a symbolic case analysis.
   paragraphs=[p.strip() for p in re.split(r'\n\s*\n',q['source']) if p.strip() and not p.startswith(('@','#','Independently'))]
   last=paragraphs[-1] if paragraphs else ''
   if last and not last.startswith('**Step'):
    rec=author_paragraph(last)
    h+=final(render_paragraph(rec) if rec else para(last))
  q['solution']=h
  MANUSCRIPT['exercises'][q['id']]={**({'supplement':SUPPLEMENTS[id]} if id in SUPPLEMENTS else {}),**({'replacement':REPLACEMENTS[id]} if id in REPLACEMENTS else {}),'title':q['title'],'mode':'actual-source-mathematics','first_matrix':d,'method':kind,'paragraph_keys':[key(' '.join(p.strip().splitlines())) for p in re.split(r'\n\s*\n',q['source']) if key(' '.join(p.strip().splitlines())) in MANUSCRIPT['paragraphs']]}
  REPORT['exercises'][q['id']]={'status':'structured','method':kind,'teaching_units':h.count('data-prose-key='),'entry_calculations':h.count('class="entry-calculation"'),'has_final':'class="final-answer"' in h,'products':h.count('class="product-demonstration"')}
 (ROOT/'source/teaching/beginner-content.json').write_text(json.dumps(MANUSCRIPT,ensure_ascii=False,indent=2,default=serializable))
 REPORT['row_entry_checks']=sum(x['entries'] for x in CHECKS if x['kind']=='row-entry-arithmetic')
 (ROOT/'reader/qa/beginner/content-revision.json').write_text(json.dumps(REPORT,ensure_ascii=False,indent=2))
 (ROOT/'reader/qa/beginner/exact-arithmetic.json').write_text(json.dumps(CHECKS,ensure_ascii=False,indent=2,default=serializable))
 return chapters,exercises
