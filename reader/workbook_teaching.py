"""Concrete arithmetic supplements and reauthored symbolic arguments."""
from fractions import Fraction as F
from authored_lessons import P,D,M,S,A,T
from beginner_math import product_nodes,array_expr,par,signed_sum,CHECKS

def entrywise(A,B=None,c=1,d=0,title='Calculate matching entries'):
 A=[[F(v) for v in r] for r in A];B=[[F(v) for v in r] for r in B] if B is not None else [[F(0)]*len(A[0]) for r in A]
 children=[P('Use the entry in the same row and column each time. A scalar multiplies every entry, including zeros and negative numbers.')];C=[]
 for i,row in enumerate(A):
  out=[]
  for j,v in enumerate(row):
   value=F(c)*v+F(d)*B[i][j];out.append(value)
   expression=par(c)+par(v)
   if d:expression+=' + '+par(d)+par(B[i][j])
   expression+=' = '+signed_sum([F(c)*v,F(d)*B[i][j]])+' = '+str(value)
   children.extend([P(f'Row {i+1}, column {j+1}:'),D(expression)])
  C.append(out)
 children.append(M(C,'Collect the answers in their original positions.'))
 CHECKS.append({'kind':'entrywise','A':A,'B':B,'c':c,'d':d,'C':C})
 return S(title,*children)

