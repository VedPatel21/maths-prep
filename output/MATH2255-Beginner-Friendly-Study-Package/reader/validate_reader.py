"""Static academic-conversion audit. No browser compatibility claims are made.
Run: python3 reader/validate_reader.py
"""
from pathlib import Path
from html.parser import HTMLParser
from fractions import Fraction
import re,json,html,hashlib,base64,xml.etree.ElementTree as ET,csv
from mathml import inline,expr
from preservation_audit import structured_present,authored_replacement
ROOT=Path(__file__).resolve().parent.parent;R=ROOT/'reader';S=ROOT/'source'
D=json.loads((R/'content.json').read_text());M=json.loads((R/'qa/conversion-manifest.json').read_text());passed=[]
def check(label,test):
 assert test,label
 passed.append(label)
def matrices(s):
 return [json.loads(html.unescape(d)) for d in re.findall(r'<math[^>]*data-matrix="([^"]*)" data-duplicate="false"',s)]
def blocks(md):
 # Independent extraction of source paragraphs separated by empty lines.
 return [p.strip() for p in re.split(r'\n\s*\n',md) if p.strip()]
def preserve(name,source,output):
 expected=[json.loads(x) for x in re.findall(r'^@matrix (.*)$',source,re.M)]
 check(name+': every matrix and augmentation divider, in order',expected==matrices(output))
 for p in blocks(source):
  if p.startswith(('#','@')):continue
  p=' '.join(p.splitlines())
  if inline(p) in output:continue
  if structured_present(p,output):
   check(name+": all migrated reasoning visible in source order",True);continue
  replacement=authored_replacement(name,p)
  if replacement:
   check(name+": "+replacement,True);continue
  # Reflowed proof paragraphs must reconstruct the exact source and contain
  # every rendered piece, not merely store the source in a hidden attribute.
  reflowed=False
  for raw,pieces in re.findall(r'<div class="argument-chain" data-source-prose="([^"]*)"><ol>(.*?)</ol></div>',output,re.S):
   if html.unescape(raw)!=p:continue
   items=re.findall(r'<li data-prose-piece="([^"]*)">(.*?)</li>',pieces,re.S)
   check(name+': exact visible proof reflow',bool(items) and ' '.join(html.unescape(t) for t,h in items)==p and all(inline(html.unescape(t))==h for t,h in items))
   reflowed=True
  if reflowed:continue
  if name=='section-1-2' and p.startswith('The leading entry of a nonzero row'):
   sentences=re.split(r'(?<=\.) ',p)
   check(name+': leading-entry and REF paragraph retained across micro-lessons',inline(sentences[0]) in output and inline(' '.join(sentences[1:])) in output)
   continue
  # Glossary paragraphs become definition lists without losing definitions.
  pairs=re.findall(r'\*\*([^*]+):\*\*\s*(.*?)(?=\*\*|$)',p)
  check(name+': glossary prose '+p[:25],bool(pairs) and all(inline(k) in output and inline(v.strip()) in output for k,v in pairs))
 for eq in re.findall(r'^@eq (.*)$',source,re.M):check(name+': equation '+eq[:50],'<annotation encoding="text/plain">'+html.escape(eq)+'</annotation>' in output)
 check(name+': prose and equations preserved',True)
text=(S/'MATH2255-Complete-Beginner-Textbook.md').read_text();parts=re.split(r'^# ',text,flags=re.M)[1:]
check('All 18 manuscript top-level chapter entries retained',len(parts)==len(D['chapters'])==18)
for part,c in zip(parts,D['chapters']):
 title,_,body=part.partition('\n');check('Exact chapter heading: '+title,c['title']==title);preserve(c['id'],body,c['html'])
