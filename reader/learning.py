"""Additive, concept-specific teaching layers. Original academic prose is retained.
Supplementary examples are explicit; original source matrix sequences are untouched.
"""
import re,html,json
from mathml import inline,math,matrix
from diagrams import figure
E=html.escape
REPORT={'concept_lessons':[],'proofs':[],'guided_exercises':{},'prose_reflows':0,'practice_cards':0}
def p(t,cls=''):return '<p'+(' class="'+cls+'"' if cls else '')+'>'+inline(t)+'</p>'
def eq(t):return '<div class="math-scroll equation" tabindex="0" aria-label="Example equation">'+math(t,True)+'</div>'
def mini(a,bar=None,cells=(),cols=(),rows=(),label='Supplementary annotated example'):
 a=[[str(v) for v in r] for r in a];s=matrix({'a':a,'bar':bar},duplicate=True);i=0
 def cell(m):
  nonlocal i
  r,c=divmod(i,len(a[0]));i+=1;style=''
  if c in cols:style+='background:#f1edfa;'
  if r in rows:style+='background:#f7edf2;'
  if (r,c) in cells:style+='background:#dceadf;outline:1.4px solid #60806a;font-weight:bold;'
  attr=m[1]
  if style:
   if 'style="' in attr:attr=attr.replace('style="','style="'+style)
   else:attr+=' style="'+style+'"'
  return '<mtd'+attr+'>'
 s=re.sub(r'<mtd([^>]*)>',cell,s)
 return '<figure class="annotated-matrix" aria-label="'+E(label,quote=True)+'">'+s+'<figcaption>'+inline(label)+'</figcaption></figure>'
def flow(*items):return '<ol class="reasoning-flow">'+''.join('<li>'+inline(s)+'</li>' for s in items)+'</ol>'
def table(headers,rows):return '<div class="rule-table" tabindex="0" role="region" aria-label="Comparison table"><table><thead><tr>'+''.join('<th scope="col">'+inline(h)+'</th>' for h in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(('<th scope="row">' if i==0 else '<td>')+inline(c)+('</th>' if i==0 else '</td>') for i,c in enumerate(row))+'</tr>' for row in rows)+'</tbody></table></div>'
def pair(left,right):return '<div class="comparison-panel"><div>'+left+'</div><div>'+right+'</div></div>'
def focus(title,meaning,visual,result=''):
 return '<div class="concept-section"><span class="component-label">SEE THE IDEA</span><h3>'+inline(title)+'</h3>'+p(meaning,'plain-meaning')+visual+(p('**Remember.** '+result,'takeaway') if result else '')+'</div>'
def argument(title,steps):return focus(title,'Follow the logical connections; each arrow needs a reason.',flow(*steps))
def numberline():
 return '<figure class="numberline"><svg viewBox="0 0 520 100" role="img" aria-label="On a number line, moving from -3 five units right ends at 2."><path d="M25 52H495" stroke="#777184"/><path d="M115 28H340l-8 -5m8 5l-8 5" fill="none" stroke="#7055a0" stroke-width="2"/>'+''.join(f'<path d="M{250+45*i} 47v10" stroke="#777184"/><text x="{250+45*i}" y="77" text-anchor="middle" font-size="14" fill="#272537">{i}</text>' for i in range(-5,6))+'<text x="220" y="19" font-size="13" text-anchor="middle" fill="#62478c">add 5: move right</text></svg><figcaption>−3 + 5 = 2. Negative positions and subtraction are different uses of the minus sign.</figcaption></figure>'

def multiplication():
 return pair('<h4>Choose one row</h4>'+mini([[2,3],[1,-5]],rows=(0,),label='Row 1 of A is (2,3).'),'<h4>Choose one column</h4>'+mini([[4,3,6],[1,-2,3]],cols=(0,),label='Column 1 of B is (4,1).'))+eq('c_{11} = (2)(4) + (3)(1) = 11')+flow('Pair corresponding entries','Multiply each pair','Add to get one output entry')

def free_choices(two=False):
 if two:return table(['Choose (s,t)','Compute x₁ = 4 − 2s + t','Solution x'],[['(0,0)','4','(4,0,0)'],['(1,0)','2','(2,1,0)'],['(0,1)','5','(5,0,1)']])+p('The two choices are independent. Requiring s = t would wrongly discard solutions.')
 return table(['Choose s = x₃','Compute x₁ = 3 + 2s, x₂ = 4 − s','Solution x'],[['0','3, 4','(3,4,0)'],['1','5, 3','(5,3,1)'],['−1','1, 5','(1,5,−1)']])+eq('(3 + 2s) - 2s = 3')+eq('(4 - s) + s = 4')

