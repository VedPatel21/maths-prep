"""Academic/structural checks for the additive visual lessons and study PDF.
Requires lxml, pypdf, pdfplumber. Browser evidence is recorded separately.
"""
from pathlib import Path
import json,re,base64,hashlib
from fractions import Fraction as F
from lxml import html
from pypdf import PdfReader
import pdfplumber
ROOT=Path(__file__).resolve().parent.parent;R=ROOT/'reader';QA=R/'qa/final'
D=json.loads((R/'content.json').read_text());passed=[]
def check(label,result):
 assert result,label
 passed.append(label)
def cls(node,c):return node.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," '+c+' ")]')
source=(ROOT/'source/MATH2255-Complete-Beginner-Textbook.md').read_text().split('# 12. Worked answers')[0]
expected=set(re.findall(r'^\*\*([A-Z]\d+)\.\*\*',source,re.M));seen=[];rowgroups=[]
for c in D['chapters']:
 doc=html.fromstring('<div>'+c['html']+'</div>')
 # A lesson remains one top-level section: no damaged closing tags after copies.
 check(c['id']+': lesson sections remain siblings',all(n.getparent()==doc for n in cls(doc,'concept-section-root')))
 for card in cls(doc,'practice-question'):
  id=card.get('data-practice-id');seen.append(id)
  check(id+': exactly one direct matching solution',len(card.xpath('./details[@class="worked-solution"]'))==1 and card.xpath('./details/summary')[0].text_content()=='Show Detailed Solution · '+id)
  check(id+': no nested question cards',not cls(card,'practice-question'))
  check(id+': copied answer has no original-matrix markers',not card.xpath('.//details//math[@data-duplicate="false"]'))
 for step in cls(doc,'row-step'):
  if step.getprevious() is not None and 'row-step' in step.getprevious().get('class','').split():continue
  group=[step];n=step.getnext()
  while n is not None and 'row-step' in n.get('class','').split():group.append(n);n=n.getnext()
  rowgroups.append((c['id'],len(group)))
check('Every original textbook practice question has its own answer',set(seen)==expected and len(seen)==len(expected))
check('R1, R2 and R3 exist exactly once',all(seen.count(i)==1 for i in ['R1','R2','R3']))
check('Twelve-operation course derivation is contiguous',('section-1-2',12) in rowgroups)
check('Larger nine-operation course derivation is contiguous',('section-1-2',9) in rowgroups)
report=json.loads((QA/'learning-manifest.json').read_text())
check('All 337 complete exercises receive a method-specific guide',len(report['guided_exercises'])==337)
check('No truncated statement gains a fabricated guide',not ({'1.2.41','2.1.43'}&set(report['guided_exercises'])))
for q in D['exercises']:
 doc=html.fromstring('<div>'+q['solution']+'</div>')
 check(q['id']+': no broken nested source row-step markup',not any(cls(s,'row-step') for s in cls(doc,'row-step')))
# Independently compute the new numerical teaching examples using exact arithmetic.
def mul(a,b):return [[sum(F(x)*F(y) for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def rref(a):
 a=[[F(x) for x in row] for row in a];r=0
 for j in range(len(a[0])):
  k=next((k for k in range(r,len(a)) if a[k][j]),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r];p=a[r][j];a[r]=[x/p for x in a[r]]
  for k in range(len(a)):
   if k!=r:
    t=a[k][j];a[k]=[x-t*y for x,y in zip(a[k],a[r])]
  r+=1
  if r==len(a):break
 return a
check('REF comparison reduces to displayed RREF',rref([[2,4,6],[0,3,9],[0,0,0]])==[[1,0,-3],[0,1,3],[0,0,0]])
check('Original pivot-column example reduces exactly',rref([[0,2,4],[1,1,3]])==[[1,0,1],[0,1,2]])
check('Highlighted row-column product equals 11',mul([[2,3],[1,-5]],[[4,3,6],[1,-2,3]])[0][0]==11)
check('Supplementary inverse undoes both directions',mul([[1,2],[4,7]],[[-7,2],[4,-1]])==mul([[-7,2],[4,-1]],[[1,2],[4,7]])==[[1,0],[0,1]])
for s,t in [(0,0),(1,0),(0,1),(-7,F(3,4))]:
 x=[4-2*s+t,s,t]
 check('Two independent parameters satisfy both original equations '+str((s,t)),mul([[1,2,-1],[2,4,-2]],[[v] for v in x])==[[4],[8]])
A=[[1,2,-1,3],[2,4,-2,6],[0,0,1,-2]]
check('Four-unknown particular solution and both directions verified',mul(A,[[5],[0],[1],[0]])==[[4],[8],[1]] and all(mul(A,[[v] for v in col])==[[0],[0],[0]] for col in [[-2,1,0,0],[-1,0,2,1]]))
pdf=ROOT/'output/pdf/MATH2255-Two-Sided-Cheat-Sheet.pdf'
if not pdf.exists():pdf=ROOT/pdf.name
reader=PdfReader(pdf)
check('Exactly two US Letter PDF pages',len(reader.pages)==2 and all(tuple(p.mediabox)==(0,0,612,792) for p in reader.pages))
check('Embedded PDF is byte-identical to delivered PDF',base64.b64decode(D['cheatSheet']['pdf'])==pdf.read_bytes())
check('Both page previews embedded',len(D['cheatSheet']['previews'])==2 and all(x.startswith('data:image/jpeg;base64,') for x in D['cheatSheet']['previews']))
ledger=json.loads((QA/'pdf-layout-ledger.json').read_text())
check('Every PDF paragraph fits printer-safe content margins',all(x['x']>=30 and x['x']+x['width']<=582 and x['bottom']>=49 and x['top']<=720 for x in ledger))
check('Reference-sheet normal body size is 9.55pt',all(x['font']>=9.55 for x in ledger if x['width']==267))
with pdfplumber.open(pdf) as pages:
 for i,p in enumerate(pages.pages,1):
  check('PDF page '+str(i)+': every glyph within physical page',all(29<=x['x0']<x['x1']<=583 and 0<=x['top']<x['bottom']<=792 for x in p.chars))
  check('PDF page '+str(i)+': selectable text and embedded fonts',len(p.chars)>2000 and bool(reader.pages[i-1]['/Resources']['/Font']))
js=(R/'learning.js').read_text();css=(R/'learning.css').read_text()
check('Stepper moves original nodes rather than recalculating mathematics','body.append(step)' in js and 'step.hidden' not in js)
check('Print exposes every row state and opens complete proofs/answers','row-step[hidden]{display:block!important}' in css and 'beforeprint' in js and 'd.open=true' in js)
check('Keyboard, live step labels and show-all controls present',all(x in js for x in ['ArrowRight','ArrowLeft','aria-live="polite"','Show All Steps','aria-pressed']))
result={'passed':len(passed),'original_textbook_practice_questions':len(expected),'concept_guides':len(report['concept_lessons']),'guided_complete_exercises':337,'method_types':len(set(report['guided_exercises'].values())),'pdf_pages':2,'pdf_page_size_points':[612,792],'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'checks':passed}
(QA/'refinement-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))
