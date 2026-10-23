"""Exact, displayed arithmetic used by the beginner teaching manuscripts."""
from fractions import Fraction as F
import re,json,html
from mathml import inline,math,matrix
CHECKS=[]
def E(s):return html.escape(str(s),quote=True)
def para(s,cls=''):return '<p'+(' class="'+cls+'"' if cls else '')+'>'+inline(s)+'</p>'
def display(s):return '<div class="math-scroll teaching-equation" tabindex="0" role="region" aria-label="Calculation">'+math(s,True)+'</div>'
def mat(a,bar=None,label=None):
 h=matrix({'a':[[str(v) for v in row] for row in a],'bar':bar},duplicate=True)
 return ('<figure class="teaching-matrix">'+h+'<figcaption>'+inline(label)+'</figcaption></figure>') if label else h
def stage(title,body,kind='calculation-step',id=None):return '<section class="teaching-stage '+kind+'"'+(' id="'+E(id)+'"' if id else '')+'><h4>'+inline(title)+'</h4>'+body+'</section>'
def final(body):return '<div class="final-answer"><span class="answer-label">FINAL ANSWER</span>'+body+'</div>'
def fs(v):return str(F(v))
def par(v):return '('+fs(v)+')'
def signed_sum(values):
 values=[F(v) for v in values];out=''
 for i,v in enumerate(values):out+=('' if i==0 else ' + ' if v>=0 else ' - ')+str(v if i==0 or v>=0 else -v)
 return out

def row_arithmetic(before,after,raw):
 a=[[F(v) for v in r] for r in before['a']];b=[[F(v) for v in r] for r in after['a']]
 op=raw.split('**')[1];rn=[int(x)-1 for x in re.findall(r'R(\d+)',op)]
 if '↔' in op:
  i,j=rn[:2];assert b[i]==a[j] and b[j]==a[i]
  CHECKS.append({'kind':'swap','operation':op,'entries':len(a[i])+len(a[j])})
  return stage('What changes in this swap?',para(f'Row {i+1} takes the complete contents of old row {j+1}. Row {j+1} takes the complete contents of old row {i+1}. No entry is multiplied or added; we only exchange the two equations.'),'entry-calculations')
 target=rn[0];src=rn[-1]
 multiplier=re.search(r'\(([-\d/]+)\)R',op)
 assert multiplier,op
 c=F(multiplier[1]);is_add='+' in op
 items=[]
 for j,(old,source,new) in enumerate(zip(a[target],a[src],b[target])):
  product=c*source
  expected=old+product if is_add else c*old
  assert expected==new,(op,j,expected,new)
  term=par(c)+par(source if is_add else old)
  exp=fs(old)+' + '+term if is_add else term
  middle=signed_sum([old,product]) if is_add else (str(c.numerator*(source if is_add else old).numerator)+'/'+str(c.denominator*(source if is_add else old).denominator))
  suffix=' (right-hand side)' if before.get('bar')==j else ''
  items.append('<div class="entry-calculation"><span class="entry-label">'+f'Row {target+1}, column {j+1}'+suffix+'</span>'+display(exp+' = '+middle+' = '+fs(new))+'</div>')
 CHECKS.append({'kind':'row-entry-arithmetic','operation':op,'entries':len(items)})
 reason=(f'Multiply each entry of old row {src+1} by {c}, then add it to the matching entry of old row {target+1}. The other row is retained.' if is_add else f'Multiply every entry of old row {target+1} by {c}. This includes the constant column when one is present. The multiplier is nonzero, so division by it undoes the step.')
 return stage('Calculate every entry in the changed row',para(reason)+''.join(items),'entry-calculations')