A0=[[2,0,-1],[4,-3,2]];B0=[[7,-5,1],[1,-4,-3]]
SUPPLEMENTS={
 '2.1.1':[S('Read the two 2 × 3 arrays',M(A0,'A'),M(B0,'B')),entrywise(A0,c=-2,title='For −2A: multiply each of the six entries by −2'),entrywise(B0,A0,1,-2,'For B − 2A: subtract twice the matching A entry')],
 '2.1.2':[S('Addition needs matching positions',M(A0,'A'),M(B0,'B')),entrywise(A0,B0,1,2,'For A + 2B: scale B, then add matching entries')],
 '2.1.3':[S('Build 3I₂ before using it',M([[3,0],[0,3]]),M([[4,-1],[5,-2]],'A')),entrywise([[3,0],[0,3]],[[4,-1],[5,-2]],1,-1,'For 3I₂ − A: subtract entry by entry'),entrywise([[4,-1],[5,-2]],c=3,title='For (3I₂)A: every entry receives a factor 3')],
 '2.1.4':[S('Read A and 5I₃',M([[9,-1,3],[-8,7,-3],[-4,1,8]],'A'),M([[5,0,0],[0,5,0],[0,0,5]],'5I₃')),entrywise([[9,-1,3],[-8,7,-3],[-4,1,8]],[[5,0,0],[0,5,0],[0,0,5]],1,-1,'For A − 5I₃: subtract 5 on the diagonal, 0 elsewhere'),entrywise([[9,-1,3],[-8,7,-3],[-4,1,8]],c=5,title='For (5I₃)A: scale every entry by 5')],
 '1.3.1':[S('Start with the actual input vectors',M([[-1],[2]],'u'),M([[-3],[3]],'v')),entrywise([[-1],[2]],[[-3],[3]],1,1,'Add u + v coordinate by coordinate'),entrywise([[-1],[2]],[[-3],[3]],1,-2,'For u − 2v: scale v first, then subtract')],
 '1.3.2':[S('Start with the actual input vectors',M([[3],[2]],'u'),M([[2],[3]],'v')),entrywise([[3],[2]],[[2],[3]],1,1,'Add u + v coordinate by coordinate'),entrywise([[3],[2]],[[2],[3]],1,-2,'For u − 2v: scale v first, then subtract')],
 '1.8.1':[S('Double each coordinate of the known input',D('2(1) = 2'),D('2(-3) = -6'),D('T(1,-3) = [2;-6]')),S('Do the same to a general input',D('T(a,b) = [2a;2b]'),P('The input is known, so these are images rather than equations to solve. The factor 2 stretches from the origin without reversing direction.'))],
 '1.8.2':[S('Multiply every coordinate by one half',D('(1/2)(1) = 1/2'),D('(1/2)(0) = 0'),D('(1/2)(-4) = -2'),D('T(1,0,-4) = [1/2;0;-2]')),S('Read the general rule',D('T(a,b,c) = [a/2;b/2;c/2]'),P('There are three output entries. The positive factor 1/2 shortens each arrow toward the origin without reversing it.'))],
 '1.8.17':[S('Use the known images, with the same weights',D('T(3u) = 3T(u) = 3[2;1]'),D('3(2) = 6'),D('3(1) = 3'),D('T(3u) = [6;3]')),S('Compute the other weighted image',D('T(2v) = 2T(v) = 2[-1;3]'),D('2(-1) = -2'),D('2(3) = 6'),D('T(2v) = [-2;6]')),S('Add the two output vectors',D('T(3u+2v) = [6;3] + [-2;6]'),D('6 + (-2) = 4'),D('3 + 6 = 9')),A(D('T(3u+2v) = [4;9]'),P('This uses linearity. The weights multiply T(u),T(v), rather than substituting u,v for their images.'))],
 '1.8.19':[S('Decompose an arbitrary input using the basis',D('x = x_1e_1 + x_2e_2'),P('The first basis vector selects the first coordinate; the second selects the second.')),S('Use linearity with the two given images',D('T(x) = x_1[2;5] + x_2[-1;6]'),D('T(x) = [2x_1-x_2;5x_1+6x_2]')),S('Substitute x = (5,−3)',D('2(5) - (-3) = 10 + 3 = 13'),D('5(5) + 6(-3) = 25 - 18 = 7')),A(D('T(5,-3) = [13;7]'),P('The preceding formula determines T for every input, not only this example.'))]
}
# These replace only the compact prose; no original source matrix state is lost.
REPLACEMENTS={
 '2.2.30':[
 S('Given and the two goals',D('(A - AX)^(-1) = X^(-1)B'),P('A, X, and A − AX are invertible square matrices. First prove B is invertible. Then solve for X, justifying every inverse used.')),
 S('Part (a): isolate B by multiplying on the left',D('X(A-AX)^(-1) = XX^(-1)B'),D('B = X(A-AX)^(-1)'),P('Both factors on the right are invertible by the hypotheses. Their product is invertible.')),
 S('Write and justify the inverse of B',D('B^(-1) = (A-AX)X^(-1)'),P('The inverse of a product reverses factor order. Multiplying these two displayed products in either order cancels adjacent inverse pairs to give I.')),
 S('Part (b): invert the original equality',D('A - AX = (X^(-1)B)^(-1)'),D('A - AX = B^(-1)X'),P('The right side must reverse order. B⁻¹ is now legal because part (a) established invertibility.')),
 S('Gather the terms containing X on the right',D('A = AX + B^(-1)X'),D('A = (A + B^(-1))X'),P('Distribute on the right to check this factoring. No factors have been commuted.')),
 S('Prove the new left factor is invertible before using it',D('A + B^(-1) = AX^(-1)'),P('Multiply the preceding equality on the right by X⁻¹. The result is a product of two invertible matrices, so A + B⁻¹ is invertible.')),
 S('Now isolate X legally',D('(A+B^(-1))^(-1)A = X')),
 S('Check against the original identity',D('A = (A+B^(-1))X'),D('A - AX = B^(-1)X'),D('(A-AX)^(-1) = (B^(-1)X)^(-1) = X^(-1)B'),P('Factoring back and then inverting recovers the original equality under the stated hypotheses.')),
 A(D('B^(-1) = (A-AX)X^(-1)'),D('X = (A+B^(-1))^(-1)A'))],
 '2.2.44':[
 S('See the pattern first for n = 3',M([[1,0,0],[1,2,0],[1,2,3]],'A: entries in column j are j on or below the diagonal.'),P('The diagonal contains positions (i,i). The subdiagonal is immediately below it, at positions (i,i−1).')),
 S('Separate the triangular pattern from the column weights',D('A = LD'),M([[1,0,0],[1,1,0],[1,1,1]],'L: ones on and below the diagonal.'),M([[1,0,0],[0,2,0],[0,0,3]],'D: column weights.'),P('Right multiplication by D scales column j of L by j, which reconstructs A.')),
 S('Undo those actions in reverse order',D('A^(-1) = D^(-1)L^(-1)'),P('L⁻¹ subtracts the preceding row; D⁻¹ divides row i by i. All divisors i are nonzero positive integers.'),M([[1,0,0],['-1/2','1/2',0],[0,'-1/3','1/3']],'Candidate B for n = 3.')),
 S('State the general candidate precisely',D('B_{ii} = 1/i'),D('B_{i,i-1} = -1/i'),P('The second formula applies for i ≥ 2. All other entries are zero.')),
 S('Verify BA by subtracting two actual rows',D('(row_i(A) - row_{i-1}(A))/i = e_i^T'),P('For i ≥ 2, the first i−1 entries cancel. The surviving entry is i in position i; division by i makes it 1. Row 1 of A is already e₁ᵀ. Hence every row of BA is the matching identity row.')),
 S('Verify AB by its entries',D('j(1/j) = 1'),P('This is the diagonal case. Below the diagonal the only two possible contributions cancel:'),D('j(1/j) + (j+1)(-1/(j+1)) = 1 - 1 = 0'),P('Above the diagonal every contribution is zero. Thus AB also equals I.')),
 A(P('The inverse has diagonal entry 1/i, subdiagonal entry −1/i, and zeros elsewhere, with the subdiagonal rule used for i ≥ 2. Both inverse identities have been verified.'))]
}