def pivot_lesson(body):
 # Five separate concepts, followed by the unabridged deeper proof.
 paras=re.findall(r'<p(?: [^>]*)?>.*?</p>',body,re.S)
 assert len(paras)>=7
 original1=paras[0];raw='The leading entry of a nonzero row is its first nonzero entry when read from left to right. A matrix is in row echelon form (REF) when all zero rows are at the bottom, each leading entry is strictly to the right of the leading entry in the row above, and every entry below a leading entry is zero. Leading entries need not be 1 in REF.'
 sentences=re.split(r'(?<=\.) ',raw);assert len(sentences)==3
 leading=focus('1 · What is a leading entry?','Read a row from left to right. Skip the zeros. The first number that remains is its leading entry.',pair(mini([[0,0,-3,6]],cells=((0,2),),label='First nonzero entry: −3.'),mini([[0,4,1,2]],cells=((0,1),),label='First nonzero entry: 4.')))+p(sentences[0])
 staircase=focus('2 · REF: build a staircase','Look down the rows: each next leading entry takes a step to the right.',mini([[2,4,6],[0,3,9],[0,0,0]],cells=((0,0),(1,1)),label='Leading entries are highlighted. The zero row is at the bottom.')+table(['REF check','What to look for'],[['Zero rows last','The completely zero row is below the nonzero rows.'],['Move right','Leading entries are in columns 1, then 2.'],['Clear below','All entries below each leading entry are zero.']]))+p(sentences[1]+' '+sentences[2])
 reduced=focus('3 · RREF: finish cleaning each pivot column','REF gives the shape. RREF also normalizes each leading entry and clears above it.',pair('<h4>REF, but not RREF</h4>'+mini([[2,4,6],[0,3,9],[0,0,0]],cells=((0,0),(1,1)),label='Leading entries 2 and 3 are not normalized.'),'<h4>RREF of the same matrix</h4>'+mini([[1,0,-3],[0,1,3],[0,0,0]],cells=((0,0),(1,1)),label='Each pivot is 1 and is alone in its column.')))+paras[1]
 pivots=focus('4 · A pivot column belongs to the original matrix','Reduce to identify column numbers; then go back to those columns in the original matrix.',pair('<h4>Original A</h4>'+mini([[0,2,4],[1,1,3]],cols=(0,1),label='Original columns 1 and 2 are the pivot columns.'),'<h4>RREF(A)</h4>'+mini([[1,0,1],[0,1,2]],cells=((0,0),(1,1)),label='Leading 1s identify pivot-column indices 1 and 2.')),'The original entry at position (1,1) is 0. A pivot position is a location, not a promise about that original number.')+paras[2]
 comparison='<div class="concept-section"><h3>5 · REF versus RREF, at a glance</h3>'+table(['Condition','REF','RREF'],[['Leading entries make a staircase','Required','Required'],['Zero rows at the bottom','Required','Required'],['Zeros below each leading entry','Required','Required'],['Each leading entry equals 1','Not required','Required'],['Zeros above every leading entry','Not required','Required'],['Unique in its row-equivalence class','No','Yes']])+'</div>'
 uniqueness=focus('6 · Why can there be only one RREF?','Different legal routes can simplify the same constraints. A fully reduced matrix records those constraints in one fixed form.',pair(mini([[2,4],[0,0]],label='One possible REF.'),mini([[1,2],[0,0]],label='The unique RREF: x₁ + 2x₂ = 0 if read homogeneously.')))+paras[3]
 h=body.find('<h3');assert h>=0
 proof=body[h:]
 proof='<details class="proof-detail"><summary>Deeper Mathematical Explanation · Explore the Full Proof</summary>'+argument('The proof in three connections',['Row operations preserve row span','The row span determines pivot-column indices','Matching pivot coordinates force corresponding rows to agree'])+proof+'</details>'
 REPORT['proofs'].append('RREF uniqueness');REPORT['prose_reflows']+=1
 return leading+staircase+reduced+pivots+comparison+uniqueness+proof

