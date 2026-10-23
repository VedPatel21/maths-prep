"""Package the final self-contained HTML, source manuscripts, code and QA."""
from pathlib import Path
import json,zipfile,hashlib,shutil
ROOT=Path(__file__).resolve().parent.parent;R=ROOT/'reader';OUT=ROOT/'output'
html=OUT/'MATH2255-Beginner-Friendly-Study-Reader-Final.html';archive=OUT/'MATH2255-Beginner-Friendly-Study-Package.zip'
reader_files=['README.md','shell.html','reader.css','reader.js','mathml.py','diagrams.py','questions.py','question-index.json','build_reader.py','validate_reader.py','package_reader.py','learning.py','learning.css','learning.js','build_cheat_sheet.py','validate_refinement.py','beginner_content.py','beginner_math.py','beginner_prose.py','authored_lessons.py','workbook_teaching.py','parameter_lessons.py','proof_contexts.py','beginner.css','preservation_audit.py','validate_beginner.py','export_manuscripts.py']
pdf=OUT/'pdf/MATH2255-Two-Sided-Cheat-Sheet.pdf'
if not pdf.exists():pdf=ROOT/pdf.name
files=[(html,html.name),(pdf,pdf.name),(R/'README.md','README.md')]
for name in reader_files:
 files.append((R/name,'reader/'+name))
for folder in ['assets','qa']:
 for p in (R/folder).rglob('*'):
  if p.is_file() and not p.name.startswith(('ocr','desktop-incomplete')):files.append((p,str(p.relative_to(ROOT))))
for p in (ROOT/'source').rglob('*'):
 if p.is_file() and '__pycache__' not in p.parts and not p.name.startswith('.'):files.append((p,str(p.relative_to(ROOT))))
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=7) as z:
 for p,name in files:z.write(p,name)
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None
 assert z.read(html.name)==html.read_bytes()
 assert z.read(pdf.name)==pdf.read_bytes()
 for p,name in files:assert z.read(name)==p.read_bytes(),name
 names=set(z.namelist())
 assert all(f'source/scans/ex-{i:02}.png' in names for i in range(1,17))
 assert 'reader/assets/OFL.txt' in names
manifest={'pdf':{'file':pdf.name,'bytes':pdf.stat().st_size,'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest()},'html':{'file':html.name,'bytes':html.stat().st_size,'sha256':hashlib.sha256(html.read_bytes()).hexdigest()},'package':{'file':archive.name,'bytes':archive.stat().st_size,'entries':len(files),'crc':'passed','sha256':hashlib.sha256(archive.read_bytes()).hexdigest()},'content':{'chapter_entries':18,'course_sections':10,'numbered_exercises':339,'complete_solutions':337,'incomplete_ids':['1.2.41','2.1.43']},'validation':{'source_preservation':json.loads((R/'qa/static-validation.json').read_text())['passed'],'beginner_acceptance':json.loads((R/'qa/beginner/acceptance-validation.json').read_text())['passed'],'refinement':json.loads((R/'qa/final/refinement-validation.json').read_text())['passed']}}
(OUT/'MATH2255-Beginner-Friendly-Delivery.json').write_text(json.dumps(manifest,indent=2))
shutil.copyfile(R/'README.md',OUT/'MATH2255-Beginner-Friendly-README.md')
print(json.dumps(manifest,indent=2))
