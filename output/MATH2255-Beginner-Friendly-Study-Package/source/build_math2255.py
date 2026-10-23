from pathlib import Path
from fractions import Fraction as F
import json,re,math,copy,html,csv,io
from PIL import Image as PILImage
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,KeepTogether,Flowable,Table,TableStyle,Image as RLImage
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'output/pdf';OUT.mkdir(parents=True,exist_ok=True)
SRC=ROOT/'source';FIG=SRC/'figures';FIG.mkdir(exist_ok=True)
CHECKS=[]
def mat(a): return [[F(str(x)) for x in row] for row in a]
def ident(n):return mat([[int(i==j) for j in range(n)] for i in range(n)])
def transpose(a):return list(map(list,zip(*a)))
def mul(a,b):return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*b)] for row in a]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(c,a):return [[F(c)*x for x in r] for r in a]
def aug(a,b):return [r+s for r,s in zip(mat(a),mat(b))]
def fs(x):return str(x)
def mtext(a,bar=None):return '@matrix '+json.dumps({'a':[[str(x) for x in r] for r in a],'bar':bar})+'\n\n'
def vec(v):return mtext([[x] for x in v])
def rowreduce(a,limit=None):
 a=mat(a); original=copy.deepcopy(a);e=ident(len(a));steps=[];piv=[];r=0
 def apply(kind,i,j=None,c=None):
  nonlocal a,e
  if kind=='swap':a[i],a[j]=a[j],a[i];e[i],e[j]=e[j],e[i];op=f'R{i+1} ↔ R{j+1}';why=f'Move a nonzero entry into row {i+1} so that it can be used as a pivot.'
  if kind=='scale':a[i]=[c*x for x in a[i]];e[i]=[c*x for x in e[i]];op=f'R{i+1} ← ({c})R{i+1}';why=f'Multiply every entry of row {i+1}, including any right-hand side, by {c}. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.'
  if kind=='replace':a[i]=[x+c*y for x,y in zip(a[i],a[j])];e[i]=[x+c*y for x,y in zip(e[i],e[j])];op=f'R{i+1} ← R{i+1} + ({c})R{j+1}';why=f'Add {c} times row {j+1} to row {i+1}. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.'
  steps.append((op,why,copy.deepcopy(a)))
 for c in range(len(a[0]) if limit is None else limit):
  k=next((i for i in range(r,len(a)) if a[i][c]),None)
  if k is None:continue
  if k!=r:apply('swap',r,k)
  if a[r][c]!=1:apply('scale',r,c=1/a[r][c])
  for i in range(r+1,len(a)):
   if a[i][c]:apply('replace',i,r,-a[i][c])
  piv.append(c);r+=1
  if r==len(a):break
 for i,c in reversed(list(enumerate(piv))):
  for j in range(i):
   if a[j][c]:apply('replace',j,i,-a[j][c])
 assert mul(e,original)==a
 CHECKS.append('row operations: exact E times original equals final')
 return a,piv,steps

def walkthrough(a,bar=None,limit=None):
 r,p,steps=rowreduce(a,limit)
 s='The starting matrix is:\n\n'+mtext(a,bar)
 if not steps:s+='It already has the required reduced form, so no row operation is necessary.\n\n'
 for k,(op,why,b) in enumerate(steps,1):s+=f'**Step {k}: {op}.** {why}\n\n'+mtext(b,bar)
 return s,r,p

def expr(c,terms):
 s=str(c) if c else ''
 for coeff,var in terms:
  if not coeff:continue
  sign=' - ' if coeff<0 else (' + ' if s else '')
  if not s and coeff<0:sign='-'
  av=abs(coeff);s+=sign+('' if av==1 else str(av)+' ')+var
 return s or '0'