G={}
def guide(key,title,meaning,visual,result=''):G[key]=focus(title,meaning,visual,result)
# Foundations: each visual teaches the named arithmetic or language idea.
guide('0.1','A sign can name a position or an operation','Start with positions, then read what the operation asks you to do.',numberline(),'Subtracting a negative means adding its opposite: 4 − (−5) = 9.')
guide('0.2','Keep the pieces the same size','Before adding fractions, rename them using the same denominator.',flow('1/2 = 3/6','1/3 = 2/6','3/6 + 2/6 = 5/6')+eq('(-3/4) + (5/6) = (-9/12) + (10/12) = 1/12'),'Add numerators after denominators match. Keep exact fractions during elimination.')
guide('0.3','An equation is a balance','Apply the same reversible operation to both sides.',flow('3x − 2 = 10','Add 2: 3x = 12','Divide by 3: x = 4','Check: 3(4) − 2 = 10'),'A subscript labels an entry; a power multiplies a quantity by itself.')
guide('0.4','A system means “all at once”','One pair must make every original equation true.',table(['Candidate','x + y = 5','x − y = 1'],[['(3,2)','3 + 2 = 5 ✓','3 − 2 = 1 ✓'],['(1,4)','1 + 4 = 5 ✓','1 − 4 = −3 ✗']]),'Checking only one equation is insufficient.')
guide('0.5','A solution is a shared point','The graphs visualize the same “all equations at once” requirement.',figure('systems'))
guide('0.6','Read the logical direction','“If” and “if and only if” ask for different arguments.',table(['Notation','Meaning','Proof needed'],[['P ⇒ Q','P guarantees Q','One direction'],['P ⇔ Q','Each guarantees the other','Both directions'],['∅ versus {0}','No members versus one zero member','Different sets']]))
# Systems and notation.
guide('1.1','Linear means no interaction between unknowns','Unknowns occur only to the first power, multiplied by fixed coefficients.',table(['Linear','Not linear in x,y','Reason'],[['2x − 3y = 7','xy = 7','Product of unknowns'],['x + y = 1','x² + y = 1','An unknown is squared'],['0x + y = 2','1/x + y = 2','An unknown is in a denominator']]))
guide('1.2','A matrix is a tidy record of equations','Each row records one equation. Coefficient columns keep the same variable order.',eq('x_1 + 2x_2 = 7')+eq('3x_1 - x_2 = 7')+mini([[1,2,7],[3,-1,7]],3,cols=(2,),label='2 rows = 2 equations; 2 coefficient columns = 2 unknowns; last column = constants.'))
guide('1.3','A legal row operation has an undo','Changing equations preserves their solutions when the change can be reversed.',table(['Operation','Undo'],[['R₂ ← R₂ − 3R₁','R₂ ← R₂ + 3R₁'],['R₁ ← 2R₁','R₁ ← (1/2)R₁'],['R₁ ↔ R₂','Swap again'],['R₁ ← 0R₁','No undo: information was erased']]))
guide('1.4','Eliminate one target at a time','Follow the verified matrix states below. The highlighted pivot supplies the row used to change another row.',flow('Locate a nonzero pivot','Clear a target entry','Read the updated constraints','Work back to the unknowns'),'Use Next Step for focus, or Show All Steps for the full calculation.')
guide('1.5','An impossible row ends the search','No choice of unknowns can make zero equal a nonzero number.',pair(mini([[0,0,0,1]],3,label='0 = 1: impossible; no solution.'),mini([[0,0,0,0]],3,label='0 = 0: always true; adds no restriction.')))
guide('1.6','Decide before doing extra arithmetic','The wording tells you whether you need a decision, one input, or the full set.',table(['Asked for','Stop when you have'],[['Consistency','A contradiction or a valid existence argument'],['Unique solution','Consistency and no free variables'],['Solve completely','Every unknown described, including all parameters']]))
# Reduction, all subtopics.
guide('2.2','Two passes, two purposes','The forward phase creates the staircase; the backward phase cleans above the pivots.',pair('<h4>Forward → REF</h4>'+mini([[2,4,6],[0,3,9],[0,0,0]],cells=((0,0),(1,1)),label='Zeros below; leading entries move right.'),'<h4>Backward → RREF</h4>'+mini([[1,0,-3],[0,1,3],[0,0,0]],cells=((0,0),(1,1)),label='Normalize and clear above.')))
guide('2.3','Find indices, then return to A','This is a rectangular-matrix question, not an augmented-system question.',flow('All 5 columns are ordinary matrix columns','Use the original verified reduction','Report original pivot-column indices'),'A final column is not automatically a right-hand side.')
guide('2.4','A skipped column tells you something','A column without an available pivot supplies no new leading position.',flow('Inspect the next possible column','If every available entry is 0, skip it','Keep the full column in every matrix'),'The original nine operations below remain available in order.')
guide('2.5','Choose the free input; calculate the rest','Here x₃ = s is free. The two pivot equations determine x₁ and x₂.',free_choices(),'Different parameter values produce different valid solutions.')
guide('2.6','Two free variables need two separate choices','The four-unknown example below has free x₂ and x₄. Choose them independently.',table(['Free choices','Basic variables'],[['x₂ = s, x₄ = t','x₁ = 5 − 2s − t'],['s,t ∈ ℝ independently','x₃ = 1 + 2t']]),'Using the same parameter for both free variables would impose an extra equation.')
guide('2.7','Existence first. Uniqueness second.','Use two separate decisions, in that order.',flow('Is there an echelon row [0 … 0 | c], c ≠ 0?','Yes: no solution. No: the system is consistent.','If consistent, are any coefficient variables free?','None: unique. At least one: infinitely many.'))
# Vectors, span, applications.
guide('3.1','A vector keeps ordered quantities together','Its entries are coordinates in a fixed order; its dimension counts those entries.',pair(mini([[2],[-1]],rows=(0,),label='A 2-entry column: first horizontal, then vertical.'),mini([[-1],[2]],rows=(0,),label='Reversing the entries gives a different vector.')))
guide('3.2','Add matching coordinates','An arrow picture and coordinate arithmetic describe the same operation.',figure('vectors'))
guide('3.3','Weights are the unknowns','A linear combination asks how much of each direction is needed.',eq('2(1,0) + 3(0,1) = (2,3)')+flow('Put the given vectors into columns','Use the target as the appended column','Solve for the weights'),'A solution to [A | b] gives the combination coefficients.')
guide('3.4','A span is everything the generators can reach','One example is a member; the span is the entire collection of weighted sums.',figure('span'),'Two vectors span a genuine plane only when they are independent.')
guide('3.5','Attach units before solving','Each coordinate records a different resource; each weight records operating time.',table(['Quantity','Mine 1 per day','Mine 2 per day'],[['Copper (metric tons)','20','30'],['Silver (kg)','550','500']])+eq('x_1(20,550) + x_2(30,500) = (150,2825)'),'The weights are days, not tons or kilograms.')
# Matrix equation.
guide('4.1','Ax is a weighted sum of columns','Each input entry weights the column in the same position.',pair(mini([[2,-1],[1,3]],cols=(0,),label='a₁ = (2,1), a₂ = (−1,3).'),eq('A(3,2) = 3(2,1) + 2(-1,3) = (4,9)')))
guide('4.2','Two views give the same output','Compute by columns or by row–column products; the coordinates must agree.',multiplication())
guide('4.3','Same problem, three languages','The unknowns and solution set stay the same when the notation changes.',flow('System: one equation per output entry','Vector equation: weighted columns equal b','Matrix equation: Ax = b'))
guide('4.4','One reachable target is not every target','Distinguish solving one system from proving that the columns fill the codomain.',pair(mini([[1,0],[0,0]],label='This A reaches (1,0), but never (0,1).'),table(['Question','Test'],[['This b?','Reduce [A | b]'],['Every b ∈ ℝᵐ?','Pivot in every row of A']])),'The row-pivot theorem applies to the coefficient matrix A.')
guide('4.5','Identity leaves every coordinate alone','Each identity column selects exactly one input coordinate.',mini([[1,0,0],[0,1,0],[0,0,1]],cells=((0,0),(1,1),(2,2)),label='I₃x = x for every three-entry input.')+eq('A(u + v) = Au + Av'))
# Homogeneous and parameter geometry.
guide('5.1','Zero is always a starting solution','With right-hand side zero, the all-zero input always works. The real question is whether anything else works.',eq('A0 = 0')+pair(mini([[1,0],[0,1]],label='Ax = 0 forces x = 0.'),mini([[1,2],[0,0]],label='x = t(−2,1) also works; t ≠ 0 is nontrivial.')))
guide('5.2','Read directions from free variables','Homogeneous solution vectors describe motions that produce no output.',flow('Append zeros','Reduce','Assign independent free parameters','Assemble the direction vectors'),'Check each direction v by Av = 0.')
guide('5.3','A particular solution chooses a new starting point','Add a homogeneous motion to p without changing the output b.',figure('translation')+eq('A(p + tv) = Ap + tAv = b + 0 = b'))
guide('5.4','Why the formula captures every solution','Start with one solution p. The difference between any other solution and p must produce zero.',pair(eq('(2-t) + t = 2'),flow('p = (2,0)','Homogeneous direction v = (−1,1)','All solutions: p + tv = (2−t,t)')))
guide('5.5','Count independent choices, after checking consistency','The solution set can be empty, or a translated set of homogeneous motions.',table(['Consistent?','Free parameters','Shape'],[['No','Irrelevant','Empty'],['Yes','0','Point'],['Yes','1','Line'],['Yes','2','Plane'],['Yes','k','Affine set of dimension k']]))
# Independence.
guide('6.1','A redundant direction adds no new reach','Dependence means a nonzero choice of weights can cancel to zero.',figure('independence')+eq('2(1,2) - (2,4) = (0,0)'),'The all-zero choice of weights proves nothing about dependence.')
guide('6.2','One relation is enough','A verified nontrivial zero combination already proves dependence.',eq('2v_1 - v_2 + v_3 = 0')+eq('v_2 = 2v_1 + v_3'),'The second vector can be built from the others.')
guide('6.3','Dependence means at least one redundant vector','Choose a nonzero coefficient in a zero combination and solve for its vector.',flow('Σ c_jv_j = 0 with some c_j ≠ 0','Move the other terms to the right','Divide by that nonzero c_j','One vector is a combination of the others'),'“At least one” does not mean “every one”.')
guide('6.4','Fast tests have one-way limits','Use the conditions exactly as stated.',table(['Situation','Conclusion'],[['Zero vector is included','Dependent'],['More vectors than entries in each','Dependent'],['Two nonzero vectors are not scalar multiples','Independent pair'],['No zero vector is included','Not enough information'],['Fewer vectors than entries','Not enough information']]))
guide('6.5','Independence forces every weight to zero','Use the columns as given; solve the homogeneous equation for their weights.',mini([[1,0,0,0],[0,1,0,0],[0,0,1,0]],3,cells=((0,0),(1,1),(2,2)),label='If the reduced coefficient block is I, all three weights are 0.'))
# Transformations.
guide('7.1','An image goes forward; a preimage solves backward','T(x) = Ax takes an input to an output. Finding an input for b means solving Ax = b.',flow('Input x in the domain','Apply A','Image Ax in the codomain')+table(['Task','Method'],[['Find T(x)','Multiply'],['Find x with T(x) = b','Solve [A | b]'],['Is b in the range?','Test consistency']]))
guide('7.2','All output coordinates must match','An input that matches only some coordinates is not a preimage.',flow('Record A and the requested b','Reduce the full augmented matrix','A contradiction means this output is unreachable'))
guide('7.3','Linearity preserves weighted combinations','A linear map can move through addition and scalar multiplication.',eq('T(cu + dv) = cT(u) + dT(v)')+table(['Rule','Linear?','Reason'],[['T(x) = 2x','Yes','Preserves every linear combination'],['T(x) = x + (1,0)','No','T(0) ≠ 0'],['T(x) = x² in ℝ','No','T(2·1) ≠ 2T(1)']]))
guide('7.4','See what changes in a shear','Horizontal displacement depends on height; the second coordinate stays the same.',figure('shear'))
guide('7.5','Use known images as building blocks','If the input is already expressed as a combination, apply the same weights to the known images.',eq('T(3u + 2v) = 3T(u) + 2T(v)'),'This shortcut requires the assumption that T is linear.')
guide('8.1','Standard basis vectors turn on one input at a time','Because e_j has a single 1, multiplying by it selects column j.',pair(mini([[1],[0]],label='e₁ selects the first column.'),mini([[0],[1]],label='e₂ selects the second column.'))+eq('A = [T(e_1),T(e_2)]'))
guide('8.2','Read coefficients by output row','Each output coordinate becomes one row of the standard matrix.',eq('T(x_1,x_2) = (x_1 - 3x_2, -2x_1 + x_2, x_1)')+mini([[1,-3],[-2,1],[1,0]],label='3 outputs → 3 rows; 2 inputs → 2 columns.'))
guide('8.3','A familiar picture has a precise rule','A reflection changes a sign; a projection deletes a coordinate.',pair('<h4>Horizontal reflection</h4>'+mini([[1,0],[0,-1]],label='(a,b) ↦ (a,−b).'),'<h4>Horizontal projection</h4>'+mini([[1,0],[0,0]],label='(a,b) ↦ (a,0).')))
guide('8.4','The rightmost matrix acts first','Keep the action order visible before multiplying.',flow('Input x','First S: A_S x','Then T: A_T(A_S x)','Combined matrix A_T A_S'))
guide('8.5','Onto asks whether every output is reachable','There must be a pivot in every output row of the coefficient matrix.',mini([[1,0,2],[0,1,-1]],cols=(0,1),label='2 pivots in 2 rows: onto ℝ², even with a free input variable.'))
guide('8.6','One-to-one asks whether inputs collide','If a nonzero input produces zero, it collides with the zero input.',flow('Au = Av','A(u − v) = 0','Only zero solves Az = 0?','Then u − v = 0, so u = v'))
guide('8.7','Existence and uniqueness are different axes','Square and invertible gives both; rectangular maps can have just one.',table(['Map','Onto?','One-to-one?'],[['(x,y) ↦ (x,y)','Yes, into ℝ²','Yes'],['(x,y) ↦ x','Yes, into ℝ','No'],['x ↦ (x,0)','No, into ℝ²','Yes'],['(x,y) ↦ (x,0)','No, into ℝ²','No']]))
# Matrix algebra.
guide('9.1','Rows first, columns second','A matrix entry aᵢⱼ is in row i and column j. Entrywise operations require the same shape.',mini([[1,2,3],[4,5,6]],cells=((1,2),),label='A 2 × 3 matrix. Highlighted entry a₂₃ = 6.')+eq('2[1,2;3,4] + [0,1;1,0] = [2,5;7,8]'))
guide('9.2','One row and one column make one entry','Matrix multiplication composes weighted sums; it is not entrywise multiplication.',multiplication())
guide('9.3','Place each computed entry in its own location','The source example calculates a 2 × 3 output, six entries in all.',multiplication(),'Compute c₁₁ first, then use the same rule for each remaining row–column pair.')
guide('9.4','Regrouping is different from reordering','Associativity moves parentheses. It does not move factors past each other.',pair(eq('(AB)C = A(BC)'),eq('AB = BA')+p('The second equation is generally false.')))
guide('9.5','A matrix may erase information','A zero product does not force a zero factor.',pair(mini([[1,0],[0,0]],label='A is nonzero.'),mini([[0,0],[0,1]],label='B is nonzero.'))+eq('AB = [0,0;0,0]'),'An invertible factor is needed for cancellation.')
guide('9.6','A power repeats the same action','For a square A, A²x applies A twice to x.',flow('x','Ax','A(Ax) = A²x'),'A⁰ = I. Negative powers require an inverse.')
guide('9.7','Transpose swaps the two indices','Turn each row into the corresponding column.',pair(mini([[1,2,3],[4,5,6]],rows=(0,),label='A: 2 × 3.'),mini([[1,4],[2,5],[3,6]],cols=(0,),label='Aᵀ: 3 × 2.'))+eq('(AB)^T = B^T A^T'))
# Inverses.
guide('10.1','Undo the change in the opposite direction','A shear changes the first coordinate by adding the second; its inverse subtracts it.',flow('(x₁,x₂)','A: (x₁+x₂,x₂)','A⁻¹: ((x₁+x₂)−x₂,x₂)','Original (x₁,x₂) restored')+figure('inverse'))
guide('10.2','Check the denominator before dividing','The determinant ad − bc tells whether this two-dimensional map can be undone.',eq('A^(-1) = (1/(ad-bc))[d,-b;-c,a]')+table(['Condition','Meaning'],[['ad − bc ≠ 0','The formula is defined; A is invertible.'],['ad − bc = 0','No two-sided inverse exists.']]))
guide('10.3','Verify with multiplication, not resemblance','For A = [1,2;4,7], the candidate inverse is [−7,2;4,−1].',eq('[1,2;4,7][-7,2;4,-1] = [1,0;0,1]'),'Check the reverse product too. Entrywise reciprocals are not an inverse.')
guide('10.4','Multiply by the undo operation','When A is invertible, left-multiplication isolates the input.',flow('Ax = b','A⁻¹Ax = A⁻¹b','Ix = A⁻¹b','x = A⁻¹b'))
guide('10.5','An elementary matrix performs one row operation','Apply the row operation to I to get E; left-multiplication EA performs it on A.',mini([[1,0],[-3,1]],label='E comes from R₂ ← R₂ − 3R₁ on I₂.')+flow('Row 1 of EA = row 1 of A','Row 2 of EA = row 2 of A − 3 row 1 of A'))
guide('10.6','Carry the identity through the same operations','The row operations that turn A into I simultaneously turn I into A⁻¹.',flow('[A | I]','Apply every operation to both blocks','[I | A⁻¹]'),'The right block is the answer only when the left block is exactly I.')
guide('10.7','Keep the two printed matrices separate','The source prints one entry inconsistently. The two original verified calculations below deliberately invert different matrices.',table(['Lecture source','First row'],[['Initial A on physical page 98','(0,1,0)'],['Augmented calculation and verification','(0,1,2)']]),'Read the qualification before interpreting either inverse.')
guide('10.8','One inverse column needs only one target','Column j of A⁻¹ is the input that maps to e_j.',eq('A x = e_j')+flow('Append only e_j','Reduce [A | e_j]','Read x as inverse column j'),'Use multiple target columns together when several columns are requested.')
guide('10.9','Undo the last action first','If AB applies B and then A, its inverse must undo A and then B.',flow('x → Bx → ABx','Undo A with A⁻¹','Undo B with B⁻¹')+eq('(AB)^(-1) = B^(-1)A^(-1)'))
# Proof skills and reference.
guide('11.1','Translate the request into a test','Start by identifying the mathematical object and the actual goal.',table(['Question asks','Translate into'],[['Is b in the span?','Do weights exist: Ax = b?'],['Independent?','Are zero weights the only solution of Ac = 0?'],['Onto?','Is every coefficient row a pivot row?'],['Invertible?','Can a square A reduce to I?']]))
guide('11.2','Build an argument, one justified link at a time','Each theorem has assumptions; check them before using its conclusion.',flow('Assumptions','Definition of the target','A justified deduction','Conclusion in the question’s language'))
guide('11.3','A counterexample must meet the assumptions','Use one example to disprove a universal claim, not to establish it.',table(['Claim','Evidence required'],[['True for all A','A general proof covering all allowed A'],['False for some A','One allowed A for which it fails'],['If and only if','Both logical directions']]))
guide('13.1','Use the words as labels for visible features','Choose a term, then connect it to the matrices, systems, or maps where it is used.',flow('Pivot: a leading location','Free variable: a coefficient column without a pivot','Span: every obtainable weighted sum','Inverse: an operation that undoes A'))
guide('13.2','Keep each formula attached to its condition','Read the assumptions before choosing a rule.',table(['Formula family','Check first'],[['Matrix product','Inner dimensions match'],['Unique system solution','Consistency, then no free variables'],['Inverse','A is square and invertible'],['Plane span','Two generators are independent']]))
guide('13.3','The section identifies the theorem numbering','Chapter 2 restarts its theorem numbers. Use the course section and theorem number together.',flow('Identify the topic','Read the exact theorem and assumptions','Check the physical source-page reference'))
guide('13.4','Name the distinction that prevents the mistake','Many errors swap two similar-sounding conditions.',table(['Keep separate','Why'],[['Rows / columns','Rows ask existence; columns ask uniqueness'],['Zero row / contradictory row','0 = 0 is harmless; 0 = 1 is impossible'],['AB / BA','Actions occur in a different order'],['A span / one vector in it','A set is not one of its members']]))

