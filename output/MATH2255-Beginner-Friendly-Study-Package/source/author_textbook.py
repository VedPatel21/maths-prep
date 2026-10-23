from build_math2255 import *
B=[]
def put(s):B.append(s.strip()+'\n\n')
def solve(a,why='',hom=False):put(system_solution(a,why,hom))
def ind(a):put(independence(a))
def inv(a):put(inverse_solution(a))
def prod(a,b):put(product_solution(a,b))
put('''# MATH 2255 - Linear Algebra Made Understandable

A Complete Beginner-to-University-Level Self-Study Textbook Based on the Supplied Lakehead University Course Material

**Prepared for independent learning from first principles.**

This book explains the ten supplied sections: 1.1-1.5, 1.7-1.9, and 2.1-2.2. Chapter 0 supplies the prerequisite arithmetic, algebra, notation, and reasoning. Section 1.6 was not supplied and has not been inserted. Original teaching examples and prerequisite explanations are additions by the author; source examples carry PDF page references.

The companion Exercise Workbook contains the supplied exercise pages and numbered worked solutions. Answers developed here are independently derived teaching solutions. Where a matching selected solution appears in the supplied course PDF, the workbook records that cross-check. Neither document claims to be an instructor-issued answer key.

# Contents

@toc

# How to use this book independently

You may open any chapter. If a symbol or an algebraic step is unfamiliar, use Chapter 0 or the glossary. The course section appears in each chapter title so that you can move between this book and your slides without guessing where a topic belongs. There is no timetable or required study duration.

Read a worked example as a chain of decisions. Before looking at a calculation, identify what the question asks: a solution, an existence decision, a span test, an independence test, an image, a standard matrix, or an inverse. These requests may use the same row-reduction calculation but require different concluding sentences.

Every significant row operation in the worked reductions is followed by the complete updated matrix. Read its rows as equations. The explanations name the unknowns, identify free choices, and verify the answer in the original data. A calculation is useful only when you can explain what it establishes.

End-of-chapter questions have worked answers in the practice-solutions chapter. The companion workbook supplies course-based practice; the questions in this textbook are original foundation and transfer practice unless explicitly labeled as a course example. You can cover an answer with a sheet of paper, attempt the question, then compare your reasoning. This is optional self-study, not a progress system.

**Conventions.** All computations here use real numbers and column vectors unless stated otherwise. A vector written (a,b,c) in a sentence represents the column with those entries. A superscript T means transpose. A superscript -1 on a matrix means inverse, not entrywise reciprocal. A vertical divider in a matrix separates coefficients from appended right-hand sides. It is not an extra column. All parameters are real unless a problem says otherwise.

**The two questions to keep separate.** Existence asks whether a solution is possible. Uniqueness asks whether two different solutions are possible. Decide existence first. An inconsistent system cannot have a unique solution, and the presence of a free coefficient variable does not repair a contradiction.

# 0. Mathematical foundations

This chapter is supplementary prerequisite teaching. It is included because the supplied linear algebra assumes these skills. None of it adds a later course topic.

## 0.1 Numbers, variables, and signs

A number can describe an amount, a position, or a change. On a number line, 3 is three units to the right of 0 and -3 is three units to the left. The minus sign can name a negative number, as in -3, or describe subtraction, as in 5 - 3. In -(-3), the outer minus asks for the opposite of -3, giving 3.

A variable is a symbol whose value is being discussed. In 2x + 3 = 11, x is unknown; in y = 2x + 3, x may be an input and y the corresponding output. The same letter need not play the same role in every problem. State what your unknowns represent before calculating an application.

Multiplication by a positive number preserves direction on the number line. Multiplication by a negative number reverses direction. Thus (-2)(3) = -6, (-2)(-3) = 6, and 2(-3) = -6. The rule for two negatives follows from distributivity: 0 = (-2)(3 + (-3)) = -6 + (-2)(-3), so the last product must be 6.

Subtraction means adding the opposite. For example, 4 - (-5) = 4 + 5 = 9, but -4 - 5 = -9. Parentheses are essential in row operations: if an entry is -5 and you subtract twice a row whose corresponding entry is -3, the new entry is -5 - 2(-3) = 1.

**Worked arithmetic.** Evaluate -3 + 2(-4) - (-5). Multiplication comes first: 2(-4) = -8. Replace subtracting -5 by adding 5. The result is -3 - 8 + 5 = -6. Do not turn the entire expression positive because it contains two minus signs; only the particular subtraction of a negative changes to addition.

## 0.2 Fractions and exact arithmetic

The fraction a/b means a divided by b, with b nonzero. Equivalent fractions are formed by multiplying or dividing both numerator and denominator by the same nonzero number. Thus 6/9 = 2/3. The fraction -2/3 equals 2/(-3), but (-2)/(-3) equals 2/3.

To add fractions, express them with a common denominator. For 1/2 + 1/3, use sixths: 3/6 + 2/6 = 5/6. Adding the denominators would produce 2/5, which is a different number. For -3/4 + 5/6, use twelfths: -9/12 + 10/12 = 1/12.

Multiply numerators together and denominators together: (2/3)(-9/4) = -18/12 = -3/2. Cancel common factors before multiplying if helpful: 9 divided by 3 is 3, and 2 divided by 4 is 1/2. Cancellation applies to factors, not arbitrary terms in a sum. You cannot cancel the 2 in (2 + 3)/2 to obtain 1 + 3.

Dividing by a nonzero fraction means multiplying by its reciprocal. Hence (3/5)/(2/7) = (3/5)(7/2) = 21/10. Division by 0 is never allowed. If a row has pivot -3, multiplying the row by -1/3 changes that pivot to 1; every entry of the row must receive the same multiplier.

**Worked row arithmetic.** If R₁ = [2, -3, 5] and R₂ = [1, 1/2, -2], then R₂ ← R₂ - (1/2)R₁ gives [1 - 1, 1/2 + 3/2, -2 - 5/2] = [0, 2, -9/2]. The fraction is exact. A rounded decimal such as -4.5 is harmless here, but fractions prevent rounding errors from accumulating in longer calculations.

## 0.3 Expressions, equality, and solving an equation

An expression such as 3x - 2 has a value after x is chosen. An equation such as 3x - 2 = 10 asserts that two expressions have equal values. A solution is a choice that makes the assertion true. Checking x = 4 gives 3(4) - 2 = 10, so 4 is a solution. Checking x = 2 gives 4 rather than 10, so 2 is not.

Use the order: grouping, powers, multiplication and division from left to right, then addition and subtraction from left to right. For 2 + 3(4 - 1)^2, first obtain 4 - 1 = 3, then 3^2 = 9, then 3·9 = 27, then 2 + 27 = 29. A subscript such as x₂ is a label; it is not a power and does not mean x squared.

Distributivity says a(b + c) = ab + ac. In -2(x - 3), distribute the negative multiplier to both terms: -2x + 6. Combining like terms gives 3x + 2x = 5x, but 3x + 2y cannot be combined unless x and y are known to be equal.

To solve an equation, preserve its truth by performing the same reversible action on both sides. Starting with 3x - 2 = 10, add 2 to both sides to get 3x = 12; divide both sides by 3 to get x = 4. The phrase 'move -2 to the other side' abbreviates adding 2 to both sides. It is not a separate rule that lets terms cross an equals sign without a reason.

**Worked fraction equation.** Solve x/3 - 2 = 5/6. Add 2 = 12/6 to both sides: x/3 = 17/6. Multiply both sides by 3: x = 17/2. Check: (17/2)/3 - 2 = 17/6 - 12/6 = 5/6. The check uses the original equation and therefore catches a sign error made during rearrangement.

Two warnings matter later. Multiplying an equation by zero loses information: x = 4 would become 0 = 0, which is true for every x. Dividing by a variable may discard solutions if that variable could be zero. Row scaling therefore uses a known nonzero number, and parameter problems require a separate case when a potential pivot becomes zero.

## 0.4 Substitution and simultaneous equations

Substitution means replacing a symbol by its stated value or expression wherever that symbol occurs. If x = 2t - 1, then 3x + 4 becomes 3(2t - 1) + 4 = 6t + 1. Keep parentheses around the replacement until you have distributed correctly.

A system asks you to satisfy several equations at the same time. Consider x + y = 5 and x - y = 1. Adding the equations gives 2x = 6, so x = 3. Substitute into the first equation: 3 + y = 5, hence y = 2. Both original equations check: 3 + 2 = 5 and 3 - 2 = 1. Satisfying only the first equation would be insufficient; (1,4) fails the second.

If the system instead says x + y = 5 and x + y = 7, subtracting the first equation from the second gives 0 = 2. This cannot be true, so no pair works. If the second equation is 2x + 2y = 10, it repeats the first equation. Every pair (5 - t,t) works, because (5 - t) + t = 5. A repeated equation supplies no new restriction.

## 0.5 Coordinates and lines

The horizontal axis is the x₁-axis and the vertical axis is the x₂-axis. Their intersection is the origin (0,0). An ordered pair (a,b) means move a units horizontally, then b units vertically. The order matters: (2,-1) and (-1,2) are different points. Three coordinates locate a point in three-dimensional space.

The graph of an equation is the set of all points satisfying it. For x₂ = 2x₁ + 1, choosing x₁ = 0,1,2 gives points (0,1), (1,3), (2,5). The line passes through all of them. Its slope 2 means a horizontal change of 1 produces a vertical change of 2. A vertical line such as x₁ = 3 cannot be written as x₂ = mx₁ + c, but it is still a linear equation.

An equation ax₁ + bx₂ = c with at least one of a,b nonzero describes a line in the plane. Two such lines can intersect once, be distinct and parallel, or coincide. Those pictures correspond to one solution, no solutions, and infinitely many solutions of a two-equation system. Equations in three variables normally describe planes; the common solution must lie in all the specified planes.

@figure systems

The diagrams show the three possibilities for two genuine lines in the plane. A system with more equations still demands a point common to every graph, not merely an intersection of two selected graphs.

## 0.6 Reading mathematical language

The symbol ℝ names the real numbers. The statement t ∈ ℝ means t is a real number. A set is a collection of objects; braces list its members. The empty set, ∅, has no members. The set {0} contains one member, zero, so it is different from ∅. In linear algebra, the zero in {0} may be a vector, whose size is determined by the context.

The statement P ⇒ Q means 'if P is true, then Q is true.' It does not automatically assert the reverse. The statement P ⇔ Q means both directions: P implies Q and Q implies P. It is read 'P if and only if Q.' To prove an equivalence, explain both directions or give a chain of already established equivalences.

A universal statement says something about every allowed object. For instance, 'every homogeneous system has a solution' includes systems of every permitted size. One numerical example cannot prove it. The vector x = 0 supplies a solution for an arbitrary matrix A, which is a general argument. A false universal statement can be disproved by a single counterexample satisfying its assumptions and violating its conclusion.

A theorem is a mathematical statement proved from definitions and accepted earlier results. Its assumptions matter. 'A consistent system with a free variable has infinitely many solutions' includes the assumption of consistency. Omitting that assumption makes the statement false. A proof is a chain of justified statements that begins with the assumptions and ends with the desired conclusion. An intuitive picture helps explain a theorem, but a proof must cover every case covered by its wording.

Sigma notation is a compact way to add indexed terms. The expression Σ from j=1 to n of a_j x_j means a₁x₁ + a₂x₂ + ... + a_n x_n. The index j runs through the indicated labels. No new operation is involved. We use expanded sums whenever they make a new idea easier to read.

## 0.7 Foundation practice

**F1.** Evaluate -2(3 - 5) + 1/2 - 5/6 exactly.

**F2.** Solve 2(x - 3)/5 = 4 and verify your answer.

**F3.** Solve x + 2y = 7 and 3x - y = 7. Explain why both equations must be checked.

**F4.** Explain the difference between x₂ and x^2, and between 'there exists a solution' and 'there exists exactly one solution.'

**F5.** Disprove: 'If two equations have one common solution, they have the same solution set.' Supply actual equations and explain their different sets.

Worked answers appear in Chapter 12.

# 1. Section 1.1 - Systems of linear equations

Source correspondence: Combined PDF pages 1-11; exercise PDF pages 1-2. This chapter expands the lecture definitions and the two principal elimination examples.

## 1.1 What makes an equation linear?

The equation 2x₁ - 3x₂ + x₃ = 7 gives a weighted sum of unknown entries. The numbers 2,-3,1 are coefficients; 7 is the constant on the right. A missing variable has coefficient 0. The general form is a₁x₁ + ... + a_n x_n = b, where the coefficients and b are fixed numbers. The unknowns appear to the first power and are not multiplied together.

Thus x₁ + 2x₂ = 3 is linear; x₁x₂ = 3, x₁^2 + x₂ = 1, and 1/x₁ + x₂ = 4 are not linear equations in these variables. A coefficient can be a fraction or a square root if it is a fixed number. The restriction concerns how the unknowns enter, not how simple the known coefficients look.

A solution is a list of numbers in the variable order that makes every equation true. The solution set contains every such list. Two systems are equivalent when their solution sets are identical. A consistent system has at least one solution; an inconsistent one has none. A linear system over ℝ has zero, one, or infinitely many solutions. It cannot have exactly two: if p and q are distinct solutions, linearity shows that p + t(q - p) is a solution for every real t.

## 1.2 Matrices record the equations without changing them

A matrix is a rectangular array. Its size is rows × columns, with rows first. The coefficient matrix records the coefficients in a fixed variable order. The augmented matrix appends the constants. For the lecture system, the coefficient rows are [1,-2,1], [0,2,-8], [-4,5,9], and the constants are [0,8,-9]. The 0 at the start of the second row means the equation has no x₁ term. It is needed to keep the other coefficients in their correct columns.

The coefficient matrix has size 3 × 3. The augmented matrix has size 3 × 4. The four columns do not mean four unknowns: one column contains the constants. In every substantial reduction below, a vertical line marks that distinction.

## 1.3 Why row operations preserve solutions

Three elementary operations are allowed. Interchange two rows. Multiply one row by a nonzero scalar. Replace one row by itself plus a multiple of a different row. The notation R₃ ← R₃ + 4R₁ means compute four times every entry of row 1, add those entries to row 3, and put the results into row 3. The arrow describes replacement, not an equation between row numbers.

Interchanging equations changes only their order. Scaling by c ≠ 0 is reversible by scaling by 1/c. Replacing equation E₃ by E₃ + 4E₁ is reversible by subtracting 4E₁. If a list satisfies the original equations, it satisfies the replacement; if it satisfies the new equations, reversal shows it satisfies the original ones. This explains preservation in both directions.

Scaling by 0 is not an elementary operation. Replacing R₃ by R₃ + 4R₁ must change the appended constant as well as every coefficient. Performing unrelated column operations generally changes which variable combinations are being represented and is not the solving method used here.

## 1.4 Complete lecture example: systematic elimination

Solve x₁ - 2x₂ + x₃ = 0, 2x₂ - 8x₃ = 8, and -4x₁ + 5x₂ + 9x₃ = -9 (Combined PDF pages 4-8). We choose pivots from left to right, eliminate below them, then clear above. Our intermediate order may differ from the slides, but each reversible operation solves the same system.
''')
solve([[1,-2,1,0],[0,2,-8,8],[-4,5,9,-9]])
put('''The unique answer (29,16,3) satisfies 29 - 32 + 3 = 0, 32 - 24 = 8, and -116 + 80 + 27 = -9. The matrix method did not introduce an approximation. It rearranged the original information until the unknown values could be read directly.

## 1.5 A contradiction ends the existence question

For the lecture system on pages 9-11, the equations are x₂ - 4x₃ = 8, 2x₁ - 3x₂ + 2x₃ = 1, and 5x₁ - 8x₂ + 7x₃ = 1. An impossible row will establish that there is no common solution. We display a full reduction here; when solving an existence-only question by hand, you may stop as soon as a contradiction appears.
''')
solve([[0,1,-4,8],[2,-3,2,1],[5,-8,7,1]])
put('''A row of zeros on the left with a nonzero right-hand side is an impossible equation. A completely zero row instead represents 0 = 0; that row is always true. Confusing these two rows reverses the consistency decision.

## 1.6 Choosing a method and writing the conclusion

Gaussian elimination means using row operations to reach a staircase arrangement, then substituting backward. Gauss-Jordan elimination continues until each pivot is 1 and its column is otherwise zero. Both methods preserve the solution set. The latter makes parameters especially easy to read.

If the question asks whether a solution exists, a consistent echelon form is enough. If it asks to solve, provide every solution, including arbitrary parameters when appropriate. If it asks for an intersection, give the point or describe the common set in the original coordinate language. If it asks to verify, substitute into the original equations; merely repeating a reduction is not the same check.

**Common mistakes.** Keeping only equations that are easy to satisfy can lose a contradiction. Forgetting a zero coefficient shifts columns. Adding rows without replacing a specified row makes the next step ambiguous. Multiplying one entry instead of the whole row changes the equations incorrectly. Always write the chosen operation and then the entire updated matrix.

## 1.7 Practice

**S11.** Solve x₁ + 2x₂ = 7 and 3x₁ - x₂ = 7 using an augmented matrix.

**S12.** Classify the systems x₁ + x₂ = 2, 2x₁ + 2x₂ = 5 and x₁ + x₂ = 2, 2x₁ + 2x₂ = 4. Give complete solution sets.

**S13.** Explain why replacing R₂ by R₂ - 3R₁ is reversible, but multiplying R₂ by 0 is not.

# 2. Section 1.2 - Row reduction and echelon forms

Source correspondence: Combined PDF pages 12-27; exercise PDF pages 3-4.

## 2.1 The staircase and the pivots

The leading entry of a nonzero row is its first nonzero entry when read from left to right. A matrix is in row echelon form (REF) when all zero rows are at the bottom, each leading entry is strictly to the right of the leading entry in the row above, and every entry below a leading entry is zero. Leading entries need not be 1 in REF.

Reduced row echelon form (RREF) also requires each leading entry to be 1 and each leading 1 to be the only nonzero entry of its column. A matrix can be REF without being RREF. For example, [2,3;0,4] is REF, but the leading entries are not 1. The notation in this sentence separates rows with a semicolon; displayed matrices below use full brackets.

A pivot position in A is the row-column location corresponding to a leading 1 in RREF(A). A pivot column is an original column containing such a position. The original entry at a pivot position can be zero: the position is identified through reduction. A pivot used during elimination is the nonzero entry currently used to cancel entries, so its numerical value can change with the sequence of operations.

The supplied uniqueness theorem states that every matrix has exactly one RREF among its row-equivalent matrices. REF is not unique, because multiplying a nonzero row by 2 may preserve its staircase shape. The RREF conditions remove that scaling freedom and all entries above pivots. More deeply, row equivalence preserves all constraints, and RREF is a canonical way to record which earliest variables are determined by later ones. The following supplementary proof explains that uniqueness rather than trying to establish it by numerical examples.

### Why two different RREF answers cannot both be right

We need one temporary piece of vocabulary. The row span of a matrix means all linear combinations of its rows, treated as horizontal lists. This is the same weighted-sum idea used for column vectors later in Section 1.3. Row operations do not change the row span. A new row is a combination of old rows, so every new-row combination is an old-row combination. Reversibility gives the opposite inclusion. Therefore row-equivalent matrices have exactly the same row span.

Suppose R and S are two RREF matrices obtained from one matrix. They have the same row span. In an RREF matrix, take any nonzero combination of its nonzero rows, and find the first row in the combination whose weight is nonzero. Its leading pivot is the first nonzero coordinate of the resulting list: all earlier row weights are zero, and all later rows are zero to the left of their own later pivots. Consequently the possible first-nonzero coordinate locations of vectors in the row span are precisely the pivot-column indices. Since R and S have the same row span, they have the same pivot columns, in the same order.

Now compare row i of R with row i of S. Their entries in every common pivot column agree: both have 1 at their own pivot and 0 at the other pivots. Their difference is in the common row span and is zero at every pivot coordinate. But any row combination in R has, in pivot column j, exactly the weight on the corresponding pivot row: the pivot columns are identity columns. If all those coordinates are zero, every row weight is zero, so the entire combination is zero. Thus the difference between the two compared rows must be zero. All corresponding nonzero rows agree, and both matrices place their remaining zero rows at the bottom. Hence R = S. This proves uniqueness while allowing different intermediate operations and different ordinary echelon forms.

## 2.2 The forward and backward phases

Start at the leftmost column containing a possible nonzero pivot. Interchange rows if needed. Use a nonzero pivot to clear entries below it. Move down one row and right to the next possible pivot column. Continue to REF. This is the forward phase. If a column has no available nonzero entry below the previous pivots, skip it; do not force a pivot there.

For the backward phase, start at the rightmost pivot, scale its row to make the pivot 1, and clear entries above it. Continue upward and leftward. Normalizing a pivot earlier, as many examples here do, is also valid. Arithmetic convenience determines the order; preserving the equations determines validity.

## 2.3 Course example: pivot columns of a rectangular matrix

The matrix on Combined PDF pages 14-17 has four rows and five columns. It is not declared an augmented matrix in that example, so all five columns are ordinary matrix columns. Row reduction finds pivot columns without making any claim about a solution set.
''')
a=[[0,-3,-6,4,9],[-1,-2,-1,3,1],[-2,-3,0,3,-1],[1,4,5,-9,-7]]
s,r,p=walkthrough(a);put(s);put('The pivots occur in columns '+', '.join(str(x+1) for x in p)+'. Mark those column numbers in the original matrix as well as the reduced one. The entries of a reduced pivot column are generally not the entries of the corresponding original column.')
put('''## 2.4 A larger course reduction

Combined PDF pages 17-22 use the following 3 × 6 matrix. This is an algorithm example, not automatically a five-variable system. We reduce every column and identify the pivots. If you later interpret the last column as appended constants, only the first five columns represent unknowns.
''')
s,r,p=walkthrough([[0,3,-6,6,4,-5],[3,-7,8,-5,8,9],[3,-9,12,-9,6,15]]);put(s)
put('''The pivots are in columns 1,2,5. Column 3 cannot acquire an additional pivot without contradicting the existing row constraints. A skipped column is mathematically meaningful; it is not an unsuccessful step.

## 2.5 Basic and free variables: what freedom means

Suppose the augmented matrix is already in the following reduced form. It has three coefficient columns and one constant column. A missing pivot in coefficient column 3 means x₃ can be chosen freely, provided no contradiction occurs. It does not mean that x₃ must be zero or that it can be omitted from the answer.
''')
solve([[1,0,-2,3],[0,1,1,4],[0,0,0,0]])
put('''For the lecture's related reduced matrix [1,0,-5 | 1], [0,1,1 | 4], [0,0,0 | 0], the same reasoning gives x₁ = 1 + 5t, x₂ = 4 - t, x₃ = t. Choosing t = 0 gives (1,4,0), and choosing t = 1 gives (6,3,1). Both satisfy x₁ - 5x₃ = 1 and x₂ + x₃ = 4. Different formulas can describe the same solution set if you choose a different parameter; RREF itself is still unique.

## 2.6 Two free variables and complete answers

More unknowns than pivots can leave several independent choices. Use a different parameter for each free variable. The following original example has four unknowns. Do not use the same t for both free variables, because that would impose an extra restriction not present in the equations.
''')
solve([[1,2,-1,3,4],[2,4,-2,6,8],[0,0,1,-2,1]])
put('''## 2.7 Existence and uniqueness theorem

**Theorem (supplied Theorem 2).** A linear system is consistent if and only if the last column of its augmented matrix is not a pivot column. Equivalently, no echelon row is [0,...,0 | c] with c ≠ 0. Once consistency is established, the solution is unique exactly when there are no free coefficient variables; it is infinite exactly when there is at least one free coefficient variable.

Why does the theorem work? A last-column pivot corresponds to an impossible equation. Without such a row, free variables can be assigned values and the pivot equations can be solved backward, which constructs a solution. With no free variables the construction has no arbitrary choices. With a free variable, changing that coordinate changes the solution itself, so infinitely many solutions result.

A zero coefficient row does not by itself prove either inconsistency or infinitely many solutions. Its constant determines whether it is a contradiction. The number of nonzero coefficient pivots relative to the number of unknowns determines whether free variables remain.

## 2.8 Practice

**R1.** Decide whether [1,2,0;0,0,1;0,0,0] is REF, RREF, both, or neither. Explain each condition.

**R2.** Solve x₁ + 2x₂ - x₃ = 4 and 2x₁ + 4x₂ - 2x₃ = 8. Use two independent parameters.

**R3.** A 3 × 5 coefficient matrix has three pivots. Is Ax = b solvable for every b ∈ ℝ^3? Can a consistent system have a unique solution? Distinguish the two conclusions.
''')
put('''# 3. Section 1.3 - Vector equations

Source correspondence: Combined PDF pages 28-36; exercise PDF pages 5-6. Applications include mine outputs and a coal-burning plant.

## 3.1 A vector keeps several quantities together

A vector is an ordered list of entries, normally written as a column. The vector (2,-1) can represent a point, a displacement, or two measured quantities. Its interpretation comes from the problem. The set ℝ^2 contains every column with two real entries; ℝ^3 contains every column with three. In ℝ^n, n is the number of entries, not the numerical size of an entry.

The vector (2,-1) can be drawn as an arrow from (0,0) to (2,-1). Moving the arrow without changing its length or direction gives the same displacement. The coordinate point is the endpoint when the arrow starts at the origin. A vector is not merely its length: (2,0) and (0,2) point in different directions.

Two vectors are equal when they have the same number of entries and their corresponding entries are equal. Addition is entrywise and needs matching sizes. For u = (2,-1), v = (-3,4), u + v = (2 - 3,-1 + 4) = (-1,3). Subtraction is addition of the opposite: u - v = (2 + 3,-1 - 4) = (5,-5).

A scalar is an ordinary number multiplying a vector. The scalar multiple cu multiplies every entry of u by c. For c = -2, -2u = (-4,2): the direction reverses and the length doubles. The zero vector has every entry zero; its size must match the surrounding calculation. Multiplication by 0 produces that vector.

@figure vectors

The left diagram adds u = (2,1) and v = (1,2). Starting at the endpoint of u and drawing a copy of v reaches u + v = (3,3). The opposite order reaches the same point. Completing the parallelogram supplies the geometric version of commutativity. The right diagram compares u, -u, and 2u.

## 3.2 Vector algebra has familiar rules

For vectors of the same size, u + v = v + u and (u + v) + w = u + (v + w). Also u + 0 = u and u + (-u) = 0. Scalars distribute: c(u + v) = cu + cv and (c + d)u = cu + du. Scalar multiplication associates: c(du) = (cd)u, and 1u = u. Each statement follows entry by entry from the corresponding real-number property.

A useful proof illustrates this. Entry i of c(u + v) is c(u_i + v_i). Real-number distributivity makes this cu_i + cv_i, which is entry i of cu + cv. Both vectors have the same size and agree in every entry, so they are equal. Checking only the first entry would not prove vector equality in general.

## 3.3 Linear combinations and unknown weights

A linear combination of v₁,...,v_p is c₁v₁ + ... + c_pv_p, where the weights c_i are scalars. The weights may be negative or zero. You are choosing how much of each available vector to use. A question asking whether b can be generated by given vectors asks whether any weights produce b exactly.

Take the lecture vectors a₁ = (1,-2,-5), a₂ = (2,5,6), b = (7,4,-3) (Combined PDF pages 32-35). The equation x₁a₁ + x₂a₂ = b means the three entries agree: x₁ + 2x₂ = 7, -2x₁ + 5x₂ = 4, and -5x₁ + 6x₂ = -3. The unknowns are the weights, not the entries of the supplied vectors.
''')
solve([[1,2,7],[-2,5,4],[-5,6,-3]],'Place a₁ and a₂ into coefficient columns and b after the divider. A solution gives the required weights.')
put('''The weights 3 and 2 mean b = 3a₁ + 2a₂. Directly, 3(1,-2,-5) + 2(2,5,6) = (3,-6,-15) + (4,10,12) = (7,4,-3). The solution answers the original generation question, not merely an unrelated system.

## 3.4 Span is the entire collection of obtainable outputs

**Definition.** Span{v₁,...,v_p} is the set of all c₁v₁ + ... + c_pv_p as the real weights vary. The braces {v₁,v₂} name a collection of the listed vectors. Span{v₁,v₂} normally contains infinitely many vectors, including 0, v₁, v₂, and many others. Do not confuse the generating collection with the set it generates.

If v ≠ 0, its scalar multiples tv form a line through the origin. If v = 0, its span is only {0}. Two nonzero vectors that are multiples of one another still span just one line. Two vectors in ℝ^3 that are not multiples span a plane through the origin. Two such vectors in ℝ^2 span the entire coordinate plane. A general span need not be a plane: it may be {0}, a line, a plane, or all of ℝ^3 in three-dimensional examples.

@figure span

The right diagram uses the coordinate directions (3,0) and (0,3). An arbitrary (a,b) equals (a/3)(3,0) + (b/3)(0,3), so every point is obtainable. The left pair contains redundant directions and cannot leave its line.

@figure plane

The shaded region represents part of the infinite x₁x₂-plane in ℝ^3, generated by u = (2,0,0) and v = (0,2,0). Its points have form (2s,2t,0), with s,t real. The adjacent three-dimensional sketch shows a homogeneous line and its translate by (0,0,1). These are coordinate projections of three-dimensional objects, not claims that the drawn angles are their true spatial angles.

To test whether b belongs to a span, solve the augmented system [v₁ ... v_p | b]. Consistency proves membership. A contradictory row proves nonmembership. A pivot in every row of the coefficient matrix proves membership for every b of the appropriate size, a stronger statement than membership of one particular b.

## 3.5 Application: mine production

Course Exercise 1.3.35 describes daily mine outputs v₁ = (20,550) and v₂ = (30,500). The first entry measures metric tons of copper; the second measures kilograms of silver. Multiplying v₁ by 5 means operating mine 1 for five days: 5v₁ = (100,2750). The two entries have different units, so they must not be added to each other.

For a target (150,2825), let x₁,x₂ be operating days for mines 1 and 2. Then x₁v₁ + x₂v₂ = (150,2825). The two entry equations track the two resources independently. Here fractional days are mathematically allowed; an actual operating policy could add a restriction, but none should be invented in the algebra.
''')
solve([[20,30,150],[550,500,2825]])
put('''The result is 3/2 days at mine 1 and 4 days at mine 2. Check copper: 20(3/2) + 30(4) = 150. Check silver: 550(3/2) + 500(4) = 2825. This is the same linear-combination method used for abstract vectors, with meanings attached to the weights and entries.

## 3.6 Practice

**V1.** For u = (1,-2), v = (2,-5), compute 4u - 3v and explain the effect of each scalar.

**V2.** Determine whether (5,1) belongs to Span{(1,1),(2,-1)}. Find weights and verify them.

**V3.** Describe Span{(2,4,0),(3,6,0)} geometrically. Is (1,0,0) in it?

**V4.** A process produces (2,5) units per batch of type A and (3,1) per batch of type B. Find nonnegative batch amounts giving (13,13), and check both quantities.

# 4. Section 1.4 - The matrix equation Ax = b

Source correspondence: Combined PDF pages 37-43; exercise PDF pages 7-8.

## 4.1 Multiplication combines columns

If A has m rows and n columns and x has n entries, Ax is the vector formed by using the entries of x as weights on the columns of A. Its size is m × 1. Thus an m × n matrix takes an input in ℝ^n and produces an output in ℝ^m. The number of columns must match the number of input entries.

Write A = [a₁ ... a_n]. Then Ax = x₁a₁ + ... + x_n a_n. This definition explains the multiplication: every column is a possible output contribution, and the input tells us how to combine them. An m × n matrix multiplied by an input with m entries is not automatically valid; check n, not m.

The row computation rule follows by examining one entry. Entry i of Ax is a_{i1}x₁ + ... + a_{in}x_n. Multiply matching entries across row i of A and down x, then add. This sum of products is sometimes called a dot product here. It is a scalar; the collection of m such scalars is the output vector.

## 4.2 Worked product using both views

Let A = [2,3; -1,5; 4,0] and x = (2,-1). The column view gives 2(2,-1,4) - (3,5,0) = (1,-7,8). The row view gives the same result with each entry shown below.
''')
prod([[2,3],[-1,5],[4,0]],[[2],[-1]])
put('''## 4.3 One problem, three equivalent languages

Consider the system x₁ + 2x₂ - x₃ = 4 and -5x₂ + 3x₃ = 1, taken from the lecture on pages 38-39. Gathering coefficients by variable gives the vector equation x₁(1,0) + x₂(2,-5) + x₃(-1,3) = (4,1). Gathering those coefficient vectors into columns gives Ax = b with A = [1,2,-1;0,-5,3], x = (x₁,x₂,x₃), and b = (4,1).

These statements have exactly the same unknowns and exactly the same solutions. Expanding Ax by columns gives the vector equation; equating its entries gives the system. The augmented matrix simply records those entry equations. A conversion question may ask only for these forms; do not solve unless required.
''')
solve([[1,2,-1,4],[0,-5,3,1]])
put('''## 4.4 A particular b versus every b

**Theorem (supplied Theorem 4).** For an m × n matrix A, the following four statements are equivalent: Ax = b has a solution for every b ∈ ℝ^m; every b ∈ ℝ^m is a linear combination of the columns; the columns span ℝ^m; A has a pivot position in every row.

The first three formulations are equivalent by the definition of Ax and span. For the pivot formulation, imagine row-reducing A while carrying an arbitrary appended b. If each coefficient row has a pivot, no row is left over that could state 0 = nonzero, so every appended b is allowed. If a coefficient row has no pivot, an appropriate b can leave a nonzero entry in that zero row, producing inconsistency. This last statement asserts some b will fail; it does not say every b fails.

For A = [1,2;2,4], b = (3,6) works, since the second equation repeats the first. But b = (3,7) fails. The column span is a line in ℝ^2, not all of ℝ^2. By contrast, A = [1,0,2;0,1,-1] has a pivot in each of its two rows and can produce every b = (b₁,b₂): choose x = (b₁,b₂,0). It still has a free input coordinate, so uniqueness does not follow.

## 4.5 Identity and distributivity

The identity matrix I_n has 1 on its main diagonal and 0 elsewhere. Its columns are the standard coordinate vectors. Consequently I_n x = x: each coordinate is copied once and nothing is mixed. The subscript records the size, so I₂ and I₃ are different matrices.

For compatible vectors u,v and scalar c, A(u + v) = Au + Av and A(cu) = cAu (supplied Theorem 5). A proof by columns writes A(u + v) = (u₁ + v₁)a₁ + ... + (u_n + v_n)a_n. Distribute and regroup to obtain (u₁a₁ + ... + u_n a_n) + (v₁a₁ + ... + v_n a_n) = Au + Av. Similarly, A(cu) = (cu₁)a₁ + ... + (cu_n)a_n = cAu. These properties later explain why matrix transformations are linear.

## 4.6 Practice

**A1.** Write 2x₁ - x₂ = 3 and x₁ + 4x₂ = 5 as a vector equation and a matrix equation, then solve.

**A2.** A is 2 × 3 and has two pivots. Explain what this says about every b ∈ ℝ^2 and about uniqueness.

**A3.** Compute [1,2,3;0,-1,4](2,1,-1) by the column and row rules. State every size.

# 5. Section 1.5 - Solution sets of linear systems

Source correspondence: Combined PDF pages 44-52; exercise PDF page 9.

## 5.1 Homogeneous means zero right-hand side

A homogeneous system has the form Ax = 0. Its zero on the right is the zero vector in ℝ^m if A is m × n. Its unknown x lies in ℝ^n. The choice x = 0 always works, because multiplying every column by weight zero gives zero. This is the trivial solution. A nontrivial solution is any solution vector with at least one nonzero entry; it need not have every entry nonzero.

A homogeneous system has a nontrivial solution if and only if at least one coefficient variable is free. There is never a contradiction, because the appended zero column stays zero under row operations. If every variable is basic, the pivot equations force every variable to zero. If some variable is free, set it to 1 and the other free variables to 0; the resulting solution is nonzero. This proves both directions.

## 5.2 The lecture homogeneous system

The lecture uses coefficient rows [3,5,-4], [-3,-2,4], [6,1,-8]. A nonzero direction of solutions would describe inputs that A sends to zero. The reduction below reveals exactly which direction survives.
''')
solve([[3,5,-4,0],[-3,-2,4,0],[6,1,-8,0]],hom=True)
put('''The solution is t(4/3,0,1), a line through the origin. You may instead use s(4,0,3). These describe the same line because t = 3s. Changing the scale of a direction vector does not change the line if the parameter still ranges over all real numbers.

## 5.3 A particular solution translates the homogeneous set

Now keep the same A and change b to (7,-1,-4), as on Combined PDF pages 47-49. This system is nonhomogeneous. Its zero input is no longer a solution. We seek one particular solution p and all allowable homogeneous directions.
''')
solve([[3,5,-4,7],[-3,-2,4,-1],[6,1,-8,-4]])
put('''Here p = (-1,2,0), v = (4/3,0,1), and x = p + tv. The fixed p chooses a starting point that already satisfies Ax = b. The scalar t is a free real number. The direction v tells how to move without changing the output, because Av = 0. At t = 0 we get p; at t = 3 we get (3,2,3). Check the latter: 9 + 10 - 12 = 7, -9 - 4 + 12 = -1, and 18 + 2 - 24 = -4.

@figure translation

The figure uses simpler two-dimensional vectors to display the same principle. Translating a line through zero by p moves every point by the same vector. The new line is parallel to the original. For several free variables, an entire plane or higher-dimensional solution set is translated in the same way.

## 5.4 Why the complete solution is p plus a homogeneous solution

**Theorem (supplied Theorem 6).** Assume Ax = b is consistent and fix a particular solution p. Then x is a solution exactly when x = p + v_h for some v_h satisfying Av_h = 0.

To prove the forward direction, let x satisfy Ax = b. Since Ap = b, A(x - p) = Ax - Ap = b - b = 0. Thus v_h = x - p is homogeneous and x = p + v_h. For the reverse direction, start with any v_h satisfying Av_h = 0. Then A(p + v_h) = Ap + Av_h = b + 0 = b, so p + v_h is a solution. Both directions are needed: one says the formula produces solutions, the other says it misses none.

The theorem requires consistency. If no particular solution exists, there is no p with which to translate. A nonhomogeneous solution set normally does not contain the origin and is not itself a span of its direction vectors.

## 5.5 Point, line, plane, or empty

With no free variables a consistent solution set is a single point. With one free variable it is a line, because the parameter direction cannot be zero: it has a 1 in its free coordinate. With two free variables it is a plane, because the two direction vectors have different free-coordinate patterns and are independent. A contradictory row makes the set empty. In larger input spaces, more free variables give analogous sets that cannot be fully drawn on a page.

For x₁ + 2x₂ - x₃ = 4, choose x₂ = s and x₃ = t. Then x = (4,0,0) + s(-2,1,0) + t(1,0,1). Setting both parameters to zero gives the particular solution. Multiplying the coefficient row by either direction gives 0. If the right side is changed to 0, the particular point disappears and the solution plane passes through the origin.

**Common mistakes.** A homogeneous system is always consistent, but may have only the trivial solution. A nontrivial solution is not the same as a nonhomogeneous system. A parametric solution must include all its coordinates; writing only x₁ = 4 - 2s + t leaves x₂ and x₃ unspecified. The parameter coefficients become direction vectors, while constants become the particular vector.

## 5.6 Practice

**H1.** Solve x₁ - 2x₂ + x₃ = 0 in parametric vector form. Show a nontrivial solution.

**H2.** Solve x₁ - 2x₂ + x₃ = 5. Compare its geometry with H1 and prove your full answer works for arbitrary parameters.

**H3.** If Ap = b and Aq = b, prove that p - q is a homogeneous solution. Explain what this says when Ax = 0 has only the trivial solution.

# 6. Section 1.7 - Linear independence

Source correspondence: Combined PDF pages 53-62; exercise PDF page 10.

## 6.1 Redundancy and the precise definition

Imagine assembling outputs from a collection of vectors. If one vector can already be constructed from the others, including it does not enlarge the span. It is redundant. Linear dependence is the algebraic way of detecting such redundancy, including cases that are hard to see geometrically.

**Definition.** The indexed collection v₁,...,v_p is linearly independent when c₁v₁ + ... + c_pv_p = 0 forces c₁ = ... = c_p = 0. It is linearly dependent when at least one choice of weights, not all zero, gives the zero vector. Such a choice is a dependence relation. 'Not all zero' means at least one weight is nonzero, not that every weight must be nonzero.

Every collection admits the zero-weight combination. Therefore the fact that Ax = 0 has a solution proves nothing about independence: it always does. The test asks whether it has only that trivial solution. Put the vectors into columns of A, solve Ax = 0, and look for free variables. Every column pivot means independent. A free weight means dependent.

@figure independence

Two nonzero vectors along one line are dependent. Two vectors in the plane that point along different lines through zero are independent. Three vectors in ℝ^3 may be independent or may lie in a common plane through zero; a picture alone should not replace a calculation when exact coordinates are available.

## 6.2 Deriving a relation in the lecture example

For v₁ = (1,2,3), v₂ = (4,5,6), v₃ = (2,1,0), the lecture finds 10v₁ - 5v₂ + 5v₃ = 0. We derive a smaller equivalent relation by choosing the free weight 1 rather than 5. The coefficient matrix contains the original vectors as columns.
''')
ind([[1,4,2],[2,5,1],[3,6,0]])
put('''The relation 2v₁ - v₂ + v₃ = 0 rearranges to v₂ = 2v₁ + v₃. Thus the second vector adds no new attainable direction. Multiplying every weight by 5 gives the lecture relation. Nontrivial relations are not unique; one verified relation is sufficient to prove dependence.

## 6.3 The characterization theorem and its proof

**Theorem (supplied Theorem 7).** A collection of at least two vectors is dependent if and only if one vector is a linear combination of the others. If v₁ ≠ 0 and the indexed collection is dependent, some later vector is a combination of its predecessors.

If v_j is a combination of the others, subtract that expression from v_j. The resulting zero combination has coefficient 1 on v_j, so it is nontrivial. Conversely, take a nontrivial zero combination and select an index j with c_j ≠ 0. Rearrange to c_jv_j = -Σ for i ≠ j of c_i v_i, then divide by c_j. The division is valid because that coefficient is nonzero. It expresses v_j in terms of the others. For the predecessor statement, choose j to be the largest index with nonzero coefficient. All later coefficients vanish; if v₁ ≠ 0 then j cannot be 1, since c₁v₁ ≠ 0 when c₁ ≠ 0.

The theorem says at least one vector is redundant, not every vector. For {0,(1,0)}, the zero vector is obtainable using the other vector with weight 0, but (1,0) is not obtainable from the zero vector. This counterexample is useful in the course true/false questions.

## 6.4 Fast tests and their limitations

A one-vector collection {v} is independent exactly when v ≠ 0. If v ≠ 0 and cv = 0, a nonzero entry of v forces c = 0. If v = 0, the coefficient c = 1 gives a nontrivial relation. A collection containing zero is therefore dependent: give zero weight 1 and all others weight 0.

Two vectors are dependent exactly when one is a scalar multiple of the other, including the case where one is zero. To prove independence of two nonzero vectors, show that no single scalar makes all coordinates match. Comparing only one coordinate is not enough when it supplies no restriction, such as a coordinate that is zero in both.

**Theorem (supplied Theorem 8).** More than n vectors in ℝ^n are dependent. Put p > n vectors into an n × p matrix. There can be at most n pivots, so at least one of the p weights is free. The homogeneous system has a nontrivial solution. The converse is false: two vectors in ℝ^3 may already be dependent, for example (1,0,0) and (2,0,0).

For an independent pair u,v in ℝ^3, w belongs to Span{u,v} exactly when {u,v,w} is dependent. The assumption that u,v are independent matters. Without it, the triple could be dependent before w was added, even if w lies outside their line.

## 6.5 An independent example

The following three columns are tested by solving the homogeneous system. A final identity coefficient block means each weight must vanish; it does not assert that the original vectors were themselves identity columns.
''')
ind([[1,0,2],[0,1,-1],[1,1,0]])
put('''## 6.6 Practice

**I1.** Test (1,2), (2,4), (0,1) for independence and give an explicit nontrivial relation.

**I2.** Test (1,0,1), (0,1,1), (1,1,0) for independence by a homogeneous system.

**I3.** Prove that a subset of an independent collection is independent. Explain why a superset of a dependent collection is dependent.

**I4.** Disprove: 'If a collection has no zero vector, then it is independent.'

# 7. Section 1.8 - Introduction to linear transformations

Source correspondence: Combined PDF pages 63-70; exercise PDF page 11.

## 7.1 Inputs, outputs, and reachable outputs

A function assigns exactly one output to every allowed input. A transformation or mapping is another name for a function. The domain lists allowed inputs. The codomain is the declared space containing the outputs. The image T(x) is the particular output produced by x. The range is the set of all outputs that are actually attained as x varies.

For T: ℝ^2 → ℝ^3 with T(x) = Ax and A a 3 × 2 matrix, each input has two entries and each output has three. The range is the span of A's columns, a subset of ℝ^3. The codomain is still ℝ^3 even if only a plane is attained. Do not shrink the codomain silently in order to make a statement about onto behavior true.

Computing T(u) means multiplying A by a known input u. Finding an x with T(x) = b means solving Ax = b. Checking whether b is in the range means deciding whether that system is consistent. These requests use different directions of the input-output relationship.

## 7.2 Complete lecture example: image and preimage

The lecture matrix is A = [1,-3;3,5;-1,7], with u = (2,-1), b = (3,2,-5), and c = (3,2,5). First compute the image of u.
''')
prod([[1,-3],[3,5],[-1,7]],[[2],[-1]])
put('Now solve for a preimage of b. The unknown is an input in ℝ^2, not an output in ℝ^3.')
solve([[1,-3,3],[3,5,2],[-1,7,-5]])
put('The input is (3/2,-1/2) and is unique. To test whether c is reachable, repeat with c as the appended column.')
solve([[1,-3,3],[3,5,2],[-1,7,5]])
put('''Thus b lies in the range and c does not. The columns are independent, so every reachable output has a unique input, but there are codomain vectors that are not reachable. This example anticipates the distinction between one-to-one and onto.

## 7.3 What linear means for a function

**Definition.** T is linear if T(u + v) = T(u) + T(v) for every pair of domain vectors and T(cu) = cT(u) for every domain vector u and every real scalar c. The first property preserves addition; the second preserves scaling. Their combination gives T(cu + dv) = cT(u) + dT(v). This is the superposition principle: a weighted combination of inputs produces the same weighted combination of outputs.

Every matrix transformation is linear because matrix-vector multiplication distributes over addition and scalar multiplication. For example, T(x₁,x₂) = (2x₁ - x₂,3x₂) has matrix [2,-1;0,3]. To prove the statement from the definition, let u = (u₁,u₂), v = (v₁,v₂). Then T(u + v) = (2u₁ + 2v₁ - u₂ - v₂,3u₂ + 3v₂) = T(u) + T(v). Also T(cu) = (2cu₁ - cu₂,3cu₂) = cT(u). Arbitrary letters make the proof cover all inputs.

Every linear T sends zero to zero: T(0) = T(0u) = 0T(u) = 0. This is a necessary condition, not a sufficient one. S(x₁,x₂) = (x₁ + 1,x₂) fails immediately because S(0) = (1,0). The rule Q(x₁,x₂) = (x₁^2,x₂) passes the zero test but fails scaling: Q(2,0) = (4,0), while 2Q(1,0) = (2,0). A counterexample proves failure; numerical examples of success cannot prove universal linearity.

## 7.4 Dilations, contractions, and shear

The rule T(x) = rx scales every vector. For 0 ≤ r ≤ 1 it is a contraction in the lecture convention, including collapse at r = 0 and no change at r = 1. For r > 1 it is a dilation. A negative r also reverses direction. Multiplying by a scalar remains linear even when the picture shrinks or reverses.

The lecture shear has A = [1,3;0,1], so T(x₁,x₂) = (x₁ + 3x₂,x₂). Points on the horizontal axis stay fixed. A point at height 2 moves 6 units horizontally, while its height is unchanged. The corners (0,0),(2,0),(2,2),(0,2) map to (0,0),(2,0),(8,2),(6,2), making a parallelogram.

@figure shear

This figure uses shear factor 1 for a compact diagram: (x₁,x₂) becomes (x₁ + x₂,x₂). Every horizontal strip moves by an amount proportional to its height. A shear changes angles and lengths but still preserves vector addition and scalar multiplication. Linearity is about these algebraic properties, not preservation of every geometric measurement.

## 7.5 Using superposition without finding the entire matrix

Suppose T(u) = (2,1) and T(v) = (-1,3), as in Course Exercise 1.8.17. Then T(3u) = 3(2,1) = (6,3), T(2v) = 2(-1,3) = (-2,6), and T(3u + 2v) = (6,3) + (-2,6) = (4,9). The known input vectors may have different coordinates from their outputs; keep u and T(u) distinct.

If a picture shows w = u + 2v, linearity gives T(w) = T(u) + 2T(v). Draw the two output displacements head to tail. Do not assume the coordinates of w are unchanged unless the transformation is known to be the identity.

## 7.6 Practice

**T1.** For T(x₁,x₂) = (x₁ + 2x₂, -x₁ + x₂), find T(3,-1), then find every input sent to (5,1).

**T2.** Decide whether S(x₁,x₂) = (x₁,x₂ + 3) and Q(x₁,x₂) = (x₁x₂,0) are linear. Give precise reasons.

**T3.** If T(u) = (1,2), T(v) = (3,-1), find T(2u - v), explaining the assumption needed.
''')
put('''# 8. Section 1.9 - The matrix of a linear transformation

Source correspondence: Combined PDF pages 71-79; exercise PDF page 12.

## 8.1 Standard basis vectors isolate one coordinate

The standard basis vector e_j has a 1 in coordinate j and 0 in every other coordinate. In ℝ^3, e₁ = (1,0,0), e₂ = (0,1,0), e₃ = (0,0,1). Every x = (x₁,x₂,x₃) equals x₁e₁ + x₂e₂ + x₃e₃. This is a coordinate identity: the coefficients simply reconstruct the entries.

If T is linear, T(x) = x₁T(e₁) + ... + x_nT(e_n). Therefore the standard matrix is A = [T(e₁) ... T(e_n)]. The output vectors become columns, not rows, because Ax combines columns with input weights. A has m rows when each T(e_j) has m entries, and n columns when there are n input coordinates.

**Theorem (supplied Theorem 10).** Every linear transformation ℝ^n → ℝ^m has a unique such matrix. Existence follows from the expansion just given. For uniqueness, if B also represents T, then its jth column is Be_j = T(e_j), so every column of B equals the corresponding column of A. Thus B = A. This is a proof for arbitrary dimensions, not a pattern guessed from one example.

## 8.2 Reading the matrix from a rule

For T(x₁,x₂) = (x₁ - 3x₂,-2x₁ + x₂,x₁), substituting e₁ = (1,0) gives (1,-2,1), and e₂ = (0,1) gives (-3,1,0). Hence:
''')
put(mtext([[1,-3],[-2,1],[1,0]]))
put('''The first row computes x₁ - 3x₂, the second computes -2x₁ + x₂, and the third computes x₁. A zero coefficient is an actual matrix entry; do not omit the 0 at the lower right. You may read coefficients directly once you understand why the column construction works.

## 8.3 Transformation reference with geometric meaning

The following matrices reproduce the types in the supplied geometric tables. Each is 2 × 2 and acts on a column (x₁,x₂). You can recover every matrix by applying the rule to e₁ and e₂.

**Reflection in the horizontal axis:** (x₁,x₂) ↦ (x₁,-x₂), matrix [1,0;0,-1]. **Reflection in the vertical axis:** (x₁,x₂) ↦ (-x₁,x₂), matrix [-1,0;0,1]. **Reflection in x₂ = x₁:** swap coordinates, matrix [0,1;1,0]. **Reflection in x₂ = -x₁:** swap and negate, matrix [0,-1;-1,0]. **Reflection in the origin:** negate both coordinates, matrix [-1,0;0,-1].

@figure reflect

**Horizontal scale by k:** (kx₁,x₂), matrix [k,0;0,1]. **Vertical scale by k:** (x₁,kx₂), matrix [1,0;0,k]. For the positive-scale tables, 0 < k < 1 contracts the named direction and k > 1 stretches it. Scaling both directions by k uses kI₂.

**Horizontal shear by k:** (x₁ + kx₂,x₂), matrix [1,k;0,1]. **Vertical shear by k:** (x₁,kx₁ + x₂), matrix [1,0;k,1]. The sign of k chooses the direction of the slant.

**Projection onto the horizontal axis:** (x₁,0), matrix [1,0;0,0]. **Projection onto the vertical axis:** (0,x₂), matrix [0,0;0,1]. A projection discards a coordinate and cannot later recover it uniquely.

@figure project

The supplied exercises also require rotations. For counterclockwise angle θ, the standard matrix is [cos θ,-sin θ;sin θ,cos θ]. The first column is the rotated unit vector (cos θ,sin θ); the second is its perpendicular companion (-sin θ,cos θ). A clockwise rotation uses negative θ. For θ = π/2 the columns are (0,1) and (-1,0); for θ = π they are (-1,0) and (0,-1). Angles in the course exercises are in radians: π radians is a half-turn, π/2 a quarter-turn, and 2π a full turn. The values at π/4 use cos(π/4) = sin(π/4) = 1/√2.

## 8.4 Composing geometric actions

When a rule says 'first S, then T,' apply S to e₁ and then T to that result; repeat with e₂. Put the two final outputs into columns. After matrix multiplication is introduced, the same process has matrix A_T A_S. The action performed first is the rightmost factor.

For the supplied Exercise 1.9.8, first reflect in the horizontal axis and then in x₂ = x₁. The first reflection sends (x₁,x₂) to (x₁,-x₂); the second swaps entries, giving (-x₂,x₁). Thus e₁ becomes e₂ and e₂ becomes -e₁. The matrix [0,-1;1,0] is a counterclockwise quarter-turn. Reversing the order produces a different rotation.

## 8.5 Onto asks about existence for every codomain vector

A mapping T: ℝ^n → ℝ^m is onto ℝ^m if every b in that declared codomain equals T(x) for at least one input x. In matrix language, Ax = b is consistent for every b ∈ ℝ^m. This is equivalent to the columns spanning ℝ^m and to a pivot in every row of A.

Being able to find an input for one specific b is insufficient. The map T(x₁,x₂) = (x₁,0) produces (3,0) but cannot produce (0,1), so it is not onto ℝ^2. It would be onto the horizontal axis if that were the declared codomain, but that is a different mapping specification.

## 8.6 One-to-one asks about collisions of inputs

A mapping is one-to-one when different inputs cannot produce the same output. Equivalently, each codomain vector has at most one preimage. Unreachable outputs are allowed in this definition. For a linear mapping, one-to-one is equivalent to Ax = 0 having only the trivial solution, to independent columns, and to a pivot in every column of A.

Here is the proof linking collisions to the homogeneous test. If Au = Av, then A(u - v) = 0. If only zero goes to zero, u - v = 0 and therefore u = v. Conversely, if a nonzero z satisfies Az = 0, then z and 0 are different inputs with the same output. So the mapping fails to be one-to-one.

@figure onto

The diagram shows projection. Two distinct inputs with the same first coordinate collide, and outputs with nonzero second coordinate are missed. Projection is neither one-to-one nor onto ℝ^2. It supplies a visible reason for both failures, which are logically separate.

## 8.7 Compare all four possibilities

The inclusion T: ℝ^2 → ℝ^3, T(a,b) = (a,b,0), has a pivot in each of its two columns. It is one-to-one because the input can be read back from the first two output entries. It is not onto ℝ^3 because outputs with nonzero third entry are impossible.

The map T: ℝ^3 → ℝ^2, T(a,b,c) = (a,b), has a pivot in each of its two rows. It is onto because every (a,b) is attained, but not one-to-one because c can vary freely. An invertible 2 × 2 scaling with nonzero factors is both. The zero map ℝ^2 → ℝ^2 is neither.

For an m × n matrix, onto requires m pivots and therefore n ≥ m. One-to-one requires n pivots and therefore m ≥ n. For a square matrix these conditions coincide. For rectangular matrices they need not. The lecture's 3 × 4 echelon example [1,-4,8,1;0,2,-1,3;0,0,0,5] is onto ℝ^3 but not one-to-one: it has three row pivots and one nonpivot input column.

## 8.8 Practice

**M1.** Find the standard matrix for T(a,b) = (2a + b,a - b,3b). Decide whether it is one-to-one and onto its declared codomain ℝ^3.

**M2.** Find the matrix for first reflecting in the vertical axis and then projecting onto the horizontal axis. Explain both lost information and attainable outputs.

**M3.** Give a matrix mapping ℝ^3 onto ℝ^2 that is not one-to-one, and a matrix mapping ℝ^2 one-to-one into ℝ^3 that is not onto. Justify by pivots.

# 9. Section 2.1 - Matrix operations

Source correspondence: Combined PDF pages 80-90; exercise PDF pages 13-14.

## 9.1 Entries, equality, and entrywise operations

If A is m × n, a_{ij} is its entry in row i, column j. The column a_j consists of a_{1j},...,a_{mj}. A diagonal entry has matching indices. A diagonal matrix is square and has zero entries off its main diagonal. An identity matrix is a diagonal matrix whose diagonal entries are all 1. A zero matrix can be any size; all its entries are zero.

Matrices are equal only if their dimensions match and every corresponding entry agrees. Addition and subtraction require equal dimensions and operate entrywise. Multiplying by a scalar scales every entry. For A = [1,-2;3,4] and B = [2,5;-1,0], A + B = [3,3;2,4], A - B = [-1,-7;4,4], and -2A = [-2,4;-6,-8]. These operations retain the original dimensions.

Addition is commutative and associative. A + 0 = A. Scalars distribute over a sum of matrices and a sum of scalars: r(A + B) = rA + rB and (r + s)A = rA + sA. Also r(sA) = (rs)A. Matching dimensions are part of every statement. A 2 × 3 matrix cannot be added to a 3 × 2 matrix just because both contain six entries.

## 9.2 Why matrix multiplication is defined differently

Suppose B transforms x into Bx, then A transforms that output into A(Bx). We want one matrix C that has the same effect. Each column b_j of B is the image of e_j after the first transformation, so the final image is Ab_j. Therefore C = AB has columns Ab₁,...,Ab_p.

If A is m × n and B is n × p, then AB is m × p. The matching n is the number of entries in each column of B, which A must be able to multiply. The output has m entries for each of the p input coordinate directions. Thus the mnemonic 'inside sizes agree, outside sizes give the answer' has a mathematical reason.

The entry formula is (AB)_{ij} = a_{i1}b_{1j} + ... + a_{in}b_{nj}. It multiplies a row by a column, not matching entries in place. Entrywise multiplication is a different operation and is not what AB denotes here.

## 9.3 Full lecture product: square times rectangular

Combined PDF pages 85-86 use A = [2,3;1,-5] and B = [4,3,6;1,-2,3]. A is 2 × 2, B is 2 × 3, so AB is 2 × 3. There are six entries to compute, and all six are shown.
''')
prod([[2,3],[1,-5]],[[4,3,6],[1,-2,3]])
put('''The other order BA is undefined here: B has three columns and A has two rows. Noncommutativity can therefore mean that one order is not even meaningful. For square matrices both orders exist, but their entries can still differ.

## 9.4 Associativity does not permit reordering

For compatible sizes, (AB)C = A(BC). This allows regrouping, not exchanging A and B. Acting on a vector, both sides perform C first, then B, then A. The column definition also proves the identity: the jth column of (AB)C is (AB)c_j = A(Bc_j), the jth column of A(BC).

The distributive laws are A(B + C) = AB + AC and (B + C)A = BA + CA. A scalar may be factored consistently: r(AB) = (rA)B = A(rB). Identity matrices have the appropriate side sizes: I_m A = A and A I_n = A when A is m × n.

For A = [1,1;0,1] and B = [1,0;0,2], AB = [1,2;0,2] whereas BA = [1,1;0,2]. Applying B first doubles vertical coordinates before the shear mixes them horizontally; reversing the order changes the result. Hence AB = BA is a special property, called commuting, not a general multiplication law.

## 9.5 Zero products and failed cancellation

Nonzero matrices can multiply to zero. Let A = [1,0;0,0] and B = [0,0;0,1]. Both are nonzero, but AB = 0 because A removes the output direction produced by B. Therefore AB = 0 does not imply A = 0 or B = 0.

For the same A, take C = 0. Then AB = AC even though B ≠ C. You cannot cancel A without an appropriate invertibility assumption. Matrix 'division' is not an operation that can be used without checking such assumptions. Similarly, (A + B)^2 expands to A^2 + AB + BA + B^2; it becomes A^2 + 2AB + B^2 only if A and B commute.

## 9.6 Powers and repeated transformations

For square A and positive integer k, A^k means k copies multiplied in order. It does not raise each entry to the kth power. For A = [1,1;0,1], A^2 = [1,2;0,1] because two horizontal shears add their effects. Its top right entry is 2, even though 1^2 = 1. By convention A^0 = I of the matching size. Powers with negative exponents require invertibility and are discussed through inverses.

## 9.7 Transpose switches rows and columns

For an m × n matrix A, A^T is n × m and has (A^T)_{ij} = a_{ji}. For A = [1,2,3;4,5,6], the transpose is [1,4;2,5;3,6]. A transpose is not an inverse: it changes the arrangement and size, not necessarily the effect of a transformation in reverse.

The supplied transpose identities are (A^T)^T = A, (A + B)^T = A^T + B^T, (rA)^T = rA^T, and (AB)^T = B^T A^T. The product order reverses. If A is m × n and B is n × p, (AB)^T is p × m. The product B^T A^T has size (p × n)(n × m), which matches; A^T B^T often fails even the size test.

A proof of the last identity examines entry i,j. Entry i,j of (AB)^T is entry j,i of AB, namely Σ over k of a_{jk}b_{ki}. Entry i,j of B^T A^T is Σ over k of (B^T)_{ik}(A^T)_{kj} = Σ over k of b_{ki}a_{jk}, the same real-number sum. Equal dimensions and entrywise equality prove the identity.

## 9.8 Practice

**O1.** Compute AB and BA for A = [1,2;0,1], B = [2,0;1,3]. Explain their difference.

**O2.** Compute the transpose of AB in O1 and verify B^T A^T gives the same matrix.

**O3.** Construct two nonzero 2 × 2 matrices whose product is zero. Explain why they disprove a cancellation claim.

**O4.** If A is 3 × 2 and B is 2 × 4, state the sizes of AB, (AB)^T, and B^T A^T. Is BA defined?

# 10. Section 2.2 - The inverse of a matrix

Source correspondence: Combined PDF pages 91-100; exercise PDF pages 15-16.

## 10.1 Undoing a transformation

An inverse reverses the effect of a square matrix on every input. An n × n matrix A is invertible if an n × n matrix C satisfies both AC = I_n and CA = I_n. This C is A^(-1). A noninvertible square matrix is singular; an invertible one is nonsingular. In this course definition, an ordinary two-sided inverse is only defined for square matrices.

The notation A^(-1) is not formed by taking reciprocals of entries. The identity conditions involve matrix multiplication. A projection is singular because it sends many different inputs to the same output; no inverse can know which original input to restore. A nonzero uniform scaling is invertible: scaling by r is undone by scaling by 1/r.

If B and C are both inverses of A, B = BI = B(AC) = (BA)C = IC = C. Thus the inverse, when it exists, is unique. Each equality has a reason: identity, inverse condition, associativity, inverse condition, identity. This short chain is a model university proof.

@figure inverse

The figure shears by (x₁ + x₂,x₂). Given the output y, subtract y₂ from y₁ to recover the input: (y₁ - y₂,y₂). The forward matrix [1,1;0,1] and backward matrix [1,-1;0,1] multiply in either order to I₂.

## 10.2 Deriving the 2 × 2 formula

Let A = [a,b;c,d]. Seek a matrix that removes the off-diagonal effects. Try C = [d,-b;-c,a]. Multiplying gives AC = [ad - bc, -ab + ba; cd - dc, -cb + da] = (ad - bc)I₂. Multiplying in the reverse order also gives (ad - bc)I₂. If δ = ad - bc is nonzero, divide C by δ to obtain the inverse.

@eq A^(-1) = (1/(ad - bc)) [d,-b; -c,a], provided ad - bc ≠ 0.

Here a,b,c,d are the four entries of A. The scalar ad - bc is its 2 × 2 determinant. The formula swaps the two diagonal entries, negates the two off-diagonal entries, and divides every resulting entry by the determinant. The order of ad and bc matters. The condition is ad - bc ≠ 0, not ab - cd ≠ 0.

Why is A singular when ad - bc = 0? If the first row is nonzero, z = (-b,a) is a nonzero vector and Az = (0,ad - bc) = 0. An inverse would imply z = A^(-1)0 = 0, a contradiction. If the first row is zero and the second is nonzero, use z = (-d,c). If both rows are zero, every nonzero vector is sent to zero. These cases establish the determinant condition without dividing by a possibly zero entry.

## 10.3 Numerical examples and direct verification

For A = [8,3;5,2], δ = 16 - 15 = 1 and A^(-1) = [2,-3;-5,8]. The product AA^(-1) has entries 16 - 15 = 1, -24 + 24 = 0, 10 - 10 = 0, -15 + 16 = 1. The reverse product also gives I₂.

For A = [3,1;7,2], δ = 6 - 7 = -1, so A^(-1) = [-2,1;7,-3]. The negative determinant changes every entry after division. Check: [3,1;7,2][-2,1;7,-3] = [1,0;0,1]. For A = [1,2;2,4], δ = 0 and the formula is unavailable. The second column is twice the first, giving a nonzero input (-2,1) mapped to zero; this explains the failure.

## 10.4 Solving Ax = b by an inverse

Assume A is invertible. Left-multiply Ax = b by A^(-1): A^(-1)Ax = A^(-1)b, so Ix = A^(-1)b and x = A^(-1)b. This supplies a solution because A(A^(-1)b) = b. It supplies the only solution because any solution must equal that expression. The multiplication must be on the left to bring A^(-1) beside A in the correct order.

For [8,3;5,2]x = (2,-1), x = [2,-3;-5,8](2,-1) = (7,-18). Verify 8(7) + 3(-18) = 2 and 5(7) + 2(-18) = -1. When several right-hand sides share one A, an inverse or a single reduction with multiple appended columns can solve them together. Computing an inverse solely for one system is not always the most efficient method; ordinary elimination already solves it.

## 10.5 Elementary matrices turn row operations into products

An elementary matrix is obtained from I by performing exactly one elementary row operation. Left-multiplying a compatible A by E performs that same operation on A. For example, E = [1,0,0;0,1,0;-4,0,1] replaces row 3 of A by row 3 minus four times row 1. This follows directly from the row-column multiplication rule: the third output row combines input rows with weights -4,0,1.

Swapping rows 1 and 2 of I₃ gives [0,1,0;1,0,0;0,0,1]. Scaling row 3 by 5 gives [1,0,0;0,1,0;0,0,5]. Each elementary matrix is invertible because its row operation is reversible. Their inverses respectively add four times row 1 to row 3, swap the same rows again, and scale row 3 by 1/5. Right multiplication would act on columns and is not the row-operation model used in this theorem.

## 10.6 Why augmenting with I finds the inverse

**Theorem (supplied Theorem 7).** A square matrix A is invertible exactly when it is row equivalent to I. A sequence of row operations that reduces A to I transforms I into A^(-1).

If the row operations correspond to E₁,...,E_p, their total effect is E_p ... E₁ A = I. Write E = E_p ... E₁. Since all elementary matrices are invertible, E is invertible and A = E^(-1), so E = A^(-1). Applying the same operations to I gives EI = E = A^(-1). Therefore [A | I] reduces to [I | A^(-1)]. The augmented columns are carried along exactly as right-hand sides were in solving systems.

If A is invertible, Ax = b is solvable for every b, so A has a pivot in every row. Since it is square, there is also a pivot in every column, and RREF(A) = I. This proves the other direction and connects inversion with the earlier pivot criteria.

## 10.7 A larger inverse with every row operation

There is a source discrepancy on Combined PDF page 98. The displayed initial A has first row (0,1,0), but its augmented matrix, subsequent steps, and page 99 verification use (0,1,2). The following example explicitly uses the latter matrix A = [0,1,2;1,0,3;4,-3,8], which is the matrix actually reduced in the slides. Its result is not asserted to invert the differently printed initial matrix.
''')
inv([[0,1,2],[1,0,3],[4,-3,8]])
put('For comparison, the matrix literally printed in the initial display, with first row (0,1,0), has a different inverse. Here is its independently computed reduction, preserving that version of the data.')
inv([[0,1,0],[1,0,3],[4,-3,8]])
put('''## 10.8 Recognizing failure and finding selected columns

For a singular A, reduction of [A | I] fails to make the left block I. The right block is then not an inverse, regardless of how many entries look convenient. One missing coefficient pivot is enough to establish noninvertibility. For A = [1,2;2,4], R₂ ← R₂ - 2R₁ creates [0,0 | -2,1]. Its left zero row proves a missing pivot; do not reinterpret all four columns as the coefficients of a different matrix and continue until the whole array has pivots.

The jth column of A^(-1) is the solution of Ax = e_j. To find only that column, reduce [A | e_j]; the other inverse columns are unnecessary. The exercise collection uses this idea for 3 × 3 matrices. Reducing [A | b₁ ... b_k] similarly solves several systems simultaneously. Each appended column remains tied to its own right-hand side.

## 10.9 Inverse identities and why order reverses

For invertible square matrices of matching size, (A^(-1))^(-1) = A, (AB)^(-1) = B^(-1)A^(-1), and (A^T)^(-1) = (A^(-1))^T. For the product identity, (AB)(B^(-1)A^(-1)) = A(BB^(-1))A^(-1) = I, and the reverse product is also I. You undo the last action first, just as a shear followed by a stretch is undone by undoing the stretch and then the shear.

For the transpose identity, transpose AA^(-1) = I to get (A^(-1))^T A^T = I. Transpose the other inverse equation to get A^T(A^(-1))^T = I. Thus both defining equations hold. There is no general identity (A + B)^(-1) = A^(-1) + B^(-1); even 1 × 1 matrices give a counterexample: (1 + 1)^(-1) = 1/2, whereas 1^(-1) + 1^(-1) = 2.

## 10.10 Practice

**N1.** Find and verify the inverse of [2,1;5,3]. Use it to solve Ax = (1,2).

**N2.** Find the inverse of [1,1,0;0,1,1;0,0,1] using [A | I].

**N3.** Find the third column of the inverse of the matrix in N2 without computing the other columns.

**N4.** Prove that if A is invertible and AB = AC, then B = C. Give a counterexample when A is singular.

# 11. Writing proofs and solving unfamiliar questions

## 11.1 Translate the request before calculating

'Is b in a span?' asks for existence of weights, so build [A | b]. 'Are these vectors independent?' asks whether Ax = 0 has only zero as a solution. 'Does T map onto its codomain?' asks for a row pivot for every output coordinate. 'Is T one-to-one?' asks for a column pivot for every input coordinate. 'Find the standard matrix' asks for T(e_j) as columns. 'Find an inverse' asks for [A | I] to become [I | C], then verification.

A question can ask for several of these at once. For example, if A is 3 × 4 with three pivots, it is onto ℝ^3 and its columns span ℝ^3. It is not one-to-one and its columns are dependent. Every b has infinitely many solutions because every b is consistent and there is one free input variable. A single pivot count supports all these statements, but each needs its own interpretation.

## 11.2 A practical proof pattern

First state the assumptions. Next state the target in the relevant definition. Then use a theorem whose assumptions are satisfied. Finally connect the result back to the target. For instance, to prove that adding a vector in a span does not change the span, suppose w = c₁v₁ + ... + c_pv_p. Every combination of the original vectors remains available after w is added, proving one inclusion. Conversely, a combination of the enlarged collection can replace its w term by that expression, producing a combination of the original vectors. Both inclusions prove equality of the spans.

A counterexample must satisfy all stated assumptions. To disprove 'a consistent system has a unique solution,' use x₁ + x₂ = 1. It is consistent because (1,0) works, but (0,1) is a different solution. An inconsistent system would not be a valid counterexample to that particular claim, because it violates the assumption of consistency.

## 11.3 True/false answers need mathematical evidence

Consider 'A matrix with a pivot in every column has columns spanning its codomain.' It is false for A = [1,0;0,1;0,0]. Each column has a pivot, but b = (0,0,1) cannot be produced. The missing row pivot is the precise reason. The counterexample states dimensions, verifies the hypothesis, and exhibits a failing output.

Now consider 'If Ax = 0 has a nontrivial solution, then the columns of A are dependent.' This is true by the definition of column dependence: Ax is the weighted column combination, and a nontrivial x gives weights not all zero. The explanation names the definition and connects both pieces of language.

## 11.4 Integrated transfer practice

**G1.** Let A = [1,2,0;0,1,1]. For b = (3,2), solve Ax = b; solve Ax = 0; decide spanning, independence, onto, and one-to-one. Explain how the solution sets are related.

**G2.** Let S(x₁,x₂) = (x₁ + 2x₂,x₂) and R(x₁,x₂) = (-x₂,x₁). Find the matrix of R after S, compute the image of (1,2), and find an inverse rule.

**G3.** Suppose A is 3 × 3 and for every b ∈ ℝ^3 there is at least one solution of Ax = b. Prove that the solution is always unique and A is invertible. Explain which part of the reasoning uses the fact that A is square.

# 12. Worked answers to textbook practice

These answers correspond to every practice question in this textbook. Course exercise answers are in the separate workbook. Calculations use the definitions and methods just developed; alternate equivalent parameters are acceptable.

## 12.1 Foundations

**F1.** Inside the parentheses, 3 - 5 = -2. Hence -2(-2) = 4. For the fractions, 1/2 - 5/6 = 3/6 - 5/6 = -2/6 = -1/3. The complete result is 4 - 1/3 = 11/3. The negative sign before the 2 multiplies the whole parenthesis.

**F2.** Multiply both sides by 5: 2(x - 3) = 20. Divide by 2: x - 3 = 10. Add 3: x = 13. In the original equation, 2(13 - 3)/5 = 20/5 = 4. Every step used the same operation on both sides with a nonzero divisor.

**F3 and S11.** The same system appears twice so that you can compare the substitution and matrix methods. Here is the complete matrix solution; the answer must satisfy both original equations.
''')
solve([[1,2,7],[3,-1,7]])
put('''**F4.** x₂ is the variable labeled 2, while x^2 multiplies x by itself. Existence means at least one list works; uniqueness adds the requirement that no different list works. A line of solutions satisfies existence but fails uniqueness.

**F5.** The equations x + y = 1 and x - y = 1 share (1,0). However, (0,1) satisfies the first and fails the second. Therefore their solution sets differ. One common point does not establish equality of two sets.

## 12.2 Systems and reduction

**S12, first system.** Subtract twice row 1 from row 2. The equations become x₁ + x₂ = 2 and 0 = 1. The latter is impossible, so there is no solution. For the second system the same operation produces 0 = 0. Set x₂ = t; then x₁ = 2 - t. Every (2 - t,t) works, and every solution must have this form because the first equation determines x₁ once x₂ is chosen.

**S13.** The replacement R₂ ← R₂ - 3R₁ is undone by R₂ ← R₂ + 3R₁, with row 1 retained. Multiplying by 0 erases the original row; infinitely many different rows become zero and there is no reciprocal multiplier to recover them.

**R1.** The nonzero rows come first, and their leading entries are in columns 1 and 3. Each leading entry is 1 and has only zeros elsewhere in its column. The matrix is therefore RREF and also REF. The 2 in a nonpivot column is allowed.

**R2.** Reduce the two-row augmented system. Its second equation repeats twice the first. There are two free variables, so the solution is a plane in ℝ^3.
''')
solve([[1,2,-1,4],[2,4,-2,8]])
put('''**R3.** Three pivots in three rows give a row pivot everywhere. Thus every b ∈ ℝ^3 is attainable. There are five unknowns but only three pivots, leaving two free variables. Since every system is consistent, each has infinitely many solutions, never a unique one.

## 12.3 Vectors and Ax = b

**V1.** 4u = (4,-8) and -3v = (-6,15). Add entrywise to get (-2,7). The factor 4 stretches u without reversing it; the factor -3 stretches v and reverses its direction. Check the second entry: -8 + 15 = 7.

**V2.** Solve c₁ + 2c₂ = 5 and c₁ - c₂ = 1. Subtract the second equation from the first: 3c₂ = 4, so c₂ = 4/3. Then c₁ = 1 + 4/3 = 7/3. Check the weighted sum: (7/3)(1,1) + (4/3)(2,-1) = (15/3,3/3) = (5,1), so membership holds.

**V3.** The second generator is 3/2 times the first. Every combination is therefore a multiple of (2,4,0), a line through the origin. If (1,0,0) were on the line, its first entry would force the multiplier to 1/2, which would make the second entry 2 rather than 0. It is outside the span.

**V4.** Let a,b be batch amounts. The equations are 2a + 3b = 13 and 5a + b = 13. From the second, b = 13 - 5a. Substitute into the first: 2a + 39 - 15a = 13, so a = 2. Then b = 3. Both are nonnegative, and 2(2) + 3(3) = 13 and 5(2) + 3 = 13.

**A1.** The vector equation is x₁(2,1) + x₂(-1,4) = (3,5). The matrix equation is [2,-1;1,4](x₁,x₂) = (3,5). Solving the system gives the following.
''')
solve([[2,-1,3],[1,4,5]])
put('''**A2.** Two row pivots mean onto ℝ^2 and existence for every b. Three columns with two pivots leave a free coordinate. Every b therefore has infinitely many inputs. Onto does not guarantee uniqueness for a rectangular matrix.

**A3.** The sizes are (2 × 3)(3 × 1) = 2 × 1. By rows, the entries are 1(2) + 2(1) + 3(-1) = 1 and 0(2) - 1(1) + 4(-1) = -5. By columns, 2(1,0) + (2,-1) - (3,4) = (1,-5), the same result.

## 12.4 Homogeneous systems and independence

**H1.** Choose x₂ = s and x₃ = t. Then x₁ = 2s - t, so x = s(2,1,0) + t(-1,0,1). Both direction vectors satisfy x₁ - 2x₂ + x₃ = 0. Choosing s = 1,t = 0 gives the nontrivial solution (2,1,0). Conversely, the single equation forces exactly the displayed first coordinate for every pair of free coordinates.

**H2.** The equation gives x₁ = 5 + 2s - t, x₂ = s, x₃ = t. Thus x = (5,0,0) + s(2,1,0) + t(-1,0,1). Substitution gives 5 + 2s - t - 2s + t = 5 for arbitrary s,t. The new plane is a translate of H1 by (5,0,0); it is parallel and does not pass through the origin.

**H3.** A(p - q) = Ap - Aq = b - b = 0, so the difference is homogeneous. If zero is the only homogeneous solution, p - q = 0, forcing p = q. Thus any consistent system with this coefficient matrix has exactly one solution.

**I1.** There are three vectors in ℝ^2, so dependence follows from the too-many-vectors theorem. More explicitly, 2(1,2) - (2,4) + 0(0,1) = 0. The weights (2,-1,0) are not all zero, so they give a valid dependence relation. Some weights may be zero.

**I2.** Use the vectors as columns and solve the homogeneous system.
''')
ind([[1,0,1],[0,1,1],[1,1,0]])
put('''**I3.** Any zero combination of vectors in the subset can be extended to a combination of the full collection by assigning coefficient 0 to every omitted vector. Full independence forces all those coefficients, including the subset coefficients, to zero. For a superset of a dependent collection, extend one known nontrivial relation by assigning zeros to every added vector. It remains nontrivial, proving dependence.

**I4.** Both (1,0) and (2,0) are nonzero, but 2(1,0) - (2,0) = 0 has nonzero weights. Thus excluding zero is necessary for independence but does not guarantee it.

## 12.5 Transformations and standard matrices

**T1.** T(3,-1) = (3 - 2,-3 - 1) = (1,-4). To find the input for (5,1), solve x₁ + 2x₂ = 5 and -x₁ + x₂ = 1. Add the equations: 3x₂ = 6, so x₂ = 2 and x₁ = 1. The answer is unique because both input columns have pivots. Check T(1,2) = (5,1).

**T2.** S is not linear because S(0,0) = (0,3) ≠ 0. Q sends zero to zero, but Q((1,0) + (0,1)) = Q(1,1) = (1,0), whereas Q(1,0) + Q(0,1) = (0,0). It fails preservation of addition and is not linear.

**T3.** Assuming T is linear, T(2u - v) = 2T(u) - T(v) = (2,4) - (3,-1) = (-1,5). Without linearity, knowledge of only two images would not determine the image of their combination.

**M1.** T(e₁) = (2,1,0), T(e₂) = (1,-1,3), so A = [2,1;1,-1;0,3]. The two columns are independent: the third row of Ax = 0 forces x₂ = 0 and the first then forces x₁ = 0. Therefore T is one-to-one. Two columns provide at most two pivots, so not all three rows can have pivots; T is not onto ℝ^3. For example, (0,0,1) would force x₂ = 1/3, x₁ = 1/3 from the second row, contradicting the first output 0.

**M2.** The reflection gives (-a,b), then projection gives (-a,0). The standard matrix is [-1,0;0,0]. All horizontal-axis outputs occur by choosing a appropriately; no output with nonzero second coordinate occurs. All inputs with the same a collide regardless of b, so the map is neither onto ℝ^2 nor one-to-one.

**M3.** [1,0,0;0,1,0] has a pivot in every row, but column 3 is nonpivot. It maps ℝ^3 onto ℝ^2 with a free third input. The matrix [1,0;0,1;0,0] has pivots in both columns but lacks a third row pivot. It is one-to-one into ℝ^3 and misses every output with nonzero third coordinate.

## 12.6 Operations and inverses

**O1.** Each order requires a separate row-column calculation.
''')
prod([[1,2],[0,1]],[[2,0],[1,3]])
prod([[2,0],[1,3]],[[1,2],[0,1]])
put('''The products are [4,6;1,3] and [2,4;1,5], respectively, so AB ≠ BA.

**O2.** Transposing AB gives [4,1;6,3]. With B^T = [2,1;0,3] and A^T = [1,0;2,1], the product B^T A^T has entries 2 + 2 = 4, 1, 6, 3, giving [4,1;6,3]. This verifies the reverse-order identity in this example.

**O3.** Let A = [1,0;0,0] and B = [0,0;0,1]. Every row-column sum in AB is zero, although both factors have an entry 1. Thus AB = A0 but B ≠ 0; cancellation of the singular left factor would be invalid.

**O4.** AB is 3 × 4, its transpose is 4 × 3, and B^T A^T has size (4 × 2)(2 × 3) = 4 × 3. BA would require the four columns of B to match the three rows of A, so BA is undefined.

**N1.** The determinant is 2(3) - 1(5) = 1, so the inverse is [3,-1;-5,2]. Multiplying A by it gives [6 - 5,-2 + 2;15 - 15,-5 + 6] = I₂; reversing the factors also gives I₂. For b = (1,2), x = (3 - 2,-5 + 4) = (1,-1). Check A(1,-1) = (1,2).

**N2.** Reduce the full augmented array, carrying three right-hand sides together.
''')
inv([[1,1,0],[0,1,1],[0,0,1]])
put('''**N3.** Solve Ax = e₃. The last row gives x₃ = 1. The second gives x₂ + 1 = 0, so x₂ = -1. The first gives x₁ - 1 = 0, so x₁ = 1. Therefore the third inverse column is (1,-1,1), agreeing with N2. The equations ensure A times this column equals e₃.

**N4.** Left-multiply AB = AC by A^(-1). Associativity yields (A^(-1)A)B = (A^(-1)A)C, so B = C. If A = [1,0;0,0], B = [0,0;0,1], C = 0, then AB = AC = 0 although B ≠ C. The invertibility hypothesis is essential.

## 12.7 Integrated practice

**G1.** The equations are x₁ + 2x₂ = 3 and x₂ + x₃ = 2. Let x₂ = t. Then x₁ = 3 - 2t and x₃ = 2 - t, giving x = (3,0,2) + t(-2,1,-1). Substitution gives 3 - 2t + 2t = 3 and t + 2 - t = 2. For the homogeneous system the same reasoning gives x = t(-2,1,-1), and A(-2,1,-1) = 0. The first solution set is a translate of the second. A has a pivot in each of its two rows, so columns span ℝ^2 and T is onto. It has three columns and two pivots, so its columns are dependent and T is not one-to-one.

**G2.** S has matrix [1,2;0,1], and R has matrix [0,-1;1,0]. Apply S first: (a,b) ↦ (a + 2b,b), then R: (-b,a + 2b). The composite matrix is [0,-1;1,2]. At (1,2) the output is (-2,5). To undo it, let (y₁,y₂) = (-b,a + 2b). Then b = -y₁ and a = y₂ + 2y₁. The inverse rule is (2y₁ + y₂,-y₁), with matrix [2,1;-1,0]. Both products with [0,-1;1,2] give I₂, and the inverse sends (-2,5) to (1,2).

**G3.** Solvability for every b gives a pivot in every row. There are three rows, hence three pivots. Since there are also exactly three columns, each column has a pivot, leaving no free variables. Therefore every consistent system has a unique solution. The RREF of a square matrix with pivots in all columns is I₃, so A is row equivalent to I₃ and is invertible by the supplied inverse theorem. Squareness converts every-row pivots into every-column pivots; that step fails for a 3 × 4 matrix.

# 13. Glossary, formulas, and theorem reference

## 13.1 Glossary

**Augmented matrix:** coefficient columns together with one or more right-hand-side columns. **Basic variable:** a variable whose coefficient column contains a pivot. **Coefficient:** a fixed number multiplying an unknown. **Codomain:** declared output space of a function. **Consistent:** possessing at least one solution. **Dependent:** admitting a zero combination with weights not all zero. **Domain:** allowed input space. **Echelon form:** zero rows last, leading entries moving right, zeros below leading entries. **Elementary matrix:** identity after one elementary row operation. **Equivalent systems:** systems with the same solution set.

**Free variable:** a nonpivot coefficient variable that can be chosen arbitrarily in a consistent system. **Homogeneous:** having zero right-hand side. **Identity matrix:** square matrix with diagonal 1 and off-diagonal 0. **Image:** output of a specified input. **Independent:** only the all-zero weights combine the vectors to zero. **Inverse:** square matrix undoing another matrix in both multiplication orders. **Linear combination:** weighted sum of vectors. **Linear transformation:** function preserving addition and scalar multiplication.

**Matrix dimensions:** rows × columns. **Nontrivial solution:** a solution vector other than zero. **One-to-one:** different inputs always have different outputs. **Onto:** every codomain vector is attained. **Parametric vector form:** a fixed vector plus arbitrary scalar multiples of fixed direction vectors. **Particular solution:** any one fixed solution of Ax = b. **Pivot column:** original matrix column corresponding to a leading entry in its echelon form. **Pivot position:** location corresponding to a leading 1 in RREF. **Range:** set of outputs actually attained.

**Reduced echelon form:** echelon form with leading 1s, each alone as a nonzero entry in its column. **Row equivalent:** connected by elementary row operations. **Scalar:** real-number multiplier in this book. **Singular:** square and not invertible. **Solution set:** all lists satisfying every equation. **Span:** all linear combinations of the listed generators. **Standard matrix:** matrix whose columns are images of standard basis vectors. **Transpose:** matrix with rows and columns exchanged. **Trivial solution:** zero input in a homogeneous system.

## 13.2 Formula reference

**Vectors:** cu + dv is computed entrywise. Span{v₁,...,v_p} = {c₁v₁ + ... + c_pv_p : c_i ∈ ℝ}. For A = [a₁ ... a_n], Ax = x₁a₁ + ... + x_n a_n and entry i is a_{i1}x₁ + ... + a_{in}x_n.

**Solutions:** homogeneous solutions satisfy Ax = 0. A consistent nonhomogeneous solution set is x = p + s₁v₁ + ... + s_kv_k, where Ap = b and Av_j = 0. Each free variable needs its own parameter.

**Products:** (m × n)(n × p) gives m × p. Entry (i,j) of AB is Σ from k=1 to n of a_{ik}b_{kj}. The standard matrix of T is [T(e₁) ... T(e_n)]. The matrix of first S then T is A_T A_S.

**Transpose:** (A^T)^T = A; (A + B)^T = A^T + B^T; (rA)^T = rA^T; (AB)^T = B^T A^T, with matching dimensions throughout.

**Inverses:** for A = [a,b;c,d], det A = ad - bc and A^(-1) = [d,-b;-c,a]/(ad - bc) when det A ≠ 0. For larger square A, [A | I] reduces to [I | A^(-1)] exactly when A is invertible. When invertible, Ax = b has x = A^(-1)b. Also (AB)^(-1) = B^(-1)A^(-1), (A^T)^(-1) = (A^(-1))^T, and (A^(-1))^(-1) = A.

**Plane transformations:** horizontal reflection [1,0;0,-1]; vertical reflection [-1,0;0,1]; coordinate swap [0,1;1,0]; reflection in negative diagonal [0,-1;-1,0]; origin reflection -I₂; horizontal scale [k,0;0,1]; vertical scale [1,0;0,k]; horizontal shear [1,k;0,1]; vertical shear [1,0;k,1]; horizontal projection [1,0;0,0]; vertical projection [0,0;0,1]; counterclockwise rotation [cos θ,-sin θ;sin θ,cos θ].

## 13.3 Theorem correspondence

Combined PDF Chapter 1 numbers its theorems continuously: Theorem 1 is uniqueness of RREF (PDF page 13); Theorem 2 is consistency and uniqueness (26); Theorem 3 equates system, vector, and matrix equations (39); Theorem 4 equates row pivots, spanning, and existence for every b (40); Theorem 5 gives matrix-vector linearity (42-43); Theorem 6 describes translated homogeneous solution sets (52); Theorem 7 characterizes dependence (58-59); Theorem 8 treats more vectors than entries (61-62); Theorem 9 treats collections containing zero (62); Theorem 10 gives the standard matrix (71-72); Theorem 11 equates one-to-one behavior with the trivial homogeneous solution (78-79); Theorem 12 equates onto with spanning and one-to-one with independence (79).

The Chapter 2 numbering restarts: Theorem 1 states addition and scalar laws (82-83); Theorem 2 states product laws (87-88); Theorem 3 states transpose identities (89-90); Theorem 4 gives the 2 × 2 inverse condition (92); Theorem 5 gives the unique solution A^(-1)b (92); Theorem 6 gives inverse identities (93); Theorem 7 equates invertibility with row equivalence to identity (96-97). Use both the course section and theorem number to identify a theorem unambiguously.

## 13.4 Common mistakes and their repairs

A pivot in every row answers an existence question for all right-hand sides. A pivot in every column answers uniqueness of inputs. Write the words 'row/output/existence' and 'column/input/uniqueness' beside a rectangular matrix before deciding.

A free coefficient variable yields infinitely many solutions only when the system is consistent. First search for an impossible row. A zero row 0 = 0 adds no constraint; a row 0 = 1 rules out all solutions.

A vector equation uses the supplied vectors as columns, not rows. The unknown weights become input entries. Original pivot columns are found by their indices; reduced columns generally have different entries and should not be substituted as the original vectors.

A zero vector in a collection guarantees dependence; a nonzero vector does not guarantee independence of a collection. A dependence relation needs weights not all zero. A theorem about all inputs needs a general proof; a failed universal statement needs only one valid counterexample.

Matrix multiplication is row by column, not entrywise. Inner dimensions must match. You may regroup associative products but may not reorder factors. Transpose and inverse reverse the order of products. Cancellation needs an invertible factor in the correct position.

Inversion requires a square matrix. For a 2 × 2 matrix check ad - bc before dividing. For row reduction carry the whole identity block with every operation. Verify against the original A, especially when the source contains a typographical discrepancy.

# 14. Sources, scope, and verification notes

## 14.1 Section correspondence

The supplied Combined PDF has lecture sections at physical PDF pages 1-11 (1.1), 12-27 (1.2), 28-36 (1.3), 37-43 (1.4), 44-52 (1.5), 53-62 (1.7), 63-70 (1.8), 71-79 (1.9), 80-90 (2.1), and 91-100 (2.2). Selected worked answers occupy pages 101-116. These are physical PDF page numbers, not the printed slide numbers.

The Exercise PDF pages are mapped in the companion workbook. Its full readable question inventory is solved there, with the two truncated question continuations identified. Section 1.4 questions 33-34 and Section 1.9 questions 31-32 are mentioned by printed group directions but their statements are absent from the supplied scans; they are not silently invented. The later exam cheat sheet is outside these two volumes.

## 14.2 Source discrepancies and assumptions

The inverse example mismatch on Combined PDF page 98 is preserved and explained in Chapter 10, with both matrices independently inverted. The nonhomogeneous slide on page 48 labels its augmented block [A 0] although the actual constants are b = (7,-1,-4); the computation is of [A b]. The phrase 'plane' for s u + t v requires u,v independent if it is to mean a genuine two-dimensional plane; dependent directions instead produce a line or {0}. Those assumptions are made explicit here.

All source pages were visually reviewed, alongside text extraction for the lectures. No missing exercise continuation has been reconstructed from a different edition. Original pedagogical explanations, diagrams, practice questions, and their answers were authored for this resource. Mathematical identities were justified with the assumptions stated. Exact computational checks accompany generated reductions: the row-operation product maps the original matrix to its reduced matrix; particular and direction vectors satisfy the original systems; products agree by two constructions; inverse products equal I in both orders. These checks support arithmetic accuracy without replacing the written reasoning.

## 14.3 A complete solution is more than a final vector

A university solution identifies the mathematical request, records the data in the right form, shows valid operations, interprets the pivots or parameters, and returns to the question's wording. Verification tests the answer against the original data. The purpose of this book is to make that chain understandable enough that the method can be carried to an unfamiliar problem.
''')
(SRC/'MATH2255-Complete-Beginner-Textbook.md').write_text('\n'.join(B))
(SRC/'textbook-computation-checks.json').write_text(json.dumps(CHECKS,indent=2))
print('Textbook words',len(' '.join(B).split()),'exact checks',len(CHECKS))