def system_solution(a,why='',hom=False):
 a=mat(a);n=len(a[0])-1
 intro=why+'\n\n' if why else ''
 intro+='Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.\n\n'
 s,r,p=walkthrough(a,n)
 if any(not any(row[:n]) and row[n] for row in r):
  bad=next(row[n] for row in r if not any(row[:n]) and row[n]);s+=f'A row now states 0 = {bad}. No choices of the unknowns can make that true. The system is inconsistent, and its solution set is empty. Free-looking coefficient columns cannot remove a contradiction.\n\n';return intro+s
 cp=[j for j in p if j<n];free=[j for j in range(n) if j not in cp];names=['s','t','u','v','w','z'][:len(free)]
 part=[F(0)]*n;dirs=[]
 for i,j in enumerate(cp):part[j]=r[i][n]
 for j in free:
  d=[F(0)]*n;d[j]=1
  for i,k in enumerate(cp):d[k]=-r[i][j]
  dirs.append(d)
 s+='**Read the equations.** '
 s+='; '.join(expr(0,[(row[j],f'x_{j+1}') for j in range(n)])+' = '+str(row[n]) for row in r if any(row)) or 'Every row is 0 = 0.'
 s+='\n\n'
 if free:
  s+='The pivot columns are '+', '.join(str(j+1) for j in cp)+'. Thus '+', '.join(f'x_{j+1}' for j in cp)+' are basic variables. '+', '.join(f'x_{j+1}' for j in free)+' have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.\n\n'
  s+='Set '+', '.join(f'x_{j+1} = {t}' for j,t in zip(free,names))+' with all parameters real. The complete coordinate answer is:\n\n'
  for i in range(n):s+='@eq '+f'x_{i+1} = '+expr(part[i],[(d[i],t) for d,t in zip(dirs,names)])+'\n\n'
  s+='In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + '+ ' + '.join(t+f' v_{i+1}' for i,t in enumerate(names))+', where:\n\n'+'p =\n\n'+vec(part)
  for i,d in enumerate(dirs):s+=f'v_{i+1} =\n\n'+vec(d)
  s+='For example, setting all parameters to 0 gives x = p. Setting '+names[0]+' = 1 and all other parameters to 0 gives:\n\n'+vec([x+y for x,y in zip(part,dirs[0])])
  s+='These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. '
  if hom:s+='Because p = 0, choosing a nonzero parameter gives a nontrivial homogeneous solution. '
 else:s+='Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:\n\n'+vec(part)
 A=[row[:n] for row in a];b=[[row[n]] for row in a]
 assert mul(A,[[x] for x in part])==b
 s+='\n\n**Verification in the original equations.** For p, the left-hand sides A p are:\n\n'+vec([row[0] for row in mul(A,[[x] for x in part])])
 s+='These entries equal the original right-hand sides, in order. '
 for i,d in enumerate(dirs):
  prod=mul(A,[[x] for x in d]);assert not any(x[0] for x in prod)
  s+=f'For direction v_{i+1}, multiplying by the original A gives the zero vector. '
 if dirs:s+='Therefore A(p + s v_1'+''.join(' + '+t+f' v_{i+1}' for i,t in enumerate(names[1:],1))+') = A p + s A v_1'+''.join(' + '+t+f' A v_{i+1}' for i,t in enumerate(names[1:],1))+' = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.'
 s+='\n\n';CHECKS.append('solution: exact A p = b and every A v = 0')
 return intro+s

def independence(a):
 a=mat(a);n=len(a[0]);s,r,p=walkthrough(aug(a,[[0] for _ in a]),n);p=[j for j in p if j<n]
 if len(p)==n:s+='Every coefficient column has a pivot. The equations force every weight to be zero. Hence the columns are linearly independent: no nontrivial dependence relation exists.\n\n'
 else:
  j=next(j for j in range(n) if j not in p);d=[F(0)]*n;d[j]=1
  for i,k in enumerate(p):d[k]=-r[i][j]
  assert not any(x[0] for x in mul(a,[[x] for x in d]))
  s+='Column '+str(j+1)+' has no pivot. Give its weight the value 1 and give any other free weights the value 0. The pivot equations determine the weights:\n\n'+vec(d)
  s+='At least one weight is nonzero. The resulting dependence relation is:\n\n@eq '+expr(0,[(d[i],f'v_{i+1}') for i in range(n)])+' = 0\n\n'
  s+='Multiplying the original columns by these weights gives the zero vector, entry by entry. This proves dependence; the existence of a zero combination with every weight zero would not prove it.\n\n'
 return s