def reflow_argument(raw):
 sentences=re.split(r'(?<=[.!?])\s+(?=[A-Z])',raw)
 if len(sentences)<3:return p(raw)
 # Preserve every sentence in order; group explanations with their local claim.
 pieces=[];current=[]
 for sentence in sentences:
  if current and (len(' '.join(current))>180 or re.match(r'(Conversely|For the reverse|Part \(|Thus|Hence|Therefore|Substitut)',sentence)):
   pieces.append(' '.join(current));current=[]
  current.append(sentence)
 if current:pieces.append(' '.join(current))
 REPORT['prose_reflows']+=1
 return '<div class="argument-chain" data-source-prose="'+E(raw,quote=True)+'"><ol>'+''.join('<li data-prose-piece="'+E(s,quote=True)+'">'+inline(s)+'</li>' for s in pieces)+'</ol></div>'

def practice_label(markup):
 annotation=re.search(r'<annotation encoding="text/plain">([A-Z])_(\d+)</annotation>',markup)
 if annotation:
  label=annotation[1]+annotation[2]
  return label if markup in (inline(label),inline(label+'.')) else None
 label=re.sub(r'<[^>]*>','',markup).rstrip('.')
 return label if re.fullmatch(r'[A-Z]\d+',label) else None

def answer_labels(markup):
 label=practice_label(markup)
 if label:return [label]
 if '<' not in markup and re.match(r'^[A-Z]\d+(?: and [A-Z]\d+)?[.,]',markup):return re.findall(r'[A-Z]\d+',markup)
 return []

