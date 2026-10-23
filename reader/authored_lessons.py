"""Question-specific teaching manuscripts. Typed nodes are exported to source/teaching.
These replace the compact practice answers in BOTH places they are displayed.
"""
from beginner_math import product_nodes,array_expr

def P(t):return {'type':'p','text':t}
def D(t):return {'type':'eq','text':t}
def M(a,label=None):return {'type':'matrix','a':a,**({'label':label} if label else {})}
def S(t,*children):return {'type':'stage','title':t,'children':list(children)}
def A(*children):return {'type':'final','children':list(children)}
def T(h,r):return {'type':'table','headers':h,'rows':r}
PRACTICE={
'F1':[
 S('Work inside the parentheses first',D('3 - 5 = -2'),P('The minus sign means move five units left from 3. The result is negative.')),
 S('Multiply by the outside −2',D('(-2)(-2) = 4'),P('A negative times a negative is positive. The outside −2 multiplies the entire parenthesis.')),
 S('Give the fractions a common denominator',D('1/2 = 3/6'),D('1/2 - 5/6 = 3/6 - 5/6 = -2/6 = -1/3'),P('Sixths have the same size, so subtract their numerators. Divide numerator and denominator by 2 to simplify.')),
 S('Combine the integer and the fraction',D('4 - 1/3 = 12/3 - 1/3 = 11/3')),
 A(D('11/3'))],
'F2':[
 S('Start with the given equation',D('2(x - 3)/5 = 4'),P('The fraction applies to all of 2(x − 3), not just to the 3.')),
 S('Undo division by 5',D('5(2(x - 3)/5) = 5(4)'),D('2(x - 3) = 20'),P('Multiply both sides by the same nonzero number to preserve equality.')),
 S('Undo multiplication by 2',D('2(x - 3)/2 = 20/2'),D('x - 3 = 10')),
 S('Undo subtraction of 3',D('x - 3 + 3 = 10 + 3'),D('x = 13')),
 S('Check in the original equation',D('2(13 - 3)/5 = 2(10)/5 = 20/5 = 4')),
 A(D('x = 13'))],
'F4':[
 S('A subscript is a label',D('x_2'),P('This means the unknown labeled 2. It does not tell you to multiply x by 2 or square it.')),
 S('A superscript can be a power',D('x^2 = x x'),P('This means multiply x by itself. If x = 3, the result is 9.')),
 S('Existence and uniqueness ask different questions',T(['Question','What must be true'],[['Does a solution exist?','At least one input satisfies every equation.'],['Is the solution unique?','One input works, and no different input works.']]),P('A whole line of solutions has many inputs, so existence holds but uniqueness fails.')),
 A(P('A label and a power have different meanings. Having a solution and having exactly one solution are different claims.'))],
'F5':[
 S('Choose equations with one shared point',D('x + y = 1'),D('x - y = 1')),
 S('Check the shared point (1,0)',D('1 + 0 = 1'),D('1 - 0 = 1'),P('It satisfies both equations.')),
 S('Find a point that belongs to only one equation',D('0 + 1 = 1'),D('0 - 1 = -1'),P('The point (0,1) satisfies the first equation and fails the second. The two solution sets therefore differ.')),
 A(P('The statement is false. One shared point does not mean two sets contain exactly the same points.'))],
'S12':[
 S('First system: write its augmented matrix',M([[1,1,2],[2,2,5]]),D('R_2 ← R_2 - 2R_1')),
 S('Calculate the new second row',D('2 - 2(1) = 0'),D('2 - 2(1) = 0'),D('5 - 2(2) = 1'),P('It says 0 = 1. No input can satisfy this.')),
 S('Second system: the constant is 4 instead',M([[1,1,2],[2,2,4]]),D('4 - 2(2) = 0'),P('The second row is now 0 = 0. It imposes no restriction, so only x₁ + x₂ = 2 remains.')),
 S('Describe every solution of the second system',D('x_2 = t'),D('x_1 = 2 - t'),D('(2-t) + t = 2'),P('Any real t works. Conversely, choosing x₂ forces exactly this value of x₁.')),
 A(P('First system: no solution.'),D('x = [2-t;t]'),P('Second system: the displayed vector for every real t.'))],
'S13':[
 S('Keep row 1 and change row 2',D('R_2 ← R_2 - 3R_1'),P('Subtract three copies of row 1 from the old row 2.')),
 S('Undo that change',D('(R_2 - 3R_1) + 3R_1 = R_2'),P('Adding back the same three copies recovers the original row.')),
 S('Compare multiplication by zero',D('0[1,2] = [0,0]'),D('0[7,-3] = [0,0]'),P('Different rows become the same zero row. Nothing in that zero row tells you which original row to recover.')),
 A(P('Adding a multiple of a retained different row is reversible. Multiplying a row by zero is not.'))],
'R1':[
 S('Locate the first nonzero entry of each nonzero row',M([[1,2,0],[0,0,1],[0,0,0]]),P('They are the 1 in column 1 and the 1 in column 3. These are the leading entries.')),
 S('Check the three REF rules',T(['Rule','What the actual matrix shows'],[['Zero rows last','The all-zero row is row 3, at the bottom.'],['Leading entries move right','Column 3 lies to the right of column 1.'],['Zeros below each leading entry','Column 1 has zeros below its leading 1; column 3 also has a zero below its leading 1.']])) ,
 S('Check the two extra RREF rules',T(['Extra rule','Check'],[['Leading entries equal 1','Both leading entries are already 1.'],['Each leading 1 is alone in its column','Column 1 is (1,0,0); column 3 is (0,1,0).']]),P('Column 2 has no pivot. The 2 in that column does not violate a pivot-column rule.')),
 A(P('The matrix is RREF and therefore also REF.'))],
'R3':[
 S('Read the dimensions',P('A 3 × 5 coefficient matrix records 3 equations in 5 unknowns. The right-hand-side vector b has 3 entries.')),
 S('Ask about existence: inspect rows',P('There are 3 pivots distributed among 3 rows.'),P('Pivots occupy different rows. Three pivots among three rows therefore give a pivot in every row. There is no unused coefficient row that could turn into 0 = a nonzero constant.')),
 S('Apply the existence theorem',D('A x = b'),P('A pivot in every coefficient row means this equation can be solved for every three-entry b.')),
 S('Ask about uniqueness: inspect columns',D('5 - 3 = 2'),P('Five unknowns but only three pivot columns leave two free variables. They can vary independently; the pivot equations determine the other unknowns.')),
 A(P('Every b in ℝ³ has a solution. Every such system has infinitely many solutions, with two free parameters; none has a unique solution.'))],
'V1':[
 S('Multiply all coordinates by their weights',D('4[1;-2] = [4;-8]'),D('(-3)[2;-5] = [-6;15]'),P('The positive factor 4 stretches u in its original direction. The negative factor −3 stretches v and reverses its direction.')),
 S('Add coordinates in matching positions',D('4 + (-6) = -2'),D('-8 + 15 = 7')),
 A(D('4u - 3v = [-2;7]'))],
'V2':[
 S('Name the two unknown weights',D('c_1[1;1] + c_2[2;-1] = [5;1]'),P('We are asking whether some amounts of the two supplied vectors add to the target.')),
 S('Match the first and second coordinates',D('c_1 + 2c_2 = 5'),D('c_1 - c_2 = 1')),
 S('Subtract the second equation from the first',D('(c_1 + 2c_2) - (c_1 - c_2) = 5 - 1'),D('3c_2 = 4'),D('c_2 = 4/3')),
 S('Use the second equation to find the other weight',D('c_1 - 4/3 = 1'),D('c_1 = 1 + 4/3 = 3/3 + 4/3 = 7/3')),
 S('Verify the actual weighted sum',D('(7/3)[1;1] + (4/3)[2;-1] = [7/3;7/3] + [8/3;-4/3]'),D('[15/3;3/3] = [5;1]')),
 A(P('Yes, the target belongs to the span.'),D('c_1 = 7/3'),D('c_2 = 4/3'))],
'V3':[
 S('Compare the two generators',D('(3/2)[2;4;0] = [3;6;0]'),P('The second arrow points along the same line as the first; it supplies no new direction.')),
 S('Describe everything they can build',D('s[2;4;0] + t[3;6;0] = (s + (3/2)t)[2;4;0]'),P('Every combination is a multiple of (2,4,0). All multiples are attainable, so the span is precisely the line through that vector and the origin.')),
 S('Test the target (1,0,0)',D('2k = 1'),D('k = 1/2'),D('4k = 4(1/2) = 2'),P('The first coordinate would force k = 1/2. That would make the second coordinate 2, but the target needs 0.')),
 A(P('The span is a line through the origin. The target (1,0,0) is outside it.'))],
'V4':[
 S('Use batch amounts as the unknowns',P('Let a be the number of type-A batches and b the number of type-B batches. Match each resource separately.'),D('2a + 3b = 13'),D('5a + b = 13')),
 S('Express b using the second equation',D('b = 13 - 5a')),
 S('Substitute into the first equation',D('2a + 3(13 - 5a) = 13'),D('2a + 39 - 15a = 13'),D('-13a = -26'),D('a = 2')),
 S('Recover b and check both resources',D('b = 13 - 5(2) = 3'),D('2(2) + 3(3) = 4 + 9 = 13'),D('5(2) + 3 = 10 + 3 = 13')),
 A(P('Use 2 type-A batches and 3 type-B batches. Both amounts are nonnegative.'))],
'A2':[
 S('Count the output equations and input coordinates',P('A has 2 rows and 3 columns. It takes a three-entry input and returns a two-entry output.')),
 S('Two pivots fill both rows',P('There is a pivot in each coefficient row. The existence theorem says Ax = b is consistent for every b in ℝ². This is what onto ℝ² means.')),
 S('Two pivots cannot fill three columns',D('3 - 2 = 1'),P('One coefficient column is nonpivot. Its input coordinate is free; choosing it determines the remaining basic coordinates.')),
 A(P('The map is onto ℝ². Every b has infinitely many inputs, with one free parameter. It is not one-to-one.'))],
'H1':[
 S('Choose the coordinates that are not determined',D('x_1 - 2x_2 + x_3 = 0'),D('x_2 = s'),D('x_3 = t'),P('The one equation can determine x₁ once x₂ and x₃ are chosen. The choices s and t are independent real numbers.')),
 S('Calculate x₁ from those choices',D('x_1 - 2s + t = 0'),D('x_1 = 2s - t')),
 S('Collect one direction for each parameter',D('x = [2s-t;s;t] = s[2;1;0] + t[-1;0;1]')),
 S('Check the entire family, not only one point',D('(2s - t) - 2s + t = 0'),P('This identity holds for every s,t. Conversely, the equation forces exactly x₁ = 2s − t, so no solutions are omitted.')),
 A(D('x = s[2;1;0] + t[-1;0;1]'),P('All s,t are real. For s = 1,t = 0 the solution is (2,1,0), which is nontrivial because it is not the zero vector.'))],
'H2':[
 S('Choose two independent free coordinates',D('x_2 = s'),D('x_3 = t')),
 S('Use the equation with right side 5',D('x_1 - 2s + t = 5'),D('x_1 = 5 + 2s - t')),
 S('Separate the starting point from the directions',D('x = [5;0;0] + s[2;1;0] + t[-1;0;1]')),
 S('Verify for arbitrary parameters',D('(5 + 2s - t) - 2s + t = 5'),P('The cancellation works for every pair of real parameters. Conversely, every solution must have these coordinates.')),
 A(D('x = [5;0;0] + s[2;1;0] + t[-1;0;1]'),P('This plane is H1 shifted by (5,0,0). The directions are unchanged, so the planes are parallel. The new plane does not pass through the origin.'))],
'H3':[
 S('Given: two inputs produce the same b',D('Ap = b'),D('Aq = b'),P('We must show that their difference produces zero. A homogeneous equation has zero on the right.')),
 S('Apply distributivity',D('A(p - q) = Ap - Aq'),P('A acts on the subtraction coordinate by coordinate.')),
 S('Substitute the two known outputs',D('Ap - Aq = b - b = 0')),
 S('Use the extra hypothesis if only zero is homogeneous',D('A(p-q) = 0'),D('p - q = 0'),D('p = q'),P('Under that hypothesis the difference cannot be any nonzero vector.')),
 A(P('The difference p − q is a homogeneous solution. If the homogeneous equation has only zero, any two solutions of Ax = b coincide; every consistent system then has exactly one solution.'))],
'I1':[
 S('What does a dependence relation ask for?',P('Find weights that are not all zero but whose weighted vectors add to zero. A zero weight on one vector is allowed.')),
 S('Use the fact that the second vector is twice the first',D('2[1;2] - [2;4] + 0[0;1] = [2;4] - [2;4] + [0;0]'),D('[0;0]')),
 S('Check the weights',D('[2;-1;0]'),P('At least the weights 2 and −1 are nonzero. This is different from choosing all three weights zero, which always works and proves no dependence.')),
 A(P('The three vectors are dependent. They also outnumber the 2 entries in each vector, which independently gives the same conclusion.'))],
'I3':[
 S('First claim: take a subset of an independent collection',P('Suppose a weighted sum of the subset vectors is zero. Assign weight 0 to every vector omitted from the full collection. The extended sum is still zero.')),
 S('Apply independence of the full collection',P('Its only zero-producing weights are all zero. In particular, the original subset weights must all be zero. That is exactly independence of the subset.')),
 S('Second claim: enlarge a dependent collection',P('Start with its known zero combination whose weights are not all zero. Give each added vector weight 0. The old nonzero weights remain nonzero, and the extended sum is still zero.')),
 A(P('Every subset of an independent collection is independent. Every superset of a dependent collection is dependent. The argument uses zero weights to pass between collections without changing the sum.'))],
'I4':[
 S('Choose two nonzero vectors on the same line',M([[1],[0]]),M([[2],[0]])),
 S('Find a nontrivial zero combination',D('2[1;0] - [2;0] = [2;0] - [2;0] = [0;0]'),P('The weights 2 and −1 are not both zero.')),
 A(P('The statement is false. Excluding the zero vector is necessary for independence, but is not sufficient: nonzero vectors may still repeat a direction.'))],
'T1':[
 S('Compute the image of the given input',D('T(3,-1) = (3 + 2(-1), -3 + (-1))'),D('T(3,-1) = (3-2,-3-1) = (1,-4)')),
 S('A preimage is an input giving the requested output',D('x_1 + 2x_2 = 5'),D('-x_1 + x_2 = 1')),
 S('Add the equations to eliminate x₁',D('3x_2 = 6'),D('x_2 = 2'),D('x_1 = 5 - 2(2) = 1')),
 S('Verify the preimage and its uniqueness',D('T(1,2) = (1 + 4,-1 + 2) = (5,1)'),P('Each input coordinate is fixed by the equations; neither is free. Equivalently, both coefficient columns have pivots.')),
 A(P('The image of (3,−1) is (1,−4). The unique input for output (5,1) is (1,2).'))],
'T2':[
 S('Test S at zero',D('S(0,0) = (0,3)'),P('A linear map must send the zero input to the zero output. This nonzero output already disproves linearity of S.')),
 S('Passing the zero test is not enough for Q',D('Q(0,0) = (0,0)'),P('We must also test whether addition is preserved.')),
 S('Compare the two sides of additivity',D('Q((1,0)+(0,1)) = Q(1,1) = (1,0)'),D('Q(1,0) + Q(0,1) = (0,0) + (0,0) = (0,0)'),P('The two outputs differ. One valid failure is enough to disprove a property required for all inputs.')),
 A(P('Neither S nor Q is linear. S fails the zero test; Q fails the addition test.'))],
'T3':[
 S('Use the given linearity assumption',D('T(2u-v) = 2T(u) - T(v)'),P('Linearity allows the same input weights to be used on the output vectors.')),
 S('Scale the first known image',D('2[1;2] = [2;4]')),
 S('Subtract the other image coordinate by coordinate',D('[2;4] - [3;-1] = [2-3;4-(-1)] = [-1;5]')),
 A(D('T(2u-v) = [-1;5]'),P('Without linearity, knowing only T(u) and T(v) would not determine this image.'))],
'M1':[
 S('Put the two basis images in columns',D('T(e_1) = [2;1;0]'),D('T(e_2) = [1;-1;3]'),M([[2,1],[1,-1],[0,3]],'Three output coordinates, two input coordinates: size 3 × 2.')),
 S('Test one-to-one behavior with zero output',D('A x = 0'),D('3x_2 = 0'),D('x_2 = 0'),D('2x_1 + 0 = 0'),D('x_1 = 0'),P('Only the zero input produces zero. Therefore different inputs cannot collide: if Au = Av, then A(u − v) = 0 forces u = v.')),
 S('Test onto behavior separately',P('Two columns can supply at most two pivots. Three output rows would require three pivots for onto ℝ³.')),
 S('Exhibit an unreachable output',D('A x = [0;0;1]'),D('3x_2 = 1'),D('x_2 = 1/3'),D('x_1 - x_2 = 0'),D('x_1 = 1/3'),D('2(1/3) + 1/3 = 1'),P('The first requested output is 0, but these forced input values produce 1. The target is unreachable.')),
 A(P('The standard matrix is the displayed 3 × 2 matrix. The map is one-to-one and is not onto ℝ³.'))],
'M2':[
 S('Apply the reflection first',D('(a,b) ↦ (-a,b)')),
 S('Apply the horizontal projection second',D('(-a,b) ↦ (-a,0)'),M([[-1,0],[0,0]])),
 S('Inspect the possible outputs',P('Every output has second coordinate 0, so (0,1) can never occur. Every horizontal output (c,0) occurs by choosing a = −c. Thus the range is exactly the horizontal axis.')),
 S('Find distinct inputs with the same output',D('(1,0) ↦ (-1,0)'),D('(1,2) ↦ (-1,0)'),P('The second input coordinate is erased. These distinct inputs collide.')),
 A(P('The map is neither onto ℝ² nor one-to-one. Its standard matrix is the displayed diagonal matrix.'))],
'M3':[
 S('Onto does not force one-to-one',M([[1,0,0],[0,1,0]]),D('(a,b,c) ↦ (a,b)'),P('Every two-entry output is reached, but c can be anything. There is a pivot in each row and a free third input.')),
 S('One-to-one does not force onto',M([[1,0],[0,1],[0,0]]),D('(a,b) ↦ (a,b,0)'),P('The output uniquely records both inputs. But any three-entry target with nonzero last coordinate is missed. There is a pivot in each column and no pivot in row 3.')),
 A(P('The first matrix is onto ℝ² and not one-to-one. The second is one-to-one into ℝ³ and not onto ℝ³.'))],
'O2':[
 S('Transpose the known product',M([[4,6],[1,3]],'AB: rows are (4,6) and (1,3).'),M([[4,1],[6,3]],'(AB)ᵀ: those rows become columns.')),
 S('Reverse the factors and transpose each',D('(AB)^T = B^T A^T'),M([[2,1],[0,3]],'Bᵀ'),M([[1,0],[2,1]],'Aᵀ')),
 S('Calculate all four entries',D('2(1) + 1(2) = 2 + 2 = 4'),D('2(0) + 1(1) = 0 + 1 = 1'),D('0(1) + 3(2) = 0 + 6 = 6'),D('0(0) + 3(1) = 0 + 3 = 3')),
 A(D('(AB)^T = B^T A^T = [4,1;6,3]'))],
'O3':[
 S('Choose two nonzero matrices',M([[1,0],[0,0]],'A'),M([[0,0],[0,1]],'B')),
 S('Check all entries of AB',D('1(0) + 0(0) = 0'),D('1(0) + 0(1) = 0'),D('0(0) + 0(0) = 0'),D('0(0) + 0(1) = 0')),
 S('Compare with the zero right factor',D('AB = [0,0;0,0] = A0'),P('B is not zero: it has a 1. A has erased the distinction between B and zero, so it cannot be canceled.')),
 A(P('AB = A0 does not force B = 0. Cancellation fails here because A is singular.'))],
'O4':[
 S('Compute the product size',D('(3 × 2)(2 × 4) → 3 × 4'),P('The two inner dimensions match. AB therefore has 3 rows and 4 columns.')),
 S('Transpose swaps the two output counts',D('(AB)^T: 4 × 3')),
 S('Check the reversed transposed product',D('B^T: 4 × 2'),D('A^T: 2 × 3'),D('(4 × 2)(2 × 3) → 4 × 3')),
 S('Check BA before attempting arithmetic',D('(2 × 4)(3 × 2)'),P('The inner counts 4 and 3 differ. BA is undefined.')),
 A(P('AB is 3 × 4. Both (AB)ᵀ and BᵀAᵀ are 4 × 3. BA is undefined.'))],
'N1':[
 S('Identify the four entries and the determinant',M([[2,1],[5,3]],'A'),D('ad - bc = 2(3) - 1(5) = 6 - 5 = 1'),P('The denominator is nonzero, so the 2 × 2 inverse formula applies.')),
 S('Swap the diagonal, negate the off-diagonal, divide by 1',D('A^(-1) = (1/1)[3,-1;-5,2] = [3,-1;-5,2]')),
 S('Verify A times its proposed inverse',D('2(3) + 1(-5) = 1'),D('2(-1) + 1(2) = 0'),D('5(3) + 3(-5) = 0'),D('5(-1) + 3(2) = 1')),
 S('Verify the reverse order too',D('3(2) + (-1)(5) = 1'),D('3(1) + (-1)(3) = 0'),D('(-5)(2) + 2(5) = 0'),D('(-5)(1) + 2(3) = 1')),
 S('Use the inverse on b = (1,2)',D('x = [3,-1;-5,2][1;2]'),D('x_1 = 3(1) - 1(2) = 1'),D('x_2 = -5(1) + 2(2) = -1')),
 S('Substitute into the original system',D('2(1) + 1(-1) = 1'),D('5(1) + 3(-1) = 2')),
 A(D('A^(-1) = [3,-1;-5,2]'),D('x = [1;-1]'))],
'N3':[
 S('One inverse column means one target',D('A x = e_3'),D('e_3 = [0;0;1]'),P('Multiplication by column 3 of A⁻¹ must produce the third identity column. Use the same upper-triangular A as N2.')),
 S('Read the last equation first',D('x_3 = 1')),
 S('Use row 2 to determine x₂',D('x_2 + x_3 = 0'),D('x_2 + 1 = 0'),D('x_2 = -1')),
 S('Use row 1 to determine x₁',D('x_1 + x_2 = 0'),D('x_1 - 1 = 0'),D('x_1 = 1')),
 S('Verify each output coordinate',D('1 + (-1) = 0'),D('-1 + 1 = 0'),D('1 = 1')),
 A(P('The third inverse column, agreeing with N2, is'),M([[1],[-1],[1]]))],
'N4':[
 S('Given: A is invertible and AB = AC',D('AB = AC'),P('We want to prove B = C. We may use A⁻¹ because invertibility is an assumption.')),
 S('Multiply both sides on the left',D('A^(-1)(AB) = A^(-1)(AC)')),
 S('Regroup without changing factor order',D('(A^(-1)A)B = (A^(-1)A)C'),D('IB = IC'),D('B = C')),
 S('Check why the hypothesis matters',M([[1,0],[0,0]],'Singular A'),M([[0,0],[0,1]],'B'),M([[0,0],[0,0]],'C'),D('AB = [0,0;0,0] = AC'),P('B and C are different even though these products are equal. A is not invertible in this counterexample.')),
 A(P('An invertible left factor can be canceled. The displayed singular example shows the assumption cannot be omitted.'))],
'G1':[
 S('Solve the system for a general output (3,2)',M([[1,2,0],[0,1,1]],'A'),D('x_1 + 2x_2 = 3'),D('x_2 + x_3 = 2')),
 S('Choose x₂ and calculate the other coordinates',D('x_2 = t'),D('x_1 = 3 - 2t'),D('x_3 = 2 - t'),D('x = [3;0;2] + t[-2;1;-1]')),
 S('Check both equations for every t',D('(3-2t) + 2t = 3'),D('t + (2-t) = 2')),
 S('Solve with zero on the right instead',D('x_1 + 2x_2 = 0'),D('x_2 + x_3 = 0'),D('x = t[-2;1;-1]'),P('The homogeneous directions are unchanged. The earlier solution set starts at (3,0,2), so it is a translated copy.')),
 S('Read spanning and onto from the rows',P('Column 1 pivots in row 1; column 2 pivots in row 2. Every row has a pivot. Thus the columns span ℝ² and the map is onto ℝ².')),
 S('Read independence and one-to-one from the columns',D('3 - 2 = 1'),P('Three columns but only two pivots leave one free weight. For example, t = 1 gives the nonzero homogeneous input (−2,1,−1). The columns are dependent and the map is not one-to-one.')),
 A(D('Ax = (3,2): x = [3;0;2] + t[-2;1;-1]'),D('Ax = 0: x = t[-2;1;-1]'),P('All t are real. The columns span ℝ² but are dependent. T is onto and not one-to-one.'))],
'G2':[
 S('Record each rule in the correct action order',M([[1,2],[0,1]],'S acts first.'),M([[0,-1],[1,0]],'R acts second.'),D('(a,b) ↦ (a+2b,b) ↦ (-b,a+2b)')),
 S('Read the composite coefficients',M([[0,-1],[1,2]],'RS: coefficient rows for (−b,a + 2b).')),
 S('Apply the rule to (1,2)',D('(-2,1+2(2)) = (-2,5)')),
 S('Solve the output equations to undo the map',D('y_1 = -b'),D('b = -y_1'),D('y_2 = a + 2b'),D('a = y_2 - 2(-y_1) = 2y_1 + y_2'),M([[2,1],[-1,0]],'Inverse matrix.')),
 S('Check both matrix products',D('[0,-1;1,2][2,1;-1,0] = [1,0;0,1]'),D('[2,1;-1,0][0,-1;1,2] = [1,0;0,1]'),P('The products can also be checked entry by entry: the off-diagonal cancellations are 2 − 2 and −2 + 2; the diagonal entries are 1.')),
 S('Undo the numerical output',D('(2(-2)+5,-(-2)) = (1,2)')),
 A(P('The composite sends (a,b) to (−b,a + 2b). Its inverse sends (y₁,y₂) to (2y₁ + y₂,−y₁).'))],
'G3':[
 S('Given and goal',P('A is 3 × 3, and Ax = b can be solved for every b in ℝ³. We must prove that each solution is unique and that A is invertible.')),
 S('Convert existence into row information',P('The all-right-hand-side existence theorem gives a pivot in every coefficient row. Three rows therefore mean three pivots.')),
 S('Use the fact that A is square',P('Those three pivots occupy three different columns. Since there are exactly three columns, every column is a pivot column. There are no free variables.')),
 S('Conclude uniqueness and invertibility',P('Consistency is given for every b. With no free variables, each such system has exactly one solution. In RREF every column now has its own leading 1 and zeros elsewhere, so RREF(A) is I₃.'),D('RREF(A) = I_3'),P('The inverse theorem says a square matrix reducible to I is invertible.')),
 S('Identify where squareness was essential',P('For a 3 × 4 matrix, three row pivots would leave a fourth column without a pivot. Existence would still hold for every three-entry b, but uniqueness would fail.')),
 A(P('Every Ax = b has exactly one solution, and A is invertible.'))]
}
# A3 is a fully authored matrix/vector demonstration, shared without abbreviation.
PRACTICE['A3']=product_nodes([[1,2,3],[0,-1,4]],[[2],[1],[-1]],('A','x'),True)
PRACTICE['A3'][0]['children'].append(P('Row 1 is (1,2,3). Row 2 is (0,−1,4). Each row has three entries, so there are three columns.'))
PRACTICE['A3'].insert(-1,S('Why the row and column methods agree',P('Each output entry adds exactly the same three products in both methods. The row method gathers the products for one output entry. The column method first builds each whole weighted column, then adds corresponding entries. Neither method changes the order of the coordinates.')))