def inverse_solution(a):
 a=mat(a);n=len(a);s,r,p=walkthrough(aug(a,ident(n)),n,limit=n)
 if [row[:n] for row in r]!=ident(n):return s+'The left block cannot become the identity: it has fewer than '+str(n)+' pivots. A is singular and has no inverse. A zero row in the left block alone is not a contradiction about the original entries; it shows a missing pivot and loss of reversibility of the transformation.\n\n'
 inv=[row[n:] for row in r];assert mul(a,inv)==ident(n) and mul(inv,a)==ident(n)
 s+='The left block is I. The right block is therefore A^(-1):\n\n'+mtext(inv)
 s+='**Verification.** Multiplying in each order gives the identity:\n\n'+mtext(mul(a,inv))+'The same elementary operations changed A into I and I into A^(-1). They amount to multiplication on the left by A^(-1), which explains why the procedure works.\n\n'
 CHECKS.append('inverse: both exact products are identity')
 return s

def product_solution(a,b):
 a=mat(a);b=mat(b)
 if len(a[0])!=len(b):return f'The left factor has {len(a[0])} columns, whereas the right factor has {len(b)} rows. The inner dimensions do not match, so this product is undefined. This is a dimension issue, not a product equal to zero.\n\n'
 c=mul(a,b);s=f'The product has {len(a)} rows and {len(b[0])} columns. Each entry uses one row of the left factor and one column of the right factor.\n\n'
 for i in range(len(a)):
  for j in range(len(b[0])):s+='@eq '+f'c_{{{i+1}{j+1}}} = '+' + '.join(f'({fs(a[i][k])})({fs(b[k][j])})' for k in range(len(b)))+' = '+fs(c[i][j])+'\n\n'
 # independent column linear combination check
 alt=transpose([[sum((b[k][j]*a[i][k] for k in range(len(b))),F(0)) for i in range(len(a))] for j in range(len(b[0]))]);assert c==alt
 s+='Collect those entries in their row and column positions:\n\n'+mtext(c)
 s+='As a second interpretation, column j of the answer is A times column j of B: it is a linear combination of the columns of A using the entries of that column of B as weights.\n\n';CHECKS.append('product: row-column and column combinations agree');return s

# Typesetting. Matrix entries retain stacked exact fractions and drawn brackets.
FONT='/System/Library/Fonts/Supplemental/'
for name,file in [('Body','STIXTwoText.ttf'),('Regular','Times New Roman.ttf'),('Bold','Times New Roman Bold.ttf'),('Italic','Times New Roman Italic.ttf')]:pdfmetrics.registerFont(TTFont(name,FONT+file))
pdfmetrics.registerFont(TTFont('Unicode','/Library/Fonts/Arial Unicode.ttf'))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold',italic='Italic',boldItalic='Bold')
class MatrixBlock(Flowable):
 def __init__(self,a,bar=None):super().__init__();self.a=a;self.bar=bar
 def wrap(self,aw,ah):
  self.size=11;self.rowh=28 if any('/' in str(x) for r in self.a for x in r) else 22
  self.cw=[max(34,max(pdfmetrics.stringWidth(str(r[j]),'Regular',11)+14 for r in self.a)) for j in range(len(self.a[0]))]
  self.width=sum(self.cw)+24;self.height=len(self.a)*self.rowh+12;self.aw=aw;return self.width,self.height
 def draw(self):
  c=self.canv;c.saveState();c.translate(max(0,(self.aw-self.width)/2),0);c.setStrokeColor(colors.HexColor('#314a5d'));c.setLineWidth(.8)
  l=4;r=self.width-4;h=self.height-3
  for x,d in [(l,1),(r,-1)]:c.line(x,3,x,h);c.line(x,3,x+5*d,3);c.line(x,h,x+5*d,h)
  if self.bar is not None:
   x=12+sum(self.cw[:self.bar]);c.setStrokeColor(colors.HexColor('#8697a0'));c.line(x,5,x,h-2)
  y=self.height-10-self.rowh/2
  for row in self.a:
   x=12
   for j,v in enumerate(row):
    v=str(v);cx=x+self.cw[j]/2;c.setFillColor(colors.HexColor('#172936'));c.setFont('Regular',11)
    if re.fullmatch(r'-?\d+/\d+',v):
     num,den=v.split('/');c.setFont('Regular',9.5);w=max(pdfmetrics.stringWidth(num,'Regular',9.5),pdfmetrics.stringWidth(den,'Regular',9.5))+5
     c.drawCentredString(cx,y+4,num);c.drawCentredString(cx,y-8,den);c.line(cx-w/2,y+1,cx+w/2,y+1)
    else:c.drawCentredString(cx,y-3,v)
    x+=self.cw[j]
   y-=self.rowh
  c.restoreState()