def inverse_formula_nodes(A):
 a,b=A[0];c,d=A[1];a,b,c,d=map(F,[a,b,c,d]);delta=a*d-b*c
 if not delta:return [S('Check the determinant first',D(par(a)+par(d)+' - '+par(b)+par(c)+' = 0')),A(P('There is no inverse. The inverse formula would require division by zero.'))]
 adj=[[d,-b],[-c,a]];inv=[[v/delta for v in row] for row in adj]
 return [S('Read the entries of the actual 2 × 2 matrix',M(A),D('a = '+str(a)),D('b = '+str(b)),D('c = '+str(c)),D('d = '+str(d))),S('Compute the denominator before dividing',D('ad - bc = '+par(a)+par(d)+' - '+par(b)+par(c)),D(str(a*d)+' - ('+str(b*c)+') = '+str(delta)),P('This determinant is nonzero, so an inverse exists.')),S('Build the adjugate, then divide every entry',M(adj,'Swap the two diagonal entries. Negate the two off-diagonal entries.'),*[D(str(v)+' / ('+str(delta)+') = '+str(v/delta)) for row in adj for v in row],M(inv,'The resulting inverse.'))]
for id,A0 in [('2.2.1',[[8,3],[5,2]]),('2.2.2',[[3,1],[7,2]]),('2.2.3',[[8,3],[-7,-3]]),('2.2.4',[[3,-2],[7,-4]])]:SUPPLEMENTS[id]=inverse_formula_nodes(A0)
SUPPLEMENTS['2.2.7']=[S('Use the known inverse on the actual target',M([[2,-3],[-5,8]],'A⁻¹'),M([[2],[-1]],'b'),D('x_1 = 2(2) + (-3)(-1) = 4 + 3 = 7'),D('x_2 = (-5)(2) + 8(-1) = -10 - 8 = -18'),P('The independent row reduction and substitution below check this same input.'))]
SUPPLEMENTS['2.2.8']=[S('Multiply the actual inverse by b',M([[-2,1],[7,-3]],'A⁻¹'),M([[-2],[3]],'b'),D('x_1 = (-2)(-2) + 1(3) = 4 + 3 = 7'),D('x_2 = 7(-2) + (-3)(3) = -14 - 9 = -23'))]
SUPPLEMENTS['2.2.9']=[S('Read the four right-hand sides separately',P('The four target columns are (−1,3), (1,−5), (2,6), and (3,5). Each column needs its own input, even when all are reduced together.'),M([[6,-1],['-5/2','1/2']],'A⁻¹'))]
for x,y in [(-1,3),(1,-5),(2,6),(3,5)]:
 SUPPLEMENTS['2.2.9'].append(S(f'Input for target ({x},{y})',D('x_1 = 6('+str(x)+') - ('+str(y)+') = '+str(6*x-y)),D('x_2 = (-5/2)('+str(x)+') + (1/2)('+str(y)+') = '+str(F(-5,2)*x+F(1,2)*y))))