CONVERSION=[
 S('1 · Start with the two equations',D('x_1 + 2x_2 - x_3 = 4'),D('-5x_2 + 3x_3 = 1'),P('We seek three numbers that make both equations true at the same time. At this stage we are changing notation, not finding their values.')),
 S('2 · Identify the three unknowns',D('x_1, x_2, x_3'),P('The subscripts 1, 2, and 3 are labels distinguishing three unknown values. They are not powers or multiplication instructions.')),
 S('3 · Read one coefficient for every variable',T(['Equation','x₁','x₂','x₃','Right side'],[['First','1','2','−1','4'],['Second','0','−5','3','1']]),P('A coefficient is the number multiplying an unknown. The second equation has no x₁ term, so its x₁ coefficient is 0. The term −x₃ means (−1)x₃.')),
 S('4 · Build A from the coefficient rows',M([[1,2,-1],[0,-5,3]],'A: 2 equations give 2 rows; 3 unknowns give 3 columns.'),P('Row 1 records the first equation. Row 2 records the second. Keep the variable order x₁,x₂,x₃ in both rows. The constants do not belong in A.')),
 S('5 · Put the unknowns in a column',D('x = [x_1;x_2;x_3]'),P('The unknown vector has size 3 × 1. Its order matches the three columns of A.')),
 S('6 · Put the constants in a separate column',D('b = [4;1]'),P('This vector has size 2 × 1. Its entries follow the order of the two equations.')),
 S('7 · Write the full matrix equation',D('[1,2,-1;0,-5,3][x_1;x_2;x_3] = [4;1]'),D('A x = b'),P('The sizes (2 × 3)(3 × 1) produce a 2 × 1 output, matching b.')),
 S('8 · Read the same multiplication by columns',D('x_1[1;0] + x_2[2;-5] + x_3[-1;3] = [4;1]'),P('The first column carries the x₁ coefficients; multiply that entire column by x₁. Do the same for columns 2 and 3, with weights x₂ and x₃. Add matching coordinates.')),
 S('9 · Expand the weighted columns to recover the system',D('[x_1;0] + [2x_2;-5x_2] + [-x_3;3x_3] = [4;1]'),D('x_1 + 2x_2 - x_3 = 4'),D('0x_1 - 5x_2 + 3x_3 = 1'),P('Matching first coordinates gives equation 1. Matching second coordinates gives equation 2. Every entry has returned to its original place.')),
 A(P('Linear system ↔ vector equation ↔ matrix equation: the unknowns and constraints are identical. Converting between these representations does not solve the system.'))]
