"""Small offline MathML compiler for the manuscripts' documented notation.
Not a general TeX engine. Explicit directives are parsed separately from prose.
Original expressions are retained in semantic annotations and data attributes.
"""
import re,html,json
E=html.escape
SUB=str.maketrans('₀₁₂₃₄₅₆₇₈₉ᵢⱼₙₘₖ','0123456789ijnmk')
SUP=str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺ⁿᵀ','0123456789-+nT')
def tag(n,s,attrs=''):return f'<{n}{(" "+attrs) if attrs else ""}>{s}</{n}>'
def row(s):return tag('mrow',s)
def matrix_node(a,bar=None,affected=(),pivot=None):
 n=len(a[0]);rows=[]
 for i,r in enumerate(a):
  cells=[]
  for j,v in enumerate(r):
   styles=[]
   if bar is not None and j==bar:styles.append('border-left:1.5px solid #706981;padding-left:.65em')
   if i in affected:styles.append('background:#f1edfa')
   if pivot==(i,j):styles.append('background:#dceadf;outline:1px solid #60806a')
   cells.append(tag('mtd',tag('mo','∗') if str(v)=='*' else expr(str(v)),f'style="{";".join(styles)}"' if styles else ''))
  rows.append(tag('mtr',''.join(cells)))
 return row('<mo fence="true" stretchy="true">[</mo>'+tag('mtable',''.join(rows),'columnalign="center" columnspacing=".75em" rowspacing=".45em"')+'<mo fence="true" stretchy="true">]</mo>')
class Parser:
 def __init__(self,s):self.s=s;self.i=0
 def skip(self):
  while self.i<len(self.s) and self.s[self.i].isspace():self.i+=1
 def seq(self,stop=''):
  out=[]
  while self.i<len(self.s):
   self.skip()
   if self.i==len(self.s) or (stop and self.s[self.i]==stop):break
   if self.s[self.i]=='/' and out:
    self.i+=1;den=self.atom(True);out[-1]=tag('mfrac',out[-1]+den);continue
   out.append(self.atom())
  return row(''.join(out))
 def atom(self,den=False):
  self.skip()
  if self.i>=len(self.s):return row('')
  c=self.s[self.i];self.i+=1
  if c in '({[':
   closing={'(':')','{':'}','[':']'}[c];start=self.i;depth=1;k=start
   while k<len(self.s):
    if self.s[k]==c:depth+=1
    if self.s[k]==closing:depth-=1
    if not depth:break
    k+=1
   body=self.s[start:k];self.i=min(k+1,len(self.s))
   if c=='[' and (',' in body or ';' in body):
    rawrows=body.split(';');bars=[len(re.split(r'\s*,\s*',r.split('|')[0].strip().rstrip(','))) if '|' in r else None for r in rawrows]
    a=[re.split(r'\s*,\s*',r.replace('|',',').strip()) for r in rawrows]
    bar=bars[0] if all(b==bars[0] for b in bars) else None
    result=matrix_node(a,bar) if len({len(r) for r in a})==1 else row('<mo>[</mo>'+expr(body)+'<mo>]</mo>')
   elif c=='{' or den:result=expr(body)
   else:result=row(tag('mo',c)+expr(body)+tag('mo',closing))
  elif c=='√':result=tag('msqrt',self.atom())
  elif c.isdigit() or c=='.' and self.i<len(self.s) and self.s[self.i].isdigit():
   m=re.match(r'[\d.]*',self.s[self.i:]);v=c+m.group();self.i+=len(m.group());result=tag('mn',E(v))
  elif c.isalpha() or c in 'ℝθδαβπ':
   # Variables are individual mathematical identifiers; genuine prose is mtext.
   m=re.match(r'[A-Za-z]+',self.s[self.i-1:])
   word=m.group() if m else c
   words={'provided','where','for','and','or','if','then','all','real','is','not','in','with','when','otherwise','det','rank','Span','sin','cos','diag','row'}
   if word in words or len(word)>4:
    self.i+=len(word)-1;result=tag('mtext' if word not in {'det','rank','Span','sin','cos','diag'} else 'mi',E(word)+' ')
   else:result=tag('mi',E(c))
  else:result=tag('mo',E({'-':'−','*':'·'}.get(c,c)))
  sub=sup=None
  while self.i<len(self.s):
   c=self.s[self.i]
   if c in '_^':
    self.i+=1;self.skip()
    if self.i<len(self.s) and self.s[self.i] in '({':
     opening=self.s[self.i];closing=')' if opening=='(' else '}';self.i+=1;start=self.i;depth=1
     while self.i<len(self.s):
      if self.s[self.i]==opening:depth+=1
      if self.s[self.i]==closing:depth-=1
      if not depth:break
      self.i+=1
     v=expr(self.s[start:self.i]);self.i+=int(self.i<len(self.s))
    else:
     m=re.match(r'\d+|[A-Za-z]',self.s[self.i:]);raw=m.group() if m else self.s[self.i:self.i+1];self.i+=len(raw);v=expr(raw)
    if c=='_':sub=v
    else:sup=v
   elif c in '₀₁₂₃₄₅₆₇₈₉ᵢⱼₙₘₖ':
    start=self.i
    while self.i<len(self.s) and self.s[self.i] in '₀₁₂₃₄₅₆₇₈₉ᵢⱼₙₘₖ':self.i+=1
    sub=expr(self.s[start:self.i].translate(SUB))
   elif c in '⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺ⁿᵀ':
    start=self.i
    while self.i<len(self.s) and self.s[self.i] in '⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺ⁿᵀ':self.i+=1
    sup=expr(self.s[start:self.i].translate(SUP))
   else:break
  if sub and sup:return tag('msubsup',result+sub+sup)
  if sub:return tag('msub',result+sub)
  if sup:return tag('msup',result+sup)
  return result