class Diagram(Flowable):
 def __init__(self,kind):super().__init__();self.kind=kind;self.width=460;self.height=225
 def draw(self):
  c=self.canv;c.saveState();c.setFont('Body',9);c.setLineWidth(.65)
  def axes(x,y,sc=18):
   c.setStrokeColor(colors.HexColor('#b8c6ce'))
   for k in range(-4,5):
    c.line(x-4*sc,y+k*sc,x+4*sc,y+k*sc);c.line(x+k*sc,y-4*sc,x+k*sc,y+4*sc)
   c.setStrokeColor(colors.HexColor('#344c5e'));c.line(x-4*sc,y,x+4*sc,y);c.line(x,y-4*sc,x,y+4*sc);c.drawString(x+4*sc+3,y,'x₁');c.drawString(x+3,y+4*sc+2,'x₂')
  def arrow(x,y,a,b,sc=18,label='',color='#007c8a',start=(0,0)):
   c.setStrokeColor(colors.HexColor(color));c.setFillColor(colors.HexColor(color));X=x+a*sc;Y=y+b*sc;c.setLineWidth(1.4);c.line(x+start[0]*sc,y+start[1]*sc,X,Y);ang=math.atan2(b-start[1],a-start[0]);
   for d in [-.45,.45]:c.line(X,Y,X-6*math.cos(ang+d),Y-6*math.sin(ang+d))
   c.drawString(X+3,Y+3,label)
  if self.kind=='plane':
   def project(ox,oy,v):return (ox-18*v[0]+22*v[1],oy-10*v[0]-5*v[1]+26*v[2])
   def line3(ox,oy,a,b,col):
    x,y=project(ox,oy,a);X,Y=project(ox,oy,b);c.setStrokeColor(colors.HexColor(col));c.line(x,y,X,Y)
   for ox in [130,355]:
    oy=105
    for v,l in [((3,0,0),'x₁'),((0,3,0),'x₂'),((0,0,3),'x₃')]:
     line3(ox,oy,(0,0,0),v,'#9eafb7');x,y=project(ox,oy,v);c.setFillColor(colors.black);c.drawString(x+3,y+3,l)
   points=[(-2,-2,0),(2,-2,0),(2,2,0),(-2,2,0)]
   pth=c.beginPath();x,y=project(130,105,points[0]);pth.moveTo(x,y)
   for v in points[1:]:x,y=project(130,105,v);pth.lineTo(x,y)
   pth.close();c.setFillColor(colors.HexColor('#d8ebee'));c.setStrokeColor(colors.HexColor('#729fa9'));c.drawPath(pth,fill=1,stroke=1)
   for v,l in [((2,0,0),'u'),((0,2,0),'v')]:line3(130,105,(0,0,0),v,'#007c8a');x,y=project(130,105,v);c.setFillColor(colors.black);c.drawString(x+4,y,l)
   for z,col,l in [(0,'#007c8a','t(1,1,0)'),(1,'#bd5b33','(0,0,1)+t(1,1,0)')]:
    line3(355,105,(-2,-2,z),(2,2,z),col);x,y=project(355,105,(2,2,z));c.setFillColor(colors.HexColor(col));c.drawString(x+5,y,l)
   c.setFillColor(colors.black);c.drawString(25,18,'Span{u,v}: the x₁x₂-plane (x₃=0)');c.drawString(270,18,'Parallel lines in three-dimensional space')
  elif self.kind=='systems':
   for q,title in enumerate(['One intersection','Parallel: no solution','Coincident: infinitely many']):
    x=75+q*155;y=110;sc=15;axes(x,y,sc);c.setStrokeColor(colors.HexColor('#007c8a'));c.line(x-3*sc,y-3*sc,x+3*sc,y+3*sc);c.setStrokeColor(colors.HexColor('#bd5b33'))
    if q==0:c.line(x-3*sc,y+3*sc,x+3*sc,y-3*sc)
    if q==1:c.line(x-3*sc,y-2*sc,x+2*sc,y+3*sc)
    if q==2:c.setDash(4,3);c.line(x-3*sc,y-3*sc,x+3*sc,y+3*sc);c.setDash()
    c.setFillColor(colors.black);c.drawCentredString(x,25,title)
  elif self.kind in ['vectors','span','translation','independence']:
   x=125;y=110;axes(x,y);x2=350;axes(x2,y)
   if self.kind=='vectors':
    arrow(x,y,2,1,label='u=(2,1)');arrow(x,y,1,2,label='v=(1,2)',color='#bd5b33');arrow(x,y,3,3,label='u+v');arrow(x,y,3,3,start=(2,1),color='#bd5b33');arrow(x,y,3,3,start=(1,2));arrow(x2,y,-2,-1,label='-u');arrow(x2,y,4,2,label='2u');c.drawString(48,18,'Head-to-tail addition');c.drawString(280,18,'Scaling preserves a line')
   elif self.kind=='translation':
    for X in [x,x2]:c.setStrokeColor(colors.HexColor('#007c8a'));c.line(X-3*18,y-3*18,X+3*18,y+3*18)
    c.setStrokeColor(colors.HexColor('#bd5b33'));c.line(x2-3*18,y-1*18,x2+1*18,y+3*18);arrow(x2,y,0,2,label='p=(0,2)',color='#bd5b33');c.drawString(40,18,'x=t(1,1): through zero');c.drawString(260,18,'x=(0,2)+t(1,1): translated line')
   else:
    arrow(x,y,2,1,label='u');arrow(x,y,4,2,label='2u',color='#bd5b33');arrow(x2,y,3,0,label='u');arrow(x2,y,0,3,label='v',color='#bd5b33');c.drawString(45,18,'One direction: a line');c.drawString(262,18,'Independent directions span the plane')
  elif self.kind in ['shear','reflect','project','inverse','onto']:
   for X in [115,345]:axes(X,105)
   if self.kind=='onto':
    arrow(115,105,2,1,label='u');arrow(115,105,2,3,label='v',color='#bd5b33');arrow(345,105,2,0,label='T(u)=T(v)');c.drawString(25,18,'Different inputs');c.drawString(245,18,'Projection: range is the x₁-axis')
   else:
    poly=[(0,0),(2,0),(2,2),(0,2),(0,0)]
    transform={'shear':lambda a,b:(a+b,b),'reflect':lambda a,b:(a,-b),'project':lambda a,b:(a,0),'inverse':lambda a,b:(a+b,b)}[self.kind]
    for X,fun,col in [(115,lambda a,b:(a,b),'#81959f'),(345,transform,'#007c8a')]:
     c.setStrokeColor(colors.HexColor(col));c.setLineWidth(2)
     for (a,b),(d,e) in zip(poly,poly[1:]):a,b=fun(a,b);d,e=fun(d,e);c.line(X+a*18,105+b*18,X+d*18,105+e*18)
    arrow(115,105,1,2,label='x');a,b=transform(1,2);arrow(345,105,a,b,label='Ax')
    c.drawString(50,18,'Input square and vector');c.drawString(260,18,{'shear':'Shear: (x₁+x₂,x₂)','reflect':'Reflection: (x₁,-x₂)','project':'Projection: (x₁,0)','inverse':'Undo shear with (y₁-y₂,y₂)'}[self.kind])
  c.restoreState()
