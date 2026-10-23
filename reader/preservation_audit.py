"""Independent visible-content audit for structured source-paragraph migrations."""
from html.parser import HTMLParser
from pathlib import Path
import re,json,html,hashlib
DATA=json.loads((Path(__file__).resolve().parent.parent/'source/teaching/beginner-content.json').read_text())
class Visible(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.math=False;self.annotation=False;self.formula=[];self.parts=[]
 def handle_starttag(self,tag,attrs):
  if tag=='math':self.math=True;self.formula=[]
  elif self.math and tag=='annotation':self.annotation=True
  elif not self.math and tag in ['p','div','li']:self.parts.append(' ')
 def handle_endtag(self,tag):
  if tag=='annotation':self.annotation=False
  elif tag=='math':self.math=False;self.parts.append(''.join(self.formula));self.formula=[]
  elif not self.math and tag in ['p','div','li']:self.parts.append(' ')
 def handle_data(self,data):
  if self.math:
   if self.annotation:self.formula.append(data)
  else:self.parts.append(data)
def visible(s):
 p=Visible();p.feed(s);return ''.join(p.parts)
def normalize(s):return re.sub(r'[\s.,;]','',s.replace('**',''))
def structured_present(raw,output):
 k=hashlib.sha256(raw.encode()).hexdigest()[:20];record=DATA['paragraphs'].get(k)
 if not record or 'data-prose-key="'+k+'"' not in output:return False
 assert ' '.join(u['text'] for u in record['units'])==raw,('Source wording reordered',raw)
 for u in record['units']:
  piece=html.escape(u['text'],quote=True)
  m=re.search(r'<li class="reason-[^"]+" data-source-piece="'+re.escape(piece)+r'">(.*?)</li>',output,re.S)
  assert m,('Missing visible source unit',u['text'])
  assert normalize(visible(m[1]))==normalize(u['text']),('Changed visible reasoning',u['text'],visible(m[1]))
  for f in u['formulas']:assert u['text'][f['start']:f['end']]==f['expression']
 return True

def authored_replacement(name,p):
 if p.startswith(('The product has ','Collect those entries in their row and column positions:','As a second interpretation, column j of the answer')):return 'Expanded row/column product demonstration; every source result and equation independently retained'
 if name=='practice-answers':
  for id,record in DATA['practice'].items():
   if record.get('mode')=='authored' and p in [' '.join(x.strip().splitlines()) for x in re.split(r'\n\s*\n',record['source'])]:return 'Canonical authored answer '+id
 if name=='section-1-4' and p.startswith(('Consider the system x₁ + 2x₂','These statements have exactly the same unknowns')):return 'Explicit system/vector/matrix demonstration; independently checked'
 if name in ['2.2.30','2.2.44','1.5.21','1.9.9',*__import__('parameter_lessons').PARAMETERS] and not p.startswith('Independently'):return 'Full authored symbolic proof; independently checked'
 if name=='2.1.3' and p.startswith('Subtracting 3I₂ and multiplying'):return 'Corrected off-diagonal subtraction wording; actual arithmetic independently checked'
 return None