def answer_map(chapters,duplicate=True):
 c=next(c for c in chapters if c['id']=='practice-answers');h=c['html'];found=[m for m in re.finditer(r'<p[^>]*><strong>(.*?)</strong>',h,re.S) if answer_labels(m[1])];out={}
 for i,m in enumerate(found):
  end=found[i+1].start() if i+1<len(found) else len(h)
  part=h[m.start():end]
  # Stop at a subsection boundary so copies never contain a closing parent.
  part=part.split('</section>\n')[0]
  part=re.split(r'</section>(?=<section class="lesson")',part)[0]
  # The final closing tag of the lesson is not part of a question's solution.
  if part.endswith('</section>'):part=part[:-10]
  part=re.sub(r'<section class="lesson".*', '',part,flags=re.S)
  if duplicate:part=part.replace('data-duplicate="false"','data-duplicate="true"')
  for label in answer_labels(m[1]):out[label]=part
 return out

def practice_extra(id):
 if id=='R1':return mini([[1,2,0],[0,0,1],[0,0,0]],cells=((0,0),(1,2)),label='Inspect columns 1 and 3; column 2 is nonpivot.')+table(['REF checklist','RREF checklist'],[['Nonzero rows before zero rows','Each leading entry is 1'],['Leading entries move right','Each pivot column is otherwise zero'],['Zeros below each leading entry','The 2 in a nonpivot column is allowed']])
 if id=='R2':return p('Choose x₂ = s and x₃ = t independently. The augmented matrix and exact row operation appear in the answer.')+free_choices(True)
 if id=='R3':return pair('<h4>Existence: every output row</h4>'+flow('3 equations → 3 rows','3 pivots → a pivot in every row','Every b ∈ ℝ³ is attainable'),'<h4>Uniqueness: every input column</h4>'+flow('5 unknowns → 5 columns','5 − 3 = 2 free variables','No consistent system has a unique solution'))
 return ''