class VectorFigure(Flowable):
 def __init__(self,kind):
  super().__init__();self.kind=kind;self.width=480;self.height=320 if kind.startswith('vector') else 255
 def draw(self):
  c=self.canv;c.saveState();c.setFont('Body',9)
  def axes(ox,oy,sc,lo,hi):
   c.setLineWidth(.3);c.setStrokeColor(colors.HexColor('#d9e2e6'))
   for k in range(lo,hi+1):
    c.line(ox+lo*sc,oy+k*sc,ox+hi*sc,oy+k*sc);c.line(ox+k*sc,oy+lo*sc,ox+k*sc,oy+hi*sc)
   c.setStrokeColor(colors.HexColor('#354e5f'));c.setLineWidth(.8);c.line(ox+lo*sc,oy,ox+hi*sc,oy);c.line(ox,oy+lo*sc,ox,oy+hi*sc)
   for k in range(lo,hi+1):
    if k and k%2==0:c.drawCentredString(ox+k*sc,oy-12,str(k));c.drawRightString(ox-4,oy+k*sc-3,str(k))
  def arrow(ox,oy,sc,v,label,col,start=(0,0),offset=(3,3)):
   c.setStrokeColor(colors.HexColor(col));c.setFillColor(colors.HexColor(col));c.setLineWidth(1.2);x,y=v;x0,y0=start;X=ox+x*sc;Y=oy+y*sc;c.line(ox+x0*sc,oy+y0*sc,X,Y);a=math.atan2(y-y0,x-x0)
   for d in [-.4,.4]:c.line(X,Y,X-6*math.cos(a+d),Y-6*math.sin(a+d))
   c.drawString(X+offset[0],Y+offset[1],label)
  palette=['#007b89','#b85c32','#547796','#865a87','#183a4a','#7d7334','#5d8851']
  if self.kind.startswith('vector'):
   u,v=([-1,2],[-3,3]) if self.kind=='vector3' else ([3,2],[2,3]);ox=230;oy=155;sc=19;axes(ox,oy,sc,-7,7)
   vs=[u,v,[-x for x in v],[-2*x for x in v],[a+b for a,b in zip(u,v)],[a-b for a,b in zip(u,v)],[a-2*b for a,b in zip(u,v)]]
   for j,(a,l) in enumerate(zip(vs,['u','v','-v','-2v','u+v','u-v','u-2v'])):arrow(ox,oy,sc,a,l,palette[j],offset=(4,3+(j%2)*6))
   c.setDash(3,3);c.setStrokeColor(colors.HexColor('#9ba8ae'));uv=vs[5];
   for a,b in [(u,uv),(vs[2],uv)]:c.line(ox+a[0]*sc,oy+a[1]*sc,ox+b[0]*sc,oy+b[1]*sc)
   c.setDash();c.setFillColor(colors.black);c.drawString(35,10,'Exact coordinate endpoints; dashed edges complete 0, u, -v, u-v.')
  elif self.kind.startswith('transform'):
   n=int(self.kind[9:]);A={13:[[-1,0],[0,-1]],14:[[.5,0],[0,.5]],15:[[0,0],[0,1]],16:[[0,1],[1,0]]}[n]
   for ox in [120,355]:axes(ox,125,16,-6,6)
   for j,v in enumerate([[5,2],[-2,4]]):
    w=[sum(A[i][k]*v[k] for k in range(2)) for i in range(2)];arrow(120,125,16,v,['u','v'][j],palette[j]);arrow(355,125,16,w,['T(u)','T(v)'][j],palette[j])
   c.setFillColor(colors.black);c.drawCentredString(120,15,'Input');c.drawCentredString(355,15,'Image')
  else:
   c.setStrokeColor(colors.HexColor('#b1bfc6'));c.line(25,75,460,75);c.line(140,30,140,235);ox=140;oy=75;sc=33
   if self.kind=='relation18':
    u=(1,-.5);v=(.8,1);w=(u[0]+2*v[0],u[1]+2*v[1]);arrow(ox,oy,sc,u,'T(u)',palette[0]);arrow(ox,oy,sc,v,'T(v)',palette[1]);arrow(ox,oy,sc,(u[0]+v[0],u[1]+v[1]),'T(v)',palette[1],start=u);arrow(ox,oy,sc,w,'T(w)',palette[2],start=(u[0]+v[0],u[1]+v[1]));arrow(ox,oy,sc,w,'T(u)+2T(v)',palette[3],offset=(5,16))
   elif self.kind=='relation13':
    u=(-1.4,.6);v=(3,.8);w=(2*u[0]+v[0],2*u[1]+v[1]);arrow(ox,oy,sc,u,'T(e₁)',palette[0]);arrow(ox,oy,sc,v,'T(e₂)',palette[1]);arrow(ox,oy,sc,(2*u[0],2*u[1]),'second T(e₁)',palette[0],start=u);arrow(ox,oy,sc,w,'T(e₂)',palette[1],start=(2*u[0],2*u[1]));arrow(ox,oy,sc,w,'T(2,1)',palette[3],offset=(5,14))
   else:
    u=(2,-.7);v=(1,.6);w=(-u[0]+3*v[0],-u[1]+3*v[1]);arrow(ox,oy,sc,u,'a₁',palette[0]);arrow(ox,oy,sc,v,'a₂',palette[1]);arrow(ox,oy,sc,(-u[0],-u[1]),'-a₁',palette[2]);start=(-u[0],-u[1])
    for j in range(3):end=(start[0]+v[0],start[1]+v[1]);arrow(ox,oy,sc,end,'a₂' if j==0 else '',palette[1],start=start);start=end
    arrow(ox,oy,sc,w,'T(-1,3)',palette[3],offset=(5,14))
   c.setFillColor(colors.black);c.drawString(20,8,'Schematic head-to-tail construction; lengths are not claimed as source coordinates.')
  c.restoreState()

