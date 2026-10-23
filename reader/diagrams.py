"""Translate the source renderer's Diagram/VectorFigure geometry to inline SVG.
The original drawing definitions are executed unchanged against an SVG canvas.
"""
import ast,math,html,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
class Flowable:pass
class Colors:
 black='#272537'
 def HexColor(self,s):return s
colors=Colors()
class PathShape:
 def __init__(self):self.commands=[]
 def moveTo(self,x,y):self.commands.append(f'M{x},{y}')
 def lineTo(self,x,y):self.commands.append(f'L{x},{y}')
 def close(self):self.commands.append('Z')
class Canvas:
 def __init__(self):self.out=[];self.style={'stroke':'#272537','fill':'#272537','width':1,'dash':''};self.stack=[]
 def saveState(self):self.stack.append(self.style.copy())
 def restoreState(self):self.style=self.stack.pop()
 def setFont(self,n,size):self.font=max(11,size)
 def setLineWidth(self,w):self.style['width']=w
 def setStrokeColor(self,c):self.style['stroke']=c
 def setFillColor(self,c):self.style['fill']=c
 def setDash(self,*v):self.style['dash']=' '.join(str(x) for x in v)
 def line(self,x,y,X,Y):self.out.append(f'<path d="M{x},{y} L{X},{Y}" fill="none" stroke="{self.style["stroke"]}" stroke-width="{self.style["width"]}" stroke-dasharray="{self.style["dash"]}"/>')
 def text(self,x,y,t,anchor):self.out.append(f'<text x="{x}" y="{-y}" transform="scale(1,-1)" text-anchor="{anchor}" fill="{self.style["fill"]}" font-size="{self.font}" font-family="Arial,sans-serif">{html.escape(t)}</text>')
 def drawString(self,x,y,t):self.text(x,y,t,'start')
 def drawCentredString(self,x,y,t):self.text(x,y,t,'middle')
 def drawRightString(self,x,y,t):self.text(x,y,t,'end')
 def beginPath(self):return PathShape()
 def drawPath(self,p,fill=0,stroke=1):self.out.append(f'<path d="{" ".join(p.commands)}" fill="{self.style["fill"] if fill else "none"}" stroke="{self.style["stroke"] if stroke else "none"}"/>')
CAPTIONS={
'systems':'Intersecting lines have one common point; parallel distinct lines have none; coincident lines have infinitely many.',
'vectors':'u = (2,1), v = (1,2). Head-to-tail addition gives u + v = (3,3). Multiplying u by −1 reverses it, and multiplying by 2 doubles its length.',
'span':'One nonzero vector and its multiples span a line. Two independent vectors span the coordinate plane.',
'independence':'Parallel generators supply one direction. Independent generators supply two distinct directions.',
'translation':'x = t(1,1) passes through the origin; x = (0,2) + t(1,1) is its parallel translated line.',
'plane':'The vectors along the first two coordinate axes span x₃ = 0. The lines t(1,1,0) and (0,0,1) + t(1,1,0) are parallel.',
'shear':'A horizontal shear sends (x₁,x₂) to (x₁ + x₂,x₂), turning the input square into a parallelogram.',
'reflect':'Reflection across the horizontal axis sends (x₁,x₂) to (x₁,−x₂).',
'project':'Projection onto the horizontal axis sends (x₁,x₂) to (x₁,0). The square collapses to a line segment.',
'onto':'Projection sends u = (2,1) and v = (2,3) to the same (2,0). Its range is the horizontal axis, so it is neither one-to-one nor onto ℝ².',
'inverse':'The shear sends (x₁,x₂) to (x₁ + x₂,x₂). Its inverse recovers x by (y₁−y₂,y₂).',
'vector3':'Exact endpoints for Exercise 1.3.3: u = (−1,2), v = (−3,3), −v = (3,−3), −2v = (6,−6), u + v = (−4,5), u − v = (2,−1), u − 2v = (5,−4).',
'vector4':'Exact endpoints for Exercise 1.3.4: u = (3,2), v = (2,3), −v = (−2,−3), −2v = (−4,−6), u + v = (5,5), u − v = (1,−1), u − 2v = (−1,−4).',
'transform13':'Exercise 1.8.13: T = −I, a half-turn about the origin. u = (5,2) maps to (−5,−2), and v = (−2,4) maps to (2,−4).',
'transform14':'Exercise 1.8.14: contraction by 1/2. The images of (5,2) and (−2,4) are (5/2,1) and (−1,2).',
'transform15':'Exercise 1.8.15: projection onto the vertical axis. The images are (0,2) and (0,4).',
'transform16':'Exercise 1.8.16: reflection in x₂ = x₁. The images are (2,5) and (4,−2).',
'relation18':'Schematic for Exercise 1.8.18: w = u + 2v, so T(w) = T(u) + 2T(v). No source coordinates are asserted.',
'relation13':'Schematic for Exercise 1.9.13: T(2,1) = 2T(e₁) + T(e₂). Lengths are illustrative; the original figure has no numerical endpoints.',
'relation14':'Schematic for Exercise 1.9.14: T(−1,3) = −a₁ + 3a₂. Lengths are illustrative; the original figure has no numerical endpoints.'}
mod=ast.parse((ROOT/'source/build_math2255.py').read_text())
classes=ast.Module(body=[n for n in mod.body if isinstance(n,ast.ClassDef) and n.name in ['Diagram','VectorFigure']],type_ignores=[])
exec(compile(classes,'source drawing geometry','exec'))
def svg(kind):
 ob=(VectorFigure if kind in ['vector3','vector4','transform13','transform14','transform15','transform16','relation18','relation13','relation14'] else Diagram)(kind);c=Canvas();ob.canv=c;ob.draw();cap=CAPTIONS[kind]
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-5 -5 {ob.width+45} {ob.height+10}" role="img" aria-label="{html.escape(cap,quote=True)}"><title>{html.escape(cap)}</title><g transform="translate(0,{ob.height}) scale(1,-1)">{"".join(c.out)}</g></svg>'
def figure(kind):return '<figure class="diagram"><div class="figure-scroll" tabindex="0" role="region" aria-label="Diagram; scroll horizontally on small screens">'+svg(kind)+'</div><figcaption>'+html.escape(CAPTIONS[kind])+'</figcaption></figure>'
if __name__=='__main__':
 out=ROOT/'reader/assets/diagrams';out.mkdir(parents=True,exist_ok=True)
 for k in CAPTIONS:(out/(k+'.svg')).write_text(svg(k))
 print(len(CAPTIONS),'SVG illustrations')
