"""Build the self-contained reader with stdlib Python + the bundled source assets.
Run from any directory: python3 reader/build_reader.py
"""
from pathlib import Path
import re,json,base64,html,hashlib,csv
from fractions import Fraction
import mathml
from mathml import inline,math,matrix
from beginner_math import row_arithmetic
from diagrams import figure,CAPTIONS,svg
from questions import Q
from learning import refine_chapters,REPORT as LEARNING_REPORT
ROOT=Path(__file__).resolve().parent.parent;HERE=ROOT/'reader';SRC=ROOT/'source';OUT=ROOT/'output';OUT.mkdir(exist_ok=True)
E=html.escape
stats={'matrices':0,'equations':0,'row_steps':0,'row_annotations_verified':0,'figures':0,'unknown_directives':[]}
MATRICES=[]
def slug(s):return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
def blockparse(md):
 blocks=[];buf=[]
 def flush():
  if buf:blocks.append(('p',' '.join(buf)));buf.clear()
 for line in md.splitlines():
  if not line.strip():flush()
  elif line.startswith('#'):
   flush();m=re.match(r'^(#+) (.*)',line);blocks.append(('h'+str(len(m[1])),m[2]))
  elif line.startswith('@'):
   flush();p=line.split(' ',1);blocks.append((p[0],p[1] if len(p)>1 else ''))
  else:buf.append(line)
 flush();return blocks

def crop(p,b,alt):
 l,t,r,bot=b;w=r-l;h=bot-t
 return f'<div class="scan-scroll" tabindex="0" role="region" aria-label="Original question crop; scroll horizontally to read on a phone"><svg class="question-crop" viewBox="{l} {t} {w} {h}" style="--crop-width:{w}px" role="img" aria-label="{E(alt,quote=True)}"><title>{E(alt)}</title><image data-page="{p}" width="1160" height="1500"/></svg></div>'

def render(md):
 b=blockparse(md);out=[];sections=False;last_matrix=None;i=0
 while i<len(b):
  typ,s=b[i]
  if typ=='h2':
   if sections:out.append('</section>')
   out.append(f'<section class="lesson" id="{slug(s)}"><h2>{inline(s)}</h2>');sections=True;last_matrix=None
  elif typ.startswith('h'):out.append(f'<{typ} id="{slug(s)}">{inline(s)}</{typ}>')
  elif typ=='@page':pass
  elif typ=='@toc':out.append('<p class="note">Use the chapter navigation or <a href="#topics">Explore Topics</a> to open any chapter.</p>')
  elif typ=='@matrix':
   d=json.loads(s);stats['matrices']+=1;MATRICES.append(d);out.append(matrix(d));last_matrix=d
  elif typ=='@eq':
   stats['equations']+=1;out.append('<div class="math-scroll equation" tabindex="0" role="region" aria-label="Equation; scroll horizontally if needed">'+math(s,True)+'</div>')
  elif typ in ['@figure','@customfig']:
   assert s in CAPTIONS,s;stats['figures']+=1;out.append(figure(s))
  elif typ=='@scan':
   p=int(re.search(r'\d+',s).group());out.append(f'<details class="source-page"><summary>View original exercise PDF page {p}</summary><div class="scan-scroll"><img data-page="{p}" alt="Original exercise PDF page {p}" class="full-scan"></div></details>')
  elif typ.startswith('@'):stats['unknown_directives'].append(typ);raise ValueError(typ)
  elif typ=='p':
   if s.startswith('**Step ') and last_matrix and i+1<len(b) and b[i+1][0]=='@matrix':
    nxt=json.loads(b[i+1][1]);changed=[];pivot=None
    try:
     a=[[Fraction(x) for x in r] for r in last_matrix['a']];c=[[Fraction(x) for x in r] for r in nxt['a']]
     assert len(a)==len(c) and all(len(x)==len(y) for x,y in zip(a,c))
     changed=[j for j in range(len(a)) if a[j]!=c[j]]
     op=s.split('**')[1];rn=[int(x)-1 for x in re.findall(r'R(\d+)',op)]
     expected=set(rn[:2] if '↔' in op else rn[:1]);assert set(changed)<=expected
     source=rn[-1];pc=next((j for j,v in enumerate(a[source]) if v),None)
     if pc is not None:pivot=(source,pc)
     stats['row_annotations_verified']+=1
    except (ValueError,AssertionError,IndexError,TypeError):changed=[];pivot=None
    stats['row_steps']+=1;stats['matrices']+=1;MATRICES.append(nxt)
    out.append('<section class="row-step"><p class="operation">'+inline(s)+'</p><div class="matrix-pair"><div><span class="math-label">Before</span>'+matrix(last_matrix,changed,pivot,True)+'</div><div><span class="math-label">After</span>'+matrix(nxt,changed)+'</div></div><p class="key">Lavender: affected row'+('s' if len(changed)>1 else '')+'.'+(' Sage: pivot used.' if pivot else '')+'</p>'+row_arithmetic(last_matrix,nxt,s)+'</section>');last_matrix=nxt;i+=1
   elif s.startswith('**Augmented matrix:**') or ('**Basic variable:**' in s and '**Coefficient:**' in s) or s.startswith('**Free variable:**') or s.startswith('**Matrix dimensions:**') or s.startswith('**Reduced echelon form:**'):
    entries=re.findall(r'\*\*([^*]+):\*\*\s*(.*?)(?=\*\*|$)',s)
    out.append('<dl class="glossary">'+''.join('<div><dt>'+inline(k)+'</dt><dd>'+inline(v.strip())+'</dd></div>' for k,v in entries)+'</dl>')
   else:
    style=''
    if re.match(r'^\*\*(Definition|In simple|Intuition|Common mistake|Important|Theorem|Verification|Final|Read the equations|Source|Coverage)',s,re.I):
     k=re.match(r'^\*\*([^*.]+)',s)[1].lower();style=' class="callout '+('verify' if 'verification' in k or 'final' in k else 'caution' if 'mistake' in k or 'source' in k or 'coverage' in k else 'concept')+'"'
    elif s.startswith('**Worked '):style=' class="worked"'
    if re.match(r'^[-*] ',s):out.append('<ul>'+''.join('<li>'+inline(t)+'</li>' for t in re.split(r'(?:^|\s)[-*] ',s)[1:])+'</ul>')
    else:out.append('<p'+style+'>'+inline(s)+'</p>')
  i+=1
 if sections:out.append('</section>')
 return ''.join(out)