styles=getSampleStyleSheet();styles.add(ParagraphStyle(name='BodyBook',fontName='Body',fontSize=11.2,leading=15.5,spaceAfter=9,textColor=colors.HexColor('#172936')))
styles.add(ParagraphStyle(name='H1Book',fontName='Bold',fontSize=23,leading=28,spaceAfter=18,textColor=colors.HexColor('#005e70')))
styles.add(ParagraphStyle(name='H2Book',fontName='Bold',fontSize=15,leading=20,spaceBefore=14,spaceAfter=9,textColor=colors.HexColor('#005e70'),keepWithNext=True))
styles.add(ParagraphStyle(name='H3Book',fontName='Bold',fontSize=12,leading=16,spaceBefore=9,spaceAfter=7,keepWithNext=True))
styles.add(ParagraphStyle(name='EqBook',fontName='Body',fontSize=12,leading=19,alignment=TA_CENTER,spaceBefore=6,spaceAfter=10))
styles.add(ParagraphStyle(name='NoteBook',parent=styles['BodyBook'],fontSize=10,leading=14,textColor=colors.HexColor('#5c6f7a')))
def fmt(t):
 t=html.escape(t).replace('&lt;br&gt;','<br/>');t=''.join(('<font name="Unicode">'+c+'</font>') if ord(c)>127 else c for c in t);t=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',t)
 t=re.sub(r'\^\((-?\d+)\)',r'<super>\1</super>',t);t=re.sub(r'\^([a-zA-Z0-9]+)',r'<super>\1</super>',t)
 t=re.sub(r'_\{([^}]+)\}',r'<sub>\1</sub>',t);t=re.sub(r'_(\d+|[a-z])',r'<sub>\1</sub>',t)
 return t