def refine_chapters(chapters,answers=None):
 answers=answer_map(chapters) if answers is None else answers
 for c in chapters:
  original=c['html'];matches=list(re.finditer(r'<section class="lesson" id="([^"]+)"><h2>(.*?)</h2>',original,re.S))
  if not matches:continue
  out=[original[:matches[0].start()]]
  for i,m in enumerate(matches):
   end=matches[i+1].start() if i+1<len(matches) else len(original)
   body=original[m.end():end];assert body.endswith('</section>'),(c['id'],m[1]);body=body[:-10]
   prefix=re.match(r'(\d+\.\d+)',re.sub(r'<[^>]*>','',m[2]));key=prefix[1] if prefix else ''
   if key=='2.1':body=pivot_lesson(body)
   else:
    guide_html=G.get(key,'')
    if guide_html:
     body=guide_html+'<div class="precise-explanation"><span class="component-label">THE COMPLETE EXPLANATION</span>'+body+'</div>'
     REPORT['concept_lessons'].append(key)
    # Keep exact formal statements recognizable; do not rewrite their claims.
    body=body.replace('class="callout concept"><strong>Theorem','class="theorem-card"><strong>Theorem')
    # Selected complete proofs get an approachable map, then a clearly labelled disclosure.
    proofstarts={'5.4':'To prove the forward direction','6.3':'If ','7.3':'Every matrix transformation is linear because','8.6':'Here is the proof linking','11.2':'First state the assumptions'}
    if key in proofstarts:
     paragraphs=list(re.finditer(r'<p[^>]*>.*?</p>',body,re.S))
     for pm in paragraphs:
      clean=re.sub(r'<[^>]*>','',pm[0])
      if clean.startswith(proofstarts[key]):
       extra=flow('State the assumptions','Use the definition','Justify each implication','Reach the claimed conclusion')
       repl='<details class="proof-detail"><summary>Explore the Full Proof · Deeper Mathematical Explanation</summary>'+extra+pm[0]+'</details>'
       body=body.replace(pm[0],repl,1);REPORT['proofs'].append(key);break
   if key.endswith(('.7','.8','.6','.10','.4')) or 'Practice' in m[2] or 'practice' in m[2]:
    # Match actual source practice IDs, not every bold label.
    def practice(pm):
     id=practice_label(pm[1])
     if id not in answers:return pm[0]
     REPORT['practice_cards']+=1
     return '<section class="practice-question" data-practice-id="'+id+'"><span class="component-label">TRY IT YOURSELF · '+id+'</span>'+pm[0]+'<details class="worked-solution"><summary>Show Detailed Solution · '+id+'</summary><div class="content">'+practice_extra(id)+answers[id]+'</div></details></section>'
    if c['id']!='practice-answers':body=re.sub(r'<p[^>]*><strong>(.*?)</strong>.*?</p>',practice,body,flags=re.S)
   # Add a short result label to existing concluding prose, without changing it.
   body=re.sub(r'<p>(Every unknown is basic.*?|A row now states.*?|Every coefficient column has a pivot.*?)</p>',r'<p class="final-answer">\1</p>',body,flags=re.S)
   out.append('<section class="lesson concept-section-root" id="'+m[1]+'"><h2>'+m[2]+'</h2>'+body+'</section>')
  c['html']=''.join(out)
 REPORT['concept_lessons'].append('2.1 (six distinct micro-lessons)')
 return chapters

