"""Two US Letter PDF pages, intended as the front and back of a study sheet.
Requires reportlab; the reading website itself has no Python dependency.
"""
from pathlib import Path
import sys,re,html,json
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'source'))
from build_math2255 import fmt as source_fmt
def fmt(t):
 return re.sub(r"_([A-Z])",r"<sub>\1</sub>",source_fmt(t))
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
OUT=ROOT/'output/pdf';OUT.mkdir(exist_ok=True)
P=OUT/'MATH2255-Two-Sided-Cheat-Sheet.pdf'
INK=colors.HexColor('#272537');PURPLE=colors.HexColor('#62478c');BORDER=colors.HexColor('#cfd2da')
styles={
 'p':ParagraphStyle('p',fontName='Body',fontSize=9.55,leading=12.5,textColor=INK,spaceAfter=5),
 'small':ParagraphStyle('small',fontName='Body',fontSize=8.3,leading=10.5,textColor=INK),
 'title':ParagraphStyle('title',fontName='Bold',fontSize=10.7,leading=13,textColor=PURPLE),
}
c=canvas.Canvas(str(P),pagesize=(612,792),pageCompression=1);c.setTitle('MATH 2255 - Two-sided study reference');c.setAuthor('MATH 2255 Visual Study Reader')
ledger=[]
def para(txt,x,y,w,sty='p'):
 p=Paragraph(fmt(txt),styles[sty]);pw,h=p.wrap(w,800);p.drawOn(c,x,y-h);ledger.append({'page':page,'text':txt,'x':x,'top':y,'bottom':y-h,'width':w,'font':styles[sty].fontSize});return y-h-5

def matrix(a,x,cy,size=10,bar=None):
 cw=max(25,max(pdfmetrics.stringWidth(str(v),'Body',size)+8 for row in a for v in row));rh=13;w=len(a[0])*cw+14;h=len(a)*rh+8;left=x;right=x+w;top=cy+h/2;bottom=cy-h/2
 c.setStrokeColor(INK);c.setLineWidth(.7)
 for xx,sgn in [(left,1),(right,-1)]:
  c.line(xx,bottom,xx,top);c.line(xx,bottom,xx+4*sgn,bottom);c.line(xx,top,xx+4*sgn,top)
 if bar is not None:c.line(left+7+bar*cw,bottom+1,left+7+bar*cw,top-1)
 for i,row in enumerate(a):
  for j,v in enumerate(row):
   xx=left+7+(j+.5)*cw;yy=top-4-(i+.5)*rh
   c.setFillColor(INK);c.setFont('Body',size)
   if '/' in str(v):
    num,den=str(v).split('/');c.setFont('Body',size*.8);c.drawCentredString(xx,yy+3,num);c.drawCentredString(xx,yy-6,den);c.line(xx-6,yy+1,xx+6,yy+1)
   else:c.drawCentredString(xx,yy-3,str(v))
 return w,h

def card(title,items,x,y,w=267):
 y=para(title,x,y,w,'title');c.setStrokeColor(BORDER);c.line(x,y+2,x+w,y+2);y-=5
 for item in items:
  if isinstance(item,str):y=para(item,x,y,w)
  elif item[0]=='inverse':
   # A^-1 = 1/(ad-bc) times the adjugate: fraction and matrix drawn as vectors.
   y-=28;c.setFont('Body',11);c.setFillColor(INK);c.drawString(x+10,y-3,'A');c.setFont('Body',7.5);c.drawString(x+18,y+4,'-1');c.setFont('Body',11);c.drawString(x+29,y-3,'=');
   cx=x+80;c.setFont('Body',10);c.drawCentredString(cx,y+6,'1');c.line(cx-25,y+2,cx+25,y+2);c.drawCentredString(cx,y-10,'ad - bc');matrix([['d','-b'],['-c','a']],x+120,y);y-=30
  elif item[0]=='matrix':
   a,bar=item[1:];h=len(a)*16+8;y-=h/2+2;matrix(a,x+(w-(len(a[0])*26+14))/2,y,bar=bar);y-=h/2+7
  elif item[0]=='pair':
   label,a=item[1:];yy=y-17;y=para(label,x,y,145);matrix(a,x+173,yy,size=9.3);y=min(y,yy-20)
 c.setStrokeColor(BORDER);y-=10
 assert y>49,(page,title,y)
 return y