class Doc(SimpleDocTemplate):
 def afterFlowable(self,f):
  if isinstance(f,Paragraph) and hasattr(f,'toclevel'):
   key='h'+str(self.seq.nextf('heading'));self.canv.bookmarkPage(key);self.canv.addOutlineEntry(f.getPlainText(),key,f.toclevel,False);self.notify('TOCEntry',(f.toclevel,f.getPlainText(),self.page,key))
def render(md,path,title):
 story=[];lines=md.splitlines();buf=[]
 def flush():
  if buf:story.append(Paragraph(fmt(' '.join(buf)),styles['BodyBook']));buf.clear()
 for line in lines:
  if not line.strip():flush();continue
  if line.startswith('# '):
   flush()
   if story:story.append(PageBreak())
   p=Paragraph(fmt(line[2:]),styles['H1Book']);p.toclevel=0;story.append(p)
  elif line.startswith('## '):flush();p=Paragraph(fmt(line[3:]),styles['H2Book']);p.toclevel=1;story.append(p)
  elif line.startswith('### '):flush();story.append(Paragraph(fmt(line[4:]),styles['H3Book']))
  elif line=='@toc':
   flush();toc=TableOfContents();toc.levelStyles=[ParagraphStyle(name='TOC0',fontName='Body',fontSize=11,leading=16,spaceBefore=7),ParagraphStyle(name='TOC1',fontName='Body',fontSize=9.5,leading=13,leftIndent=15)];story.append(toc)
  elif line.startswith('@matrix '):
   flush();d=json.loads(line[8:]);
   if story and isinstance(story[-1],Paragraph):story[-1].keepWithNext=True
   story.append(MatrixBlock(d['a'],d.get('bar')));story.append(Spacer(1,8))
  elif line.startswith('@eq '):flush();story.append(Paragraph(fmt(line[4:]),styles['EqBook']))
  elif line.startswith('@customfig '):flush();story.append(VectorFigure(line[11:]));story.append(Spacer(1,8))
  elif line.startswith('@figure '):flush();story.append(Diagram(line[8:]));story.append(Spacer(1,8))
  elif line=='@page':flush();story.append(PageBreak())
  elif line.startswith('@scan '):
   flush();p=SRC/'scans'/line[6:];scan=PILImage.open(p).convert('RGB');mask=scan.convert('L').point(lambda x:255 if x<190 else 0);box=mask.getbbox()
   if box:
    l,t,r,b=box;scan=scan.crop((max(0,l-12),max(0,t-12),min(scan.width,r+12),min(scan.height,b+12)))
   memory=io.BytesIO();scan.save(memory,format='PNG');memory.seek(0);im=RLImage(memory);sc=min(508/im.imageWidth,635/im.imageHeight);im.drawWidth=im.imageWidth*sc;im.drawHeight=im.imageHeight*sc;story.append(im)
  else:buf.append(line)
 flush()
 def footer(c,d):
  c.saveState();c.setFont('Body',8);c.setFillColor(colors.HexColor('#627681'));c.drawString(52,765,'MATH 2255 • LINEAR ALGEBRA MADE UNDERSTANDABLE');c.setStrokeColor(colors.HexColor('#d0dce1'));c.line(52,757,560,757);c.drawString(52,28,title);c.drawRightString(560,28,str(d.page));c.restoreState()
 d=Doc(str(path),pagesize=(612,792),rightMargin=52,leftMargin=52,topMargin=55,bottomMargin=48,title=title,author='Personal MATH 2255 study resource')
 d.multiBuild(story,onFirstPage=footer,onLaterPages=footer)

if __name__=='__main__':
 for stem,title in [('MATH2255-Complete-Beginner-Textbook','Textbook'),('MATH2255-Exercises-and-Detailed-Solutions','Exercise workbook and worked solutions')]:
  p=SRC/(stem+'.md')
  if p.exists():render(p.read_text(),OUT/(stem+'.pdf'),title)