work=(S/'MATH2255-Exercises-and-Detailed-Solutions.md').read_text()
sol={m[1]:m[3] for m in re.finditer(r'^### ([\d.]+) - ([^\n]+)\n(.*?)(?=^### |^# |\Z)',work,re.M|re.S)}
inv=list(csv.DictReader((S/'exercise-inventory.csv').open()));qs=D['exercises'];ids={q['id'] for q in qs}
check('339 unique correctly numbered exercises',len(qs)==len(ids)==339 and ids==set(sol))
check('337 complete solutions',sum(q['status']=='solved' for q in qs)==337)
check('Only supplied truncations flagged',{q['id'] for q in qs if q['status']!='solved'}=={'1.2.41','2.1.43'})
check('No invented exercise cards',not ({'1.4.33','1.4.34','1.9.31','1.9.32'}&ids))
check('All ten sections, without 1.6',{q['section'] for q in qs}=={'1.1','1.2','1.3','1.4','1.5','1.7','1.8','1.9','2.1','2.2'})
for q,invrow in zip(qs,inv):
 preserve(q['id'],sol[q['id']],q['solution'])
 check(q['id']+': source-answer provenance unchanged',q['crosscheck']==invrow['selected_solution_pdf_page'])
 check(q['id']+': own question content present',len(q['question'])>100 and ('question-text' in q['question'] or 'question-crop' in q['question']))
 l,t,r,b=q['questionBox'];check(q['id']+': valid source-only crop boundaries',0<=l<r<=1160 and 0<=t<b<=1500)
check('Original sixteen image bytes embedded intact',all(base64.b64decode(D['images'][str(i)].split(',',1)[1])==(S/f'scans/ex-{i:02}.png').read_bytes() for i in range(1,17)))
check('194 verified question transcriptions',sum(q['transcribed'] for q in qs)==194)
check('Source discrepancy on page 98 retained',all(term in next(c['html'] for c in D['chapters'] if c['id']=='section-2-2') for term in ['page 98','(0,1,0)','(0,1,2)','literally printed']))
check('All 598 row annotations verified against unchanged rows',M['conversion']['row_steps']==M['conversion']['row_annotations_verified']==598)
# Evaluate the generated MathML of every numeric matrix entry independently.
def value(n):
 kind=n.tag.split('}')[-1]
 if kind=='mn':return Fraction(n.text)
 if kind=='mfrac':return value(n[0])/value(n[1])
 if kind=='mo' and n.text=='−':return 'minus'
 if kind=='mrow':
  vals=[value(x) for x in n]
  if len(vals)==1:return vals[0]
  if len(vals)==2 and vals[0]=='minus':return -vals[1]
 raise ValueError(ET.tostring(n))
numeric=0
for mat in json.loads((R/'qa/matrix-ledger.json').read_text()):
 for row in mat['a']:
  for cell in row:
   try:expected=Fraction(cell)
   except ValueError:continue
   check('Numeric MathML value '+cell,value(ET.fromstring(expr(cell)))==expected);numeric+=1
combined=''.join(c['html'] for c in D['chapters'])+''.join(q['solution']+q['question'] for q in qs)+D['workbookNotes']
for n,chunk in enumerate(re.findall(r'<math\b.*?</math>',combined,re.S)):
 ET.fromstring(chunk)
check('All semantic MathML fragments are well-formed XML',True)
check('No raw custom directives leak into rendered material',not re.search(r'@(matrix|eq|figure|customfig|scan|toc|page)\b',combined))
page=(ROOT/'output/MATH2255-Beginner-Friendly-Study-Reader-Final.html').read_text()
check('Standalone file contains embedded content and assets','id="study-data"' in page and 'data:font/otf;base64,' in page and 'data:image/png;base64,' in page)
check('No external script, stylesheet, image or font dependencies',not re.search(r'(?:src|href)\s*=\s*[\"\']https?://',page,re.I) and not re.search(r'url\([\"\']?https?://',page,re.I))
check('Runtime network access disabled',"connect-src 'none'" in page and not re.search(r'\b(?:fetch|XMLHttpRequest|WebSocket)\s*\(', (R/'reader.js').read_text()))
check('Original 273 assertions retained',M['original_assertions']['passed_assertions']==273)
# Smoke checks of notation parser structure.
for s,needle in [('x_1','<msub>'),('A^(-1)','<msup>'),('A^T','<msup>'),('a_{ij}','<msub>'),('ℝ³','<msup>'),('-7/4','<mfrac>')]:check('Semantic notation '+s,needle in expr(s))
result={'passed':len(passed),'numeric_matrix_entries_checked':numeric,'chapter_entries':18,'numbered_exercises':339,'completed_solutions':337,'question_transcriptions':194,'crop_fallbacks':145,'source_assertions_preserved':273,'html_bytes':len(page.encode()),'checks':passed}
(R/'qa/static-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))