def expr(s):
 # Signed numeric fractions attach the minus to the numerator, never lose it.
 return Parser(s).seq()
def math(s,display=False):
 return '<math xmlns="http://www.w3.org/1998/Math/MathML"'+(' display="block"' if display else '')+'>'+tag('semantics',expr(s)+tag('annotation',E(s),'encoding="text/plain"'))+'</math>'
def matrix(d,affected=(),pivot=None,duplicate=False):
 a=d['a'];bar=d.get('bar');label='Matrix: '+'; '.join(', '.join(r[:bar])+(' | '+', '.join(r[bar:]) if bar else '') if bar else ', '.join(r) for r in a)
 return '<div class="math-scroll" tabindex="0" role="region" aria-label="Matrix; scroll horizontally if needed"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block" data-matrix="'+E(json.dumps(d),quote=True)+'" data-duplicate="'+str(duplicate).lower()+'" aria-label="'+E(label,quote=True)+'">'+matrix_node(a,bar,affected,pivot)+'</math></div>'
# Deliberately bounded inline tokens. Prose is never run through the math lexer.
INLINE=re.compile(r'\[[^\[\]\n]*(?:,|;)[^\[\]\n]*\]|(?<![\w.])[-−]?\d+/\d+(?![\w/])|[A-Za-zℝθαβπ](?:_\{[^}]+\}|_(?:\d+|[a-z])|\^\([^()]+\)|\^\{[^}]+\}|\^[\w]+|[₀₁₂₃₄₅₆₇₈₉ᵢⱼₙₘₖ]+|[⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺ⁿᵀ]+)+|(?<!\w)R\d+(?!\w)')
def inline_plain(s):
 out=[];pos=0
 for m in INLINE.finditer(s):
  out.append(E(s[pos:m.start()]));raw=m.group();node=math(re.sub(r'^R(\d+)$',r'R_\1',raw));out.append('<span class="inline-math-scroll" tabindex="0" role="region" aria-label="Inline matrix; scroll horizontally if needed">'+node+'</span>' if raw.startswith('[') else node);pos=m.end()
 out.append(E(s[pos:]));return ''.join(out)
def inline(s):
 # Bold and emphasis are structural, not global mathematical replacements.
 parts=re.split(r'(\*\*.*?\*\*)',s)
 return ''.join('<strong>'+inline_plain(p[2:-2])+'</strong>' if p.startswith('**') and p.endswith('**') else inline_plain(p) for p in parts)
