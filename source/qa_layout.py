from pathlib import Path
import json,sys,re
import pdfplumber,pypdfium2 as pdfium
from PIL import Image,ImageDraw
from build_math2255 import ROOT,SRC,OUT,pdfmetrics
report={}
for tag,name in [('textbook','MATH2255-Complete-Beginner-Textbook'),('workbook','MATH2255-Exercises-and-Detailed-Solutions')]:
 pdf=OUT/(name+'.pdf');d=ROOT/'tmp/pdfs'/('final_'+tag);d.mkdir(parents=True,exist_ok=True)
 doc=pdfium.PdfDocument(str(pdf));texts=[];outside=[];empty=[];markers={}
 with pdfplumber.open(pdf) as pp:
  for i,page in enumerate(pp.pages,1):
   t=page.extract_text() or '';texts.append(t)
   for ch in page.chars:
    if 48 < ch['top'] < 742 and ch['text'].strip() and (ch['x0']<49 or ch['x1']>564):outside.append({'page':i,'text':ch['text'],'x0':ch['x0'],'x1':ch['x1']})
   if len(t)<100 and not page.images:empty.append(i)
   for term in ['0.6 Reading','3.4 Span','2.1.13','1.3.3 -','1.8.13 -','1.8.18 -','1.9.13 -','1.9.14 -','2.2.41 -','2.2.46 -','10.7 A larger','2.2.32 -']:
    if term in t:markers[term]=i
   img=doc[i-1].render(scale=1.05).to_pil().convert('RGB');img.save(d/f'p-{i:03}.jpg',quality=85)
 for start in range(1,len(doc)+1,20):
  sheet=Image.new('RGB',(1500,1660),'#d8dfe2');dr=ImageDraw.Draw(sheet)
  for k,i in enumerate(range(start,min(start+20,len(doc)+1))):
   im=Image.open(d/f'p-{i:03}.jpg');im.thumbnail((290,386));x=(k%5)*300+5;y=(k//5)*415+20;sheet.paste(im,(x,y));dr.text((x,y-15),f'{tag} p. {i}',fill='black')
  sheet.save(d/f'contact-{start:03}.jpg',quality=92)
 joined='\n'.join(texts)
 report[tag]={'pages':len(doc),'outside_body_bounds':outside,'suspect_empty_pages':empty,'sample_markers':markers,'literal_caret_count':joined.count('^'),'replacement_character_count':joined.count('\ufffd')}
 (d/'extracted.txt').write_text(joined)
 print(tag,json.dumps(report[tag],ensure_ascii=False)[:3000],flush=True)
(SRC/'layout-qa.json').write_text(json.dumps(report,indent=2))