def product_nodes(A,B,names=('A','x'),columns=True):
 A=[[F(x) for x in r] for r in A];B=[[F(x) for x in r] for r in B];m=len(A);n=len(A[0]);r=len(B);p=len(B[0]);out=[]
 out.append({'type':'stage','title':f'Read {names[0]}: {m} rows, {n} columns','children':[{'type':'p','text':'A row runs horizontally, from left to right. A column runs vertically, from top to bottom. Count rows first when writing a size.'},{'type':'matrix','a':A,'label':f'{names[0]} has size {m} × {n}.'}]})
 out.append({'type':'stage','title':f'Read {names[1]}: {r} rows, {p} column'+('s' if p!=1 else ''),'children':[{'type':'matrix','a':B,'label':f'{names[1]} has size {r} × {p}.'}]})
 if n!=r:
  out.append({'type':'final','children':[{'type':'p','text':f'The product is undefined. The left factor has {n} columns, but the right factor has {r} rows. These inner counts must match.'}]});return out
 C=[[sum((A[i][k]*B[k][j] for k in range(n)),F(0)) for j in range(p)] for i in range(m)]
 out.append({'type':'dimension','left':[m,n],'right':[r,p],'result':[m,p]})
 for i in range(m):
  for j in range(p):
   products=[A[i][k]*B[k][j] for k in range(n)];exp=' + '.join(par(A[i][k])+par(B[k][j]) for k in range(n))
   out.append({'type':'stage','title':f'Calculate output row {i+1}'+(f', column {j+1}' if p>1 else ''),'children':[{'type':'p','text':f'Take row {i+1} of {names[0]} and column {j+1} of {names[1]}. Pair entries in their original order: multiply the first pair, the second pair, and so on. Then add.'},{'type':'highlight-product','A':A,'B':B,'row':i,'col':j},{'type':'eq','text':exp},{'type':'eq','text':signed_sum(products)},{'type':'eq','text':fs(C[i][j])}]})
 out.append({'type':'stage','title':'Put the entries into their output positions','children':[{'type':'matrix','a':C,'label':f'The result has {m} rows and {p} column'+('s.' if p!=1 else '.')}]})
 if columns and p==1:
  children=[{'type':'p','text':f'The entries of {names[1]} are weights. Weight 1 multiplies column 1 of {names[0]}, weight 2 multiplies column 2, and so on. A negative weight reverses the sign of every entry in that column.'}]
  for k in range(n):
   col=[[A[i][k]] for i in range(m)];weighted=[[B[k][0]*A[i][k]] for i in range(m)]
   children.extend([{'type':'p','text':f'Column {k+1}, with weight {B[k][0]}:'},{'type':'eq','text':str(B[k][0])+' '+array_expr(col)+' = '+array_expr(weighted)}])
  for i in range(m):children.append({'type':'eq','text':f'\u0079_{i+1} = '+signed_sum([B[k][0]*A[i][k] for k in range(n)])+' = '+fs(C[i][0])})
  children.extend([{'type':'matrix','a':C},{'type':'p','text':'Both methods add exactly the same products. The row method groups them by output entry. The column method groups them by input weight. Regrouping a finite sum does not change its value.'}])
  out.append({'type':'stage','title':'Check with the column method','children':children})
 if columns and p>1:
  children=[{'type':'p','text':'For each output column, use the matching column of the right factor as weights on all columns of the left factor. This is the same row arithmetic grouped vertically.'}]
  for j in range(p):
   terms=['('+str(B[k][j])+')'+array_expr([[A[i][k]] for i in range(m)]) for k in range(n)]
   children.append({'type':'eq','text':'c_'+str(j+1)+' = '+' + '.join(terms)+' = '+array_expr([[C[i][j]] for i in range(m)])})
  out.append({'type':'stage','title':'Check the result one output column at a time','children':children})
 out.append({'type':'final','children':[{'type':'eq','text':names[0]+names[1]+' = '+array_expr(C)},{'type':'p','text':f'Dimensions: ({m} × {n})({r} × {p}) = {m} × {p}.'}]})
 CHECKS.append({'kind':'product','A':A,'B':B,'C':C})
 return out

def array_expr(a):return '['+';'.join(','.join(str(x) for x in row) for row in a)+']'
def render_nodes(nodes):
 out=[]
 for n in nodes:
  t=n['type']
  if t=='p':out.append(para(n['text']))
  elif t=='eq':out.append(display(n['text']))
  elif t=='matrix':out.append(mat(n['a'],n.get('bar'),n.get('label')))
  elif t=='stage':out.append(stage(n['title'],render_nodes(n['children']),n.get('kind','calculation-step')))
  elif t=='final':out.append(final(render_nodes(n['children'])))
  elif t=='html':out.append(n['html'])
  elif t=='table':
   from learning import table
   out.append(table(n['headers'],n['rows']))
  elif t=='dimension':
   m,k=n['left'];r,p=n['right'];out.append(stage('Check that multiplication is allowed','<div class="dimension-check"><span>('+str(m)+' × <strong>'+str(k)+'</strong>)</span><span>(<strong>'+str(r)+'</strong> × '+str(p)+')</span><span>→ '+str(m)+' × '+str(p)+'</span></div>'+para(f'The highlighted inner counts are both {k}: every row of the left factor has one entry for every row of the right factor. The outside counts tell us the output has {m} rows and {p} column'+('s.' if p!=1 else '.')),'dimension-stage'))
  elif t=='highlight-product':
   from learning import mini
   out.append('<div class="pairing-example">'+mini(n['A'],rows=(n['row'],),label=f'Use this highlighted row {n["row"]+1}.')+mini(n['B'],cols=(n['col'],),label=f'Pair it with highlighted column {n["col"]+1}.')+'</div>')
  else:raise ValueError(t)
 return ''.join(out)

def serializable(value):
 if isinstance(value,F):return str(value)
 raise TypeError(type(value).__name__)
