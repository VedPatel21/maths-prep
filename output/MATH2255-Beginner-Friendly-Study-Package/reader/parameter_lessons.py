"""Question-specific algebra for parameter, span, and dependence cases.
The original rigorous manuscript is retained in source/ for comparison.
"""
from authored_lessons import P,D,M,S,A

PARAMETERS={
'1.1.23':[
 S('Eliminate x₁ from the second equation',D('R_2 ← R_2 - 3R_1'),P('Subtract three copies of equation 1 from equation 2. The x₁ terms cancel.'),D('[0,6-3h|-4]'),D('(6-3h)x_2 = -4')),
 S('Find the value that makes division impossible',D('6 - 3h = 0'),D('-3h = -6'),D('h = 2'),P('At this value the equation becomes:'),D('0x_2 = -4'),D('0 = -4'),P('No choice of either unknown can make this true.')),
 S('Check all other values',D('x_2 = -4/(6-3h)'),P('If h ≠ 2, the denominator is nonzero. This fixes x₂, and the first equation then fixes x₁. There is no contradictory row.')),
 A(D('h ≠ 2'),P('Exactly these values give a consistent system. Consistent means at least one solution exists.'))],
'1.1.24':[
 S('Remove x₁ from equation 2',D('R_2 ← R_2 + 2R_1'),D('[0,4+2h|0]'),D('(4+2h)x_2 = 0'),P('The right side is zero. A zero coefficient is harmless if the right side is also zero.')),
 S('Case 1: the coefficient is nonzero',D('4 + 2h ≠ 0'),D('h ≠ -2'),D('x_2 = 0/(4+2h) = 0'),P('The first row can then be solved for x₁.')),
 S('Case 2: the coefficient is zero',D('4 + 2h = 0'),D('2h = -4'),D('h = -2'),D('0x_2 = 0'),P('This equation is true for every x₂. Choose x₂ and use row 1 to determine x₁.')),
 A(P('Every real h gives a consistent system. Both cases have solutions.'))],
'1.1.25':[
 S('Cancel the first coefficient in row 2',D('R_2 ← R_2 + 4R_1'),D('[0,h+12|0]'),D('(h+12)x_2 = 0')),
 S('When h ≠ −12, divide by the nonzero coefficient',D('x_2 = 0/(h+12) = 0'),P('Row 1 then determines x₁.')),
 S('When h = −12, read the equation without dividing',D('(-12+12)x_2 = 0'),D('0 = 0'),P('This is true for any x₂. The first equation still supplies a compatible x₁.')),
 A(P('Every real h is allowed. A row of zeros with a zero right side adds no restriction.'))],
'1.1.26':[
 S('Eliminate the second equation’s unknown terms',D('R_2 ← R_2 + 3R_1'),D('[0,0|5+3h]'),D('0x_1 + 0x_2 = 5+3h'),D('0 = 5+3h')),
 S('Make the remaining equality true',D('5+3h = 0'),D('3h = -5'),D('h = -5/3'),P('We subtract 5 from both sides, then divide both sides by 3.')),
 S('Check the value and rule out the others',D('5+3(-5/3) = 5-5 = 0'),P('The last row is now 0 = 0. The first equation still has solutions. Every other h leaves zero equal to a nonzero number.')),
 A(D('h = -5/3'))],
'1.1.35':[
 S('First remove the x₁ term from row 3',D('R_3 ← R_3 + 2R_1'),D('[0,-3,5|k+2g]'),P('Apply the same operation to the right side: k becomes k + 2g.')),
 S('Then cancel the remaining x₂ and x₃ terms',D('R_3 ← R_3 + R_2'),D('-3 + 3 = 0'),D('5 + (-5) = 0'),D('[0,0,0|k+2g+h]')),
 S('Interpret the last row',D('0 = k+2g+h'),P('The first two coefficient rows have pivots, meaning leading nonzero coefficients that determine basic variables. The last row is the only possible contradiction.')),
 A(D('2g+h+k = 0'),P('This condition is necessary and sufficient for consistency.'))],
'1.1.37':[
 S('Given and what “every f,g” requires',D('x_1 + 3x_2 = f'),D('cx_1 + dx_2 = g'),P('The numbers c,d stay fixed. A solution must exist for every possible right side f,g.')),
 S('Subtract c times equation 1 from equation 2',D('(cx_1+dx_2) - c(x_1+3x_2) = g-cf'),D('cx_1+dx_2-cx_1-3cx_2 = g-cf'),D('(d-3c)x_2 = g-cf')),
 S('Why d = 3c fails the requirement',D('f = 0'),D('g = 1'),D('0x_2 = 1-c(0) = 1'),P('This choice gives 0 = 1, so at least one right side fails.')),
 S('Why d ≠ 3c succeeds for every right side',D('x_2 = (g-cf)/(d-3c)'),D('x_1 = f-3x_2'),P('The denominator is nonzero. These formulas therefore produce both unknowns for any real f,g.')),
 S('Verify the formulas in the second equation',D('cx_1+dx_2 = c(f-3x_2)+dx_2'),D('cx_1+dx_2 = cf+(d-3c)x_2'),D('cx_1+dx_2 = cf+(g-cf) = g')),
 A(D('d ≠ 3c'),P('This is both necessary and sufficient.'))],
'1.2.21':[
 S('Cancel the second row’s unknown terms',D('R_2 ← R_2 - 2R_1'),D('0 = 7-2h'),P('A zero left side must have a zero right side.')),
 S('Solve this condition for h',D('7-2h = 0'),D('-2h = -7'),D('h = 7/2')),
 S('Check consistency',D('7-2(7/2) = 7-7 = 0'),P('This makes row 2 redundant. Row 1 still has solutions. Any other h leaves a contradiction.')),
 A(D('h = 7/2'))],
'1.2.22':[
 S('Remove the first coefficient from row 2',D('R_2 ← R_2 - 5R_1'),D('[0,h+15|3]'),D('(h+15)x_2 = 3')),
 S('Test the zero coefficient case',D('h+15 = 0'),D('h = -15'),D('0x_2 = 3'),P('This is impossible because multiplying any number by zero gives zero.')),
 S('Solve when the coefficient is nonzero',D('x_2 = 3/(h+15)'),P('For every h ≠ −15, this is defined. Row 1 then determines x₁.')),
 A(D('h ≠ -15'))],
'1.2.23':[
 S('Reduce the problem to one remaining constraint',D('R_2 ← R_2 - 4R_1'),D('(8-4h)x_2 = k-8'),P('The number multiplying x₂ decides whether x₂ is determined or free. If that number is zero, check the right side before deciding.')),
 S('Case 1: 8 − 4h is nonzero',D('8-4h ≠ 0'),D('h ≠ 2'),D('x_2 = (k-8)/(8-4h)'),P('There is one x₂ for every k. Equation 1 then fixes one x₁, so the solution is unique. Example: h = 0, k = 0.')),
 S('Case 2: h = 2, but k ≠ 8',D('(8-4(2))x_2 = k-8'),D('0 = k-8'),P('The right side is nonzero. There is no solution. Example: h = 2, k = 0 gives 0 = −8.')),
 S('Case 3: h = 2 and k = 8',D('0x_2 = 8-8'),D('0 = 0'),P('There is no restriction on x₂. Choose x₂ freely; equation 1 determines x₁. Different choices give infinitely many solutions.')),
 A(P('No solution: h = 2 and k ≠ 8. Unique solution: h ≠ 2, with any k. Infinitely many: h = 2 and k = 8. These cases exhaust every possibility.'))],
'1.2.24':[
 S('Eliminate x₁ from equation 2',D('R_2 ← R_2 - 3R_1'),D('(h-9)x_2 = k-6')),
 S('Nonzero coefficient: h ≠ 9',D('x_2 = (k-6)/(h-9)'),D('x_1 = 2-3x_2'),P('Both unknowns are fixed. There is exactly one solution for any k. Example: h = 0, k = 0.')),
 S('Zero coefficient, nonzero right side',D('h = 9'),D('0x_2 = k-6'),P('If k ≠ 6, this is impossible. Example: h = 9, k = 0 gives 0 = −6.')),
 S('Zero coefficient, zero right side',D('h = 9'),D('k = 6'),D('0 = 0'),D('x_2 = t'),D('x_1 = 2-3t'),P('The letter t means any real choice. Two possible choices are:'),D('t = 0: [x_1;x_2] = [2;0]'),D('t = 1: [x_1;x_2] = [-1;1]'),P('Both satisfy x₁ + 3x₂ = 2; the second equation repeats three times that equality.')),
 A(P('No solution: h = 9 and k ≠ 6. Unique solution: h ≠ 9, any k. Infinitely many: h = 9 and k = 6.'))],
'1.3.17':[
 S('Membership means finding two weights',D('b = αa_1+βa_2'),P('α and β are numbers multiplying the two given vectors. Equality of vectors requires equality in every coordinate.'),D('α-2β = 4'),D('4α-3β = 1')),
 S('Use the first equation to replace α in the second',D('α = 4+2β'),D('4(4+2β)-3β = 1'),D('16+8β-3β = 1'),D('16+5β = 1'),D('5β = -15'),D('β = -3')),
 S('Find the other weight',D('α = 4+2(-3)'),D('α = 4-6 = -2')),
 S('Now calculate the required third coordinate',D('h = -2α+7β'),D('h = -2(-2)+7(-3)'),D('h = 4-21 = -17')),
 S('Verify every coordinate, not only the last',D('(-2)(1)+(-3)(-2) = -2+6 = 4'),D('(-2)(4)+(-3)(-3) = -8+9 = 1'),D('(-2)(-2)+(-3)(7) = 4-21 = -17')),
 A(D('h = -17'),D('-2a_1-3a_2 = [4;1;-17]'),P('The forced weights show necessity. The full coordinate check shows sufficiency.'))],
'1.3.18':[
 S('Write the target as a weighted sum',D('y = αv_1+βv_2'),D('α-3β = h'),D('β = -5'),D('-2α+8β = -3'),P('Each equation comes from one matching coordinate. Start with the second because it already gives β.')),
 S('Use β = −5 in the third equation',D('-2α+8(-5) = -3'),D('-2α-40 = -3'),D('-2α = 37'),D('α = -37/2')),
 S('Use both weights to find h',D('h = -37/2-3(-5)'),D('h = -37/2+15'),D('h = -37/2+30/2 = -7/2')),
 S('Check the second and third coordinates too',D('0(-37/2)+1(-5) = -5'),D('(-2)(-37/2)+8(-5) = 37-40 = -3')),
 A(D('h = -7/2'),D('y = (-37/2)v_1-5v_2'),P('The weights are forced by coordinates 2 and 3 and verify the entire target.'))],
'1.3.21':[
 S('Given and what must be shown',D('u = [2;-1]'),D('v = [2;1]'),D('αu+βv = [h;k]'),P('h,k are any real target coordinates. We must find weights α,β for every such target. This is what spanning all of ℝ² means.')),
 S('Translate the weighted sum into coordinate equations',D('2α+2β = h'),D('-α+β = k')),
 S('Solve the second equation for β',D('β = k+α'),P('Add α to both sides. Substitute this expression for β in the first equation.')),
 S('Solve carefully for α',D('2α+2(k+α) = h'),D('2α+2k+2α = h'),D('4α+2k = h'),D('4α = h-2k'),D('α = (h-2k)/4 = h/4-k/2')),
 S('Then calculate β',D('β = k+h/4-k/2'),D('β = h/4+k/2')),
 S('Verify the first coordinate',D('2α+2β = 2(h/4-k/2)+2(h/4+k/2)'),D('2α+2β = h/2-k+h/2+k = h')),
 S('Verify the second coordinate',D('-α+β = -(h/4-k/2)+(h/4+k/2)'),D('-α+β = -h/4+k/2+h/4+k/2 = k')),
 A(D('α = h/4-k/2'),D('β = h/4+k/2'),P('The fixed denominators 4 and 2 are nonzero. The weights exist for every real h,k, so u and v span ℝ².'))],
'1.7.9':[
 S('Part (a): express v₃ using v₁ and v₂',D('v_3 = αv_1+βv_2'),D('α-3β = 2'),D('-3α+10β = -7')),
 S('Solve the first two coordinate equations',D('α = 2+3β'),D('-3(2+3β)+10β = -7'),D('-6-9β+10β = -7'),D('β = -1'),D('α = 2+3(-1) = -1')),
 S('Compute the third coordinate these weights force',D('h = 2α-6β'),D('h = 2(-1)-6(-1)'),D('h = -2+6 = 4')),
 S('Part (b): check the first pair before using the span test',P('A zero combination of v₁,v₂ gives these same first two equations with zero right sides:'),D('α-3β = 0'),D('-3α+10β = 0'),D('α = 3β'),D('-9β+10β = β = 0'),D('α = 0'),P('Only zero weights work, so the pair is independent. Therefore adding v₃ creates dependence exactly when v₃ is in their span.')),
 S('Show an actual nonzero relation at h = 4',D('v_3 = -v_1-v_2'),D('v_1+v_2+v_3 = 0'),P('The weights (1,1,1) are not all zero. This is a nontrivial relation.')),
 A(P('(a) Membership holds exactly for h = 4. (b) The triple is dependent exactly for h = 4. The conclusion in part (b) uses the independence of the original pair.'))],
'1.7.10':[
 S('Inspect the given pair first',D('v_2 = -2v_1'),D('2v_1+v_2 = 0'),P('The two vectors are already dependent. Every combination of them is a multiple of v₁, so they span a line.')),
 S('Part (a): test whether v₃ is on that line',P('Its first two coordinates are 2 and −10. Matching the first forces a multiplier of 2, and the second matches that same multiplier.'),D('v_3 = 2v_1'),D('h = 2(-3) = -6'),P('At h = −6 all three coordinates match, so membership holds. Any other h makes the third coordinate fail.')),
 S('Part (b): keep the existing relation',D('2v_1+v_2+0v_3 = 0'),P('The weights 2,1,0 are not all zero. This works for every h because v₃ has weight zero.')),
 A(P('(a) v₃ belongs to Span{v₁,v₂} exactly when h = −6. (b) The triple is dependent for every real h. Adding a vector cannot remove an existing dependence relation.'))],
'1.7.11':[
 S('Start the zero-combination test',D('c_1v_1+c_2v_2+c_3v_3 = 0'),D('c_1+3c_2-c_3 = 0'),D('-c_1-5c_2+5c_3 = 0'),P('Dependence requires weights c₁,c₂,c₃ that are not all zero.')),
 S('Add the first two equations',D('-2c_2+4c_3 = 0'),D('-2c_2 = -4c_3'),D('c_2 = 2c_3'),D('c_1 = -3(2c_3)+c_3 = -5c_3')),
 S('Substitute in the third-coordinate equation',D('4c_1+7c_2+hc_3 = 0'),D('4(-5c_3)+7(2c_3)+hc_3 = 0'),D('(-20+14+h)c_3 = 0'),D('(h-6)c_3 = 0')),
 S('Decide whether nonzero weights can exist',P('If c₃ = 0, the preceding formulas force c₂ = c₁ = 0. A nontrivial relation therefore needs c₃ ≠ 0, which forces h − 6 = 0.'),D('h = 6'),D('c_3 = 1'),D('c_2 = 2'),D('c_1 = -5')),
 S('Verify those weights',D('-5+3(2)-1 = 0'),D('-(-5)-5(2)+5 = 0'),D('4(-5)+7(2)+6 = -20+14+6 = 0')),
 A(P('Dependent exactly for h = 6, with relation −5v₁ + 2v₂ + v₃ = 0. For h ≠ 6 only zero weights work, so the vectors are independent.'))],
'1.7.12':[
 S('Look at the plane containing all three vectors',D('x_1 = 2x_3'),P('Each given vector has first coordinate twice its third, whatever h is. We will exhibit an actual dependence relation, rather than relying only on the picture of three arrows in a plane.')),
 S('Solve the first zero-combination equation',D('2c_1-6c_2+8c_3 = 0'),D('2c_1 = 6c_2-8c_3'),D('c_1 = 3c_2-4c_3')),
 S('Use this in the second-coordinate equation',D('-5c_2+(h+16)c_3 = 0'),P('Choose c₃ = 5 so the factor 5 cancels without dividing by an expression involving h.'),D('-5c_2+5(h+16) = 0'),D('c_2 = h+16')),
 S('Find c₁ and verify the remaining conditions',D('c_1 = 3(h+16)-4(5)'),D('c_1 = 3h+48-20 = 3h+28'),D('2(3h+28)-6(h+16)+8(5) = 0'),D('-5(h+16)+(h+16)(5) = 0'),P('The third-coordinate sum is half the first-coordinate sum, hence is also zero.')),
 A(D('(3h+28)v_1+(h+16)v_2+5v_3 = 0'),P('The weight 5 is nonzero, so this is a nontrivial relation for every real h. The vectors are always dependent.'))],
'1.7.13':[
 S('Observe the repeated coordinate condition',P('For each vector the third coordinate is −3 times the first. It suffices to make the first two coordinate sums zero; the third will then also be zero.')),
 S('Solve the first-coordinate relation',D('c_1-2c_2+3c_3 = 0'),D('c_1 = 2c_2-3c_3')),
 S('Use the second-coordinate relation',D('c_2+(h-15)c_3 = 0'),D('c_3 = 1'),D('c_2 = 15-h'),D('c_1 = 2(15-h)-3'),D('c_1 = 30-2h-3 = 27-2h')),
 S('Verify the coordinate sums',D('(27-2h)-2(15-h)+3 = 27-2h-30+2h+3 = 0'),D('(15-h)+(h-15)(1) = 0'),P('The third sum is −3 times zero. The third weight is 1, so the weights are not all zero.')),
 A(D('(27-2h)v_1+(15-h)v_2+v_3 = 0'),P('A nontrivial relation exists for every real h. Thus the vectors are always dependent.'))],
'1.7.14':[
 S('Write a zero combination coordinate by coordinate',D('c_1-5c_2+c_3 = 0'),D('-c_1+7c_2+c_3 = 0'),P('We are testing whether any nonzero choice of weights gives the zero vector.')),
 S('Add to eliminate c₁',D('2c_2+2c_3 = 0'),D('c_2 = -c_3'),D('c_1 = 5(-c_3)-c_3 = -6c_3')),
 S('Substitute these expressions into coordinate 3',D('3c_1+8c_2+hc_3 = 0'),D('3(-6c_3)+8(-c_3)+hc_3 = 0'),D('(-18-8+h)c_3 = 0'),D('(h-26)c_3 = 0')),
 S('Determine when the weights can be nontrivial',P('If h ≠ 26, c₃ must be zero. Then c₂ and c₁ are also zero. If h = 26, choose c₃ = 1.'),D('(c_1,c_2,c_3) = (-6,-1,1)')),
 S('Check that relation at h = 26',D('-6-5(-1)+1 = -6+5+1 = 0'),D('-(-6)+7(-1)+1 = 6-7+1 = 0'),D('3(-6)+8(-1)+26 = -18-8+26 = 0')),
 A(P('Dependent exactly when h = 26, with −6v₁ − v₂ + v₃ = 0. Independent for every other h.'))]
}