def classify(q):
 t=q['title'].lower();s=q['source']
 if q['id'] in ['1.4.1','1.4.2','1.4.3','1.4.4']:return 'product'
 if q['id'] in ['2.2.26','2.2.29','2.2.30','2.2.33','2.2.34','2.2.37','2.2.38']:return 'proof'
 if t.startswith('true/false'):return 'true-false'
 if 'find only' in t and 'inverse column' in t:return 'inverse-column'
 if q['id'] in ['2.1.1','2.1.2','2.1.3','2.1.4']:return 'matrix-expressions'
 if any(x in t for x in ['prove','show ','why ','explain','cancellation','cancel ','solve ab','solve a =','unique matrix solution']):return 'proof'
 if 'inverse' in t and 'formula' in t and t.startswith('find'):return 'inverse-formula'
 if t.startswith('verify the inverse'):return 'inverse-check'
 if 'inverse' in t and ('to solve' in t or 'systems by' in t):return 'inverse-solve'
 if 'inverse' in t or 'invers' in t:
  return 'inverse' if t.startswith(('find','inverse of','inverses of')) else 'proof'
 if any(x in t for x in ['independen','dependen','relation among']):return 'independence'
 if any(x in t for x in ['span','combination','spanned','column span']):return 'span'
 if 'transpose' in t:return 'transpose'
 if re.search(r'^@eq c_\{',s,re.M) or any(x in t for x in ['product','multiply','multiplication','compute ad']):return 'product'
 if any(x in t for x in ['transformat','image','geometric','reflection','rotation','shear','implementing','matrix from']):return 'transformation'
 if 'The starting matrix is:' in s:return 'systems'
 return 'structure'

