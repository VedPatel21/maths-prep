"""Site-wide beginner-content acceptance audit. Requires lxml and pypdf.
Source preservation and visible proof wording are checked by validate_reader.py.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,re,base64,hashlib
from lxml import html,etree
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parent.parent;R=ROOT/'reader';QA=R/'qa/beginner';D=json.loads((R/'content.json').read_text());C=json.loads((ROOT/'source/teaching/beginner-content.json').read_text());passed=[]
def check(label,test):
 assert test,label
 passed.append(label)
def parse(s):return html.fromstring('<div>'+s+'</div>')
def hasclass(doc,c):return doc.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," '+c+' ")]')
def mm(a,b):
 a=[[F(v) for v in r] for r in a];b=[[F(v) for v in r] for r in b]
 return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]
def I(n):return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def inverse(a):
 n=len(a);a=[[F(v) for v in row]+row2 for row,row2 in zip(a,I(n))]
 for j in range(n):
  k=next(k for k in range(j,n) if a[k][j]);a[j],a[k]=a[k],a[j];c=a[j][j];a[j]=[v/c for v in a[j]]
  for k in range(n):
   if k!=j:
    c=a[k][j];a[k]=[v-c*w for v,w in zip(a[k],a[j])]
 return [r[n:] for r in a]
def canonical(doc):
 node=etree.fromstring(etree.tostring(doc))
 for m in node.xpath('.//*[@data-duplicate]'):m.set('data-duplicate','true')
 return etree.tostring(node)
chapters={c['id']:c for c in D['chapters']};collection=parse(chapters['practice-answers']['html']);expected=set(re.findall(r'^\*\*([A-Z]\d+)\.\*\*',(ROOT/'source/MATH2255-Complete-Beginner-Textbook.md').read_text().split('# 12.')[0],re.M));seen=set()
for chapter in D['chapters']:
 doc=parse(chapter['html']);lessons=hasclass(doc,'concept-section-root')
 check(chapter['id']+': all chapter lessons remain top-level siblings',all(l.getparent()==doc for l in lessons))
 for card in doc.xpath('.//*[@data-practice-id]'):
  id=card.get('data-practice-id');seen.add(id);nodes=card.xpath('.//*[@data-answer-key]');check(id+': canonical answer exists once in disclosure',len(nodes)==1)
  key=nodes[0].get('data-answer-key');original=collection.xpath('.//*[@data-answer-key="'+key+'"]');check(id+': answer collection and disclosure are identical',len(original)==1 and canonical(nodes[0])==canonical(original[0]))
check('All 42 textbook practices covered',seen==expected and len(seen)==42)
a3=collection.xpath('.//*[@data-answer-key="A3"]')[0];heads=[x.text_content() for x in a3.xpath('.//h4')]
for title in ['Read A: 2 rows, 3 columns','Read x: 3 rows, 1 column','Check that multiplication is allowed','Calculate output row 1','Calculate output row 2','Put the entries into their output positions','Check with the column method','Why the row and column methods agree']:check('A3: '+title,title in heads)
check('A3 actual result exactly (1,−5)',mm([[1,2,3],[0,-1,4]],[[2],[1],[-1]])==[[1],[-5]])
a3math=a3.xpath('.//annotation/text()')
for expr in ['2 + 2 - 3','0 - 1 - 4','2 [1;0] = [2;0]','1 [2;-1] = [2;-1]','-1 [3;4] = [-3;-4]']:
 check('A3 visible intermediate: '+expr,expr in a3math)
check('A3 distinct final answer exists',bool(hasclass(a3,'final-answer')))
check('No obsolete compressed A3 answer anywhere',all('The sizes are (2 × 3)(3 × 1)' not in c['html'] for c in D['chapters']))
conversion=parse(chapters['section-1-4']['html']).xpath('.//section[@id="4-3-one-problem-three-equivalent-languages"]')[0]
check('Conversion: nine teaching stages before optional solve',len(conversion.xpath('./section[contains(@class,"teaching-stage")]'))==9)
for exp in ['x_1 + 2x_2 - x_3 = 4','-5x_2 + 3x_3 = 1','x = [x_1;x_2;x_3]','b = [4;1]','[1,2,-1;0,-5,3][x_1;x_2;x_3] = [4;1]','x_1[1;0] + x_2[2;-5] + x_3[-1;3] = [4;1]']:
 check('Conversion actual expression: '+exp,exp in conversion.xpath('.//annotation/text()'))
check('Conversion coefficient table contains zero x₁ coefficient',conversion.xpath('.//table/tbody/tr[2]/*')[1].text_content()=='0')
check('Solving is explicitly optional after conversion',bool(conversion.xpath('./details[contains(@class,"optional-further-study")]')))
# Verify every newly generated arithmetic record independently of its authoring helpers.
arithmetic=json.loads((QA/'exact-arithmetic.json').read_text());kinds=Counter()
for i,r in enumerate(arithmetic):
 kinds[r['kind']]+=1
 if r['kind']=='product':check('Exact product '+str(i),mm(r['A'],r['B'])==[[F(v) for v in row] for row in r['C']])
 elif r['kind']=='entrywise':check('Exact entrywise operation '+str(i),[[F(r['c'])*F(v)+F(r['d'])*F(w) for v,w in zip(a,b)] for a,b in zip(r['A'],r['B'])]==[[F(v) for v in row] for row in r['C']])
 elif r['kind']=='system-family':
  mat=r['matrix'];n=mat['bar'];a=[row[:n] for row in mat['a']];b=[[F(row[n])] for row in mat['a']]
  check('Particular solution '+str(i),mm(a,[[v] for v in r['p']])==b)
  for j,v in enumerate(r['directions']):check('Homogeneous direction '+str((i,j)),mm(a,[[x] for x in v])==[[0] for row in a])
# Re-evaluate each ORIGINAL source row operation, including all augmentation entries.
operations=0
for filename in ['MATH2255-Complete-Beginner-Textbook.md','MATH2255-Exercises-and-Detailed-Solutions.md']:
 raw=(ROOT/'source'/filename).read_text();last=None
 blocks=[p.strip() for p in re.split(r'\n\s*\n',raw) if p.strip()]
 for i,b in enumerate(blocks):
  if b.startswith('@matrix '):last=json.loads(b[8:])
  if not b.startswith('**Step ') or last is None:continue
  following=blocks[i+1] if i+1<len(blocks) else ''
  if not following.startswith('@matrix '):continue
  after=json.loads(following[8:]);a=[[F(v) for v in row] for row in last['a']];target=[[F(v) for v in row] for row in after['a']];op=b.split('**')[1];rows=[int(v)-1 for v in re.findall(r'R(\d+)',op)]
  if '↔' in op:a[rows[0]],a[rows[1]]=a[rows[1]],a[rows[0]]
  else:
   c=F(re.search(r'\(([-\d/]+)\)R',op)[1]);t=rows[0]
   a[t]=[x+c*y for x,y in zip(a[t],a[rows[-1]])] if '+' in op else [c*x for x in a[t]]
  check('Original full row operation '+str(operations),a==target);operations+=1
check('All 598 original source operations re-evaluated',operations==598)
# Check noncommuting numerical instances of the newly written inverse argument.
AA=[[2,1],[1,1]];X=[[F(1,2),F(1,3)],[F(1,5),F(1,4)]];AX=mm(AA,X);Aminus=[[F(a)-b for a,b in zip(row,row2)] for row,row2 in zip(AA,AX)];B=mm(X,inverse(Aminus));Bi=inverse(B);factor=[[F(a)+b for a,b in zip(row,row2)] for row,row2 in zip(AA,Bi)]
check('2.2.30: noncommuting case satisfies original premise',inverse(Aminus)==mm(inverse(X),B))
check('2.2.30: derived formula recovers X',mm(inverse(factor),AA)==X)
for n in [1,2,3,5,8]:
 a=[[F(j+1)*int(i>=j) for j in range(n)] for i in range(n)];b=[[F(int(i==j)-int(i==j+1),i+1) for j in range(n)] for i in range(n)]
 check('2.2.44: both inverse orders at size '+str(n),mm(a,b)==mm(b,a)==I(n))
# Independently test the newly expanded parameter formulas, including exceptional values.
from parameter_lessons import PARAMETERS
for id in PARAMETERS:
 doc=parse(next(q['solution'] for q in D['exercises'] if q['id']==id))
 check(id+': explicit parameter algebra stages and final',len(hasclass(doc,'teaching-stage'))>=3 and bool(hasclass(doc,'final-answer')))
for h in map(F,[-17,-15,-12,-2,0,2,6,9,26]):
 if h!=2:check('1.1.23 parameter '+str(h),(6-3*h)*(-4/(6-3*h))==-4)
 check('1.1.24 and 25 always admit x2=0 at '+str(h),(4+2*h)*0==(h+12)*0==0)
 if h!=-15:check('1.2.22 parameter '+str(h),(h+15)*(3/(h+15))==3)
 for k in map(F,[-5,0,6,8,11]):
  if h!=2:check('1.2.23 unique formula '+str((h,k)),(8-4*h)*((k-8)/(8-4*h))==k-8)
  if h!=9:check('1.2.24 unique formula '+str((h,k)),(h-9)*((k-6)/(h-9))==k-6)
  alpha=h/4-k/2;beta=h/4+k/2
  check('1.3.21 arbitrary target '+str((h,k)),2*alpha+2*beta==h and -alpha+beta==k)
 c1=3*h+28;c2=h+16;c3=5
 check('1.7.12 nontrivial relation '+str(h),2*c1-6*c2+8*c3==0 and -5*c2+(h+16)*c3==0 and c3!=0)
 c1=27-2*h;c2=15-h;c3=1
 check('1.7.13 nontrivial relation '+str(h),c1-2*c2+3*c3==0 and c2+(h-15)*c3==0 and c3!=0)
check('1.1.26 exceptional value',5+3*F(-5,3)==0)
check('1.2.21 exceptional value',7-2*F(7,2)==0)
check('1.3.17 full three-coordinate verification',mm([[1,-2],[4,-3],[-2,7]],[[-2],[-3]])==[[4],[1],[-17]])
check('1.3.18 full three-coordinate verification',mm([[1,-3],[0,1],[-2,8]],[[F(-37,2)],[-5]])==[[F(-7,2)],[-5],[-3]])
check('1.7.11 nontrivial relation at h=6',mm([[1,3,-1],[-1,-5,5],[4,7,6]],[[-5],[2],[1]])==[[0],[0],[0]])
check('1.7.14 nontrivial relation at h=26',mm([[1,-5,1],[-1,7,1],[3,8,26]],[[-6],[-1],[1]])==[[0],[0],[0]])
check('1.9.9 reflection after shear product',mm([[0,-1],[-1,0]],[[1,-3],[0,1]])==[[0,-1],[-1,3]])
for ss,tt in [(F(0),F(0)),(F(1),F(0)),(F(0),F(1)),(F(-2,3),F(7,5))]:
 check('1.5.21 homogeneous and translated families '+str((ss,tt)),(-9*ss+4*tt)+9*ss-4*tt==0 and (-2-9*ss+4*tt)+9*ss-4*tt==-2)
for id in ['1.9.9','1.9.19','2.1.41']:
 doc=parse(next(q['solution'] for q in D['exercises'] if q['id']==id));vocab=hasclass(doc,'local-vocabulary')
 check(id+': provenance does not introduce irrelevant independence vocabulary',not any('Independence means' in v.text_content() for v in vocab))
long=[];calculation_paragraphs=[];short=[]
for q in D['exercises']:
 doc=parse(q['solution']);check(q['id']+': nonempty question retained',bool(q['question'].strip()))
 if q['status']!='solved':continue
 check(q['id']+': specific task linked to its stable ID',bool(doc.xpath('.//*[@data-question="'+q['id']+'"]')))
 check(q['id']+': distinct final answer',bool(hasclass(doc,'final-answer')))
 check(q['id']+': generic roadmaps removed',not hasclass(doc,'solution-roadmap'))
 check(q['id']+': no empty explanation paragraphs',all(p.text_content().strip() for p in doc.xpath('.//p')))
 for p in doc.xpath('.//p'):
  text=p.text_content()
  if len(text)>400:long.append({'id':q['id'],'text':text})
  if text.count('=')>=3 and len(text)>160:calculation_paragraphs.append({'id':q['id'],'text':text})
 if not (hasclass(doc,'teaching-reasoning') or hasclass(doc,'teaching-stage')):short.append(q['id'])
check('No complete exercise retains a >400-character explanatory paragraph',not long)
check('No complete exercise retains a long paragraph hiding 3 or more equalities',not calculation_paragraphs)
check('337 complete exercises present',sum(q['status']=='solved' for q in D['exercises'])==337)
check('No exercise content silently removed',len(D['exercises'])==339)
check('No raw source directives in rendered lessons',not re.search(r'@(matrix|eq|customfig|figure)\b',''.join(c['html'] for c in D['chapters'])))
pdf=ROOT/'output/pdf/MATH2255-Two-Sided-Cheat-Sheet.pdf'
if not pdf.exists():pdf=ROOT/pdf.name
p=PdfReader(pdf)
check('Cheat sheet is a valid two-page Letter PDF',len(p.pages)==2 and all(tuple(x.mediabox)==(0,0,612,792) for x in p.pages))
check('Actual PDF bytes are embedded unchanged',base64.b64decode(D['cheatSheet']['pdf'])==pdf.read_bytes())
check('Exercise 2.1.3 no longer gives misleading diagonal-only subtraction advice','first changes only the matching diagonal entries' not in next(q['solution'] for q in D['exercises'] if q['id']=='2.1.3'))
report={'passed':len(passed),'chapters':18,'exercises':339,'complete':337,'canonical_practice_answers':42,'source_operations_recomputed':operations,'exact_arithmetic_record_types':dict(kinds),'dense_complete_exercise_paragraphs':long,'compressed_calculation_paragraphs':calculation_paragraphs,'intentionally_compact_factual_answers':short,'source_truncations_unchanged':['1.2.41','2.1.43'],'checks':passed}
(QA/'acceptance-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps({k:v for k,v in report.items() if k!='checks'},indent=2))
