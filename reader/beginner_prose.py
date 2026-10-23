"""Compile source reasoning into semantic teaching units, without word-count cuts.
Mathematical clauses become display expressions; logical implications stay ordered.
The source wording of each migrated paragraph is kept in the authoring record.
"""
import re,html,hashlib
from mathml import inline,math
from beginner_math import para,display,stage,final

def key(s):return hashlib.sha256(s.encode()).hexdigest()[:20]
# English words delimit mathematical expressions. Single-letter variables and
# recognizable matrix products/functions remain part of the expression.
MATHWORDS={'Span','rank','det','diag','sin','cos','AB','BA','AC','CA','BC','CB','CD','DC','AD','DA','AX','XA','BX','XB','Ax','Au','Av','Ap','Aq','Ac','Az','Bx','Tx','EA','AI','IA','IX','XI','ABC','ABx','cu','cv','du','dv','cf','ad','bc','ab','cd','ABCD','ADBC','PQ','QP'}
WORDS=re.compile(r'[A-Za-z]+')
def formula_runs(s):
 # Find maximal mathematical spans separated by prose words or sentence stops.
 bounds=[]
 for m in WORDS.finditer(s):
  word=m[0]
  if len(word)>1 and word not in MATHWORDS and not (word.isupper() and len(word)<=4) and not (m.start()>=2 and s[m.start()-2:m.start()]=='_{'):bounds.append((m.start(),m.end()))
 for m in re.finditer(r'[.!?:]|\*\*',s):bounds.append((m.start(),m.end()))
 bounds.sort();ranges=[];start=0
 for a,b in bounds:
  if a>start:ranges.append((start,a))
  start=max(start,b)
 if start<len(s):ranges.append((start,len(s)))
 out=[]
 for a,b in ranges:
  chunk=s[a:b];left=len(chunk)-len(chunk.lstrip(' ,;'));right=len(chunk.rstrip(' ,;'))
  chunk=chunk[left:right];a+=left;b=a+len(chunk)
  # A trailing variable after a prose comma belongs to the following clause.
  trailing=re.search(r',\s*[A-Za-z](?:[₀-₉]|_\d+)?$',chunk)
  if trailing:chunk=chunk[:trailing.start()];b=a+len(chunk)
  if not re.search(r'[=⇔⇒↦∈≠≤≥]',chunk) or re.search(r'[=⇔⇒↦∈≠≤≥]\s*$',chunk):continue
  # Avoid mangled fragments with unbalanced grouping. Their sentence remains
  # readable inline rather than pretending to display an invalid expression.
  if any(chunk.count(l)!=chunk.count(r) for l,r in [('(',')'),('[',']'),('{','}')]):continue
  if not re.search(r'[A-Za-z0-9₀-₉ℝθ]',chunk):continue
  out.append((a,b,chunk))
 return out

def sentence_units(raw):
 # A period ends a mathematical assertion; semicolons separate independent
 # cases/calculations. Logical contrasts get their own reasoning stage.
 sentences=re.split(r'(?<=[.!?])\s+(?=[A-Z“\[])|(?<=;)\s+(?=(?:[A-Za-z(\[]))',raw)
 out=[]
 for s in sentences:
  pieces=re.split(r'(?<=,)\s+(?=(?:so |hence |therefore |but |whereas ))',s)
  out.extend(p for p in pieces if p)
 return out

def author_paragraph(raw):
 units=sentence_units(raw)
 formulas=sum(len(formula_runs(s)) for s in units)
 meaningful=len(units)>1 and (formulas or re.search(r'\b(proof|pivot|consistent|independen\w*|dependen\w*|inverse|because|therefore|Thus|Hence|Conversely|linear|coefficient|free variable|span|row|column|matrix|solution|vector|scalar|coordinate|definition|parameter|theorem)\b',raw,re.I))
 if not meaningful and not (len(formula_runs(raw)) and raw.count('=')>=2):return None
 steps=[]
 for s in units:
  role='explanation'
  if re.match(r'(?:\*\*)?(?:If |Suppose |Let |Assume |Given |For .*assum)',s):role='condition'
  elif re.match(r'(?:Thus|Hence|Therefore|Consequently|This proves|So |Both |Every solution|The answer)',s):role='conclusion'
  elif re.match(r'(?:Conversely|For the reverse|For the other|For a superset)',s):role='reverse-direction'
  elif re.search(r'\b(because|since|preserv|reversib|definition)\b',s):role='justification'
  runs=formula_runs(s)
  if runs and role=='explanation':role='calculation'
  steps.append({'text':s,'role':role,'formulas':[{'start':a,'end':b,'expression':t} for a,b,t in runs]})
 return {'source':raw,'units':steps}

def render_paragraph(record):
 raw=record['source'];units=record['units'];out=[]
 for u in units:
  s=u['text'];runs=u['formulas'];pieces=[];pos=0
  for f in runs:
   prefix=s[pos:f['start']].strip()
   if prefix:pieces.append(para(prefix,'math-context'))
   pieces.append(display(f['expression']));pos=f['end']
  tail=s[pos:].strip()
  if tail and tail not in ['.',',',';']:pieces.append(para(tail,'math-context'))
  if not runs:pieces=[para(s)]
  out.append('<li class="reason-'+u['role']+'" data-source-piece="'+html.escape(s,quote=True)+'">'+''.join(pieces)+'</li>')
 return '<div class="teaching-reasoning" data-prose-key="'+key(raw)+'"><ol>'+''.join(out)+'</ol></div>'

def transform(raw_source,rendered,records):
 for raw in re.split(r'\n\s*\n',raw_source):
  raw=raw.strip()
  if not raw or raw.startswith(('#','@','**Step ','Independently derived')):continue
  raw=' '.join(raw.splitlines());k=key(raw);record=records.get(k)
  if not record:continue
  target=inline(raw)
  pattern=r'<p(?: [^>]*)?>'+re.escape(target)+r'</p>'
  rendered=re.sub(pattern,lambda m:render_paragraph(record),rendered)
 return rendered