from parameter_lessons import PARAMETERS
REPLACEMENTS.update(PARAMETERS)
# Two composition/family examples reviewed directly in the rendered workbook.
REPLACEMENTS['1.5.21']=[
 S('Compare the two equations',D('x_1+9x_2-4x_3 = 0'),D('x_1+9x_2-4x_3 = -2'),P('The left sides are identical; only the target changes. We will describe every solution of each equation.')),
 S('Choose the two free coordinates',D('x_2 = s'),D('x_3 = t'),P('One equation determines x₁ after any real choices s,t. A free coordinate is one we can choose rather than one forced to a single value.')),
 S('Solve the homogeneous equation for x₁',D('x_1+9s-4t = 0'),D('x_1 = -9s+4t'),D('x = [-9s+4t;s;t]'),D('x = s[-9;1;0]+t[4;0;1]')),
 S('Solve the equation with right side −2',D('x_1+9s-4t = -2'),D('x_1 = -2-9s+4t'),D('x = [-2;0;0]+s[-9;1;0]+t[4;0;1]')),
 S('See different choices give different solutions',D('s = 0, t = 0: x = [-2;0;0]'),D('s = 1, t = 0: x = [-11;1;0]'),D('s = 0, t = 1: x = [2;0;1]'),P('These are three examples for the equation with right side −2. The same choices in the homogeneous family omit the starting vector (−2,0,0).')),
 S('Verify both families for arbitrary choices',D('(-9s+4t)+9s-4t = 0'),D('(-2-9s+4t)+9s-4t = -2')),
 S('Explain the geometry and the complete solution sets',P('The directions (−9,1,0) and (4,0,1) are independent: the second coordinate of a zero combination forces its first weight to be zero, and the third forces its other weight to be zero. Two independent directions generate a plane. Both families use exactly these directions, so the planes are parallel. Their right sides differ, so no point lies on both.')),
 A(D('Ax = 0: x = s[-9;1;0]+t[4;0;1]'),D('Ax = -2: x = [-2;0;0]+s[-9;1;0]+t[4;0;1]'),P('Here s,t range independently over all real numbers. The second plane is the first translated by (−2,0,0).'))]
REPLACEMENTS['1.9.9']=[
 S('Identify the order of the two actions',P('First perform the horizontal shear sending e₂ to e₂ − 3e₁. Then reflect in the line x₂ = −x₁. The output of the first action becomes the input to the second.')),
 S('Build the shear from the images of the basis vectors',D('e_1 = [1;0]'),D('e_2 = [0;1]'),D('S(e_1) = [1;0]'),D('S(e_2) = [0;1]-3[1;0] = [-3;1]'),D('S = [1,-3;0,1]'),P('A standard matrix has the image of e₁ in column 1 and the image of e₂ in column 2.')),
 S('Build the reflection in the same way',D('R(e_1) = [0;-1]'),D('R(e_2) = [-1;0]'),D('R = [0,-1;-1,0]'),P('Reflection in x₂ = −x₁ swaps the coordinates and negates both. The line itself stays fixed.')),
 S('Apply shear, then reflection to an arbitrary input',D('S[x_1;x_2] = [x_1-3x_2;x_2]'),D('R[x_1-3x_2;x_2] = [-x_2;-(x_1-3x_2)]'),D('T(x) = [-x_2;-x_1+3x_2]')),
 S('Multiply R times S in that order',D('a_{11} = 0(1)+(-1)(0) = 0+0 = 0'),D('a_{12} = 0(-3)+(-1)(1) = 0-1 = -1'),D('a_{21} = (-1)(1)+0(0) = -1+0 = -1'),D('a_{22} = (-1)(-3)+0(1) = 3+0 = 3')),
 A(D('A = RS = [0,-1;-1,3]'),P('The rightmost factor acts first. This matrix produces the coordinate rule obtained above.'))]