def header(side,title):
 c.setFillColor(PURPLE);c.setFont('Bold',9);c.drawString(30,762,'MATH 2255  /  LINEAR ALGEBRA');c.setFillColor(INK);c.setFont('Body',20);c.drawString(30,736,title)
 para('Printable study reference. The supplied documents do not confirm examination permission.',30,720,552,'small')
 c.setStrokeColor(BORDER);c.line(30,700,582,700);c.setFont('Body',8);c.setFillColor(INK);c.drawString(30,27,'US Letter  •  Print at actual size (100%)  •  Duplex: flip on the long edge');c.drawRightString(582,27,f'Side {side} / 2')
page=1;header(1,'Systems, vectors & linear mappings')
y=686
for title,items in [
('01  Read the system, then reduce',[
'**A** is m × n: m equations, n unknowns. In [A | b], the final column is data, not an extra unknown.',
'**Legal row operations:** interchange two rows; multiply a row by c ≠ 0; add c times another retained row. Apply the operation to the entire row, including b.',
'**Forward:** move left to right, place a nonzero pivot, clear below; skip an unavailable column. **Backward:** normalize pivots to 1 and clear above.']),
('02  REF, RREF & pivot locations',[
'**REF:** zero rows last; leading entries move strictly right; zeros below every leading entry. Leading entries need not be 1.',
'**RREF:** REF + each leading entry is 1 + each pivot 1 is alone in its column. RREF is unique; ordinary REF is not.',
'**Pivot columns:** use the original column indices corresponding to leading 1s in RREF. A numerical pivot during elimination may change.']),
('03  Read the answer after elimination',[
'**No solution:** an echelon row [0 ... 0 | c], c ≠ 0. Equivalently, the appended column is a pivot column.',
'**Consistent + no free variables:** one solution. **Consistent + a free variable:** infinitely many. A zero row [0 ... 0 | 0] is harmless.',
'If rank(A) = r, the number of free variables is n - r. Assign a different real parameter to each free variable.',
'**Template:** x = p + s₁v₁ + ... + s_k v_k, where Ap = b and Av_j = 0. Homogeneous: b = 0, so p may be 0.']),
('04  A complete parameter example',[
('matrix',[[1,2,-1,4],[0,0,0,0]],3),
'x₂ = s, x₃ = t; x₁ = 4 - 2s + t. Thus x = (4,0,0) + s(-2,1,0) + t(1,0,1), s,t ∈ ℝ.',
'**Check:** (4 - 2s + t) + 2s - t = 4. The redundant second equation adds no restriction.'])]:y=card(title,items,30,y)
y=686
for title,items in [
('05  Vectors, combinations & span',[
'Add matching coordinates; a scalar multiplies every coordinate. cu + dv is a linear combination. Zero weights are allowed.',
'**Ax = b** means x₁a₁ + ... + x_n a_n = b, with a_j the columns of A. Solve [A | b] for the weights.',
'**b ∈ Span{a₁,...,a_n} ⇔ Ax = b is consistent.** One nonzero direction spans a line; two independent directions span a plane. Every span contains 0.']),
('06  Independence = no redundant direction',[
'**Test:** solve Ac = 0 with the vectors as columns. Only c = 0 ⇒ independent. A solution with some c_j ≠ 0 ⇒ dependent.',
'**Dependence relation:** c₁v₁ + ... + c_p v_p = 0 with weights not all zero. Rearrange a nonzero-weight term to exhibit redundancy.',
'Any collection containing 0 is dependent. Two vectors are dependent iff one is a scalar multiple of the other. More than n vectors in ℝ^n are dependent; the converse is false.']),
('07  From a rule to a standard matrix',[
'**Linearity:** T(u + v) = T(u) + T(v) and T(cu) = cT(u), for all allowed u,v,c. T(0) = 0 is necessary, not sufficient.',
'**A = [T(e₁) ... T(e_n)].** Domain ℝ^n counts columns; codomain ℝ^m counts rows. Then T(x) = Ax.',
'**Composition:** first S, then T gives A_T A_S. The rightmost action happens first.']),
('08  Keep existence & uniqueness separate',[
'For A of size m × n and T: ℝ^n → ℝ^m:',
'**Onto ⇔ columns span ℝ^m ⇔ pivot in every row ⇔ Ax = b solvable for every b in the codomain.**',
'**One-to-one ⇔ columns independent ⇔ pivot in every column ⇔ Ax = 0 has only the trivial solution.**',
'A 3 × 5 matrix with 3 pivots is onto ℝ³, with 2 free variables. Every b is attainable, but no solution is unique.'])]:y=card(title,items,315,y)
c.showPage();page=2;header(2,'Matrix algebra, inverses & methods')
y=686
for title,items in [
('09  Dimensions before arithmetic',[
'**Addition:** same dimensions; add entries. **AB:** (m × n)(n × p) gives m × p. Inner dimensions must match.',
'**Entry (i,j):** row i of A dotted with column j of B: (AB)_{ij} = Σ from k=1 to n of a_{ik}b_{kj}.',
'**Example:** [2,3] paired with (4,1) gives 2·4 + 3·1 = 11. Column j of AB is A b_j.']),
('10  Algebra rules & common traps',[
'**Valid:** A(BC) = (AB)C; A(B + C) = AB + AC; (A + B)C = AC + BC; AI = IA = A (matching sizes).',
'**Generally false:** AB = BA; AB = 0 ⇒ A = 0 or B = 0; AB = AC ⇒ B = C. Cancellation needs an invertible factor on the correct side.',
'**Transpose:** (A^T)^T = A; (A + B)^T = A^T + B^T; (cA)^T = cA^T; (AB)^T = B^T A^T.']),
('11  Inverse: a two-sided undo operation',[
'Only square matrices have the ordinary inverse. A^(-1)A = AA^(-1) = I. For A = [a,b;c,d], the inverse exists iff ad - bc ≠ 0.',
('inverse',),
'**Gauss-Jordan:** reduce [A | I] to [I | A^(-1)]. Carry every operation through both blocks. If A cannot reduce to I, it is singular.',
'**Solve:** x = A^(-1)b. **Selected column j:** solve Ax = e_j; there is no need to compute all of A^(-1).']),
('12  Inverse identities (invertible factors)',[
'(AB)^(-1) = B^(-1)A^(-1); (A^T)^(-1) = (A^(-1))^T; (A^(-1))^(-1) = A.',
'**Check an inverse:** multiply with the original A in both orders. Do not take reciprocals of entries.'])]:y=card(title,items,30,y)
y=686
for title,items in [
('13  Plane transformations: x ↦ Ax',[
('pair','Horizontal-axis reflection',[['1','0'],['0','-1']]),
('pair','Vertical-axis reflection',[['-1','0'],['0','1']]),
('pair','Reflection in x₂ = x₁',[['0','1'],['1','0']]),
('pair','Horizontal projection',[['1','0'],['0','0']]),
('pair','Horizontal shear (factor k)',[['1','k'],['0','1']]),
('pair','Scale both coordinates by k',[['k','0'],['0','k']]),
('pair','Counterclockwise rotation θ',[['cos θ','-sin θ'],['sin θ','cos θ']]),
'Clockwise rotation uses a negative θ. A positive scale k > 1 stretches; 0 < k < 1 contracts. Inverse shear replaces k by -k.']),
('14  Choose a method, then verify',[
'**System / span / range:** form [A | b] → reduce → check consistency → parameterize if needed → verify Ap = b and Av_j = 0.',
'**Independence / one-to-one:** solve Ac = 0; decide whether any nonzero weight vector exists.',
'**Onto / every b:** check for a pivot in every coefficient row, not merely every row of [A | b].',
'**Proof:** state assumptions → use the definition → justify each implication → return to the claim. For “iff”, prove both directions.',
'**True/false:** a true universal claim needs a general reason; a false one needs a valid counterexample. One successful example never proves “for all”.']),
('15  Before writing the final line',[
'Check dimensions, signs, free parameters, assumptions, and factor order. State “no solution”, “one solution”, or the full parameterized set as the question requires.',
'Source scope: sections 1.1-1.5, 1.7-1.9, 2.1-2.2. No 1.6. The lecture inverse typo on physical page 98 is explained in the reader.'])]:y=card(title,items,315,y)
c.save()
(ROOT/'reader/qa/final/pdf-layout-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2))
print(P)
