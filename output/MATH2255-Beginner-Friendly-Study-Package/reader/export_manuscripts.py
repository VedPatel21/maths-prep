"""Export the fully revised reader as editable Markdown plus separate SVGs.
Rebuild inputs are original manuscripts + source/teaching/beginner-content.json.
These exports make the complete resulting teaching sequence reviewable in text.
Requires lxml (also used by the extended acceptance audit).
"""
from pathlib import Path
from lxml import html,etree
import json,re,hashlib,html as html_lib
ROOT=Path(__file__).resolve().parent.parent
DEST=ROOT/'source/teaching';FIG=DEST/'figures';FIG.mkdir(parents=True,exist_ok=True)
DATA=json.loads((ROOT/'reader/content.json').read_text())
def svg_file(m):
 raw=m[0]
 raw=re.sub(r'<image data-page="(\d+)"',lambda x:'<image href="../../scans/ex-'+x[1].zfill(2)+'.png"',raw)
 if 'xmlns=' not in raw.split('>')[0]:raw=raw.replace('<svg','<svg xmlns="http://www.w3.org/2000/svg"',1)
 name=hashlib.sha256(raw.encode()).hexdigest()[:16]+'.svg';(FIG/name).write_text(raw)
 label=re.search(r'aria-label="([^"]+)"',raw)
 label=html_lib.unescape(label[1]) if label else 'Mathematical illustration'
 return '<img src="figures/'+name+'" alt="'+html_lib.escape(label,quote=True)+'">'
def inline(node):
 return (node.text or '')+''.join(convert(c)+(c.tail or '') for c in node)
def convert(n):
 tag=n.tag if isinstance(n.tag,str) else ''
 if tag=='math':
  if n.get('data-matrix'):return '\n\n@matrix '+n.get('data-matrix')+'\n\n'
  annotations=n.xpath('.//annotation[@encoding="text/plain"]/text()')
  if annotations:
   s=annotations[0]
   return '\n\n@eq '+s+'\n\n' if n.get('display')=='block' else '`'+s+'`'
  return etree.tostring(n,encoding='unicode',with_tail=False)
 if tag=='img':return '!['+n.get('alt','Diagram').replace(']','\\]')+']('+n.get('src','')+')'
 text=inline(n)
 if tag in ['script','style']:return ''
 if re.fullmatch(r'h[1-6]',tag):return '\n\n'+'#'*int(tag[1])+' '+text.strip()+'\n\n'
 if tag in ['strong','b']:return '**'+text+'**'
 if tag=='em':return '*'+text+'*'
 if tag=='a':
  href=n.get('href','');return '['+text+']('+href+')' if href and not href.startswith(('blob:','data:')) else text
 if tag=='br':return '\n'
 if tag=='li':return '\n- '+text.strip()+'\n'
 if tag in ['ul','ol']:return '\n'+text+'\n'
 if tag=='table':
  rows=[]
  for row in n.xpath('.//tr'):
   cells=[re.sub(r'\s+',' ',inline(c)).strip().replace('|','\\|') for c in row if c.tag in ['th','td']]
   if cells:rows.append('| '+' | '.join(cells)+' |')
  if len(rows)>1:rows.insert(1,'| '+' | '.join(['---']*len(n.xpath('.//tr')[0]))+' |')
  return '\n\n'+'\n'.join(rows)+'\n\n'
 if tag=='summary':return '\n\n**'+text.strip()+'**\n\n'
 if tag in ['p','div','section','details','figure','figcaption','dl','dt','dd']:return '\n\n'+text.strip()+'\n\n'
 return text
def export(s):
 s=re.sub(r'<svg\b.*?</svg>',svg_file,s,flags=re.S)
 tree=html.fromstring('<div>'+s+'</div>')
 return re.sub(r'\n[ \t]+\n','\n\n',re.sub(r'\n{3,}','\n\n',convert(tree))).strip()+'\n'
intro='''> Fully revised teaching manuscript exported from the delivered reader. Native display equations use @eq; complete matrices use @matrix JSON. Figures are editable SVGs. The build uses the original source manuscripts plus beginner-content.json as its canonical teaching records; edit those records to persist changes, then rebuild and export again.\n\n'''
textbook=intro+'\n\n'.join('# '+c['title']+'\n\n'+export(c['html']) for c in DATA['chapters'])
workbook=intro
for q in DATA['exercises']:
 workbook+='## '+q['id']+' · '+q['title']+'\n\n'+export(q['question'])+'\n\n### Explanation\n\n'+export(q['solution'])+'\n\n'
for name,text in [('MATH2255-Beginner-Friendly-Textbook.md',textbook),('MATH2255-Beginner-Friendly-Workbook.md',workbook)]:
 assert 'data:image/' not in text
 (DEST/name).write_text(text)
print(json.dumps({'textbook_bytes':len(textbook.encode()),'workbook_bytes':len(workbook.encode()),'editable_figures':len(list(FIG.glob('*.svg')))},indent=2))