def question(id,seen=None):
 q=Q[id];out=[]
 if 'text' in q:out.append('<div class="question-text">'+render(q['text'])+'</div>')
 else:
  if q['instruction']:out.append('<p>'+inline(q['instruction'])+'</p>')
  out.append(crop(q['page'],q['box'],'Original statement of Exercise '+id+'. '+q['instruction']))
 for p,l,t,r,b in q.get('extra',[]):out.append(crop(p,[l,t,r,b],'Source figure or shared mathematical data for Exercise '+id))
 for ref in q.get('dependencies',[]):
  rq=Q[ref];out.append('<div class="given-reference"><h3>Given in Exercise '+ref+'</h3>')
  out.append(render(rq['text']) if 'text' in rq else ('<p>'+inline(rq['instruction'])+'</p>'+crop(rq['page'],rq['box'],'Referenced question '+ref)))
  out.append('</div>')
 return ''.join(out)

textbook=(SRC/'MATH2255-Complete-Beginner-Textbook.md').read_text();workbook=(SRC/'MATH2255-Exercises-and-Detailed-Solutions.md').read_text()
parts=re.split(r'^# ',textbook,flags=re.M)[1:];chapters=[]
for i,part in enumerate(parts):
 title,_,body=part.partition('\n');num=re.match(r'^(\d+)\.',title);section=re.search(r'Section ([\d.]+)',title)
 id='section-'+section[1].replace('.','-') if section else {'0':'foundations','11':'proofs','12':'practice-answers','13':'reference','14':'sources'}.get(num[1] if num else '',slug(title))
 if title=='Contents':id='contents'
 if title.startswith('MATH 2255'):id='about'
 if title.startswith('How to'):id='how-to'
 chapters.append({'id':id,'title':title,'section':section[1] if section else None,'html':render(body),'headings':[{'title':s,'id':slug(s)} for t,s in blockparse(body) if t.startswith('h')],'source':body})
solutions={m[1]:{'title':m[2],'source':m[3]} for m in re.finditer(r'^### ([\d.]+) - ([^\n]+)\n(.*?)(?=^### |^# |\Z)',workbook,re.M|re.S)}
inventory=list(csv.DictReader((SRC/'exercise-inventory.csv').open()))
exercises=[]
for item in inventory:
 id=item['section']+'.'+item['exercise'];s=solutions[id];q=Q[id]
 exercises.append({'id':id,'section':item['section'],'number':int(item['exercise']),'title':s['title'],'status':item['status'],'crosscheck':item['selected_solution_pdf_page'],'page':q['page'],'question':question(id),'questionBox':q['box'],'transcribed':'text' in q,'solution':render(s['source']),'source':s['source']})
# Refine the existing content after the exact academic conversion.
from beginner_content import revise
revise(chapters,exercises)
from beginner_content import REPORT as BEGINNER_REPORT
LEARNING_REPORT['guided_exercises']={k:v['method'] for k,v in BEGINNER_REPORT['exercises'].items() if v['status']=='structured'}
(HERE/'qa/final/learning-manifest.json').write_text(json.dumps(LEARNING_REPORT,ensure_ascii=False,indent=2))
# Preserve workbook front matter, reading directions, section introductions, and back matter.
notes=[]
for part in re.split(r'^# ',workbook,flags=re.M)[1:]:
 title,_,body=part.partition('\n')
 if title=='Contents':continue
 if title.startswith('Section '):
  body=body.split('## Original exercises')[0]
  notes.append('<h2>'+inline(title)+'</h2>'+render(body))
 else:notes.append('<h2>'+inline(title)+'</h2>'+render(body))
# Include the redistributed font's notice and licence in the standalone reader.
licence=(HERE/'assets/FONT-NOTICE.txt').read_text()+'\n\n'+(HERE/'assets/OFL.txt').read_text()
next(c for c in chapters if c['id']=='sources')['html']+='<details class="source-page font-license"><summary>Typeface attribution and licence</summary><pre>'+E(licence)+'</pre></details>'
# Retain all originals independently of the visible conversion.
images={}
for p in range(1,17):images[str(p)]='data:image/png;base64,'+base64.b64encode((SRC/f'scans/ex-{p:02}.png').read_bytes()).decode()
fontpath=HERE/'assets/STIXTwoMath.otf'
if not fontpath.exists():fontpath=Path('/System/Library/Fonts/Supplemental/STIXTwoMath.otf')
(HERE/'assets/STIXTwoMath.otf').write_bytes(fontpath.read_bytes())
font=base64.b64encode(fontpath.read_bytes()).decode()
sheetpath=OUT/'pdf/MATH2255-Two-Sided-Cheat-Sheet.pdf'
if not sheetpath.exists():sheetpath=ROOT/sheetpath.name
sheet={'name':sheetpath.name,'pdf':base64.b64encode(sheetpath.read_bytes()).decode(),'previews':['data:image/jpeg;base64,'+base64.b64encode((HERE/f'assets/cheat-sheet/side-{i}.jpg').read_bytes()).decode() for i in [1,2]]}
data={'cheatSheet':sheet,'chapters':[{k:v for k,v in c.items() if k!='source'} for c in chapters],'exercises':[{k:v for k,v in e.items() if k!='source'} for e in exercises],'images':images,'workbookNotes':''.join(notes)}
manifest={'chapters':[{'id':c['id'],'title':c['title'],'source_sha256':hashlib.sha256(c['source'].encode()).hexdigest()} for c in chapters], 'exercises':[{'id':e['id'],'status':e['status'],'page':e['page'],'source_sha256':hashlib.sha256(e['source'].encode()).hexdigest(),'transcribed':e['transcribed']} for e in exercises], 'conversion':stats,'original_assertions':json.loads((SRC/'mathematical-qa.json').read_text()),'renderer':'Native semantic MathML with embedded STIX Two Math font. No runtime dependencies or network fetches.'}
(HERE/'qa/conversion-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
(HERE/'qa/matrix-ledger.json').write_text(json.dumps(MATRICES,ensure_ascii=False))
(HERE/'content.json').write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')))
for k in CAPTIONS:(HERE/'assets/diagrams'/f'{k}.svg').write_text(svg(k))
css=(HERE/'reader.css').read_text()+'\n'+(HERE/'learning.css').read_text()+'\n'+(HERE/'beginner.css').read_text();js=(HERE/'reader.js').read_text()+'\n'+(HERE/'learning.js').read_text();shell=(HERE/'shell.html').read_text()
output=shell.replace('/* FONT */',f'@font-face{{font-family:StudyMath;src:url(data:font/otf;base64,{font}) format("opentype");font-display:swap}}').replace('/* CSS */',css).replace('/* DATA */',json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')).replace('/* JS */',js)
(OUT/'MATH2255-Beginner-Friendly-Study-Reader-Final.html').write_text(output)
print(json.dumps({'chapters':len(chapters),'exercises':len(exercises),'transcribed':sum(e['transcribed'] for e in exercises),'size_MB':round(len(output.encode())/1e6,2),'conversion':stats},indent=2))
