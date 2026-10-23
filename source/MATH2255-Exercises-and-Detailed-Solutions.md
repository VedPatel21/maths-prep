# MATH 2255 - Complete Exercise Workbook and Worked Solutions

Companion to Linear Algebra Made Understandable

This volume preserves the supplied exercise pages, organized by section, and gives a numbered answer for each complete visible question. Original question numbers are retained, including all visible subparts. The source is Exercises_Merged.pdf (16 physical PDF pages). Selected course solutions are from physical pages 101-116 of Heli-exam_prep_Combined.pdf.

**Coverage boundary.** There are 337 complete numbered questions and two cut-off numbered questions in the supplied scans. The incomplete entries are 1.2.41 and 2.1.43; their missing continuations are identified at their positions. Printed directions also mention 1.4.33-34 and 1.9.31-32, whose actual statements are absent. No unseen continuation or absent statement is invented. Exercise 2.1.14 refers to a cost matrix in an example not supplied; its requested structural interpretation can still be fully answered from the description in the question.

Computations and proofs here are independently written teaching solutions. A source cross-check label means the matching supplied selected solution was used to validate the result, not that all wording or steps are official. Full row reductions may choose different valid operations from those shown in the source. Exact fractions are retained. For parametric answers, different symbols or nonzero rescalings of directions may describe the same set.

# Contents

@toc

# Reading the worked solutions

The original scans supply the question statements. The answers restate the mathematical task and then explain the method. The displayed matrices after row operations are full updated matrices, not unrecorded leaps. After a reduction, the answer translates the rows into equations, identifies the free choices, and verifies against the original entries. For independence, the unknowns are the weights of the vectors. For a range or span question, the unknowns are weights producing the target output.

When an exercise asks only for existence, an answer may show more reduction than strictly necessary to make the reasoning self-contained. You may stop a hand calculation once a contradiction or the required pivot information is established. When an exercise asks for no full solution, its answer below stops at that decision and explains why it is sufficient.

Proof answers state the assumptions and connect them with the definitions. A false universal statement is accompanied by an explicit counterexample or a precise failure of its definition. A true/false label by itself is never the justification.


# Section 1.1 - Systems of linear equations


Original question pages follow. They preserve the exact wording, subparts, diagrams, and numerical data of the supplied exercise scans. Worked solutions begin immediately after these pages. A brief paraphrase at each answer identifies the task; consult the reproduced question for its full wording.


## Original exercises - source PDF page 1

@scan ex-01.png

@page


## Original exercises - source PDF page 2

@scan ex-02.png

@page


## Worked solutions


### 1.1.1 - Solve the system / find the common point

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "5", "7"], ["-2", "-7", "-5"]], "bar": 2}

**Step 1: R2 ← R2 + (2)R1.** Add 2 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "5", "7"], ["0", "3", "9"]], "bar": 2}

**Step 2: R2 ← (1/3)R2.** Multiply every entry of row 2, including any right-hand side, by 1/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "5", "7"], ["0", "1", "3"]], "bar": 2}

**Step 3: R1 ← R1 + (-5)R2.** Add -5 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-8"], ["0", "1", "3"]], "bar": 2}

**Read the equations.** x_1 = -8; x_2 = 3

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["-8"], ["3"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["7"], ["-5"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.1.2 - Solve the system / find the common point

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["2", "4", "-4"], ["5", "7", "11"]], "bar": 2}

**Step 1: R1 ← (1/2)R1.** Multiply every entry of row 1, including any right-hand side, by 1/2. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "2", "-2"], ["5", "7", "11"]], "bar": 2}

**Step 2: R2 ← R2 + (-5)R1.** Add -5 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "2", "-2"], ["0", "-3", "21"]], "bar": 2}

**Step 3: R2 ← (-1/3)R2.** Multiply every entry of row 2, including any right-hand side, by -1/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "2", "-2"], ["0", "1", "-7"]], "bar": 2}

**Step 4: R1 ← R1 + (-2)R2.** Add -2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "12"], ["0", "1", "-7"]], "bar": 2}

**Read the equations.** x_1 = 12; x_2 = -7

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["12"], ["-7"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["-4"], ["11"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.1.3 - Solve the system / find the common point

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 101.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "5", "7"], ["1", "-2", "-2"]], "bar": 2}

**Step 1: R2 ← R2 + (-1)R1.** Add -1 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "5", "7"], ["0", "-7", "-9"]], "bar": 2}

**Step 2: R2 ← (-1/7)R2.** Multiply every entry of row 2, including any right-hand side, by -1/7. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "5", "7"], ["0", "1", "9/7"]], "bar": 2}

**Step 3: R1 ← R1 + (-5)R2.** Add -5 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "4/7"], ["0", "1", "9/7"]], "bar": 2}

**Read the equations.** x_1 = 4/7; x_2 = 9/7

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["4/7"], ["9/7"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["7"], ["-2"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.1.4 - Solve the system / find the common point

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-5", "1"], ["3", "-7", "5"]], "bar": 2}

**Step 1: R2 ← R2 + (-3)R1.** Add -3 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-5", "1"], ["0", "8", "2"]], "bar": 2}

**Step 2: R2 ← (1/8)R2.** Multiply every entry of row 2, including any right-hand side, by 1/8. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-5", "1"], ["0", "1", "1/4"]], "bar": 2}

**Step 3: R1 ← R1 + (5)R2.** Add 5 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "9/4"], ["0", "1", "1/4"]], "bar": 2}

**Read the equations.** x_1 = 9/4; x_2 = 1/4

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["9/4"], ["1/4"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["1"], ["5"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.1.5 - Describe the next two row operations

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The last row already gives x₄ = -5, and the third row gives x₃ = 2. To continue the backward phase, first replace R₂ by R₂ + 3R₃, clearing -3 above the pivot in column 3. Then replace R₁ by R₁ - 5R₃, clearing 5 in that column. The complete updated arrays are:

@matrix {"a": [["1", "-4", "5", "0", "7"], ["0", "1", "0", "0", "12"], ["0", "0", "1", "0", "2"], ["0", "0", "0", "1", "-5"]], "bar": 4}

@matrix {"a": [["1", "-4", "0", "0", "-3"], ["0", "1", "0", "0", "12"], ["0", "0", "1", "0", "2"], ["0", "0", "0", "1", "-5"]], "bar": 4}

These are valid next operations; other equivalent backward-phase orders may also be used.


### 1.1.6 - Describe the next two row operations

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

There is still a 3 below the pivot in column 3. Replace R₄ by R₄ - 3R₃ to eliminate it. Then scale R₄ by -1/5 so its leading entry becomes 1. Carry the appended constant through both operations:

@matrix {"a": [["1", "-6", "4", "0", "-1"], ["0", "2", "-7", "0", "4"], ["0", "0", "1", "2", "-3"], ["0", "0", "0", "-5", "15"]], "bar": 4}

@matrix {"a": [["1", "-6", "4", "0", "-1"], ["0", "2", "-7", "0", "4"], ["0", "0", "1", "2", "-3"], ["0", "0", "0", "1", "-3"]], "bar": 4}

The fourth equation is now x₄ = -3, ready for backward elimination.


### 1.1.7 - Continue reduction and describe the full solution set

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 101.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "7", "3", "-4"], ["0", "1", "-1", "3"], ["0", "0", "0", "1"], ["0", "0", "1", "-2"]], "bar": 3}

**Step 1: R3 ↔ R4.** Move a nonzero entry into row 3 so that it can be used as a pivot.

@matrix {"a": [["1", "7", "3", "-4"], ["0", "1", "-1", "3"], ["0", "0", "1", "-2"], ["0", "0", "0", "1"]], "bar": 3}

**Step 2: R1 ← R1 + (4)R4.** Add 4 times row 4 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "7", "3", "0"], ["0", "1", "-1", "3"], ["0", "0", "1", "-2"], ["0", "0", "0", "1"]], "bar": 3}

**Step 3: R2 ← R2 + (-3)R4.** Add -3 times row 4 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "7", "3", "0"], ["0", "1", "-1", "0"], ["0", "0", "1", "-2"], ["0", "0", "0", "1"]], "bar": 3}

**Step 4: R3 ← R3 + (2)R4.** Add 2 times row 4 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "7", "3", "0"], ["0", "1", "-1", "0"], ["0", "0", "1", "0"], ["0", "0", "0", "1"]], "bar": 3}

**Step 5: R1 ← R1 + (-3)R3.** Add -3 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "7", "0", "0"], ["0", "1", "-1", "0"], ["0", "0", "1", "0"], ["0", "0", "0", "1"]], "bar": 3}

**Step 6: R2 ← R2 + (1)R3.** Add 1 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "7", "0", "0"], ["0", "1", "0", "0"], ["0", "0", "1", "0"], ["0", "0", "0", "1"]], "bar": 3}

**Step 7: R1 ← R1 + (-7)R2.** Add -7 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "0"], ["0", "1", "0", "0"], ["0", "0", "1", "0"], ["0", "0", "0", "1"]], "bar": 3}

A row now states 0 = 1. No choices of the unknowns can make that true. The system is inconsistent, and its solution set is empty. Free-looking coefficient columns cannot remove a contradiction.


### 1.1.8 - Continue reduction and describe the full solution set

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "1", "2", "0"], ["0", "1", "7", "0"], ["0", "0", "2", "-2"]], "bar": 3}

**Step 1: R3 ← (1/2)R3.** Multiply every entry of row 3, including any right-hand side, by 1/2. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "1", "2", "0"], ["0", "1", "7", "0"], ["0", "0", "1", "-1"]], "bar": 3}

**Step 2: R1 ← R1 + (-2)R3.** Add -2 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "1", "0", "2"], ["0", "1", "7", "0"], ["0", "0", "1", "-1"]], "bar": 3}

**Step 3: R2 ← R2 + (-7)R3.** Add -7 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "1", "0", "2"], ["0", "1", "0", "7"], ["0", "0", "1", "-1"]], "bar": 3}

**Step 4: R1 ← R1 + (-1)R2.** Add -1 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "-5"], ["0", "1", "0", "7"], ["0", "0", "1", "-1"]], "bar": 3}

**Read the equations.** x_1 = -5; x_2 = 7; x_3 = -1

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["-5"], ["7"], ["-1"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["0"], ["0"], ["-2"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.1.9 - Continue reduction and describe the full solution set

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 101.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-1", "0", "0", "-4"], ["0", "1", "-3", "0", "-7"], ["0", "0", "1", "-3", "-1"], ["0", "0", "0", "0", "4"]], "bar": 4}

**Step 1: R4 ← (1/4)R4.** Multiply every entry of row 4, including any right-hand side, by 1/4. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-1", "0", "0", "-4"], ["0", "1", "-3", "0", "-7"], ["0", "0", "1", "-3", "-1"], ["0", "0", "0", "0", "1"]], "bar": 4}

**Step 2: R1 ← R1 + (4)R4.** Add 4 times row 4 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-1", "0", "0", "0"], ["0", "1", "-3", "0", "-7"], ["0", "0", "1", "-3", "-1"], ["0", "0", "0", "0", "1"]], "bar": 4}

**Step 3: R2 ← R2 + (7)R4.** Add 7 times row 4 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-1", "0", "0", "0"], ["0", "1", "-3", "0", "0"], ["0", "0", "1", "-3", "-1"], ["0", "0", "0", "0", "1"]], "bar": 4}

**Step 4: R3 ← R3 + (1)R4.** Add 1 times row 4 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-1", "0", "0", "0"], ["0", "1", "-3", "0", "0"], ["0", "0", "1", "-3", "0"], ["0", "0", "0", "0", "1"]], "bar": 4}

**Step 5: R2 ← R2 + (3)R3.** Add 3 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-1", "0", "0", "0"], ["0", "1", "0", "-9", "0"], ["0", "0", "1", "-3", "0"], ["0", "0", "0", "0", "1"]], "bar": 4}

**Step 6: R1 ← R1 + (1)R2.** Add 1 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "-9", "0"], ["0", "1", "0", "-9", "0"], ["0", "0", "1", "-3", "0"], ["0", "0", "0", "0", "1"]], "bar": 4}

A row now states 0 = 1. No choices of the unknowns can make that true. The system is inconsistent, and its solution set is empty. Free-looking coefficient columns cannot remove a contradiction.


### 1.1.10 - Continue reduction and describe the full solution set

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-2", "0", "3", "0"], ["0", "1", "0", "-4", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "0"]], "bar": 4}

**Step 1: R1 ← R1 + (-3)R4.** Add -3 times row 4 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-2", "0", "0", "0"], ["0", "1", "0", "-4", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "0"]], "bar": 4}

**Step 2: R2 ← R2 + (4)R4.** Add 4 times row 4 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-2", "0", "0", "0"], ["0", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "0"]], "bar": 4}

**Step 3: R1 ← R1 + (2)R2.** Add 2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "0", "0"], ["0", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "0"]], "bar": 4}

**Read the equations.** x_1 = 0; x_2 = 0; x_3 = 0; x_4 = 0

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["0"], ["0"], ["0"], ["0"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["0"], ["0"], ["0"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.1.11 - Continue reduction and describe the full solution set

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 101.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["0", "1", "4", "-4"], ["1", "3", "3", "-2"], ["3", "7", "5", "6"]], "bar": 3}

**Step 1: R1 ↔ R2.** Move a nonzero entry into row 1 so that it can be used as a pivot.

@matrix {"a": [["1", "3", "3", "-2"], ["0", "1", "4", "-4"], ["3", "7", "5", "6"]], "bar": 3}

**Step 2: R3 ← R3 + (-3)R1.** Add -3 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "3", "-2"], ["0", "1", "4", "-4"], ["0", "-2", "-4", "12"]], "bar": 3}

**Step 3: R3 ← R3 + (2)R2.** Add 2 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "3", "-2"], ["0", "1", "4", "-4"], ["0", "0", "4", "4"]], "bar": 3}

**Step 4: R3 ← (1/4)R3.** Multiply every entry of row 3, including any right-hand side, by 1/4. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "3", "3", "-2"], ["0", "1", "4", "-4"], ["0", "0", "1", "1"]], "bar": 3}

**Step 5: R1 ← R1 + (-3)R3.** Add -3 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "0", "-5"], ["0", "1", "4", "-4"], ["0", "0", "1", "1"]], "bar": 3}

**Step 6: R2 ← R2 + (-4)R3.** Add -4 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "0", "-5"], ["0", "1", "0", "-8"], ["0", "0", "1", "1"]], "bar": 3}

**Step 7: R1 ← R1 + (-3)R2.** Add -3 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "19"], ["0", "1", "0", "-8"], ["0", "0", "1", "1"]], "bar": 3}

**Read the equations.** x_1 = 19; x_2 = -8; x_3 = 1

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["19"], ["-8"], ["1"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["-4"], ["-2"], ["6"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.1.12 - Continue reduction and describe the full solution set

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-3", "4", "-4"], ["3", "-7", "7", "-8"], ["-4", "6", "2", "4"]], "bar": 3}

**Step 1: R2 ← R2 + (-3)R1.** Add -3 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "4", "-4"], ["0", "2", "-5", "4"], ["-4", "6", "2", "4"]], "bar": 3}

**Step 2: R3 ← R3 + (4)R1.** Add 4 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "4", "-4"], ["0", "2", "-5", "4"], ["0", "-6", "18", "-12"]], "bar": 3}

**Step 3: R2 ← (1/2)R2.** Multiply every entry of row 2, including any right-hand side, by 1/2. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-3", "4", "-4"], ["0", "1", "-5/2", "2"], ["0", "-6", "18", "-12"]], "bar": 3}

**Step 4: R3 ← R3 + (6)R2.** Add 6 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "4", "-4"], ["0", "1", "-5/2", "2"], ["0", "0", "3", "0"]], "bar": 3}

**Step 5: R3 ← (1/3)R3.** Multiply every entry of row 3, including any right-hand side, by 1/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-3", "4", "-4"], ["0", "1", "-5/2", "2"], ["0", "0", "1", "0"]], "bar": 3}

**Step 6: R1 ← R1 + (-4)R3.** Add -4 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "0", "-4"], ["0", "1", "-5/2", "2"], ["0", "0", "1", "0"]], "bar": 3}

**Step 7: R2 ← R2 + (5/2)R3.** Add 5/2 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "0", "-4"], ["0", "1", "0", "2"], ["0", "0", "1", "0"]], "bar": 3}

**Step 8: R1 ← R1 + (3)R2.** Add 3 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "2"], ["0", "1", "0", "2"], ["0", "0", "1", "0"]], "bar": 3}

**Read the equations.** x_1 = 2; x_2 = 2; x_3 = 0

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["2"], ["2"], ["0"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["-4"], ["-8"], ["4"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.1.13 - Continue reduction and describe the full solution set

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "0", "-3", "8"], ["2", "2", "9", "7"], ["0", "1", "5", "-2"]], "bar": 3}

**Step 1: R2 ← R2 + (-2)R1.** Add -2 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-3", "8"], ["0", "2", "15", "-9"], ["0", "1", "5", "-2"]], "bar": 3}

**Step 2: R2 ← (1/2)R2.** Multiply every entry of row 2, including any right-hand side, by 1/2. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "0", "-3", "8"], ["0", "1", "15/2", "-9/2"], ["0", "1", "5", "-2"]], "bar": 3}

**Step 3: R3 ← R3 + (-1)R2.** Add -1 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-3", "8"], ["0", "1", "15/2", "-9/2"], ["0", "0", "-5/2", "5/2"]], "bar": 3}

**Step 4: R3 ← (-2/5)R3.** Multiply every entry of row 3, including any right-hand side, by -2/5. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "0", "-3", "8"], ["0", "1", "15/2", "-9/2"], ["0", "0", "1", "-1"]], "bar": 3}

**Step 5: R1 ← R1 + (3)R3.** Add 3 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "5"], ["0", "1", "15/2", "-9/2"], ["0", "0", "1", "-1"]], "bar": 3}

**Step 6: R2 ← R2 + (-15/2)R3.** Add -15/2 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "5"], ["0", "1", "0", "3"], ["0", "0", "1", "-1"]], "bar": 3}

**Read the equations.** x_1 = 5; x_2 = 3; x_3 = -1

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["5"], ["3"], ["-1"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["8"], ["7"], ["-2"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.1.14 - Continue reduction and describe the full solution set

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-3", "0", "5"], ["-1", "1", "5", "2"], ["0", "1", "1", "0"]], "bar": 3}

**Step 1: R2 ← R2 + (1)R1.** Add 1 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "0", "5"], ["0", "-2", "5", "7"], ["0", "1", "1", "0"]], "bar": 3}

**Step 2: R2 ← (-1/2)R2.** Multiply every entry of row 2, including any right-hand side, by -1/2. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-3", "0", "5"], ["0", "1", "-5/2", "-7/2"], ["0", "1", "1", "0"]], "bar": 3}

**Step 3: R3 ← R3 + (-1)R2.** Add -1 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "0", "5"], ["0", "1", "-5/2", "-7/2"], ["0", "0", "7/2", "7/2"]], "bar": 3}

**Step 4: R3 ← (2/7)R3.** Multiply every entry of row 3, including any right-hand side, by 2/7. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-3", "0", "5"], ["0", "1", "-5/2", "-7/2"], ["0", "0", "1", "1"]], "bar": 3}

**Step 5: R2 ← R2 + (5/2)R3.** Add 5/2 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "0", "5"], ["0", "1", "0", "-1"], ["0", "0", "1", "1"]], "bar": 3}

**Step 6: R1 ← R1 + (3)R2.** Add 3 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "2"], ["0", "1", "0", "-1"], ["0", "0", "1", "1"]], "bar": 3}

**Read the equations.** x_1 = 2; x_2 = -1; x_3 = 1

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["2"], ["-1"], ["1"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["5"], ["2"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.1.15 - Verify the solution of Exercise 11

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 102.

To verify the full solution set rather than one numerical sample, first obtain its exact parameterization and then substitute the constant and every parameter direction into the original coefficient matrix. The final verification below performs this check for all parameter values.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["0", "1", "4", "-4"], ["1", "3", "3", "-2"], ["3", "7", "5", "6"]], "bar": 3}

**Step 1: R1 ↔ R2.** Move a nonzero entry into row 1 so that it can be used as a pivot.

@matrix {"a": [["1", "3", "3", "-2"], ["0", "1", "4", "-4"], ["3", "7", "5", "6"]], "bar": 3}

**Step 2: R3 ← R3 + (-3)R1.** Add -3 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "3", "-2"], ["0", "1", "4", "-4"], ["0", "-2", "-4", "12"]], "bar": 3}

**Step 3: R3 ← R3 + (2)R2.** Add 2 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "3", "-2"], ["0", "1", "4", "-4"], ["0", "0", "4", "4"]], "bar": 3}

**Step 4: R3 ← (1/4)R3.** Multiply every entry of row 3, including any right-hand side, by 1/4. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "3", "3", "-2"], ["0", "1", "4", "-4"], ["0", "0", "1", "1"]], "bar": 3}

**Step 5: R1 ← R1 + (-3)R3.** Add -3 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "0", "-5"], ["0", "1", "4", "-4"], ["0", "0", "1", "1"]], "bar": 3}

**Step 6: R2 ← R2 + (-4)R3.** Add -4 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "0", "-5"], ["0", "1", "0", "-8"], ["0", "0", "1", "1"]], "bar": 3}

**Step 7: R1 ← R1 + (-3)R2.** Add -3 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "19"], ["0", "1", "0", "-8"], ["0", "0", "1", "1"]], "bar": 3}

**Read the equations.** x_1 = 19; x_2 = -8; x_3 = 1

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["19"], ["-8"], ["1"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["-4"], ["-2"], ["6"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.1.16 - Verify the solution of Exercise 12

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

To verify the full solution set rather than one numerical sample, first obtain its exact parameterization and then substitute the constant and every parameter direction into the original coefficient matrix. The final verification below performs this check for all parameter values.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-3", "4", "-4"], ["3", "-7", "7", "-8"], ["-4", "6", "2", "4"]], "bar": 3}

**Step 1: R2 ← R2 + (-3)R1.** Add -3 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "4", "-4"], ["0", "2", "-5", "4"], ["-4", "6", "2", "4"]], "bar": 3}

**Step 2: R3 ← R3 + (4)R1.** Add 4 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "4", "-4"], ["0", "2", "-5", "4"], ["0", "-6", "18", "-12"]], "bar": 3}

**Step 3: R2 ← (1/2)R2.** Multiply every entry of row 2, including any right-hand side, by 1/2. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-3", "4", "-4"], ["0", "1", "-5/2", "2"], ["0", "-6", "18", "-12"]], "bar": 3}

**Step 4: R3 ← R3 + (6)R2.** Add 6 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "4", "-4"], ["0", "1", "-5/2", "2"], ["0", "0", "3", "0"]], "bar": 3}

**Step 5: R3 ← (1/3)R3.** Multiply every entry of row 3, including any right-hand side, by 1/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-3", "4", "-4"], ["0", "1", "-5/2", "2"], ["0", "0", "1", "0"]], "bar": 3}

**Step 6: R1 ← R1 + (-4)R3.** Add -4 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "0", "-4"], ["0", "1", "-5/2", "2"], ["0", "0", "1", "0"]], "bar": 3}

**Step 7: R2 ← R2 + (5/2)R3.** Add 5/2 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "0", "-4"], ["0", "1", "0", "2"], ["0", "0", "1", "0"]], "bar": 3}

**Step 8: R1 ← R1 + (3)R2.** Add 3 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "2"], ["0", "1", "0", "2"], ["0", "0", "1", "0"]], "bar": 3}

**Read the equations.** x_1 = 2; x_2 = 2; x_3 = 0

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["2"], ["2"], ["0"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["-4"], ["-8"], ["4"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.1.17 - Verify the solution of Exercise 13

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

To verify the full solution set rather than one numerical sample, first obtain its exact parameterization and then substitute the constant and every parameter direction into the original coefficient matrix. The final verification below performs this check for all parameter values.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "0", "-3", "8"], ["2", "2", "9", "7"], ["0", "1", "5", "-2"]], "bar": 3}

**Step 1: R2 ← R2 + (-2)R1.** Add -2 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-3", "8"], ["0", "2", "15", "-9"], ["0", "1", "5", "-2"]], "bar": 3}

**Step 2: R2 ← (1/2)R2.** Multiply every entry of row 2, including any right-hand side, by 1/2. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "0", "-3", "8"], ["0", "1", "15/2", "-9/2"], ["0", "1", "5", "-2"]], "bar": 3}

**Step 3: R3 ← R3 + (-1)R2.** Add -1 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-3", "8"], ["0", "1", "15/2", "-9/2"], ["0", "0", "-5/2", "5/2"]], "bar": 3}

**Step 4: R3 ← (-2/5)R3.** Multiply every entry of row 3, including any right-hand side, by -2/5. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "0", "-3", "8"], ["0", "1", "15/2", "-9/2"], ["0", "0", "1", "-1"]], "bar": 3}

**Step 5: R1 ← R1 + (3)R3.** Add 3 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "5"], ["0", "1", "15/2", "-9/2"], ["0", "0", "1", "-1"]], "bar": 3}

**Step 6: R2 ← R2 + (-15/2)R3.** Add -15/2 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "5"], ["0", "1", "0", "3"], ["0", "0", "1", "-1"]], "bar": 3}

**Read the equations.** x_1 = 5; x_2 = 3; x_3 = -1

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["5"], ["3"], ["-1"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["8"], ["7"], ["-2"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.1.18 - Verify the solution of Exercise 14

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

To verify the full solution set rather than one numerical sample, first obtain its exact parameterization and then substitute the constant and every parameter direction into the original coefficient matrix. The final verification below performs this check for all parameter values.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-3", "0", "5"], ["-1", "1", "5", "2"], ["0", "1", "1", "0"]], "bar": 3}

**Step 1: R2 ← R2 + (1)R1.** Add 1 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "0", "5"], ["0", "-2", "5", "7"], ["0", "1", "1", "0"]], "bar": 3}

**Step 2: R2 ← (-1/2)R2.** Multiply every entry of row 2, including any right-hand side, by -1/2. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-3", "0", "5"], ["0", "1", "-5/2", "-7/2"], ["0", "1", "1", "0"]], "bar": 3}

**Step 3: R3 ← R3 + (-1)R2.** Add -1 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "0", "5"], ["0", "1", "-5/2", "-7/2"], ["0", "0", "7/2", "7/2"]], "bar": 3}

**Step 4: R3 ← (2/7)R3.** Multiply every entry of row 3, including any right-hand side, by 2/7. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-3", "0", "5"], ["0", "1", "-5/2", "-7/2"], ["0", "0", "1", "1"]], "bar": 3}

**Step 5: R2 ← R2 + (5/2)R3.** Add 5/2 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "0", "5"], ["0", "1", "0", "-1"], ["0", "0", "1", "1"]], "bar": 3}

**Step 6: R1 ← R1 + (3)R2.** Add 3 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "2"], ["0", "1", "0", "-1"], ["0", "0", "1", "1"]], "bar": 3}

**Read the equations.** x_1 = 2; x_2 = -1; x_3 = 1

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["2"], ["-1"], ["1"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["5"], ["2"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.1.19 - Decide consistency without solving completely

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 102.

The starting matrix is:

@matrix {"a": [["1", "0", "3", "0", "2"], ["0", "1", "0", "-3", "3"], ["0", "-2", "3", "2", "1"], ["3", "0", "0", "7", "-5"]], "bar": 4}

**Step 1: R4 ← R4 + (-3)R1.** Add -3 times row 1 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "3", "0", "2"], ["0", "1", "0", "-3", "3"], ["0", "-2", "3", "2", "1"], ["0", "0", "-9", "7", "-11"]], "bar": 4}

**Step 2: R3 ← R3 + (2)R2.** Add 2 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "3", "0", "2"], ["0", "1", "0", "-3", "3"], ["0", "0", "3", "-4", "7"], ["0", "0", "-9", "7", "-11"]], "bar": 4}

**Step 3: R3 ← (1/3)R3.** Multiply every entry of row 3, including any right-hand side, by 1/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "0", "3", "0", "2"], ["0", "1", "0", "-3", "3"], ["0", "0", "1", "-4/3", "7/3"], ["0", "0", "-9", "7", "-11"]], "bar": 4}

**Step 4: R4 ← R4 + (9)R3.** Add 9 times row 3 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "3", "0", "2"], ["0", "1", "0", "-3", "3"], ["0", "0", "1", "-4/3", "7/3"], ["0", "0", "0", "-5", "10"]], "bar": 4}

**Step 5: R4 ← (-1/5)R4.** Multiply every entry of row 4, including any right-hand side, by -1/5. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "0", "3", "0", "2"], ["0", "1", "0", "-3", "3"], ["0", "0", "1", "-4/3", "7/3"], ["0", "0", "0", "1", "-2"]], "bar": 4}

**Step 6: R2 ← R2 + (3)R4.** Add 3 times row 4 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "3", "0", "2"], ["0", "1", "0", "0", "-3"], ["0", "0", "1", "-4/3", "7/3"], ["0", "0", "0", "1", "-2"]], "bar": 4}

**Step 7: R3 ← R3 + (4/3)R4.** Add 4/3 times row 4 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "3", "0", "2"], ["0", "1", "0", "0", "-3"], ["0", "0", "1", "0", "-1/3"], ["0", "0", "0", "1", "-2"]], "bar": 4}

**Step 8: R1 ← R1 + (-3)R3.** Add -3 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "0", "3"], ["0", "1", "0", "0", "-3"], ["0", "0", "1", "0", "-1/3"], ["0", "0", "0", "1", "-2"]], "bar": 4}

The coefficient part has a leading entry in each of its four rows, and there is no row [0,0,0,0 | nonzero]. Back substitution is therefore possible, so the system is consistent. No input values need to be computed for this question. The four coefficient pivots also show uniqueness, although only consistency was requested.


### 1.1.20 - Decide consistency without solving completely

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The starting matrix is:

@matrix {"a": [["1", "0", "0", "-2", "-3"], ["0", "2", "2", "0", "0"], ["0", "0", "1", "3", "1"], ["-2", "3", "2", "1", "5"]], "bar": 4}

**Step 1: R4 ← R4 + (2)R1.** Add 2 times row 1 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "-2", "-3"], ["0", "2", "2", "0", "0"], ["0", "0", "1", "3", "1"], ["0", "3", "2", "-3", "-1"]], "bar": 4}

**Step 2: R2 ← (1/2)R2.** Multiply every entry of row 2, including any right-hand side, by 1/2. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "0", "0", "-2", "-3"], ["0", "1", "1", "0", "0"], ["0", "0", "1", "3", "1"], ["0", "3", "2", "-3", "-1"]], "bar": 4}

**Step 3: R4 ← R4 + (-3)R2.** Add -3 times row 2 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "-2", "-3"], ["0", "1", "1", "0", "0"], ["0", "0", "1", "3", "1"], ["0", "0", "-1", "-3", "-1"]], "bar": 4}

**Step 4: R4 ← R4 + (1)R3.** Add 1 times row 3 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "-2", "-3"], ["0", "1", "1", "0", "0"], ["0", "0", "1", "3", "1"], ["0", "0", "0", "0", "0"]], "bar": 4}

**Step 5: R2 ← R2 + (-1)R3.** Add -1 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "-2", "-3"], ["0", "1", "0", "-3", "-1"], ["0", "0", "1", "3", "1"], ["0", "0", "0", "0", "0"]], "bar": 4}

The coefficient part has a leading entry in each of its four rows, and there is no row [0,0,0,0 | nonzero]. Back substitution is therefore possible, so the system is consistent. No input values need to be computed for this question. The four coefficient pivots also show uniqueness, although only consistency was requested.


### 1.1.21 - Do the three lines share a point?

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 102.

A common point must satisfy all three line equations simultaneously. Solve the combined system, not just two selected equations.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-4", "1"], ["2", "-1", "-3"], ["-1", "-3", "4"]], "bar": 2}

**Step 1: R2 ← R2 + (-2)R1.** Add -2 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-4", "1"], ["0", "7", "-5"], ["-1", "-3", "4"]], "bar": 2}

**Step 2: R3 ← R3 + (1)R1.** Add 1 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-4", "1"], ["0", "7", "-5"], ["0", "-7", "5"]], "bar": 2}

**Step 3: R2 ← (1/7)R2.** Multiply every entry of row 2, including any right-hand side, by 1/7. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-4", "1"], ["0", "1", "-5/7"], ["0", "-7", "5"]], "bar": 2}

**Step 4: R3 ← R3 + (7)R2.** Add 7 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-4", "1"], ["0", "1", "-5/7"], ["0", "0", "0"]], "bar": 2}

**Step 5: R1 ← R1 + (4)R2.** Add 4 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-13/7"], ["0", "1", "-5/7"], ["0", "0", "0"]], "bar": 2}

**Read the equations.** x_1 = -13/7; x_2 = -5/7

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["-13/7"], ["-5/7"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["1"], ["-3"], ["4"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.1.22 - Do the three planes share a point?

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Put all three plane equations into one system. A point common to only two planes would not answer the question.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "2", "1", "4"], ["0", "1", "-1", "1"], ["1", "0", "3", "0"]], "bar": 3}

**Step 1: R3 ← R3 + (-1)R1.** Add -1 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "2", "1", "4"], ["0", "1", "-1", "1"], ["0", "-2", "2", "-4"]], "bar": 3}

**Step 2: R3 ← R3 + (2)R2.** Add 2 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "2", "1", "4"], ["0", "1", "-1", "1"], ["0", "0", "0", "-2"]], "bar": 3}

**Step 3: R3 ← (-1/2)R3.** Multiply every entry of row 3, including any right-hand side, by -1/2. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "2", "1", "4"], ["0", "1", "-1", "1"], ["0", "0", "0", "1"]], "bar": 3}

**Step 4: R1 ← R1 + (-4)R3.** Add -4 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "2", "1", "0"], ["0", "1", "-1", "1"], ["0", "0", "0", "1"]], "bar": 3}

**Step 5: R2 ← R2 + (-1)R3.** Add -1 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "2", "1", "0"], ["0", "1", "-1", "0"], ["0", "0", "0", "1"]], "bar": 3}

**Step 6: R1 ← R1 + (-2)R2.** Add -2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "3", "0"], ["0", "1", "-1", "0"], ["0", "0", "0", "1"]], "bar": 3}

A row now states 0 = 1. No choices of the unknowns can make that true. The system is inconsistent, and its solution set is empty. Free-looking coefficient columns cannot remove a contradiction.


### 1.1.23 - Choose h for consistency

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 102.

Apply R₂ ← R₂ - 3R₁. The second row becomes [0, 6 - 3h | -4], representing (6 - 3h)x₂ = -4. If h = 2, it says 0 = -4, which is impossible. If h ≠ 2, divide by the nonzero 6 - 3h to determine x₂, and the first row determines x₁. Thus consistency holds exactly for h ≠ 2.


### 1.1.24 - Choose h for consistency

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Apply R₂ ← R₂ + 2R₁. The result is [0,4 + 2h | 0]. If h ≠ -2, it determines x₂ = 0; if h = -2, it is the always true equation 0 = 0. In either case the first row can be solved for x₁. Therefore every real h gives a consistent system.


### 1.1.25 - Choose h for consistency

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 102.

Apply R₂ ← R₂ + 4R₁, giving [0,h + 12 | 0]. The equation (h + 12)x₂ = 0 always has the choice x₂ = 0, including when h = -12. The first equation then fixes a compatible x₁. Every real h is allowed; a zero coefficient is harmless when the corresponding constant is also zero.


### 1.1.26 - Choose h for consistency

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Apply R₂ ← R₂ + 3R₁. The second row is [0,0 | 5 + 3h]. Consistency requires 5 + 3h = 0, hence h = -5/3. At that value the second equation repeats a multiple of the first, which still has solutions. At every other h the system contains a contradiction.


### 1.1.27 - True/false: Every elementary row operation is reversible

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** Interchanging twice restores the rows; scaling by c ≠ 0 is undone by 1/c; adding c times another row is undone by adding -c times that retained row. Reversal is precisely why these operations preserve the solution set.


### 1.1.28 - True/false: Row operations on an augmented matrix preserve the solution set

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** Each operation transforms equations by a reversible change. Any original solution satisfies the new equations, and reversing the operations proves that every new solution satisfies the old equations. The right-hand-side column must participate in the operations.


### 1.1.29 - True/false: A 5 × 6 matrix has six rows

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** Rows are counted first. A 5 × 6 matrix has five rows and six columns. For example, writing five horizontal lists each with six entries constructs exactly this size.


### 1.1.30 - True/false: Same number of rows implies row equivalence

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** The 2 × 2 zero matrix and I₂ have the same row count but cannot be row equivalent. Every row operation on a zero matrix leaves it zero, so it cannot become I₂.


### 1.1.31 - True/false: A solution set is one list satisfying every equation

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** One such list is a solution. The solution set is the collection of all such lists. The equation x₁ + x₂ = 1 has solutions (1,0) and (0,1), among infinitely many others; neither individual list is its entire solution set.


### 1.1.32 - True/false: An inconsistent system has more than one solution

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** Inconsistent means no solutions at all. For instance, x₁ = 0 and x₁ = 1 cannot both hold, so the solution set is empty. More than one solution belongs to the consistent category.


### 1.1.33 - True/false: Existence and uniqueness are fundamental questions

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** Existence asks whether at least one input list satisfies all equations. If one exists, uniqueness asks whether there is any different one. These decisions distinguish no solution, one solution, and infinitely many solutions.


### 1.1.34 - True/false: Equivalent systems have the same solution set

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** This is the definition of equivalent systems. Their equations may look different; the requirement is that exactly the same lists satisfy every equation in each system.


### 1.1.35 - Find the consistency relation among g,h,k

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Use R₃ ← R₃ + 2R₁, which gives third row [0,-3,5 | k + 2g]. Then use R₃ ← R₃ + R₂, giving [0,0,0 | k + 2g + h]. The first two coefficient rows have pivots, so this final row is the only possible contradiction. Consistency is equivalent to 2g + h + k = 0.


### 1.1.36 - Construct three systems with the prescribed unique solution

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Start with the augmented matrix [I₃ | p], where p = (-2,1,0). It clearly states those three values and has one pivot per unknown. Reversible row operations produce other systems with exactly the same unique solution. Three examples are:

@matrix {"a": [["1", "0", "0", "-2"], ["0", "1", "0", "1"], ["0", "0", "1", "0"]], "bar": 3}

@matrix {"a": [["1", "1", "0", "-1"], ["0", "1", "0", "1"], ["0", "0", "1", "0"]], "bar": 3}

@matrix {"a": [["2", "0", "0", "-4"], ["0", "1", "1", "1"], ["0", "0", "1", "0"]], "bar": 3}

The second adds row 2 to row 1 of the first. The third scales row 1 by 2 and adds row 3 to row 2. Substitute p into every row to verify the appended constants.


### 1.1.37 - What must c,d satisfy if all f,g are allowed?

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Subtract c times the first equation from the second. The resulting equation is (d - 3c)x₂ = g - cf. For this to be solvable for every pair f,g, its coefficient cannot vanish: if d = 3c, choosing f = 0,g = 1 creates 0 = 1. Conversely, if d ≠ 3c, x₂ = (g - cf)/(d - 3c) always exists and x₁ = f - 3x₂ completes the solution. Thus d ≠ 3c is necessary and sufficient.


# Section 1.2 - Row reduction and echelon forms


Original question pages follow. They preserve the exact wording, subparts, diagrams, and numerical data of the supplied exercise scans. Worked solutions begin immediately after these pages. A brief paraphrase at each answer identifies the task; consult the reproduced question for its full wording.


## Original exercises - source PDF page 3

@scan ex-03.png

@page


## Original exercises - source PDF page 4

@scan ex-04.png

@page


## Worked solutions


### 1.2.1 - Classify each displayed matrix

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 103.

(a) is RREF: its leading entries are 1 in columns 1,2,3 and each pivot column is otherwise zero. (b) is REF only: the leading 1 in column 3 has a nonzero entry above it. (c) is RREF: its pivots are in columns 1 and 2, and zero rows are at the bottom; entries in column 3 are allowed because it is nonpivot. (d) is REF only: the leading entries progress through columns 1,2,4,5, but some are 2,3,4 instead of 1 and pivot columns have entries above. None of these four matrices fails REF.


### 1.2.2 - Classify each displayed matrix

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

(a) is RREF: pivots in columns 1 and 3 are 1 and alone in their columns. (b) is not REF, since the second and third rows have leading entries in the same column 2; a leading entry must move strictly right. (c) is not REF, because a zero row lies above nonzero rows. (d) is REF only: leading columns are 2,3,5, but leading entries 2 and 3 are not normalized and entries above them are nonzero. Check REF conditions before the extra RREF conditions.


### 1.2.3 - Reduce and identify original pivot positions

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 103.

The starting matrix is:

@matrix {"a": [["1", "2", "3", "4"], ["4", "5", "6", "7"], ["6", "7", "8", "9"]], "bar": null}

**Step 1: R2 ← R2 + (-4)R1.** Add -4 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "2", "3", "4"], ["0", "-3", "-6", "-9"], ["6", "7", "8", "9"]], "bar": null}

**Step 2: R3 ← R3 + (-6)R1.** Add -6 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "2", "3", "4"], ["0", "-3", "-6", "-9"], ["0", "-5", "-10", "-15"]], "bar": null}

**Step 3: R2 ← (-1/3)R2.** Multiply every entry of row 2, including any right-hand side, by -1/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "2", "3", "4"], ["0", "1", "2", "3"], ["0", "-5", "-10", "-15"]], "bar": null}

**Step 4: R3 ← R3 + (5)R2.** Add 5 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "2", "3", "4"], ["0", "1", "2", "3"], ["0", "0", "0", "0"]], "bar": null}

**Step 5: R1 ← R1 + (-2)R2.** Add -2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-1", "-2"], ["0", "1", "2", "3"], ["0", "0", "0", "0"]], "bar": null}

The pivot columns, numbered in the original matrix, are 1, 2. The corresponding pivot positions are (1,1), (2,2). Mark these same locations in the original array. A pivot position is a location, not necessarily a nonzero original entry.


### 1.2.4 - Reduce and identify original pivot positions

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The starting matrix is:

@matrix {"a": [["1", "3", "5", "7"], ["3", "5", "7", "9"], ["5", "7", "9", "1"]], "bar": null}

**Step 1: R2 ← R2 + (-3)R1.** Add -3 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "5", "7"], ["0", "-4", "-8", "-12"], ["5", "7", "9", "1"]], "bar": null}

**Step 2: R3 ← R3 + (-5)R1.** Add -5 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "5", "7"], ["0", "-4", "-8", "-12"], ["0", "-8", "-16", "-34"]], "bar": null}

**Step 3: R2 ← (-1/4)R2.** Multiply every entry of row 2, including any right-hand side, by -1/4. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "3", "5", "7"], ["0", "1", "2", "3"], ["0", "-8", "-16", "-34"]], "bar": null}

**Step 4: R3 ← R3 + (8)R2.** Add 8 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "5", "7"], ["0", "1", "2", "3"], ["0", "0", "0", "-10"]], "bar": null}

**Step 5: R3 ← (-1/10)R3.** Multiply every entry of row 3, including any right-hand side, by -1/10. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "3", "5", "7"], ["0", "1", "2", "3"], ["0", "0", "0", "1"]], "bar": null}

**Step 6: R1 ← R1 + (-7)R3.** Add -7 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "5", "0"], ["0", "1", "2", "3"], ["0", "0", "0", "1"]], "bar": null}

**Step 7: R2 ← R2 + (-3)R3.** Add -3 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "5", "0"], ["0", "1", "2", "0"], ["0", "0", "0", "1"]], "bar": null}

**Step 8: R1 ← R1 + (-3)R2.** Add -3 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-1", "0"], ["0", "1", "2", "0"], ["0", "0", "0", "1"]], "bar": null}

The pivot columns, numbered in the original matrix, are 1, 2, 4. The corresponding pivot positions are (1,1), (2,2), (3,4). Mark these same locations in the original array. A pivot position is a location, not necessarily a nonzero original entry.


### 1.2.5 - All possible REF patterns for a nonzero 2 × 2 matrix

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Use p for a required nonzero leading entry and * for an arbitrary entry, possibly zero. There may be one pivot in column 1, one pivot in column 2, or two pivots. The exhaustive patterns are [p,*;0,0], [0,p;0,0], and [p,*;0,p]. A zero matrix is excluded by the question. There cannot be a second pivot in the same column, nor a nonzero row below a zero row.


### 1.2.6 - All possible REF patterns for a nonzero 3 × 2 matrix

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

There are at most two pivots because there are two columns. Append a zero third row to each pattern in Exercise 5: [p,*;0,0;0,0], [0,p;0,0;0,0], [p,*;0,p;0,0]. Here p is nonzero and * is arbitrary. These cover one pivot in either column and two pivots in successive columns. No three-pivot pattern is possible.


### 1.2.7 - Find every solution

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 103.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "3", "4", "7"], ["3", "9", "7", "6"]], "bar": 3}

**Step 1: R2 ← R2 + (-3)R1.** Add -3 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "4", "7"], ["0", "0", "-5", "-15"]], "bar": 3}

**Step 2: R2 ← (-1/5)R2.** Multiply every entry of row 2, including any right-hand side, by -1/5. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "3", "4", "7"], ["0", "0", "1", "3"]], "bar": 3}

**Step 3: R1 ← R1 + (-4)R2.** Add -4 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "0", "-5"], ["0", "0", "1", "3"]], "bar": 3}

**Read the equations.** x_1 + 3 x_2 = -5; x_3 = 3

The pivot columns are 1, 3. Thus x_1, x_3 are basic variables. x_2 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_2 = s with all parameters real. The complete coordinate answer is:

@eq x_1 = -5 - 3 s

@eq x_2 = s

@eq x_3 = 3

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1, where:

p =

@matrix {"a": [["-5"], ["0"], ["3"]], "bar": null}

v_1 =

@matrix {"a": [["-3"], ["1"], ["0"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["-8"], ["1"], ["3"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["7"], ["6"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. Therefore A(p + s v_1) = A p + s A v_1 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.2.8 - Find every solution

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "4", "0", "7"], ["2", "7", "0", "11"]], "bar": 3}

**Step 1: R2 ← R2 + (-2)R1.** Add -2 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "4", "0", "7"], ["0", "-1", "0", "-3"]], "bar": 3}

**Step 2: R2 ← (-1)R2.** Multiply every entry of row 2, including any right-hand side, by -1. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "4", "0", "7"], ["0", "1", "0", "3"]], "bar": 3}

**Step 3: R1 ← R1 + (-4)R2.** Add -4 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "-5"], ["0", "1", "0", "3"]], "bar": 3}

**Read the equations.** x_1 = -5; x_2 = 3

The pivot columns are 1, 2. Thus x_1, x_2 are basic variables. x_3 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_3 = s with all parameters real. The complete coordinate answer is:

@eq x_1 = -5

@eq x_2 = 3

@eq x_3 = s

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1, where:

p =

@matrix {"a": [["-5"], ["3"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["0"], ["0"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["-5"], ["3"], ["1"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["7"], ["11"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. Therefore A(p + s v_1) = A p + s A v_1 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.2.9 - Find every solution

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 103.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["0", "1", "-6", "5"], ["1", "-2", "7", "-4"]], "bar": 3}

**Step 1: R1 ↔ R2.** Move a nonzero entry into row 1 so that it can be used as a pivot.

@matrix {"a": [["1", "-2", "7", "-4"], ["0", "1", "-6", "5"]], "bar": 3}

**Step 2: R1 ← R1 + (2)R2.** Add 2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-5", "6"], ["0", "1", "-6", "5"]], "bar": 3}

**Read the equations.** x_1 - 5 x_3 = 6; x_2 - 6 x_3 = 5

The pivot columns are 1, 2. Thus x_1, x_2 are basic variables. x_3 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_3 = s with all parameters real. The complete coordinate answer is:

@eq x_1 = 6 + 5 s

@eq x_2 = 5 + 6 s

@eq x_3 = s

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1, where:

p =

@matrix {"a": [["6"], ["5"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["5"], ["6"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["11"], ["11"], ["1"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["5"], ["-4"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. Therefore A(p + s v_1) = A p + s A v_1 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.2.10 - Find every solution

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-2", "-1", "3"], ["3", "-6", "-2", "2"]], "bar": 3}

**Step 1: R2 ← R2 + (-3)R1.** Add -3 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-2", "-1", "3"], ["0", "0", "1", "-7"]], "bar": 3}

**Step 2: R1 ← R1 + (1)R2.** Add 1 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-2", "0", "-4"], ["0", "0", "1", "-7"]], "bar": 3}

**Read the equations.** x_1 - 2 x_2 = -4; x_3 = -7

The pivot columns are 1, 3. Thus x_1, x_3 are basic variables. x_2 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_2 = s with all parameters real. The complete coordinate answer is:

@eq x_1 = -4 + 2 s

@eq x_2 = s

@eq x_3 = -7

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1, where:

p =

@matrix {"a": [["-4"], ["0"], ["-7"]], "bar": null}

v_1 =

@matrix {"a": [["2"], ["1"], ["0"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["-2"], ["1"], ["-7"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["3"], ["2"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. Therefore A(p + s v_1) = A p + s A v_1 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.2.11 - Find every solution

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 104.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["3", "-4", "2", "0"], ["-9", "12", "-6", "0"], ["-6", "8", "-4", "0"]], "bar": 3}

**Step 1: R1 ← (1/3)R1.** Multiply every entry of row 1, including any right-hand side, by 1/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-4/3", "2/3", "0"], ["-9", "12", "-6", "0"], ["-6", "8", "-4", "0"]], "bar": 3}

**Step 2: R2 ← R2 + (9)R1.** Add 9 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-4/3", "2/3", "0"], ["0", "0", "0", "0"], ["-6", "8", "-4", "0"]], "bar": 3}

**Step 3: R3 ← R3 + (6)R1.** Add 6 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-4/3", "2/3", "0"], ["0", "0", "0", "0"], ["0", "0", "0", "0"]], "bar": 3}

**Read the equations.** x_1 - 4/3 x_2 + 2/3 x_3 = 0

The pivot columns are 1. Thus x_1 are basic variables. x_2, x_3 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_2 = s, x_3 = t with all parameters real. The complete coordinate answer is:

@eq x_1 = 4/3 s - 2/3 t

@eq x_2 = s

@eq x_3 = t

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1 + t v_2, where:

p =

@matrix {"a": [["0"], ["0"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["4/3"], ["1"], ["0"]], "bar": null}

v_2 =

@matrix {"a": [["-2/3"], ["0"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["4/3"], ["1"], ["0"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["0"], ["0"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. For direction v_2, multiplying by the original A gives the zero vector. Therefore A(p + s v_1 + t v_2) = A p + s A v_1 + t A v_2 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.2.12 - Find every solution

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-7", "0", "6", "5"], ["0", "0", "1", "-2", "-3"], ["-1", "7", "-4", "2", "7"]], "bar": 4}

**Step 1: R3 ← R3 + (1)R1.** Add 1 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-7", "0", "6", "5"], ["0", "0", "1", "-2", "-3"], ["0", "0", "-4", "8", "12"]], "bar": 4}

**Step 2: R3 ← R3 + (4)R2.** Add 4 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-7", "0", "6", "5"], ["0", "0", "1", "-2", "-3"], ["0", "0", "0", "0", "0"]], "bar": 4}

**Read the equations.** x_1 - 7 x_2 + 6 x_4 = 5; x_3 - 2 x_4 = -3

The pivot columns are 1, 3. Thus x_1, x_3 are basic variables. x_2, x_4 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_2 = s, x_4 = t with all parameters real. The complete coordinate answer is:

@eq x_1 = 5 + 7 s - 6 t

@eq x_2 = s

@eq x_3 = -3 + 2 t

@eq x_4 = t

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1 + t v_2, where:

p =

@matrix {"a": [["5"], ["0"], ["-3"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["7"], ["1"], ["0"], ["0"]], "bar": null}

v_2 =

@matrix {"a": [["-6"], ["0"], ["2"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["12"], ["1"], ["-3"], ["0"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["5"], ["-3"], ["7"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. For direction v_2, multiplying by the original A gives the zero vector. Therefore A(p + s v_1 + t v_2) = A p + s A v_1 + t A v_2 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.2.13 - Find every solution

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 104.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-3", "0", "-1", "0", "-2"], ["0", "1", "0", "0", "-4", "1"], ["0", "0", "0", "1", "9", "-4"], ["0", "0", "0", "0", "0", "0"]], "bar": 5}

**Step 1: R1 ← R1 + (1)R3.** Add 1 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "0", "0", "9", "-6"], ["0", "1", "0", "0", "-4", "1"], ["0", "0", "0", "1", "9", "-4"], ["0", "0", "0", "0", "0", "0"]], "bar": 5}

**Step 2: R1 ← R1 + (3)R2.** Add 3 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "0", "-3", "-3"], ["0", "1", "0", "0", "-4", "1"], ["0", "0", "0", "1", "9", "-4"], ["0", "0", "0", "0", "0", "0"]], "bar": 5}

**Read the equations.** x_1 - 3 x_5 = -3; x_2 - 4 x_5 = 1; x_4 + 9 x_5 = -4

The pivot columns are 1, 2, 4. Thus x_1, x_2, x_4 are basic variables. x_3, x_5 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_3 = s, x_5 = t with all parameters real. The complete coordinate answer is:

@eq x_1 = -3 + 3 t

@eq x_2 = 1 + 4 t

@eq x_3 = s

@eq x_4 = -4 - 9 t

@eq x_5 = t

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1 + t v_2, where:

p =

@matrix {"a": [["-3"], ["1"], ["0"], ["-4"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["0"], ["0"], ["1"], ["0"], ["0"]], "bar": null}

v_2 =

@matrix {"a": [["3"], ["4"], ["0"], ["-9"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["-3"], ["1"], ["1"], ["-4"], ["0"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["-2"], ["1"], ["-4"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. For direction v_2, multiplying by the original A gives the zero vector. Therefore A(p + s v_1 + t v_2) = A p + s A v_1 + t A v_2 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.2.14 - Find every solution

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "2", "-5", "-4", "0", "-5"], ["0", "1", "-6", "-4", "0", "2"], ["0", "0", "0", "0", "1", "0"], ["0", "0", "0", "0", "0", "0"]], "bar": 5}

**Step 1: R1 ← R1 + (-2)R2.** Add -2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "7", "4", "0", "-9"], ["0", "1", "-6", "-4", "0", "2"], ["0", "0", "0", "0", "1", "0"], ["0", "0", "0", "0", "0", "0"]], "bar": 5}

**Read the equations.** x_1 + 7 x_3 + 4 x_4 = -9; x_2 - 6 x_3 - 4 x_4 = 2; x_5 = 0

The pivot columns are 1, 2, 5. Thus x_1, x_2, x_5 are basic variables. x_3, x_4 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_3 = s, x_4 = t with all parameters real. The complete coordinate answer is:

@eq x_1 = -9 - 7 s - 4 t

@eq x_2 = 2 + 6 s + 4 t

@eq x_3 = s

@eq x_4 = t

@eq x_5 = 0

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1 + t v_2, where:

p =

@matrix {"a": [["-9"], ["2"], ["0"], ["0"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["-7"], ["6"], ["1"], ["0"], ["0"]], "bar": null}

v_2 =

@matrix {"a": [["-4"], ["4"], ["0"], ["1"], ["0"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["-16"], ["8"], ["1"], ["0"], ["0"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["-5"], ["2"], ["0"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. For direction v_2, multiplying by the original A gives the zero vector. Therefore A(p + s v_1 + t v_2) = A p + s A v_1 + t A v_2 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.2.15 - Write the equations and verify Exercise 9

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 105.

To verify the full solution set rather than one numerical sample, first obtain its exact parameterization and then substitute the constant and every parameter direction into the original coefficient matrix. The final verification below performs this check for all parameter values.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["0", "1", "-6", "5"], ["1", "-2", "7", "-4"]], "bar": 3}

**Step 1: R1 ↔ R2.** Move a nonzero entry into row 1 so that it can be used as a pivot.

@matrix {"a": [["1", "-2", "7", "-4"], ["0", "1", "-6", "5"]], "bar": 3}

**Step 2: R1 ← R1 + (2)R2.** Add 2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-5", "6"], ["0", "1", "-6", "5"]], "bar": 3}

**Read the equations.** x_1 - 5 x_3 = 6; x_2 - 6 x_3 = 5

The pivot columns are 1, 2. Thus x_1, x_2 are basic variables. x_3 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_3 = s with all parameters real. The complete coordinate answer is:

@eq x_1 = 6 + 5 s

@eq x_2 = 5 + 6 s

@eq x_3 = s

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1, where:

p =

@matrix {"a": [["6"], ["5"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["5"], ["6"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["11"], ["11"], ["1"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["5"], ["-4"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. Therefore A(p + s v_1) = A p + s A v_1 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.2.16 - Write the equations and verify Exercise 10

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

To verify the full solution set rather than one numerical sample, first obtain its exact parameterization and then substitute the constant and every parameter direction into the original coefficient matrix. The final verification below performs this check for all parameter values.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-2", "-1", "3"], ["3", "-6", "-2", "2"]], "bar": 3}

**Step 1: R2 ← R2 + (-3)R1.** Add -3 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-2", "-1", "3"], ["0", "0", "1", "-7"]], "bar": 3}

**Step 2: R1 ← R1 + (1)R2.** Add 1 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-2", "0", "-4"], ["0", "0", "1", "-7"]], "bar": 3}

**Read the equations.** x_1 - 2 x_2 = -4; x_3 = -7

The pivot columns are 1, 3. Thus x_1, x_3 are basic variables. x_2 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_2 = s with all parameters real. The complete coordinate answer is:

@eq x_1 = -4 + 2 s

@eq x_2 = s

@eq x_3 = -7

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1, where:

p =

@matrix {"a": [["-4"], ["0"], ["-7"]], "bar": null}

v_1 =

@matrix {"a": [["2"], ["1"], ["0"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["-2"], ["1"], ["-7"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["3"], ["2"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. Therefore A(p + s v_1) = A p + s A v_1 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.2.17 - Write the equations and verify Exercise 11

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 105.

To verify the full solution set rather than one numerical sample, first obtain its exact parameterization and then substitute the constant and every parameter direction into the original coefficient matrix. The final verification below performs this check for all parameter values.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["3", "-4", "2", "0"], ["-9", "12", "-6", "0"], ["-6", "8", "-4", "0"]], "bar": 3}

**Step 1: R1 ← (1/3)R1.** Multiply every entry of row 1, including any right-hand side, by 1/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-4/3", "2/3", "0"], ["-9", "12", "-6", "0"], ["-6", "8", "-4", "0"]], "bar": 3}

**Step 2: R2 ← R2 + (9)R1.** Add 9 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-4/3", "2/3", "0"], ["0", "0", "0", "0"], ["-6", "8", "-4", "0"]], "bar": 3}

**Step 3: R3 ← R3 + (6)R1.** Add 6 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-4/3", "2/3", "0"], ["0", "0", "0", "0"], ["0", "0", "0", "0"]], "bar": 3}

**Read the equations.** x_1 - 4/3 x_2 + 2/3 x_3 = 0

The pivot columns are 1. Thus x_1 are basic variables. x_2, x_3 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_2 = s, x_3 = t with all parameters real. The complete coordinate answer is:

@eq x_1 = 4/3 s - 2/3 t

@eq x_2 = s

@eq x_3 = t

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1 + t v_2, where:

p =

@matrix {"a": [["0"], ["0"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["4/3"], ["1"], ["0"]], "bar": null}

v_2 =

@matrix {"a": [["-2/3"], ["0"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["4/3"], ["1"], ["0"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["0"], ["0"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. For direction v_2, multiplying by the original A gives the zero vector. Therefore A(p + s v_1 + t v_2) = A p + s A v_1 + t A v_2 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.2.18 - Write the equations and verify Exercise 12

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

To verify the full solution set rather than one numerical sample, first obtain its exact parameterization and then substitute the constant and every parameter direction into the original coefficient matrix. The final verification below performs this check for all parameter values.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-7", "0", "6", "5"], ["0", "0", "1", "-2", "-3"], ["-1", "7", "-4", "2", "7"]], "bar": 4}

**Step 1: R3 ← R3 + (1)R1.** Add 1 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-7", "0", "6", "5"], ["0", "0", "1", "-2", "-3"], ["0", "0", "-4", "8", "12"]], "bar": 4}

**Step 2: R3 ← R3 + (4)R2.** Add 4 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-7", "0", "6", "5"], ["0", "0", "1", "-2", "-3"], ["0", "0", "0", "0", "0"]], "bar": 4}

**Read the equations.** x_1 - 7 x_2 + 6 x_4 = 5; x_3 - 2 x_4 = -3

The pivot columns are 1, 3. Thus x_1, x_3 are basic variables. x_2, x_4 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_2 = s, x_4 = t with all parameters real. The complete coordinate answer is:

@eq x_1 = 5 + 7 s - 6 t

@eq x_2 = s

@eq x_3 = -3 + 2 t

@eq x_4 = t

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1 + t v_2, where:

p =

@matrix {"a": [["5"], ["0"], ["-3"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["7"], ["1"], ["0"], ["0"]], "bar": null}

v_2 =

@matrix {"a": [["-6"], ["0"], ["2"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["12"], ["1"], ["-3"], ["0"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["5"], ["-3"], ["7"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. For direction v_2, multiplying by the original A gives the zero vector. Therefore A(p + s v_1 + t v_2) = A p + s A v_1 + t A v_2 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.2.19 - Consistency and uniqueness of symbolic echelon patterns

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 105.

(a) has pivots in all three coefficient columns and none in the last column. There is no contradictory row and no free variable, so it is consistent with a unique solution. (b) has a required nonzero pivot in the final appended column of its last row. That row means 0 = p with p ≠ 0, so it is inconsistent regardless of the entries marked *. The number of other free columns cannot remove that contradiction.


### 1.2.20 - Consistency and uniqueness of symbolic echelon patterns

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

(a) has two coefficient columns, both pivot columns, and a zero last row. The zero row is 0 = 0, so the system is consistent with a unique solution. (b) has five columns in total: four coefficient columns and one appended column. Its three pivots are in coefficient columns 1,3,4. No last-column pivot appears, so the system is consistent. Column 2 is free, giving infinitely many solutions. In both parts, consistency must be decided before uniqueness.


### 1.2.21 - Choose h for consistency

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 105.

Apply R₂ ← R₂ - 2R₁. The last equation is 0 = 7 - 2h. It is true exactly when h = 7/2; then the first row still has solutions and the second is redundant. Any other h leaves a contradiction. Thus the allowed value is 7/2.


### 1.2.22 - Choose h for consistency

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Apply R₂ ← R₂ - 5R₁. The second row becomes [0,h + 15 | 3]. If h = -15, it states 0 = 3 and is impossible. For any h ≠ -15, it determines x₂ = 3/(h + 15), and row 1 determines x₁. Therefore consistency holds exactly for h ≠ -15.


### 1.2.23 - Choose h,k for none, one, or infinitely many

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Subtract four times equation 1 from equation 2 to obtain (8 - 4h)x₂ = k - 8. No solution requires h = 2,k ≠ 8, for example (h,k) = (2,0). A unique solution requires h ≠ 2, with any k, for example (0,0). Infinitely many require h = 2,k = 8, making the second equation a repeat of the first. These are all cases because a one-variable equation has either a nonzero coefficient or a zero coefficient, with a zero or nonzero right side.


### 1.2.24 - Choose h,k for none, one, or infinitely many

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Subtract three times equation 1 from equation 2. The remaining constraint is (h - 9)x₂ = k - 6. No solution occurs for h = 9,k ≠ 6; choose (9,0). A unique solution occurs for h ≠ 9, any k; choose (0,0). Infinitely many occur exactly for h = 9,k = 6. When the second row is 0 = 0, x₂ is free and row 1 gives x₁ = 2 - 3x₂.


### 1.2.25 - True/false: Different reductions may give different RREFs

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** RREF is unique within a row-equivalence class. Different pivot choices can give different intermediate arrays and REF matrices, but satisfying all RREF conditions yields the same final matrix.


### 1.2.26 - True/false: Echelon form is unique

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** The row matrices [1,2] and [2,4] are row equivalent and both REF, but unequal. Only the reduced echelon form is unique; scaling a leading entry can change an ordinary echelon form.


### 1.2.27 - True/false: The algorithm applies only to augmented matrices

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** Row operations apply to any rectangular matrix. For example, Exercises 3 and 4 ask for reduction of a matrix without declaring its last column a right-hand side. The algorithm is not limited to system notation.


### 1.2.28 - True/false: Pivot positions depend on row interchange choices

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** Pivot positions are defined by the unique RREF, so choices during valid reduction cannot alter them. The actual numerical pivots used in intermediate steps may differ, which is a different notion.


### 1.2.29 - True/false: A basic variable corresponds to a coefficient pivot column

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** This is the definition. The restriction to coefficient columns matters because an appended pivot is a consistency obstruction, not another input variable.


### 1.2.30 - True/false: REF is obtained by the forward phase

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** The forward phase places pivots from left to right and clears below them. Clearing above pivots and normalizing any remaining nonunit pivots completes the backward phase to RREF.


### 1.2.31 - True/false: A parametric description solves the system

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** A complete parametric description lists every solution and only solutions. That is precisely what solving asks for. An incomplete subset, such as setting all free variables to zero, would not solve the whole system.


### 1.2.32 - True/false: Free variables imply a unique solution

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** A consistent system x₁ + x₂ = 1 has free x₂ and solutions (1 - t,t), giving infinitely many. If a system with a nonpivot coefficient column is inconsistent, it has no solutions instead. Neither case establishes uniqueness.


### 1.2.33 - True/false: A final row [0,0,0,0,5] implies inconsistency

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** Interpreting the last entry as appended constant gives 0 = 5. No variable values satisfy it, and row operations preserve solutions, so the original system has none.


### 1.2.34 - True/false: A general solution explicitly describes every solution

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** This is what general means: the parameters produce all possible solutions, rather than one example. It must include the values or formulas for each original variable and specify any free parameters.


### 1.2.35 - Three pivots in a 3 × 5 coefficient matrix

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 105.

Yes, the system is consistent for every right-hand side. Three pivots distributed among three rows put a pivot in every coefficient row. No zero coefficient row remains to support a nonzero appended pivot. The existence theorem therefore applies. There are still two nonpivot coefficient columns, so consistency does not mean uniqueness.


### 1.2.36 - Last column of a 3 × 5 augmented matrix is pivot

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

No, the system is inconsistent. There are four coefficient columns; the fifth is the appended right-hand side. A pivot there is a row with four coefficient zeros followed by a nonzero constant. It expresses an impossible equation. It is not a fifth unknown.


### 1.2.37 - Why does a row pivot everywhere imply consistency?

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 105.

After row-reducing the coefficient matrix, each row has a nonzero leading coefficient. Carrying any right-hand side through the same operations cannot create an extra row beyond these coefficient rows. Thus no equation 0 = nonzero occurs. One can choose free variables and back substitute, so the system is consistent for every right-hand side.


### 1.2.38 - Three equations, three variables, every column pivot

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Three column pivots in a 3 × 3 coefficient matrix also occupy all three rows. Therefore every b is consistent. Every unknown is basic because each column has a pivot, so no free choices remain. Combining existence and absence of free variables proves exactly one solution. Squareness is needed to infer all-row pivots from all-column pivots here.


### 1.2.39 - Restate uniqueness using pivot columns

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

For a consistent system, the solution is unique if and only if every coefficient column is a pivot column. A nonpivot coefficient column is a free variable and permits multiple solutions. The consistency assumption already rules out a pivot in the appended column; do not count that column as an unknown.


### 1.2.40 - Pivot information for a unique consistent solution

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The appended column must not be a pivot column, ensuring existence. Every coefficient column must be a pivot column, ensuring no free variables. Both conditions are required. If either fails, the system has no solution or infinitely many, respectively. Extra zero rows are allowed when there are more equations than unknowns.


### 1.2.41 - Cut-off underdetermined-system question

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The scan supplies only the opening definition: fewer equations than unknowns is called underdetermined. Its actual requested subparts or continuation are absent. No specific answer to the missing task can be reconstructed faithfully. The readable mathematical statement implies that a consistent underdetermined system has a free variable and therefore infinitely many solutions; it may also be inconsistent. This observation addresses only the visible definition, not an invented continuation. A better scan of the following original textbook page is needed for the complete question.


# Section 1.3 - Vector equations


Original question pages follow. They preserve the exact wording, subparts, diagrams, and numerical data of the supplied exercise scans. Worked solutions begin immediately after these pages. A brief paraphrase at each answer identifies the task; consult the reproduced question for its full wording.


## Original exercises - source PDF page 5

@scan ex-05.png

@page


## Original exercises - source PDF page 6

@scan ex-06.png

@page


## Worked solutions


### 1.3.1 - Compute u + v and u - 2v

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 106.

Add matching entries for u + v. For u - 2v, first multiply every entry of v by 2, then subtract matching entries.

u + v =

@matrix {"a": [["-4"], ["5"]], "bar": null}

u - 2v =

@matrix {"a": [["5"], ["-4"]], "bar": null}

Each vector retains the original number of entries; the scalar 2 multiplies the entire vector v.


### 1.3.2 - Compute u + v and u - 2v

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Add matching entries for u + v. For u - 2v, first multiply every entry of v by 2, then subtract matching entries.

u + v =

@matrix {"a": [["5"], ["5"]], "bar": null}

u - 2v =

@matrix {"a": [["-1"], ["-4"]], "bar": null}

Each vector retains the original number of entries; the scalar 2 multiplies the entire vector v.


### 1.3.3 - Draw the requested vector arrows

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 106.

Draw every arrow from the origin to its endpoint: u = (-1,2), v = (-3,3), -v = (3,-3), -2v = (6,-6), u + v = (-4,5), u - v = (2,-1), and u - 2v = (5,-4). Multiplication by a negative scalar reverses the v direction. To check the parallelogram, its adjacent corners are 0,u,-v and its opposite corner is u + (-v) = (2,-1). The figure below is a coordinate sketch of these exact endpoints.

@customfig vector3


### 1.3.4 - Draw the requested vector arrows

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Use endpoints u = (3,2), v = (2,3), -v = (-2,-3), -2v = (-4,-6), u + v = (5,5), u - v = (1,-1), and u - 2v = (-1,-4). These come from scaling every coordinate and then adding corresponding coordinates. The parallelogram with corners 0,u,-v has fourth corner u - v = (1,-1). All arrows and the parallelogram are shown below.

@customfig vector4


### 1.3.5 - Convert the vector equation to a system

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Equate corresponding entries. The first row gives 6x₁ - 3x₂ = 1, the second gives -x₁ + 4x₂ = -7, and the third gives 5x₁ + 0x₂ = -5. Thus the equivalent system is 6x₁ - 3x₂ = 1; -x₁ + 4x₂ = -7; 5x₁ = -5. This is a conversion question, so no solving is required. The zero entry in the second vector is why its coefficient vanishes in the last equation.


### 1.3.6 - Convert the vector equation to a system

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The vectors have two entries, so there are two equations, even though there are three weights. Entry 1 gives -2x₁ + 8x₂ + x₃ = 0; entry 2 gives 3x₁ + 5x₂ - 6x₃ = 0. The three supplied vectors are coefficient columns, not three separate equations. Conversely, collecting those two equations by unknown reproduces the given vector equation.


### 1.3.7 - Read a,b,c,d from the oblique grid

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 107.

Use the two slanted grid directions as u and v coordinates. Starting at 0, a is one step along u and two steps opposite v, so a = u - 2v. Moving one more u step gives b = 2u - 2v. Point c is 3/2 v-steps to the negative-v side of b, hence c = 2u - (7/2)v. Point d is three u-steps and four negative v-steps from 0, so d = 3u - 4v. The two directions are not parallel and their grid extends across the whole plane, so every vector in ℝ^2 can be expressed using u,v. Half steps are allowed because the weights are real, not restricted to integers.


### 1.3.8 - Read w,x,y,z from the oblique grid

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The grid gives w = -u + 2v, x = -2u + 2v, y = -2u + (7/2)v, and z = -3u + 4v. For example, w lies one u-step below the point 2v, while x lies two u-steps below 2v. Points y and z can be obtained by reversing the walks for c and d in Exercise 7: y = -c and z = -d. All of ℝ^2 is obtainable because the two displayed directions are independent, so their linear combinations fill the plane. The grid indicates geometric weights, not physical pixel distances along the printed page.


### 1.3.9 - Write an equivalent vector equation

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 107.

Read the coefficients vertically by variable. The x₁ column is (0,4,-1), the x₂ column is (1,6,3), and the x₃ column is (5,-1,-8). Therefore x₁(0,4,-1) + x₂(1,6,3) + x₃(5,-1,-8) = (0,0,0). Expanding the three entries reproduces x₂ + 5x₃ = 0; 4x₁ + 6x₂ - x₃ = 0; -x₁ + 3x₂ - 8x₃ = 0.


### 1.3.10 - Write an equivalent vector equation

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The coefficients of x₁ are (4,1,8), those of x₂ are (1,-7,6), and those of x₃ are (3,-2,-5). Thus x₁(4,1,8) + x₂(1,-7,6) + x₃(3,-2,-5) = (9,2,15). The right side contains the original constants in equation order. Equality of corresponding entries proves equivalence of the vector equation and the three original equations.


### 1.3.11 - Is the target a linear combination of the columns?

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 108.

The target belongs to the requested span exactly when this augmented system has a solution. Its solution entries are the weights on the original columns.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "0", "5", "2"], ["-2", "1", "-6", "-1"], ["0", "2", "8", "6"]], "bar": 3}

**Step 1: R2 ← R2 + (2)R1.** Add 2 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "5", "2"], ["0", "1", "4", "3"], ["0", "2", "8", "6"]], "bar": 3}

**Step 2: R3 ← R3 + (-2)R2.** Add -2 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "5", "2"], ["0", "1", "4", "3"], ["0", "0", "0", "0"]], "bar": 3}

**Read the equations.** x_1 + 5 x_3 = 2; x_2 + 4 x_3 = 3

The pivot columns are 1, 2. Thus x_1, x_2 are basic variables. x_3 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_3 = s with all parameters real. The complete coordinate answer is:

@eq x_1 = 2 - 5 s

@eq x_2 = 3 - 4 s

@eq x_3 = s

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1, where:

p =

@matrix {"a": [["2"], ["3"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["-5"], ["-4"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["-3"], ["-1"], ["1"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["2"], ["-1"], ["6"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. Therefore A(p + s v_1) = A p + s A v_1 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.3.12 - Is the target a linear combination of the columns?

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The target belongs to the requested span exactly when this augmented system has a solution. Its solution entries are the weights on the original columns.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "0", "2", "-5"], ["-2", "5", "0", "11"], ["2", "5", "8", "-7"]], "bar": 3}

**Step 1: R2 ← R2 + (2)R1.** Add 2 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "2", "-5"], ["0", "5", "4", "1"], ["2", "5", "8", "-7"]], "bar": 3}

**Step 2: R3 ← R3 + (-2)R1.** Add -2 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "2", "-5"], ["0", "5", "4", "1"], ["0", "5", "4", "3"]], "bar": 3}

**Step 3: R2 ← (1/5)R2.** Multiply every entry of row 2, including any right-hand side, by 1/5. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "0", "2", "-5"], ["0", "1", "4/5", "1/5"], ["0", "5", "4", "3"]], "bar": 3}

**Step 4: R3 ← R3 + (-5)R2.** Add -5 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "2", "-5"], ["0", "1", "4/5", "1/5"], ["0", "0", "0", "2"]], "bar": 3}

**Step 5: R3 ← (1/2)R3.** Multiply every entry of row 3, including any right-hand side, by 1/2. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "0", "2", "-5"], ["0", "1", "4/5", "1/5"], ["0", "0", "0", "1"]], "bar": 3}

**Step 6: R1 ← R1 + (5)R3.** Add 5 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "2", "0"], ["0", "1", "4/5", "1/5"], ["0", "0", "0", "1"]], "bar": 3}

**Step 7: R2 ← R2 + (-1/5)R3.** Add -1/5 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "2", "0"], ["0", "1", "4/5", "0"], ["0", "0", "0", "1"]], "bar": 3}

A row now states 0 = 1. No choices of the unknowns can make that true. The system is inconsistent, and its solution set is empty. Free-looking coefficient columns cannot remove a contradiction.


### 1.3.13 - Is the target a linear combination of the columns?

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 108.

The target belongs to the requested span exactly when this augmented system has a solution. Its solution entries are the weights on the original columns.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-4", "2", "3"], ["0", "3", "5", "-7"], ["-2", "8", "-4", "-3"]], "bar": 3}

**Step 1: R3 ← R3 + (2)R1.** Add 2 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-4", "2", "3"], ["0", "3", "5", "-7"], ["0", "0", "0", "3"]], "bar": 3}

**Step 2: R2 ← (1/3)R2.** Multiply every entry of row 2, including any right-hand side, by 1/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-4", "2", "3"], ["0", "1", "5/3", "-7/3"], ["0", "0", "0", "3"]], "bar": 3}

**Step 3: R3 ← (1/3)R3.** Multiply every entry of row 3, including any right-hand side, by 1/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-4", "2", "3"], ["0", "1", "5/3", "-7/3"], ["0", "0", "0", "1"]], "bar": 3}

**Step 4: R1 ← R1 + (-3)R3.** Add -3 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-4", "2", "0"], ["0", "1", "5/3", "-7/3"], ["0", "0", "0", "1"]], "bar": 3}

**Step 5: R2 ← R2 + (7/3)R3.** Add 7/3 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-4", "2", "0"], ["0", "1", "5/3", "0"], ["0", "0", "0", "1"]], "bar": 3}

**Step 6: R1 ← R1 + (4)R2.** Add 4 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "26/3", "0"], ["0", "1", "5/3", "0"], ["0", "0", "0", "1"]], "bar": 3}

A row now states 0 = 1. No choices of the unknowns can make that true. The system is inconsistent, and its solution set is empty. Free-looking coefficient columns cannot remove a contradiction.


### 1.3.14 - Is the target a linear combination of the columns?

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The target belongs to the requested span exactly when this augmented system has a solution. Its solution entries are the weights on the original columns.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-2", "-6", "11"], ["0", "3", "7", "-5"], ["1", "-2", "5", "9"]], "bar": 3}

**Step 1: R3 ← R3 + (-1)R1.** Add -1 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-2", "-6", "11"], ["0", "3", "7", "-5"], ["0", "0", "11", "-2"]], "bar": 3}

**Step 2: R2 ← (1/3)R2.** Multiply every entry of row 2, including any right-hand side, by 1/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-2", "-6", "11"], ["0", "1", "7/3", "-5/3"], ["0", "0", "11", "-2"]], "bar": 3}

**Step 3: R3 ← (1/11)R3.** Multiply every entry of row 3, including any right-hand side, by 1/11. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-2", "-6", "11"], ["0", "1", "7/3", "-5/3"], ["0", "0", "1", "-2/11"]], "bar": 3}

**Step 4: R1 ← R1 + (6)R3.** Add 6 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-2", "0", "109/11"], ["0", "1", "7/3", "-5/3"], ["0", "0", "1", "-2/11"]], "bar": 3}

**Step 5: R2 ← R2 + (-7/3)R3.** Add -7/3 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-2", "0", "109/11"], ["0", "1", "0", "-41/33"], ["0", "0", "1", "-2/11"]], "bar": 3}

**Step 6: R1 ← R1 + (2)R2.** Add 2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "245/33"], ["0", "1", "0", "-41/33"], ["0", "0", "1", "-2/11"]], "bar": 3}

**Read the equations.** x_1 = 245/33; x_2 = -41/33; x_3 = -2/11

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["245/33"], ["-41/33"], ["-2/11"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["11"], ["-5"], ["9"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.3.15 - List five vectors in the span with their weights

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 108.

Choose weights (0,0),(1,0),(0,1),(1,1),(1,-1). They give five explicit combinations:

0v₁ + (0)v₂ =

@matrix {"a": [["0"], ["0"], ["0"]], "bar": null}

1v₁ + (0)v₂ =

@matrix {"a": [["7"], ["1"], ["-6"]], "bar": null}

0v₁ + (1)v₂ =

@matrix {"a": [["-5"], ["3"], ["0"]], "bar": null}

1v₁ + (1)v₂ =

@matrix {"a": [["2"], ["4"], ["-6"]], "bar": null}

1v₁ + (-1)v₂ =

@matrix {"a": [["12"], ["-2"], ["-6"]], "bar": null}

Each is in the span by its displayed construction. Zero weights are allowed, so the zero vector is included. No diagram is required by the source question.


### 1.3.16 - List five vectors in the span with their weights

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Choose weights (0,0),(1,0),(0,1),(1,1),(1,-1). They give five explicit combinations:

0v₁ + (0)v₂ =

@matrix {"a": [["0"], ["0"], ["0"]], "bar": null}

1v₁ + (0)v₂ =

@matrix {"a": [["3"], ["0"], ["2"]], "bar": null}

0v₁ + (1)v₂ =

@matrix {"a": [["-2"], ["0"], ["3"]], "bar": null}

1v₁ + (1)v₂ =

@matrix {"a": [["1"], ["0"], ["5"]], "bar": null}

1v₁ + (-1)v₂ =

@matrix {"a": [["5"], ["0"], ["-1"]], "bar": null}

Each is in the span by its displayed construction. Zero weights are allowed, so the zero vector is included. No diagram is required by the source question.


### 1.3.17 - Choose h so b lies in the spanned plane

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Let b = αa₁ + βa₂. The first two coordinate equations are α - 2β = 4 and 4α - 3β = 1. Substituting α = 4 + 2β into the second gives 16 + 5β = 1, so β = -3 and α = -2. The third coordinate must therefore equal -2α + 7β = 4 - 21 = -17. Thus h = -17 is necessary and sufficient. At that value, -2a₁ - 3a₂ = (4,1,-17), verifying membership.


### 1.3.18 - Choose h so y lies in the generated plane

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Write y = αv₁ + βv₂. The second coordinate gives β = -5. The third gives -2α + 8(-5) = -3, so α = -37/2. The first must then be h = α - 3β = -37/2 + 15 = -7/2. Substituting these weights produces (-7/2,-5,-3), so this value is sufficient as well as necessary.


### 1.3.19 - Describe the span geometrically

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The vector (12,3,-9) is 3/2 times (8,2,-6). Hence every combination of the two is a multiple of the first. Their span is the line {t(8,2,-6): t ∈ ℝ}, passing through the origin. It is not a plane because the second generator supplies no new direction. The first vector is nonzero, so the span is more than just {0}.


### 1.3.20 - Describe the span of Exercise 16 geometrically

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Both vectors (3,0,2) and (-2,0,3) have zero second coordinate, so their span is contained in the x₁x₃-plane. They are independent because a scalar matching the first entries would be -2/3, which does not match the third entries. More explicitly, an arbitrary (r,0,s) is α(3,0,2) + β(-2,0,3) with α = (3r + 2s)/13 and β = (-2r + 3s)/13. Thus every point of that plane is obtained, and the span equals the plane.


### 1.3.21 - Show that every (h,k) is in Span{u,v}

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The entry equations are 2α + 2β = h and -α + β = k. Adding after solving gives α = h/4 - k/2 and β = h/4 + k/2. These formulas are defined for every real h,k because their denominators are fixed nonzero numbers. Substitution gives first entry h and second entry k. Therefore every vector in ℝ^2 is in the span, not merely some selected numerical targets.


### 1.3.22 - Construct a nonzero-entry matrix whose columns miss b

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Choose A with every entry 1, and b = (1,0,0). Each column is (1,1,1), so any column combination has the form (t,t,t). It cannot equal b because its first and second entries would need to be both 1 and 0. All nine entries of A are nonzero and b lies in ℝ^3, satisfying the question. Dependence of the columns here leaves only a line of reachable outputs.


### 1.3.23 - True/false: A column (-4,3) may also be denoted [-4 3]

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** The displayed horizontal array is a 1 × 2 row matrix, whereas the given vector is a 2 × 1 column. Equal matrices require matching sizes. An ordered-pair notation in prose can stand for a vector, but a displayed row matrix is not literally the same matrix.


### 1.3.24 - True/false: A list of five real numbers is a vector in ℝ^5

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** In the course convention, the ordered list supplies the five entries of a column vector. The coordinates may be arbitrary real numbers; the superscript 5 records the entry count.


### 1.3.25 - True/false: (-2,5) and (-5,2) lie on one line through zero

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** If the second were c times the first, the first entries would give c = 5/2, but the second entries would then give 25/2 rather than 2. Thus the vectors are not scalar multiples and do not lie on one origin line.


### 1.3.26 - True/false: Adding u - v to v gives u

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** Entrywise, (u_i - v_i) + v_i = u_i for every i. Equivalently, associativity and additive inverses give (u - v) + v = u + (-v + v) = u.


### 1.3.27 - True/false: One half of v₁ is a linear combination of v₁,v₂

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** Use weights 1/2 and 0. The definition permits zero weights, so (1/2)v₁ + 0v₂ is a valid combination even though the second vector makes no contribution.


### 1.3.28 - True/false: Linear-combination weights cannot all be zero

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** That restriction belongs to a dependence relation, not an arbitrary linear combination. All-zero weights give the zero vector, which is always in a span.


### 1.3.29 - True/false: The augmented system and its vector equation have the same solutions

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** The weighted column combination equals b exactly when each coordinate equation is satisfied. Those coordinate equations are precisely the rows of [a₁ a₂ a₃ | b], with the same unknown weights.


### 1.3.30 - True/false: For nonzero u,v, the span includes the line through u and zero

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** Set the weight of v to 0 and let the weight of u vary over ℝ. This produces every tu, the entire origin line through u, regardless of whether v adds another direction.


### 1.3.31 - True/false: Span{u,v} is always a plane

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** If v = 2u with u ≠ 0, all combinations are multiples of u, so the span is a line. If both vectors are zero it is {0}. A genuine plane requires independent directions.


### 1.3.32 - True/false: Testing consistency of [a₁ a₂ a₃ | b] tests span membership

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** A solution provides weights producing b from the three columns, which is exactly membership in their span. Inconsistency proves that no such weights exist.


### 1.3.33 - Distinguish the listed columns from their span

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 109.

Part (a): b is not equal to any of the three listed columns, so it is not in {a₁,a₂,a₃}, a set with three vectors. Part (b): W is their span and contains infinitely many vectors since a₁ ≠ 0; membership of b in W is decided by the following system. Part (c): independently of reduction, a₁ = 1a₁ + 0a₂ + 0a₃, so a₁ lies in W.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "0", "-4", "4"], ["0", "3", "-2", "1"], ["-2", "6", "3", "-4"]], "bar": 3}

**Step 1: R3 ← R3 + (2)R1.** Add 2 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-4", "4"], ["0", "3", "-2", "1"], ["0", "6", "-5", "4"]], "bar": 3}

**Step 2: R2 ← (1/3)R2.** Multiply every entry of row 2, including any right-hand side, by 1/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "0", "-4", "4"], ["0", "1", "-2/3", "1/3"], ["0", "6", "-5", "4"]], "bar": 3}

**Step 3: R3 ← R3 + (-6)R2.** Add -6 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-4", "4"], ["0", "1", "-2/3", "1/3"], ["0", "0", "-1", "2"]], "bar": 3}

**Step 4: R3 ← (-1)R3.** Multiply every entry of row 3, including any right-hand side, by -1. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "0", "-4", "4"], ["0", "1", "-2/3", "1/3"], ["0", "0", "1", "-2"]], "bar": 3}

**Step 5: R1 ← R1 + (4)R3.** Add 4 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "-4"], ["0", "1", "-2/3", "1/3"], ["0", "0", "1", "-2"]], "bar": 3}

**Step 6: R2 ← R2 + (2/3)R3.** Add 2/3 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "-4"], ["0", "1", "0", "-1"], ["0", "0", "1", "-2"]], "bar": 3}

**Read the equations.** x_1 = -4; x_2 = -1; x_3 = -2

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["-4"], ["-1"], ["-2"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["4"], ["1"], ["-4"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.3.34 - Is b in W, and why is the third column in W?

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Part (a) is the consistency test below. Part (b) follows directly from the definition: a₃ = 0a₁ + 0a₂ + 1a₃, so the third column belongs to W even without solving any equations.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["2", "0", "6", "10"], ["-1", "8", "5", "3"], ["1", "-2", "1", "3"]], "bar": 3}

**Step 1: R1 ← (1/2)R1.** Multiply every entry of row 1, including any right-hand side, by 1/2. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "0", "3", "5"], ["-1", "8", "5", "3"], ["1", "-2", "1", "3"]], "bar": 3}

**Step 2: R2 ← R2 + (1)R1.** Add 1 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "3", "5"], ["0", "8", "8", "8"], ["1", "-2", "1", "3"]], "bar": 3}

**Step 3: R3 ← R3 + (-1)R1.** Add -1 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "3", "5"], ["0", "8", "8", "8"], ["0", "-2", "-2", "-2"]], "bar": 3}

**Step 4: R2 ← (1/8)R2.** Multiply every entry of row 2, including any right-hand side, by 1/8. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "0", "3", "5"], ["0", "1", "1", "1"], ["0", "-2", "-2", "-2"]], "bar": 3}

**Step 5: R3 ← R3 + (2)R2.** Add 2 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "3", "5"], ["0", "1", "1", "1"], ["0", "0", "0", "0"]], "bar": 3}

**Read the equations.** x_1 + 3 x_3 = 5; x_2 + x_3 = 1

The pivot columns are 1, 2. Thus x_1, x_2 are basic variables. x_3 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_3 = s with all parameters real. The complete coordinate answer is:

@eq x_1 = 5 - 3 s

@eq x_2 = 1 - s

@eq x_3 = s

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1, where:

p =

@matrix {"a": [["5"], ["1"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["-3"], ["-1"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["2"], ["0"], ["1"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["10"], ["3"], ["3"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. Therefore A(p + s v_1) = A p + s A v_1 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.3.35 - Mine production: interpretation, model, and operating days

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Part (a): 5v₁ = (100,2750) is five days of mine 1 output, with copper in metric tons and silver in kilograms. Part (b): x₁v₁ + x₂v₂ = (150,2825), where the weights are operating days. Part (c): solve that two-coordinate system as follows.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["20", "30", "150"], ["550", "500", "2825"]], "bar": 2}

**Step 1: R1 ← (1/20)R1.** Multiply every entry of row 1, including any right-hand side, by 1/20. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "3/2", "15/2"], ["550", "500", "2825"]], "bar": 2}

**Step 2: R2 ← R2 + (-550)R1.** Add -550 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3/2", "15/2"], ["0", "-325", "-1300"]], "bar": 2}

**Step 3: R2 ← (-1/325)R2.** Multiply every entry of row 2, including any right-hand side, by -1/325. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "3/2", "15/2"], ["0", "1", "4"]], "bar": 2}

**Step 4: R1 ← R1 + (-3/2)R2.** Add -3/2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "3/2"], ["0", "1", "4"]], "bar": 2}

**Read the equations.** x_1 = 3/2; x_2 = 4

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["3/2"], ["4"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["150"], ["2825"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.3.36 - Coal plant: heat, vector model, and fuel amounts

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Part (a): heat is 27.6x₁ + 30.2x₂ million Btu. Part (b): total output is x₁(27.6,3100,250) + x₂(30.2,6400,360), whose coordinates measure heat, sulfur dioxide grams, and particulate grams. Part (c): set this vector equal to (162,23610,1623). Decimal source coefficients are represented exactly as fractions during reduction. The weights give tons of anthracite and bituminous coal, respectively.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["138/5", "151/5", "162"], ["3100", "6400", "23610"], ["250", "360", "1623"]], "bar": 2}

**Step 1: R1 ← (5/138)R1.** Multiply every entry of row 1, including any right-hand side, by 5/138. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "151/138", "135/23"], ["3100", "6400", "23610"], ["250", "360", "1623"]], "bar": 2}

**Step 2: R2 ← R2 + (-3100)R1.** Add -3100 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "151/138", "135/23"], ["0", "207550/69", "124530/23"], ["250", "360", "1623"]], "bar": 2}

**Step 3: R3 ← R3 + (-250)R1.** Add -250 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "151/138", "135/23"], ["0", "207550/69", "124530/23"], ["0", "5965/69", "3579/23"]], "bar": 2}

**Step 4: R2 ← (69/207550)R2.** Multiply every entry of row 2, including any right-hand side, by 69/207550. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "151/138", "135/23"], ["0", "1", "9/5"], ["0", "5965/69", "3579/23"]], "bar": 2}

**Step 5: R3 ← R3 + (-5965/69)R2.** Add -5965/69 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "151/138", "135/23"], ["0", "1", "9/5"], ["0", "0", "0"]], "bar": 2}

**Step 6: R1 ← R1 + (-151/138)R2.** Add -151/138 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "39/10"], ["0", "1", "9/5"], ["0", "0", "0"]], "bar": 2}

**Read the equations.** x_1 = 39/10; x_2 = 9/5

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["39/10"], ["9/5"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["162"], ["23610"], ["1623"]], "bar": null}

These entries equal the original right-hand sides, in order.


# Section 1.4 - The matrix equation Ax = b


Original question pages follow. They preserve the exact wording, subparts, diagrams, and numerical data of the supplied exercise scans. Worked solutions begin immediately after these pages. A brief paraphrase at each answer identifies the task; consult the reproduced question for its full wording.


## Original exercises - source PDF page 7

@scan ex-07.png

@page


## Original exercises - source PDF page 8

@scan ex-08.png

@page


## Worked solutions


### 1.4.1 - Compute the product, or explain why undefined

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The left factor has 2 columns, whereas the right factor has 3 rows. The inner dimensions do not match, so this product is undefined. This is a dimension issue, not a product equal to zero.


### 1.4.2 - Compute the product, or explain why undefined

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The left factor has 1 columns, whereas the right factor has 2 rows. The inner dimensions do not match, so this product is undefined. This is a dimension issue, not a product equal to zero.


### 1.4.3 - Compute the product, or explain why undefined

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The product has 3 rows and 1 columns. Each entry uses one row of the left factor and one column of the right factor.

@eq c_{11} = (6)(1) + (5)(-3) = -9

@eq c_{21} = (-4)(1) + (-3)(-3) = 5

@eq c_{31} = (7)(1) + (6)(-3) = -11

Collect those entries in their row and column positions:

@matrix {"a": [["-9"], ["5"], ["-11"]], "bar": null}

As a second interpretation, column j of the answer is A times column j of B: it is a linear combination of the columns of A using the entries of that column of B as weights.


### 1.4.4 - Compute the product, or explain why undefined

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The product has 2 rows and 1 columns. Each entry uses one row of the left factor and one column of the right factor.

@eq c_{11} = (8)(1) + (3)(1) + (1)(1) = 12

@eq c_{21} = (5)(1) + (1)(1) + (2)(1) = 8

Collect those entries in their row and column positions:

@matrix {"a": [["12"], ["8"]], "bar": null}

As a second interpretation, column j of the answer is A times column j of B: it is a linear combination of the columns of A using the entries of that column of B as weights.


### 1.4.5 - Convert the matrix equation to a vector equation

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Use each input entry as the weight of the corresponding matrix column: 5(5,-2) - (1,-7) + 3(-8,3) - 2(4,-5) = (-8,16). Check the coordinates: 25 - 1 - 24 - 8 = -8 and -10 + 7 + 9 + 10 = 16. This matches the given equation and preserves the order of the four input weights.


### 1.4.6 - Convert the matrix equation to a vector equation

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The two columns are (7,2,9,-3) and (-3,1,-6,2), and the input weights are -2,-5. Thus -2(7,2,9,-3) - 5(-3,1,-6,2) = (1,-9,12,-4). Entrywise checks are -14 + 15 = 1, -4 - 5 = -9, -18 + 30 = 12, and 6 - 10 = -4.


### 1.4.7 - Convert the vector equation to matrix form

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Place the three four-entry vectors into columns, keeping their unknown weights in the same order. The equation is A(x₁,x₂,x₃) = (6,-8,0,-7), where:

@matrix {"a": [["4", "-5", "7"], ["-1", "3", "-8"], ["7", "-5", "0"], ["-4", "1", "2"]], "bar": null}

A is 4 × 3, so multiplying its three-entry input produces the four-entry target. Expanding the product by columns recovers the original vector equation.


### 1.4.8 - Convert the vector equation to matrix form

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Use the four supplied two-entry vectors as columns. Then [4,-4,-5,3;-2,5,4,0](z₁,z₂,z₃,z₄) = (4,13). The coefficient matrix is 2 × 4 and the unknown vector has four entries. Multiplication sums the four weighted columns, giving exactly the original vector equation.


### 1.4.9 - Write vector and matrix forms of the system

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 110.

The vector equation is x₁(3,0) + x₂(1,1) + x₃(-5,4) = (9,0). The matrix equation is [3,1,-5;0,1,4](x₁,x₂,x₃) = (9,0). In both forms, the missing x₁ term in the second equation is represented by a zero. Equating entries recovers the original system, so the solution sets agree.


### 1.4.10 - Write vector and matrix forms of the system

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The vector equation is x₁(8,5,1) + x₂(-1,4,-3) = (4,1,2). The matrix equation is [8,-1;5,4;1,-3](x₁,x₂) = (4,1,2). There are two unknowns and three equations, so the matrix must be 3 × 2. No solving is requested; the conversion is justified by expansion of Ax.


### 1.4.11 - Solve Ax = b and write the answer as a vector

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 110.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "2", "4", "-2"], ["0", "1", "5", "2"], ["-2", "-4", "-3", "9"]], "bar": 3}

**Step 1: R3 ← R3 + (2)R1.** Add 2 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "2", "4", "-2"], ["0", "1", "5", "2"], ["0", "0", "5", "5"]], "bar": 3}

**Step 2: R3 ← (1/5)R3.** Multiply every entry of row 3, including any right-hand side, by 1/5. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "2", "4", "-2"], ["0", "1", "5", "2"], ["0", "0", "1", "1"]], "bar": 3}

**Step 3: R1 ← R1 + (-4)R3.** Add -4 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "2", "0", "-6"], ["0", "1", "5", "2"], ["0", "0", "1", "1"]], "bar": 3}

**Step 4: R2 ← R2 + (-5)R3.** Add -5 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "2", "0", "-6"], ["0", "1", "0", "-3"], ["0", "0", "1", "1"]], "bar": 3}

**Step 5: R1 ← R1 + (-2)R2.** Add -2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "0"], ["0", "1", "0", "-3"], ["0", "0", "1", "1"]], "bar": 3}

**Read the equations.** x_1 = 0; x_2 = -3; x_3 = 1

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["0"], ["-3"], ["1"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["-2"], ["2"], ["9"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.4.12 - Solve Ax = b and write the answer as a vector

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "2", "1", "0"], ["-3", "-1", "2", "1"], ["0", "5", "3", "-1"]], "bar": 3}

**Step 1: R2 ← R2 + (3)R1.** Add 3 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "2", "1", "0"], ["0", "5", "5", "1"], ["0", "5", "3", "-1"]], "bar": 3}

**Step 2: R2 ← (1/5)R2.** Multiply every entry of row 2, including any right-hand side, by 1/5. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "2", "1", "0"], ["0", "1", "1", "1/5"], ["0", "5", "3", "-1"]], "bar": 3}

**Step 3: R3 ← R3 + (-5)R2.** Add -5 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "2", "1", "0"], ["0", "1", "1", "1/5"], ["0", "0", "-2", "-2"]], "bar": 3}

**Step 4: R3 ← (-1/2)R3.** Multiply every entry of row 3, including any right-hand side, by -1/2. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "2", "1", "0"], ["0", "1", "1", "1/5"], ["0", "0", "1", "1"]], "bar": 3}

**Step 5: R1 ← R1 + (-1)R3.** Add -1 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "2", "0", "-1"], ["0", "1", "1", "1/5"], ["0", "0", "1", "1"]], "bar": 3}

**Step 6: R2 ← R2 + (-1)R3.** Add -1 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "2", "0", "-1"], ["0", "1", "0", "-4/5"], ["0", "0", "1", "1"]], "bar": 3}

**Step 7: R1 ← R1 + (-2)R2.** Add -2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "3/5"], ["0", "1", "0", "-4/5"], ["0", "0", "1", "1"]], "bar": 3}

**Read the equations.** x_1 = 3/5; x_2 = -4/5; x_3 = 1

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["3/5"], ["-4/5"], ["1"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["0"], ["1"], ["-1"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.4.13 - Is the given vector in the column span?

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 110.

Membership means that a weighted sum of A’s columns equals the given vector. Use that vector as the appended column; consistency answers yes and a contradiction answers no.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["3", "-5", "0"], ["-2", "6", "4"], ["1", "1", "4"]], "bar": 2}

**Step 1: R1 ← (1/3)R1.** Multiply every entry of row 1, including any right-hand side, by 1/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-5/3", "0"], ["-2", "6", "4"], ["1", "1", "4"]], "bar": 2}

**Step 2: R2 ← R2 + (2)R1.** Add 2 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-5/3", "0"], ["0", "8/3", "4"], ["1", "1", "4"]], "bar": 2}

**Step 3: R3 ← R3 + (-1)R1.** Add -1 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-5/3", "0"], ["0", "8/3", "4"], ["0", "8/3", "4"]], "bar": 2}

**Step 4: R2 ← (3/8)R2.** Multiply every entry of row 2, including any right-hand side, by 3/8. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-5/3", "0"], ["0", "1", "3/2"], ["0", "8/3", "4"]], "bar": 2}

**Step 5: R3 ← R3 + (-8/3)R2.** Add -8/3 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-5/3", "0"], ["0", "1", "3/2"], ["0", "0", "0"]], "bar": 2}

**Step 6: R1 ← R1 + (5/3)R2.** Add 5/3 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "5/2"], ["0", "1", "3/2"], ["0", "0", "0"]], "bar": 2}

**Read the equations.** x_1 = 5/2; x_2 = 3/2

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["5/2"], ["3/2"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["0"], ["4"], ["4"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.4.14 - Is the given vector in the column span?

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Membership means that a weighted sum of A’s columns equals the given vector. Use that vector as the appended column; consistency answers yes and a contradiction answers no.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["5", "8", "7", "2"], ["0", "1", "-1", "-3"], ["1", "3", "0", "2"]], "bar": 3}

**Step 1: R1 ← (1/5)R1.** Multiply every entry of row 1, including any right-hand side, by 1/5. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "8/5", "7/5", "2/5"], ["0", "1", "-1", "-3"], ["1", "3", "0", "2"]], "bar": 3}

**Step 2: R3 ← R3 + (-1)R1.** Add -1 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "8/5", "7/5", "2/5"], ["0", "1", "-1", "-3"], ["0", "7/5", "-7/5", "8/5"]], "bar": 3}

**Step 3: R3 ← R3 + (-7/5)R2.** Add -7/5 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "8/5", "7/5", "2/5"], ["0", "1", "-1", "-3"], ["0", "0", "0", "29/5"]], "bar": 3}

**Step 4: R3 ← (5/29)R3.** Multiply every entry of row 3, including any right-hand side, by 5/29. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "8/5", "7/5", "2/5"], ["0", "1", "-1", "-3"], ["0", "0", "0", "1"]], "bar": 3}

**Step 5: R1 ← R1 + (-2/5)R3.** Add -2/5 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "8/5", "7/5", "0"], ["0", "1", "-1", "-3"], ["0", "0", "0", "1"]], "bar": 3}

**Step 6: R2 ← R2 + (3)R3.** Add 3 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "8/5", "7/5", "0"], ["0", "1", "-1", "0"], ["0", "0", "0", "1"]], "bar": 3}

**Step 7: R1 ← R1 + (-8/5)R2.** Add -8/5 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "3", "0"], ["0", "1", "-1", "0"], ["0", "0", "0", "1"]], "bar": 3}

A row now states 0 = 1. No choices of the unknowns can make that true. The system is inconsistent, and its solution set is empty. Free-looking coefficient columns cannot remove a contradiction.


### 1.4.15 - Describe all b for which Ax = b is consistent

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 110.

The second row of A = [2,-1;-6,3] is -3 times its first. Applying R₂ ← R₂ + 3R₁ to [A | b] gives [0,0 | b₂ + 3b₁]. Thus consistency holds exactly for b₂ = -3b₁. These b form the origin line {t(1,-3):t ∈ ℝ}. For example b = (0,1) fails, so existence does not hold for all ℝ^2. Conversely, when the condition holds, the first equation 2x₁ - x₂ = b₁ always has solutions.


### 1.4.16 - Describe all consistent right-hand sides for the 3 × 3 matrix

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The rows of A = [1,-3,-4;-3,2,6;5,-1,-8] satisfy row 3 = -row 1 - 2 row 2. Therefore any solution must satisfy b₃ = -b₁ - 2b₂. To see sufficiency, use R₂ ← R₂ + 3R₁ to get [0,-7,-6 | b₂ + 3b₁], and R₃ ← R₃ - 5R₁ to get [0,14,12 | b₃ - 5b₁]. Adding twice the new row 2 to row 3 gives [0,0,0 | b₃ + b₁ + 2b₂]. If the stated relation holds, the first two rows have pivots and can be solved. The allowed b form a plane in ℝ^3, not all of ℝ^3.


### 1.4.17 - Determine spanning / all-right-hand-side existence

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The starting matrix is:

@matrix {"a": [["1", "3", "0", "3"], ["-1", "-1", "-1", "1"], ["0", "-4", "2", "-8"], ["2", "0", "3", "-1"]], "bar": null}

**Step 1: R2 ← R2 + (1)R1.** Add 1 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "0", "3"], ["0", "2", "-1", "4"], ["0", "-4", "2", "-8"], ["2", "0", "3", "-1"]], "bar": null}

**Step 2: R4 ← R4 + (-2)R1.** Add -2 times row 1 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "0", "3"], ["0", "2", "-1", "4"], ["0", "-4", "2", "-8"], ["0", "-6", "3", "-7"]], "bar": null}

**Step 3: R2 ← (1/2)R2.** Multiply every entry of row 2, including any right-hand side, by 1/2. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "3", "0", "3"], ["0", "1", "-1/2", "2"], ["0", "-4", "2", "-8"], ["0", "-6", "3", "-7"]], "bar": null}

**Step 4: R3 ← R3 + (4)R2.** Add 4 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "0", "3"], ["0", "1", "-1/2", "2"], ["0", "0", "0", "0"], ["0", "-6", "3", "-7"]], "bar": null}

**Step 5: R4 ← R4 + (6)R2.** Add 6 times row 2 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "0", "3"], ["0", "1", "-1/2", "2"], ["0", "0", "0", "0"], ["0", "0", "0", "5"]], "bar": null}

**Step 6: R3 ↔ R4.** Move a nonzero entry into row 3 so that it can be used as a pivot.

@matrix {"a": [["1", "3", "0", "3"], ["0", "1", "-1/2", "2"], ["0", "0", "0", "5"], ["0", "0", "0", "0"]], "bar": null}

**Step 7: R3 ← (1/5)R3.** Multiply every entry of row 3, including any right-hand side, by 1/5. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "3", "0", "3"], ["0", "1", "-1/2", "2"], ["0", "0", "0", "1"], ["0", "0", "0", "0"]], "bar": null}

**Step 8: R1 ← R1 + (-3)R3.** Add -3 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "0", "0"], ["0", "1", "-1/2", "2"], ["0", "0", "0", "1"], ["0", "0", "0", "0"]], "bar": null}

**Step 9: R2 ← R2 + (-2)R3.** Add -2 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "0", "0"], ["0", "1", "-1/2", "0"], ["0", "0", "0", "1"], ["0", "0", "0", "0"]], "bar": null}

**Step 10: R1 ← R1 + (-3)R2.** Add -3 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "3/2", "0"], ["0", "1", "-1/2", "0"], ["0", "0", "0", "1"], ["0", "0", "0", "0"]], "bar": null}

There are 3 coefficient pivots among four rows. At least one row lacks a pivot. Hence the columns do not span ℝ^4, and some b ∈ ℝ^4 cannot be produced. Solvability for individual targets may still occur. This follows from the every-row pivot equivalence in Section 1.4.


### 1.4.18 - Determine spanning / all-right-hand-side existence

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The starting matrix is:

@matrix {"a": [["1", "3", "-2", "2"], ["0", "1", "1", "-5"], ["1", "2", "-3", "7"], ["-2", "-8", "2", "-1"]], "bar": null}

**Step 1: R3 ← R3 + (-1)R1.** Add -1 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "-2", "2"], ["0", "1", "1", "-5"], ["0", "-1", "-1", "5"], ["-2", "-8", "2", "-1"]], "bar": null}

**Step 2: R4 ← R4 + (2)R1.** Add 2 times row 1 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "-2", "2"], ["0", "1", "1", "-5"], ["0", "-1", "-1", "5"], ["0", "-2", "-2", "3"]], "bar": null}

**Step 3: R3 ← R3 + (1)R2.** Add 1 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "-2", "2"], ["0", "1", "1", "-5"], ["0", "0", "0", "0"], ["0", "-2", "-2", "3"]], "bar": null}

**Step 4: R4 ← R4 + (2)R2.** Add 2 times row 2 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "-2", "2"], ["0", "1", "1", "-5"], ["0", "0", "0", "0"], ["0", "0", "0", "-7"]], "bar": null}

**Step 5: R3 ↔ R4.** Move a nonzero entry into row 3 so that it can be used as a pivot.

@matrix {"a": [["1", "3", "-2", "2"], ["0", "1", "1", "-5"], ["0", "0", "0", "-7"], ["0", "0", "0", "0"]], "bar": null}

**Step 6: R3 ← (-1/7)R3.** Multiply every entry of row 3, including any right-hand side, by -1/7. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "3", "-2", "2"], ["0", "1", "1", "-5"], ["0", "0", "0", "1"], ["0", "0", "0", "0"]], "bar": null}

**Step 7: R1 ← R1 + (-2)R3.** Add -2 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "-2", "0"], ["0", "1", "1", "-5"], ["0", "0", "0", "1"], ["0", "0", "0", "0"]], "bar": null}

**Step 8: R2 ← R2 + (5)R3.** Add 5 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "-2", "0"], ["0", "1", "1", "0"], ["0", "0", "0", "1"], ["0", "0", "0", "0"]], "bar": null}

**Step 9: R1 ← R1 + (-3)R2.** Add -3 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-5", "0"], ["0", "1", "1", "0"], ["0", "0", "0", "1"], ["0", "0", "0", "0"]], "bar": null}

There are 3 coefficient pivots among four rows. At least one row lacks a pivot. Hence the columns do not span ℝ^4, and some b ∈ ℝ^4 cannot be produced. Solvability for individual targets may still occur. This follows from the every-row pivot equivalence in Section 1.4.


### 1.4.19 - Determine spanning / all-right-hand-side existence

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The starting matrix is:

@matrix {"a": [["1", "3", "0", "3"], ["-1", "-1", "-1", "1"], ["0", "-4", "2", "-8"], ["2", "0", "3", "-1"]], "bar": null}

**Step 1: R2 ← R2 + (1)R1.** Add 1 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "0", "3"], ["0", "2", "-1", "4"], ["0", "-4", "2", "-8"], ["2", "0", "3", "-1"]], "bar": null}

**Step 2: R4 ← R4 + (-2)R1.** Add -2 times row 1 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "0", "3"], ["0", "2", "-1", "4"], ["0", "-4", "2", "-8"], ["0", "-6", "3", "-7"]], "bar": null}

**Step 3: R2 ← (1/2)R2.** Multiply every entry of row 2, including any right-hand side, by 1/2. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "3", "0", "3"], ["0", "1", "-1/2", "2"], ["0", "-4", "2", "-8"], ["0", "-6", "3", "-7"]], "bar": null}

**Step 4: R3 ← R3 + (4)R2.** Add 4 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "0", "3"], ["0", "1", "-1/2", "2"], ["0", "0", "0", "0"], ["0", "-6", "3", "-7"]], "bar": null}

**Step 5: R4 ← R4 + (6)R2.** Add 6 times row 2 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "0", "3"], ["0", "1", "-1/2", "2"], ["0", "0", "0", "0"], ["0", "0", "0", "5"]], "bar": null}

**Step 6: R3 ↔ R4.** Move a nonzero entry into row 3 so that it can be used as a pivot.

@matrix {"a": [["1", "3", "0", "3"], ["0", "1", "-1/2", "2"], ["0", "0", "0", "5"], ["0", "0", "0", "0"]], "bar": null}

**Step 7: R3 ← (1/5)R3.** Multiply every entry of row 3, including any right-hand side, by 1/5. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "3", "0", "3"], ["0", "1", "-1/2", "2"], ["0", "0", "0", "1"], ["0", "0", "0", "0"]], "bar": null}

**Step 8: R1 ← R1 + (-3)R3.** Add -3 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "0", "0"], ["0", "1", "-1/2", "2"], ["0", "0", "0", "1"], ["0", "0", "0", "0"]], "bar": null}

**Step 9: R2 ← R2 + (-2)R3.** Add -2 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "0", "0"], ["0", "1", "-1/2", "0"], ["0", "0", "0", "1"], ["0", "0", "0", "0"]], "bar": null}

**Step 10: R1 ← R1 + (-3)R2.** Add -3 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "3/2", "0"], ["0", "1", "-1/2", "0"], ["0", "0", "0", "1"], ["0", "0", "0", "0"]], "bar": null}

There are 3 coefficient pivots among four rows. At least one row lacks a pivot. Hence the columns do not span ℝ^4, and some b ∈ ℝ^4 cannot be produced. Solvability for individual targets may still occur. This follows from the every-row pivot equivalence in Section 1.4.


### 1.4.20 - Determine spanning / all-right-hand-side existence

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The starting matrix is:

@matrix {"a": [["1", "3", "-2", "2"], ["0", "1", "1", "-5"], ["1", "2", "-3", "7"], ["-2", "-8", "2", "-1"]], "bar": null}

**Step 1: R3 ← R3 + (-1)R1.** Add -1 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "-2", "2"], ["0", "1", "1", "-5"], ["0", "-1", "-1", "5"], ["-2", "-8", "2", "-1"]], "bar": null}

**Step 2: R4 ← R4 + (2)R1.** Add 2 times row 1 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "-2", "2"], ["0", "1", "1", "-5"], ["0", "-1", "-1", "5"], ["0", "-2", "-2", "3"]], "bar": null}

**Step 3: R3 ← R3 + (1)R2.** Add 1 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "-2", "2"], ["0", "1", "1", "-5"], ["0", "0", "0", "0"], ["0", "-2", "-2", "3"]], "bar": null}

**Step 4: R4 ← R4 + (2)R2.** Add 2 times row 2 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "-2", "2"], ["0", "1", "1", "-5"], ["0", "0", "0", "0"], ["0", "0", "0", "-7"]], "bar": null}

**Step 5: R3 ↔ R4.** Move a nonzero entry into row 3 so that it can be used as a pivot.

@matrix {"a": [["1", "3", "-2", "2"], ["0", "1", "1", "-5"], ["0", "0", "0", "-7"], ["0", "0", "0", "0"]], "bar": null}

**Step 6: R3 ← (-1/7)R3.** Multiply every entry of row 3, including any right-hand side, by -1/7. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "3", "-2", "2"], ["0", "1", "1", "-5"], ["0", "0", "0", "1"], ["0", "0", "0", "0"]], "bar": null}

**Step 7: R1 ← R1 + (-2)R3.** Add -2 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "-2", "0"], ["0", "1", "1", "-5"], ["0", "0", "0", "1"], ["0", "0", "0", "0"]], "bar": null}

**Step 8: R2 ← R2 + (5)R3.** Add 5 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "-2", "0"], ["0", "1", "1", "0"], ["0", "0", "0", "1"], ["0", "0", "0", "0"]], "bar": null}

**Step 9: R1 ← R1 + (-3)R2.** Add -3 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-5", "0"], ["0", "1", "1", "0"], ["0", "0", "0", "1"], ["0", "0", "0", "0"]], "bar": null}

There are 3 coefficient pivots among four rows. At least one row lacks a pivot. Hence the columns do not span ℝ^4, and some b ∈ ℝ^4 cannot be produced. Solvability for individual targets may still occur. This follows from the every-row pivot equivalence in Section 1.4.


### 1.4.21 - Do three vectors span ℝ^4?

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

No. Put them into a 4 × 3 matrix. It has only three columns, so there can be at most three pivots, fewer than the four required row pivots. The columns therefore cannot span ℝ^4 by the spanning theorem. This argument uses the dimensions and applies to any three vectors in ℝ^4, including the displayed ones.


### 1.4.22 - Do the three displayed vectors span ℝ^3?

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The starting matrix is:

@matrix {"a": [["0", "0", "4", "0"], ["0", "-3", "-1", "0"], ["-2", "8", "-5", "0"]], "bar": 3}

**Step 1: R1 ↔ R3.** Move a nonzero entry into row 1 so that it can be used as a pivot.

@matrix {"a": [["-2", "8", "-5", "0"], ["0", "-3", "-1", "0"], ["0", "0", "4", "0"]], "bar": 3}

**Step 2: R1 ← (-1/2)R1.** Multiply every entry of row 1, including any right-hand side, by -1/2. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-4", "5/2", "0"], ["0", "-3", "-1", "0"], ["0", "0", "4", "0"]], "bar": 3}

**Step 3: R2 ← (-1/3)R2.** Multiply every entry of row 2, including any right-hand side, by -1/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-4", "5/2", "0"], ["0", "1", "1/3", "0"], ["0", "0", "4", "0"]], "bar": 3}

**Step 4: R3 ← (1/4)R3.** Multiply every entry of row 3, including any right-hand side, by 1/4. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-4", "5/2", "0"], ["0", "1", "1/3", "0"], ["0", "0", "1", "0"]], "bar": 3}

**Step 5: R1 ← R1 + (-5/2)R3.** Add -5/2 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-4", "0", "0"], ["0", "1", "1/3", "0"], ["0", "0", "1", "0"]], "bar": 3}

**Step 6: R2 ← R2 + (-1/3)R3.** Add -1/3 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-4", "0", "0"], ["0", "1", "0", "0"], ["0", "0", "1", "0"]], "bar": 3}

**Step 7: R1 ← R1 + (4)R2.** Add 4 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "0"], ["0", "1", "0", "0"], ["0", "0", "1", "0"]], "bar": 3}

Every coefficient column has a pivot. The equations force every weight to be zero. Hence the columns are linearly independent: no nontrivial dependence relation exists.


For 1.4.22 specifically, the independent three-column conclusion gives three pivots in a 3 × 3 matrix, hence a pivot in every row. Thus the displayed vectors do span ℝ^3. Independence and spanning coincide here because the matrix is square.


### 1.4.23 - True/false: Ax = b is called a vector equation

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** In the course terminology it is a matrix equation. Its expanded column combination is the vector equation. These are equivalent descriptions, but the question asks for their names.


### 1.4.24 - True/false: A matrix equation has an equivalent vector equation

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** By definition, Ax is the weighted sum of A’s columns. Expanding it gives the vector equation with exactly the same unknown weights and solution set.


### 1.4.25 - True/false: If Ax = b is inconsistent, b is outside the column span

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** Membership in the span means some input weights produce b. Inconsistency means no input does. These are opposite outcomes of exactly the same test.


### 1.4.26 - True/false: b is a column combination exactly when Ax = b has a solution

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** A solution x supplies the combination weights. Conversely, any combination weights can be assembled into x and produce a solution. This proves both directions.


### 1.4.27 - True/false: A pivot in every row of [A b] ensures consistency

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** For A = [0] and b = [1], the augmented matrix [0 | 1] has a pivot in its only row, but the pivot is in the appended column and says 0 = 1. The row-pivot condition must apply to A itself.


### 1.4.28 - True/false: If columns do not span ℝ^m, some b is inconsistent

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** Not spanning means at least one vector in ℝ^m is outside the set of column combinations. Selecting that b gives an inconsistent Ax = b. It does not imply that every b is inconsistent; b = 0 always works.


### 1.4.29 - True/false: The first entry of Ax is a sum of products

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** It is a_{11}x₁ + ... + a_{1n}x_n, pairing the first row with x. The column definition gives this same entry after collecting all first coordinates.


### 1.4.30 - True/false: Every linear combination can be written as Ax

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** Place its vectors as columns of A and its weights as entries of x. If the vectors all have the same number of entries, the dimensions match and the product is that combination.


### 1.4.31 - True/false: If columns span ℝ^m, every b gives consistency

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** Spanning states that each b ∈ ℝ^m is obtainable with some weights. Those weights form an x satisfying Ax = b. This is one of the supplied equivalent conditions.


### 1.4.32 - True/false: [a₁ a₂ a₃ b] and Ax = b have the same solutions

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** With A = [a₁ a₂ a₃], the appended system equates each entry of x₁a₁ + x₂a₂ + x₃a₃ to b. This is exactly Ax = b and has the same three unknown weights.


# Section 1.5 - Solution sets of linear systems


Original question pages follow. They preserve the exact wording, subparts, diagrams, and numerical data of the supplied exercise scans. Worked solutions begin immediately after these pages. A brief paraphrase at each answer identifies the task; consult the reproduced question for its full wording.


## Original exercises - source PDF page 9

@scan ex-09.png

@page


## Worked solutions


### 1.5.1 - Does a nontrivial homogeneous solution exist?

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The all-zero input is always a solution. Nontrivial solutions exist precisely when a coefficient variable is free. Although a partial forward reduction often suffices, the full reduction here makes the distinction and verification explicit.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["2", "-5", "8", "0"], ["-2", "-7", "1", "0"], ["4", "2", "7", "0"]], "bar": 3}

**Step 1: R1 ← (1/2)R1.** Multiply every entry of row 1, including any right-hand side, by 1/2. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-5/2", "4", "0"], ["-2", "-7", "1", "0"], ["4", "2", "7", "0"]], "bar": 3}

**Step 2: R2 ← R2 + (2)R1.** Add 2 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-5/2", "4", "0"], ["0", "-12", "9", "0"], ["4", "2", "7", "0"]], "bar": 3}

**Step 3: R3 ← R3 + (-4)R1.** Add -4 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-5/2", "4", "0"], ["0", "-12", "9", "0"], ["0", "12", "-9", "0"]], "bar": 3}

**Step 4: R2 ← (-1/12)R2.** Multiply every entry of row 2, including any right-hand side, by -1/12. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-5/2", "4", "0"], ["0", "1", "-3/4", "0"], ["0", "12", "-9", "0"]], "bar": 3}

**Step 5: R3 ← R3 + (-12)R2.** Add -12 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-5/2", "4", "0"], ["0", "1", "-3/4", "0"], ["0", "0", "0", "0"]], "bar": 3}

**Step 6: R1 ← R1 + (5/2)R2.** Add 5/2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "17/8", "0"], ["0", "1", "-3/4", "0"], ["0", "0", "0", "0"]], "bar": 3}

**Read the equations.** x_1 + 17/8 x_3 = 0; x_2 - 3/4 x_3 = 0

The pivot columns are 1, 2. Thus x_1, x_2 are basic variables. x_3 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_3 = s with all parameters real. The complete coordinate answer is:

@eq x_1 = -17/8 s

@eq x_2 = 3/4 s

@eq x_3 = s

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1, where:

p =

@matrix {"a": [["0"], ["0"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["-17/8"], ["3/4"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["-17/8"], ["3/4"], ["1"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. Because p = 0, choosing a nonzero parameter gives a nontrivial homogeneous solution. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["0"], ["0"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. Therefore A(p + s v_1) = A p + s A v_1 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.5.2 - Does a nontrivial homogeneous solution exist?

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The all-zero input is always a solution. Nontrivial solutions exist precisely when a coefficient variable is free. Although a partial forward reduction often suffices, the full reduction here makes the distinction and verification explicit.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-3", "7", "0"], ["-2", "1", "-4", "0"], ["1", "2", "9", "0"]], "bar": 3}

**Step 1: R2 ← R2 + (2)R1.** Add 2 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "7", "0"], ["0", "-5", "10", "0"], ["1", "2", "9", "0"]], "bar": 3}

**Step 2: R3 ← R3 + (-1)R1.** Add -1 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "7", "0"], ["0", "-5", "10", "0"], ["0", "5", "2", "0"]], "bar": 3}

**Step 3: R2 ← (-1/5)R2.** Multiply every entry of row 2, including any right-hand side, by -1/5. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-3", "7", "0"], ["0", "1", "-2", "0"], ["0", "5", "2", "0"]], "bar": 3}

**Step 4: R3 ← R3 + (-5)R2.** Add -5 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "7", "0"], ["0", "1", "-2", "0"], ["0", "0", "12", "0"]], "bar": 3}

**Step 5: R3 ← (1/12)R3.** Multiply every entry of row 3, including any right-hand side, by 1/12. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-3", "7", "0"], ["0", "1", "-2", "0"], ["0", "0", "1", "0"]], "bar": 3}

**Step 6: R1 ← R1 + (-7)R3.** Add -7 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "0", "0"], ["0", "1", "-2", "0"], ["0", "0", "1", "0"]], "bar": 3}

**Step 7: R2 ← R2 + (2)R3.** Add 2 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "0", "0"], ["0", "1", "0", "0"], ["0", "0", "1", "0"]], "bar": 3}

**Step 8: R1 ← R1 + (3)R2.** Add 3 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "0"], ["0", "1", "0", "0"], ["0", "0", "1", "0"]], "bar": 3}

**Read the equations.** x_1 = 0; x_2 = 0; x_3 = 0

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["0"], ["0"], ["0"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["0"], ["0"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.5.3 - Does a nontrivial homogeneous solution exist?

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The all-zero input is always a solution. Nontrivial solutions exist precisely when a coefficient variable is free. Although a partial forward reduction often suffices, the full reduction here makes the distinction and verification explicit.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["-3", "5", "-7", "0"], ["-6", "7", "1", "0"]], "bar": 3}

**Step 1: R1 ← (-1/3)R1.** Multiply every entry of row 1, including any right-hand side, by -1/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-5/3", "7/3", "0"], ["-6", "7", "1", "0"]], "bar": 3}

**Step 2: R2 ← R2 + (6)R1.** Add 6 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-5/3", "7/3", "0"], ["0", "-3", "15", "0"]], "bar": 3}

**Step 3: R2 ← (-1/3)R2.** Multiply every entry of row 2, including any right-hand side, by -1/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-5/3", "7/3", "0"], ["0", "1", "-5", "0"]], "bar": 3}

**Step 4: R1 ← R1 + (5/3)R2.** Add 5/3 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-6", "0"], ["0", "1", "-5", "0"]], "bar": 3}

**Read the equations.** x_1 - 6 x_3 = 0; x_2 - 5 x_3 = 0

The pivot columns are 1, 2. Thus x_1, x_2 are basic variables. x_3 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_3 = s with all parameters real. The complete coordinate answer is:

@eq x_1 = 6 s

@eq x_2 = 5 s

@eq x_3 = s

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1, where:

p =

@matrix {"a": [["0"], ["0"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["6"], ["5"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["6"], ["5"], ["1"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. Because p = 0, choosing a nonzero parameter gives a nontrivial homogeneous solution. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["0"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. Therefore A(p + s v_1) = A p + s A v_1 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.5.4 - Does a nontrivial homogeneous solution exist?

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The all-zero input is always a solution. Nontrivial solutions exist precisely when a coefficient variable is free. Although a partial forward reduction often suffices, the full reduction here makes the distinction and verification explicit.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["-5", "7", "9", "0"], ["1", "-2", "6", "0"]], "bar": 3}

**Step 1: R1 ← (-1/5)R1.** Multiply every entry of row 1, including any right-hand side, by -1/5. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-7/5", "-9/5", "0"], ["1", "-2", "6", "0"]], "bar": 3}

**Step 2: R2 ← R2 + (-1)R1.** Add -1 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-7/5", "-9/5", "0"], ["0", "-3/5", "39/5", "0"]], "bar": 3}

**Step 3: R2 ← (-5/3)R2.** Multiply every entry of row 2, including any right-hand side, by -5/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-7/5", "-9/5", "0"], ["0", "1", "-13", "0"]], "bar": 3}

**Step 4: R1 ← R1 + (7/5)R2.** Add 7/5 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-20", "0"], ["0", "1", "-13", "0"]], "bar": 3}

**Read the equations.** x_1 - 20 x_3 = 0; x_2 - 13 x_3 = 0

The pivot columns are 1, 2. Thus x_1, x_2 are basic variables. x_3 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_3 = s with all parameters real. The complete coordinate answer is:

@eq x_1 = 20 s

@eq x_2 = 13 s

@eq x_3 = s

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1, where:

p =

@matrix {"a": [["0"], ["0"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["20"], ["13"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["20"], ["13"], ["1"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. Because p = 0, choosing a nonzero parameter gives a nontrivial homogeneous solution. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["0"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. Therefore A(p + s v_1) = A p + s A v_1 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.5.5 - Describe all homogeneous solutions in parametric vector form

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

In Exercises 7-12 the displayed source matrix is row equivalent to A, not an augmented matrix. Append a zero column to every displayed row; every original column remains a coefficient column.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "3", "1", "0"], ["-4", "-9", "2", "0"], ["0", "-3", "-6", "0"]], "bar": 3}

**Step 1: R2 ← R2 + (4)R1.** Add 4 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "1", "0"], ["0", "3", "6", "0"], ["0", "-3", "-6", "0"]], "bar": 3}

**Step 2: R2 ← (1/3)R2.** Multiply every entry of row 2, including any right-hand side, by 1/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "3", "1", "0"], ["0", "1", "2", "0"], ["0", "-3", "-6", "0"]], "bar": 3}

**Step 3: R3 ← R3 + (3)R2.** Add 3 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "1", "0"], ["0", "1", "2", "0"], ["0", "0", "0", "0"]], "bar": 3}

**Step 4: R1 ← R1 + (-3)R2.** Add -3 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-5", "0"], ["0", "1", "2", "0"], ["0", "0", "0", "0"]], "bar": 3}

**Read the equations.** x_1 - 5 x_3 = 0; x_2 + 2 x_3 = 0

The pivot columns are 1, 2. Thus x_1, x_2 are basic variables. x_3 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_3 = s with all parameters real. The complete coordinate answer is:

@eq x_1 = 5 s

@eq x_2 = -2 s

@eq x_3 = s

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1, where:

p =

@matrix {"a": [["0"], ["0"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["5"], ["-2"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["5"], ["-2"], ["1"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. Because p = 0, choosing a nonzero parameter gives a nontrivial homogeneous solution. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["0"], ["0"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. Therefore A(p + s v_1) = A p + s A v_1 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.5.6 - Describe all homogeneous solutions in parametric vector form

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

In Exercises 7-12 the displayed source matrix is row equivalent to A, not an augmented matrix. Append a zero column to every displayed row; every original column remains a coefficient column.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "3", "-5", "0"], ["1", "4", "-8", "0"], ["-3", "-7", "9", "0"]], "bar": 3}

**Step 1: R2 ← R2 + (-1)R1.** Add -1 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "-5", "0"], ["0", "1", "-3", "0"], ["-3", "-7", "9", "0"]], "bar": 3}

**Step 2: R3 ← R3 + (3)R1.** Add 3 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "-5", "0"], ["0", "1", "-3", "0"], ["0", "2", "-6", "0"]], "bar": 3}

**Step 3: R3 ← R3 + (-2)R2.** Add -2 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "-5", "0"], ["0", "1", "-3", "0"], ["0", "0", "0", "0"]], "bar": 3}

**Step 4: R1 ← R1 + (-3)R2.** Add -3 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "4", "0"], ["0", "1", "-3", "0"], ["0", "0", "0", "0"]], "bar": 3}

**Read the equations.** x_1 + 4 x_3 = 0; x_2 - 3 x_3 = 0

The pivot columns are 1, 2. Thus x_1, x_2 are basic variables. x_3 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_3 = s with all parameters real. The complete coordinate answer is:

@eq x_1 = -4 s

@eq x_2 = 3 s

@eq x_3 = s

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1, where:

p =

@matrix {"a": [["0"], ["0"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["-4"], ["3"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["-4"], ["3"], ["1"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. Because p = 0, choosing a nonzero parameter gives a nontrivial homogeneous solution. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["0"], ["0"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. Therefore A(p + s v_1) = A p + s A v_1 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.5.7 - Describe all homogeneous solutions in parametric vector form

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

In Exercises 7-12 the displayed source matrix is row equivalent to A, not an augmented matrix. Append a zero column to every displayed row; every original column remains a coefficient column.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "3", "-3", "7", "0"], ["0", "1", "-4", "5", "0"]], "bar": 4}

**Step 1: R1 ← R1 + (-3)R2.** Add -3 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "9", "-8", "0"], ["0", "1", "-4", "5", "0"]], "bar": 4}

**Read the equations.** x_1 + 9 x_3 - 8 x_4 = 0; x_2 - 4 x_3 + 5 x_4 = 0

The pivot columns are 1, 2. Thus x_1, x_2 are basic variables. x_3, x_4 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_3 = s, x_4 = t with all parameters real. The complete coordinate answer is:

@eq x_1 = -9 s + 8 t

@eq x_2 = 4 s - 5 t

@eq x_3 = s

@eq x_4 = t

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1 + t v_2, where:

p =

@matrix {"a": [["0"], ["0"], ["0"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["-9"], ["4"], ["1"], ["0"]], "bar": null}

v_2 =

@matrix {"a": [["8"], ["-5"], ["0"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["-9"], ["4"], ["1"], ["0"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. Because p = 0, choosing a nonzero parameter gives a nontrivial homogeneous solution. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["0"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. For direction v_2, multiplying by the original A gives the zero vector. Therefore A(p + s v_1 + t v_2) = A p + s A v_1 + t A v_2 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.5.8 - Describe all homogeneous solutions in parametric vector form

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

In Exercises 7-12 the displayed source matrix is row equivalent to A, not an augmented matrix. Append a zero column to every displayed row; every original column remains a coefficient column.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-2", "-9", "5", "0"], ["0", "1", "2", "-6", "0"]], "bar": 4}

**Step 1: R1 ← R1 + (2)R2.** Add 2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-5", "-7", "0"], ["0", "1", "2", "-6", "0"]], "bar": 4}

**Read the equations.** x_1 - 5 x_3 - 7 x_4 = 0; x_2 + 2 x_3 - 6 x_4 = 0

The pivot columns are 1, 2. Thus x_1, x_2 are basic variables. x_3, x_4 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_3 = s, x_4 = t with all parameters real. The complete coordinate answer is:

@eq x_1 = 5 s + 7 t

@eq x_2 = -2 s + 6 t

@eq x_3 = s

@eq x_4 = t

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1 + t v_2, where:

p =

@matrix {"a": [["0"], ["0"], ["0"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["5"], ["-2"], ["1"], ["0"]], "bar": null}

v_2 =

@matrix {"a": [["7"], ["6"], ["0"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["5"], ["-2"], ["1"], ["0"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. Because p = 0, choosing a nonzero parameter gives a nontrivial homogeneous solution. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["0"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. For direction v_2, multiplying by the original A gives the zero vector. Therefore A(p + s v_1 + t v_2) = A p + s A v_1 + t A v_2 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.5.9 - Describe all homogeneous solutions in parametric vector form

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

In Exercises 7-12 the displayed source matrix is row equivalent to A, not an augmented matrix. Append a zero column to every displayed row; every original column remains a coefficient column.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["3", "-9", "6", "0"], ["-1", "3", "-2", "0"]], "bar": 3}

**Step 1: R1 ← (1/3)R1.** Multiply every entry of row 1, including any right-hand side, by 1/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-3", "2", "0"], ["-1", "3", "-2", "0"]], "bar": 3}

**Step 2: R2 ← R2 + (1)R1.** Add 1 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "2", "0"], ["0", "0", "0", "0"]], "bar": 3}

**Read the equations.** x_1 - 3 x_2 + 2 x_3 = 0

The pivot columns are 1. Thus x_1 are basic variables. x_2, x_3 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_2 = s, x_3 = t with all parameters real. The complete coordinate answer is:

@eq x_1 = 3 s - 2 t

@eq x_2 = s

@eq x_3 = t

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1 + t v_2, where:

p =

@matrix {"a": [["0"], ["0"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["3"], ["1"], ["0"]], "bar": null}

v_2 =

@matrix {"a": [["-2"], ["0"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["3"], ["1"], ["0"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. Because p = 0, choosing a nonzero parameter gives a nontrivial homogeneous solution. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["0"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. For direction v_2, multiplying by the original A gives the zero vector. Therefore A(p + s v_1 + t v_2) = A p + s A v_1 + t A v_2 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.5.10 - Describe all homogeneous solutions in parametric vector form

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

In Exercises 7-12 the displayed source matrix is row equivalent to A, not an augmented matrix. Append a zero column to every displayed row; every original column remains a coefficient column.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "3", "0", "-4", "0"], ["2", "6", "0", "-8", "0"]], "bar": 4}

**Step 1: R2 ← R2 + (-2)R1.** Add -2 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "0", "-4", "0"], ["0", "0", "0", "0", "0"]], "bar": 4}

**Read the equations.** x_1 + 3 x_2 - 4 x_4 = 0

The pivot columns are 1. Thus x_1 are basic variables. x_2, x_3, x_4 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_2 = s, x_3 = t, x_4 = u with all parameters real. The complete coordinate answer is:

@eq x_1 = -3 s + 4 u

@eq x_2 = s

@eq x_3 = t

@eq x_4 = u

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1 + t v_2 + u v_3, where:

p =

@matrix {"a": [["0"], ["0"], ["0"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["-3"], ["1"], ["0"], ["0"]], "bar": null}

v_2 =

@matrix {"a": [["0"], ["0"], ["1"], ["0"]], "bar": null}

v_3 =

@matrix {"a": [["4"], ["0"], ["0"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["-3"], ["1"], ["0"], ["0"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. Because p = 0, choosing a nonzero parameter gives a nontrivial homogeneous solution. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["0"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. For direction v_2, multiplying by the original A gives the zero vector. For direction v_3, multiplying by the original A gives the zero vector. Therefore A(p + s v_1 + t v_2 + u v_3) = A p + s A v_1 + t A v_2 + u A v_3 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.5.11 - Describe all homogeneous solutions in parametric vector form

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

In Exercises 7-12 the displayed source matrix is row equivalent to A, not an augmented matrix. Append a zero column to every displayed row; every original column remains a coefficient column.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-4", "-2", "0", "3", "-5", "0"], ["0", "0", "1", "0", "0", "-1", "0"], ["0", "0", "0", "0", "1", "-4", "0"], ["0", "0", "0", "0", "0", "0", "0"]], "bar": 6}

**Step 1: R1 ← R1 + (-3)R3.** Add -3 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-4", "-2", "0", "0", "7", "0"], ["0", "0", "1", "0", "0", "-1", "0"], ["0", "0", "0", "0", "1", "-4", "0"], ["0", "0", "0", "0", "0", "0", "0"]], "bar": 6}

**Step 2: R1 ← R1 + (2)R2.** Add 2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-4", "0", "0", "0", "5", "0"], ["0", "0", "1", "0", "0", "-1", "0"], ["0", "0", "0", "0", "1", "-4", "0"], ["0", "0", "0", "0", "0", "0", "0"]], "bar": 6}

**Read the equations.** x_1 - 4 x_2 + 5 x_6 = 0; x_3 - x_6 = 0; x_5 - 4 x_6 = 0

The pivot columns are 1, 3, 5. Thus x_1, x_3, x_5 are basic variables. x_2, x_4, x_6 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_2 = s, x_4 = t, x_6 = u with all parameters real. The complete coordinate answer is:

@eq x_1 = 4 s - 5 u

@eq x_2 = s

@eq x_3 = u

@eq x_4 = t

@eq x_5 = 4 u

@eq x_6 = u

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1 + t v_2 + u v_3, where:

p =

@matrix {"a": [["0"], ["0"], ["0"], ["0"], ["0"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["4"], ["1"], ["0"], ["0"], ["0"], ["0"]], "bar": null}

v_2 =

@matrix {"a": [["0"], ["0"], ["0"], ["1"], ["0"], ["0"]], "bar": null}

v_3 =

@matrix {"a": [["-5"], ["0"], ["1"], ["0"], ["4"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["4"], ["1"], ["0"], ["0"], ["0"], ["0"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. Because p = 0, choosing a nonzero parameter gives a nontrivial homogeneous solution. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["0"], ["0"], ["0"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. For direction v_2, multiplying by the original A gives the zero vector. For direction v_3, multiplying by the original A gives the zero vector. Therefore A(p + s v_1 + t v_2 + u v_3) = A p + s A v_1 + t A v_2 + u A v_3 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.5.12 - Describe all homogeneous solutions in parametric vector form

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

In Exercises 7-12 the displayed source matrix is row equivalent to A, not an augmented matrix. Append a zero column to every displayed row; every original column remains a coefficient column.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "5", "2", "-6", "9", "0", "0"], ["0", "0", "1", "-7", "4", "-8", "0"], ["0", "0", "0", "0", "0", "1", "0"], ["0", "0", "0", "0", "0", "0", "0"]], "bar": 6}

**Step 1: R2 ← R2 + (8)R3.** Add 8 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "5", "2", "-6", "9", "0", "0"], ["0", "0", "1", "-7", "4", "0", "0"], ["0", "0", "0", "0", "0", "1", "0"], ["0", "0", "0", "0", "0", "0", "0"]], "bar": 6}

**Step 2: R1 ← R1 + (-2)R2.** Add -2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "5", "0", "8", "1", "0", "0"], ["0", "0", "1", "-7", "4", "0", "0"], ["0", "0", "0", "0", "0", "1", "0"], ["0", "0", "0", "0", "0", "0", "0"]], "bar": 6}

**Read the equations.** x_1 + 5 x_2 + 8 x_4 + x_5 = 0; x_3 - 7 x_4 + 4 x_5 = 0; x_6 = 0

The pivot columns are 1, 3, 6. Thus x_1, x_3, x_6 are basic variables. x_2, x_4, x_5 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_2 = s, x_4 = t, x_5 = u with all parameters real. The complete coordinate answer is:

@eq x_1 = -5 s - 8 t - u

@eq x_2 = s

@eq x_3 = 7 t - 4 u

@eq x_4 = t

@eq x_5 = u

@eq x_6 = 0

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1 + t v_2 + u v_3, where:

p =

@matrix {"a": [["0"], ["0"], ["0"], ["0"], ["0"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["-5"], ["1"], ["0"], ["0"], ["0"], ["0"]], "bar": null}

v_2 =

@matrix {"a": [["-8"], ["0"], ["7"], ["1"], ["0"], ["0"]], "bar": null}

v_3 =

@matrix {"a": [["-1"], ["0"], ["-4"], ["0"], ["1"], ["0"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["-5"], ["1"], ["0"], ["0"], ["0"], ["0"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. Because p = 0, choosing a nonzero parameter gives a nontrivial homogeneous solution. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["0"], ["0"], ["0"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. For direction v_2, multiplying by the original A gives the zero vector. For direction v_3, multiplying by the original A gives the zero vector. Therefore A(p + s v_1 + t v_2 + u v_3) = A p + s A v_1 + t A v_2 + u A v_3 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.5.13 - Verify the full homogeneous set from Exercise 9

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

To verify the full solution set rather than one numerical sample, first obtain its exact parameterization and then substitute the constant and every parameter direction into the original coefficient matrix. The final verification below performs this check for all parameter values.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["3", "-9", "6", "0"], ["-1", "3", "-2", "0"]], "bar": 3}

**Step 1: R1 ← (1/3)R1.** Multiply every entry of row 1, including any right-hand side, by 1/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-3", "2", "0"], ["-1", "3", "-2", "0"]], "bar": 3}

**Step 2: R2 ← R2 + (1)R1.** Add 1 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "2", "0"], ["0", "0", "0", "0"]], "bar": 3}

**Read the equations.** x_1 - 3 x_2 + 2 x_3 = 0

The pivot columns are 1. Thus x_1 are basic variables. x_2, x_3 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_2 = s, x_3 = t with all parameters real. The complete coordinate answer is:

@eq x_1 = 3 s - 2 t

@eq x_2 = s

@eq x_3 = t

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1 + t v_2, where:

p =

@matrix {"a": [["0"], ["0"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["3"], ["1"], ["0"]], "bar": null}

v_2 =

@matrix {"a": [["-2"], ["0"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["3"], ["1"], ["0"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["0"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. For direction v_2, multiplying by the original A gives the zero vector. Therefore A(p + s v_1 + t v_2) = A p + s A v_1 + t A v_2 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.5.14 - Verify the full homogeneous set from Exercise 10

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

To verify the full solution set rather than one numerical sample, first obtain its exact parameterization and then substitute the constant and every parameter direction into the original coefficient matrix. The final verification below performs this check for all parameter values.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "3", "0", "-4", "0"], ["2", "6", "0", "-8", "0"]], "bar": 4}

**Step 1: R2 ← R2 + (-2)R1.** Add -2 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "0", "-4", "0"], ["0", "0", "0", "0", "0"]], "bar": 4}

**Read the equations.** x_1 + 3 x_2 - 4 x_4 = 0

The pivot columns are 1. Thus x_1 are basic variables. x_2, x_3, x_4 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_2 = s, x_3 = t, x_4 = u with all parameters real. The complete coordinate answer is:

@eq x_1 = -3 s + 4 u

@eq x_2 = s

@eq x_3 = t

@eq x_4 = u

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1 + t v_2 + u v_3, where:

p =

@matrix {"a": [["0"], ["0"], ["0"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["-3"], ["1"], ["0"], ["0"]], "bar": null}

v_2 =

@matrix {"a": [["0"], ["0"], ["1"], ["0"]], "bar": null}

v_3 =

@matrix {"a": [["4"], ["0"], ["0"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["-3"], ["1"], ["0"], ["0"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["0"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. For direction v_2, multiplying by the original A gives the zero vector. For direction v_3, multiplying by the original A gives the zero vector. Therefore A(p + s v_1 + t v_2 + u v_3) = A p + s A v_1 + t A v_2 + u A v_3 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.5.15 - Verify the full homogeneous set from Exercise 11

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

To verify the full solution set rather than one numerical sample, first obtain its exact parameterization and then substitute the constant and every parameter direction into the original coefficient matrix. The final verification below performs this check for all parameter values.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-4", "-2", "0", "3", "-5", "0"], ["0", "0", "1", "0", "0", "-1", "0"], ["0", "0", "0", "0", "1", "-4", "0"], ["0", "0", "0", "0", "0", "0", "0"]], "bar": 6}

**Step 1: R1 ← R1 + (-3)R3.** Add -3 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-4", "-2", "0", "0", "7", "0"], ["0", "0", "1", "0", "0", "-1", "0"], ["0", "0", "0", "0", "1", "-4", "0"], ["0", "0", "0", "0", "0", "0", "0"]], "bar": 6}

**Step 2: R1 ← R1 + (2)R2.** Add 2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-4", "0", "0", "0", "5", "0"], ["0", "0", "1", "0", "0", "-1", "0"], ["0", "0", "0", "0", "1", "-4", "0"], ["0", "0", "0", "0", "0", "0", "0"]], "bar": 6}

**Read the equations.** x_1 - 4 x_2 + 5 x_6 = 0; x_3 - x_6 = 0; x_5 - 4 x_6 = 0

The pivot columns are 1, 3, 5. Thus x_1, x_3, x_5 are basic variables. x_2, x_4, x_6 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_2 = s, x_4 = t, x_6 = u with all parameters real. The complete coordinate answer is:

@eq x_1 = 4 s - 5 u

@eq x_2 = s

@eq x_3 = u

@eq x_4 = t

@eq x_5 = 4 u

@eq x_6 = u

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1 + t v_2 + u v_3, where:

p =

@matrix {"a": [["0"], ["0"], ["0"], ["0"], ["0"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["4"], ["1"], ["0"], ["0"], ["0"], ["0"]], "bar": null}

v_2 =

@matrix {"a": [["0"], ["0"], ["0"], ["1"], ["0"], ["0"]], "bar": null}

v_3 =

@matrix {"a": [["-5"], ["0"], ["1"], ["0"], ["4"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["4"], ["1"], ["0"], ["0"], ["0"], ["0"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["0"], ["0"], ["0"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. For direction v_2, multiplying by the original A gives the zero vector. For direction v_3, multiplying by the original A gives the zero vector. Therefore A(p + s v_1 + t v_2 + u v_3) = A p + s A v_1 + t A v_2 + u A v_3 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.5.16 - Verify the full homogeneous set from Exercise 12

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

To verify the full solution set rather than one numerical sample, first obtain its exact parameterization and then substitute the constant and every parameter direction into the original coefficient matrix. The final verification below performs this check for all parameter values.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "5", "2", "-6", "9", "0", "0"], ["0", "0", "1", "-7", "4", "-8", "0"], ["0", "0", "0", "0", "0", "1", "0"], ["0", "0", "0", "0", "0", "0", "0"]], "bar": 6}

**Step 1: R2 ← R2 + (8)R3.** Add 8 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "5", "2", "-6", "9", "0", "0"], ["0", "0", "1", "-7", "4", "0", "0"], ["0", "0", "0", "0", "0", "1", "0"], ["0", "0", "0", "0", "0", "0", "0"]], "bar": 6}

**Step 2: R1 ← R1 + (-2)R2.** Add -2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "5", "0", "8", "1", "0", "0"], ["0", "0", "1", "-7", "4", "0", "0"], ["0", "0", "0", "0", "0", "1", "0"], ["0", "0", "0", "0", "0", "0", "0"]], "bar": 6}

**Read the equations.** x_1 + 5 x_2 + 8 x_4 + x_5 = 0; x_3 - 7 x_4 + 4 x_5 = 0; x_6 = 0

The pivot columns are 1, 3, 6. Thus x_1, x_3, x_6 are basic variables. x_2, x_4, x_5 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_2 = s, x_4 = t, x_5 = u with all parameters real. The complete coordinate answer is:

@eq x_1 = -5 s - 8 t - u

@eq x_2 = s

@eq x_3 = 7 t - 4 u

@eq x_4 = t

@eq x_5 = u

@eq x_6 = 0

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1 + t v_2 + u v_3, where:

p =

@matrix {"a": [["0"], ["0"], ["0"], ["0"], ["0"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["-5"], ["1"], ["0"], ["0"], ["0"], ["0"]], "bar": null}

v_2 =

@matrix {"a": [["-8"], ["0"], ["7"], ["1"], ["0"], ["0"]], "bar": null}

v_3 =

@matrix {"a": [["-1"], ["0"], ["-4"], ["0"], ["1"], ["0"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["-5"], ["1"], ["0"], ["0"], ["0"], ["0"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["0"], ["0"], ["0"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. For direction v_2, multiplying by the original A gives the zero vector. For direction v_3, multiplying by the original A gives the zero vector. Therefore A(p + s v_1 + t v_2 + u v_3) = A p + s A v_1 + t A v_2 + u A v_3 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.5.17 - Write the given solution line using vectors

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Set x₃ = t. Then x = (5 + 4t,-2 - 7t,t) = (5,-2,0) + t(4,-7,1). The first vector is one point on the line; the second is its nonzero direction. Conversely, every t supplies exactly the three stated coordinate formulas, so the vector equation describes the entire given set. It is a line in ℝ^3 through (5,-2,0), parallel to (4,-7,1).


### 1.5.18 - Write the given line in ℝ^4 using vectors

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Let x₄ = t. The entries become (3t,8 + t,2 - 5t,t). Separate the constants from the coefficient of t: x = (0,8,2,0) + t(3,1,-5,1). This is a line in ℝ^4, meaning a set with one real parameter and a nonzero direction, even though it cannot be drawn completely in a plane. At t = 0 it passes through the displayed fixed vector.


### 1.5.19 - Solve and compare with Exercise 5

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The coefficient matrix is exactly that of Exercise 5. Thus its homogeneous direction is the same. The particular vector below translates the origin line to a parallel line; check that its output is the new right-hand side.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "3", "1", "1"], ["-4", "-9", "2", "-1"], ["0", "-3", "-6", "-3"]], "bar": 3}

**Step 1: R2 ← R2 + (4)R1.** Add 4 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "1", "1"], ["0", "3", "6", "3"], ["0", "-3", "-6", "-3"]], "bar": 3}

**Step 2: R2 ← (1/3)R2.** Multiply every entry of row 2, including any right-hand side, by 1/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "3", "1", "1"], ["0", "1", "2", "1"], ["0", "-3", "-6", "-3"]], "bar": 3}

**Step 3: R3 ← R3 + (3)R2.** Add 3 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "1", "1"], ["0", "1", "2", "1"], ["0", "0", "0", "0"]], "bar": 3}

**Step 4: R1 ← R1 + (-3)R2.** Add -3 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-5", "-2"], ["0", "1", "2", "1"], ["0", "0", "0", "0"]], "bar": 3}

**Read the equations.** x_1 - 5 x_3 = -2; x_2 + 2 x_3 = 1

The pivot columns are 1, 2. Thus x_1, x_2 are basic variables. x_3 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_3 = s with all parameters real. The complete coordinate answer is:

@eq x_1 = -2 + 5 s

@eq x_2 = 1 - 2 s

@eq x_3 = s

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1, where:

p =

@matrix {"a": [["-2"], ["1"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["5"], ["-2"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["3"], ["-1"], ["1"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["1"], ["-1"], ["-3"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. Therefore A(p + s v_1) = A p + s A v_1 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.5.20 - Solve and compare with Exercise 6

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The coefficient matrix is that of Exercise 6. The new solution set, if consistent, is a translate of its homogeneous line, with the same nonzero direction. The reduction and verification show the translating point explicitly.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "3", "-5", "4"], ["1", "4", "-8", "7"], ["-3", "-7", "9", "-6"]], "bar": 3}

**Step 1: R2 ← R2 + (-1)R1.** Add -1 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "-5", "4"], ["0", "1", "-3", "3"], ["-3", "-7", "9", "-6"]], "bar": 3}

**Step 2: R3 ← R3 + (3)R1.** Add 3 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "-5", "4"], ["0", "1", "-3", "3"], ["0", "2", "-6", "6"]], "bar": 3}

**Step 3: R3 ← R3 + (-2)R2.** Add -2 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3", "-5", "4"], ["0", "1", "-3", "3"], ["0", "0", "0", "0"]], "bar": 3}

**Step 4: R1 ← R1 + (-3)R2.** Add -3 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "4", "-5"], ["0", "1", "-3", "3"], ["0", "0", "0", "0"]], "bar": 3}

**Read the equations.** x_1 + 4 x_3 = -5; x_2 - 3 x_3 = 3

The pivot columns are 1, 2. Thus x_1, x_2 are basic variables. x_3 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_3 = s with all parameters real. The complete coordinate answer is:

@eq x_1 = -5 - 4 s

@eq x_2 = 3 + 3 s

@eq x_3 = s

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1, where:

p =

@matrix {"a": [["-5"], ["3"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["-4"], ["3"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["-9"], ["6"], ["1"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["4"], ["7"], ["-6"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. Therefore A(p + s v_1) = A p + s A v_1 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.5.21 - Compare two planes with the same left side

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

For the homogeneous equation choose x₂ = s,x₃ = t. Then x₁ = -9s + 4t and x = s(-9,1,0) + t(4,0,1). For right side -2, x₁ = -2 - 9s + 4t and x = (-2,0,0) + s(-9,1,0) + t(4,0,1). The directions are independent because their second and third coordinates isolate s and t, so both sets are planes. Substitution gives 0 and -2 respectively for every s,t. The planes are parallel and distinct, related by translation by (-2,0,0).


### 1.5.22 - Compare the two solution planes

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

For x₁ - 3x₂ + 5x₃ = 0, let x₂ = s,x₃ = t, giving x = s(3,1,0) + t(-5,0,1). For right side 4, the full solution is x = (4,0,0) + s(3,1,0) + t(-5,0,1). Each substitution cancels the parameter terms, leaving the respective constant. Independent directions make both sets planes. The homogeneous plane passes through zero; the second is its translate by (4,0,0), parallel and distinct.


# Section 1.7 - Linear independence


Original question pages follow. They preserve the exact wording, subparts, diagrams, and numerical data of the supplied exercise scans. Worked solutions begin immediately after these pages. A brief paraphrase at each answer identifies the task; consult the reproduced question for its full wording.


## Original exercises - source PDF page 10

@scan ex-10.png

@page


## Worked solutions


### 1.7.1 - Test independence using the homogeneous equation

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The starting matrix is:

@matrix {"a": [["5", "7", "-2", "0"], ["1", "2", "-1", "0"], ["0", "-6", "6", "0"]], "bar": 3}

**Step 1: R1 ← (1/5)R1.** Multiply every entry of row 1, including any right-hand side, by 1/5. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "7/5", "-2/5", "0"], ["1", "2", "-1", "0"], ["0", "-6", "6", "0"]], "bar": 3}

**Step 2: R2 ← R2 + (-1)R1.** Add -1 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "7/5", "-2/5", "0"], ["0", "3/5", "-3/5", "0"], ["0", "-6", "6", "0"]], "bar": 3}

**Step 3: R2 ← (5/3)R2.** Multiply every entry of row 2, including any right-hand side, by 5/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "7/5", "-2/5", "0"], ["0", "1", "-1", "0"], ["0", "-6", "6", "0"]], "bar": 3}

**Step 4: R3 ← R3 + (6)R2.** Add 6 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "7/5", "-2/5", "0"], ["0", "1", "-1", "0"], ["0", "0", "0", "0"]], "bar": 3}

**Step 5: R1 ← R1 + (-7/5)R2.** Add -7/5 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "1", "0"], ["0", "1", "-1", "0"], ["0", "0", "0", "0"]], "bar": 3}

Column 3 has no pivot. Give its weight the value 1 and give any other free weights the value 0. The pivot equations determine the weights:

@matrix {"a": [["-1"], ["1"], ["1"]], "bar": null}

At least one weight is nonzero. The resulting dependence relation is:

@eq -v_1 + v_2 + v_3 = 0

Multiplying the original columns by these weights gives the zero vector, entry by entry. This proves dependence; the existence of a zero combination with every weight zero would not prove it.


### 1.7.2 - Test independence using the homogeneous equation

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The starting matrix is:

@matrix {"a": [["0", "0", "-3", "0"], ["0", "5", "4", "0"], ["2", "-8", "1", "0"]], "bar": 3}

**Step 1: R1 ↔ R3.** Move a nonzero entry into row 1 so that it can be used as a pivot.

@matrix {"a": [["2", "-8", "1", "0"], ["0", "5", "4", "0"], ["0", "0", "-3", "0"]], "bar": 3}

**Step 2: R1 ← (1/2)R1.** Multiply every entry of row 1, including any right-hand side, by 1/2. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-4", "1/2", "0"], ["0", "5", "4", "0"], ["0", "0", "-3", "0"]], "bar": 3}

**Step 3: R2 ← (1/5)R2.** Multiply every entry of row 2, including any right-hand side, by 1/5. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-4", "1/2", "0"], ["0", "1", "4/5", "0"], ["0", "0", "-3", "0"]], "bar": 3}

**Step 4: R3 ← (-1/3)R3.** Multiply every entry of row 3, including any right-hand side, by -1/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-4", "1/2", "0"], ["0", "1", "4/5", "0"], ["0", "0", "1", "0"]], "bar": 3}

**Step 5: R1 ← R1 + (-1/2)R3.** Add -1/2 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-4", "0", "0"], ["0", "1", "4/5", "0"], ["0", "0", "1", "0"]], "bar": 3}

**Step 6: R2 ← R2 + (-4/5)R3.** Add -4/5 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-4", "0", "0"], ["0", "1", "0", "0"], ["0", "0", "1", "0"]], "bar": 3}

**Step 7: R1 ← R1 + (4)R2.** Add 4 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "0"], ["0", "1", "0", "0"], ["0", "0", "1", "0"]], "bar": 3}

Every coefficient column has a pivot. The equations force every weight to be zero. Hence the columns are linearly independent: no nontrivial dependence relation exists.


### 1.7.3 - Test independence using the homogeneous equation

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The starting matrix is:

@matrix {"a": [["1", "-3", "0"], ["-3", "6", "0"]], "bar": 2}

**Step 1: R2 ← R2 + (3)R1.** Add 3 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "0"], ["0", "-3", "0"]], "bar": 2}

**Step 2: R2 ← (-1/3)R2.** Multiply every entry of row 2, including any right-hand side, by -1/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-3", "0"], ["0", "1", "0"]], "bar": 2}

**Step 3: R1 ← R1 + (3)R2.** Add 3 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0"], ["0", "1", "0"]], "bar": 2}

Every coefficient column has a pivot. The equations force every weight to be zero. Hence the columns are linearly independent: no nontrivial dependence relation exists.


### 1.7.4 - Test independence using the homogeneous equation

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The starting matrix is:

@matrix {"a": [["-1", "-2", "0"], ["4", "8", "0"]], "bar": 2}

**Step 1: R1 ← (-1)R1.** Multiply every entry of row 1, including any right-hand side, by -1. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "2", "0"], ["4", "8", "0"]], "bar": 2}

**Step 2: R2 ← R2 + (-4)R1.** Add -4 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "2", "0"], ["0", "0", "0"]], "bar": 2}

Column 2 has no pivot. Give its weight the value 1 and give any other free weights the value 0. The pivot equations determine the weights:

@matrix {"a": [["-2"], ["1"]], "bar": null}

At least one weight is nonzero. The resulting dependence relation is:

@eq -2 v_1 + v_2 = 0

Multiplying the original columns by these weights gives the zero vector, entry by entry. This proves dependence; the existence of a zero combination with every weight zero would not prove it.


### 1.7.5 - Test independence using the homogeneous equation

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The starting matrix is:

@matrix {"a": [["0", "-8", "5", "0"], ["3", "-7", "4", "0"], ["-1", "5", "-4", "0"], ["1", "-3", "2", "0"]], "bar": 3}

**Step 1: R1 ↔ R2.** Move a nonzero entry into row 1 so that it can be used as a pivot.

@matrix {"a": [["3", "-7", "4", "0"], ["0", "-8", "5", "0"], ["-1", "5", "-4", "0"], ["1", "-3", "2", "0"]], "bar": 3}

**Step 2: R1 ← (1/3)R1.** Multiply every entry of row 1, including any right-hand side, by 1/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-7/3", "4/3", "0"], ["0", "-8", "5", "0"], ["-1", "5", "-4", "0"], ["1", "-3", "2", "0"]], "bar": 3}

**Step 3: R3 ← R3 + (1)R1.** Add 1 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-7/3", "4/3", "0"], ["0", "-8", "5", "0"], ["0", "8/3", "-8/3", "0"], ["1", "-3", "2", "0"]], "bar": 3}

**Step 4: R4 ← R4 + (-1)R1.** Add -1 times row 1 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-7/3", "4/3", "0"], ["0", "-8", "5", "0"], ["0", "8/3", "-8/3", "0"], ["0", "-2/3", "2/3", "0"]], "bar": 3}

**Step 5: R2 ← (-1/8)R2.** Multiply every entry of row 2, including any right-hand side, by -1/8. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-7/3", "4/3", "0"], ["0", "1", "-5/8", "0"], ["0", "8/3", "-8/3", "0"], ["0", "-2/3", "2/3", "0"]], "bar": 3}

**Step 6: R3 ← R3 + (-8/3)R2.** Add -8/3 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-7/3", "4/3", "0"], ["0", "1", "-5/8", "0"], ["0", "0", "-1", "0"], ["0", "-2/3", "2/3", "0"]], "bar": 3}

**Step 7: R4 ← R4 + (2/3)R2.** Add 2/3 times row 2 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-7/3", "4/3", "0"], ["0", "1", "-5/8", "0"], ["0", "0", "-1", "0"], ["0", "0", "1/4", "0"]], "bar": 3}

**Step 8: R3 ← (-1)R3.** Multiply every entry of row 3, including any right-hand side, by -1. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-7/3", "4/3", "0"], ["0", "1", "-5/8", "0"], ["0", "0", "1", "0"], ["0", "0", "1/4", "0"]], "bar": 3}

**Step 9: R4 ← R4 + (-1/4)R3.** Add -1/4 times row 3 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-7/3", "4/3", "0"], ["0", "1", "-5/8", "0"], ["0", "0", "1", "0"], ["0", "0", "0", "0"]], "bar": 3}

**Step 10: R1 ← R1 + (-4/3)R3.** Add -4/3 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-7/3", "0", "0"], ["0", "1", "-5/8", "0"], ["0", "0", "1", "0"], ["0", "0", "0", "0"]], "bar": 3}

**Step 11: R2 ← R2 + (5/8)R3.** Add 5/8 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-7/3", "0", "0"], ["0", "1", "0", "0"], ["0", "0", "1", "0"], ["0", "0", "0", "0"]], "bar": 3}

**Step 12: R1 ← R1 + (7/3)R2.** Add 7/3 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "0"], ["0", "1", "0", "0"], ["0", "0", "1", "0"], ["0", "0", "0", "0"]], "bar": 3}

Every coefficient column has a pivot. The equations force every weight to be zero. Hence the columns are linearly independent: no nontrivial dependence relation exists.


### 1.7.6 - Test independence using the homogeneous equation

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The starting matrix is:

@matrix {"a": [["-4", "-3", "0", "0"], ["0", "-1", "4", "0"], ["1", "0", "3", "0"], ["5", "4", "6", "0"]], "bar": 3}

**Step 1: R1 ← (-1/4)R1.** Multiply every entry of row 1, including any right-hand side, by -1/4. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "3/4", "0", "0"], ["0", "-1", "4", "0"], ["1", "0", "3", "0"], ["5", "4", "6", "0"]], "bar": 3}

**Step 2: R3 ← R3 + (-1)R1.** Add -1 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3/4", "0", "0"], ["0", "-1", "4", "0"], ["0", "-3/4", "3", "0"], ["5", "4", "6", "0"]], "bar": 3}

**Step 3: R4 ← R4 + (-5)R1.** Add -5 times row 1 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3/4", "0", "0"], ["0", "-1", "4", "0"], ["0", "-3/4", "3", "0"], ["0", "1/4", "6", "0"]], "bar": 3}

**Step 4: R2 ← (-1)R2.** Multiply every entry of row 2, including any right-hand side, by -1. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "3/4", "0", "0"], ["0", "1", "-4", "0"], ["0", "-3/4", "3", "0"], ["0", "1/4", "6", "0"]], "bar": 3}

**Step 5: R3 ← R3 + (3/4)R2.** Add 3/4 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3/4", "0", "0"], ["0", "1", "-4", "0"], ["0", "0", "0", "0"], ["0", "1/4", "6", "0"]], "bar": 3}

**Step 6: R4 ← R4 + (-1/4)R2.** Add -1/4 times row 2 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3/4", "0", "0"], ["0", "1", "-4", "0"], ["0", "0", "0", "0"], ["0", "0", "7", "0"]], "bar": 3}

**Step 7: R3 ↔ R4.** Move a nonzero entry into row 3 so that it can be used as a pivot.

@matrix {"a": [["1", "3/4", "0", "0"], ["0", "1", "-4", "0"], ["0", "0", "7", "0"], ["0", "0", "0", "0"]], "bar": 3}

**Step 8: R3 ← (1/7)R3.** Multiply every entry of row 3, including any right-hand side, by 1/7. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "3/4", "0", "0"], ["0", "1", "-4", "0"], ["0", "0", "1", "0"], ["0", "0", "0", "0"]], "bar": 3}

**Step 9: R2 ← R2 + (4)R3.** Add 4 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3/4", "0", "0"], ["0", "1", "0", "0"], ["0", "0", "1", "0"], ["0", "0", "0", "0"]], "bar": 3}

**Step 10: R1 ← R1 + (-3/4)R2.** Add -3/4 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "0"], ["0", "1", "0", "0"], ["0", "0", "1", "0"], ["0", "0", "0", "0"]], "bar": 3}

Every coefficient column has a pivot. The equations force every weight to be zero. Hence the columns are linearly independent: no nontrivial dependence relation exists.


### 1.7.7 - Test independence using the homogeneous equation

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The starting matrix is:

@matrix {"a": [["1", "4", "-3", "0", "0"], ["-2", "-7", "5", "1", "0"], ["-4", "-5", "7", "5", "0"]], "bar": 4}

**Step 1: R2 ← R2 + (2)R1.** Add 2 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "4", "-3", "0", "0"], ["0", "1", "-1", "1", "0"], ["-4", "-5", "7", "5", "0"]], "bar": 4}

**Step 2: R3 ← R3 + (4)R1.** Add 4 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "4", "-3", "0", "0"], ["0", "1", "-1", "1", "0"], ["0", "11", "-5", "5", "0"]], "bar": 4}

**Step 3: R3 ← R3 + (-11)R2.** Add -11 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "4", "-3", "0", "0"], ["0", "1", "-1", "1", "0"], ["0", "0", "6", "-6", "0"]], "bar": 4}

**Step 4: R3 ← (1/6)R3.** Multiply every entry of row 3, including any right-hand side, by 1/6. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "4", "-3", "0", "0"], ["0", "1", "-1", "1", "0"], ["0", "0", "1", "-1", "0"]], "bar": 4}

**Step 5: R1 ← R1 + (3)R3.** Add 3 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "4", "0", "-3", "0"], ["0", "1", "-1", "1", "0"], ["0", "0", "1", "-1", "0"]], "bar": 4}

**Step 6: R2 ← R2 + (1)R3.** Add 1 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "4", "0", "-3", "0"], ["0", "1", "0", "0", "0"], ["0", "0", "1", "-1", "0"]], "bar": 4}

**Step 7: R1 ← R1 + (-4)R2.** Add -4 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "-3", "0"], ["0", "1", "0", "0", "0"], ["0", "0", "1", "-1", "0"]], "bar": 4}

Column 4 has no pivot. Give its weight the value 1 and give any other free weights the value 0. The pivot equations determine the weights:

@matrix {"a": [["3"], ["0"], ["1"], ["1"]], "bar": null}

At least one weight is nonzero. The resulting dependence relation is:

@eq 3 v_1 + v_3 + v_4 = 0

Multiplying the original columns by these weights gives the zero vector, entry by entry. This proves dependence; the existence of a zero combination with every weight zero would not prove it.


### 1.7.8 - Test independence using the homogeneous equation

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The starting matrix is:

@matrix {"a": [["1", "-3", "3", "-2", "0"], ["-3", "7", "-1", "2", "0"], ["0", "1", "-4", "3", "0"]], "bar": 4}

**Step 1: R2 ← R2 + (3)R1.** Add 3 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "3", "-2", "0"], ["0", "-2", "8", "-4", "0"], ["0", "1", "-4", "3", "0"]], "bar": 4}

**Step 2: R2 ← (-1/2)R2.** Multiply every entry of row 2, including any right-hand side, by -1/2. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-3", "3", "-2", "0"], ["0", "1", "-4", "2", "0"], ["0", "1", "-4", "3", "0"]], "bar": 4}

**Step 3: R3 ← R3 + (-1)R2.** Add -1 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "3", "-2", "0"], ["0", "1", "-4", "2", "0"], ["0", "0", "0", "1", "0"]], "bar": 4}

**Step 4: R1 ← R1 + (2)R3.** Add 2 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "3", "0", "0"], ["0", "1", "-4", "2", "0"], ["0", "0", "0", "1", "0"]], "bar": 4}

**Step 5: R2 ← R2 + (-2)R3.** Add -2 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "3", "0", "0"], ["0", "1", "-4", "0", "0"], ["0", "0", "0", "1", "0"]], "bar": 4}

**Step 6: R1 ← R1 + (3)R2.** Add 3 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-9", "0", "0"], ["0", "1", "-4", "0", "0"], ["0", "0", "0", "1", "0"]], "bar": 4}

Column 3 has no pivot. Give its weight the value 1 and give any other free weights the value 0. The pivot equations determine the weights:

@matrix {"a": [["9"], ["4"], ["1"], ["0"]], "bar": null}

At least one weight is nonzero. The resulting dependence relation is:

@eq 9 v_1 + 4 v_2 + v_3 = 0

Multiplying the original columns by these weights gives the zero vector, entry by entry. This proves dependence; the existence of a zero combination with every weight zero would not prove it.


### 1.7.9 - h for span membership and for dependence

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The first two vectors are independent: the first two coordinate equations α - 3β = 2 and -3α + 10β = -7 give β = -1 and α = -1. Thus a third vector in their span must have third entry 2α - 6β = 4. Conversely, at h = 4, v₃ = -v₁ - v₂, giving the nontrivial relation v₁ + v₂ + v₃ = 0. Therefore (a) span membership holds exactly for h = 4, and (b) the three-vector collection is dependent exactly for h = 4. The equivalence in (b) uses independence of the first pair.


### 1.7.10 - Distinguish membership from preexisting dependence

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Here v₂ = -2v₁, so the first two vectors already span only the line through v₁. Since the first two entries of v₃ are 2,-10, membership would require v₃ = 2v₁ and therefore h = -6. This proves part (a). For part (b), 2v₁ + v₂ + 0v₃ = 0 is a nontrivial relation for every h. Thus the triple is dependent for all h, including those for which v₃ is outside the original line. Do not use the independent-pair equivalence without its assumption.


### 1.7.11 - Find h for dependence

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

In a relation c₁v₁ + c₂v₂ + c₃v₃ = 0, the first two coordinates give c₁ + 3c₂ - c₃ = 0 and -c₁ - 5c₂ + 5c₃ = 0. Adding gives -2c₂ + 4c₃ = 0, so c₂ = 2c₃ and then c₁ = -5c₃. The last coordinate is 4c₁ + 7c₂ + hc₃ = (h - 6)c₃ = 0. A nontrivial relation requires c₃ ≠ 0, hence h = 6. At h = 6, weights (-5,2,1) give zero in all coordinates; otherwise every weight is zero and the vectors are independent.


### 1.7.12 - Find h for dependence

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The first and third coordinates of all three vectors satisfy entry 1 = 2 × entry 3. Thus the three vectors lie in the plane x₁ = 2x₃ for every h. Derive an explicit relation from 2c₁ - 6c₂ + 8c₃ = 0, so c₁ = 3c₂ - 4c₃. The second equation becomes -5c₂ + (h + 16)c₃ = 0. Choose c₃ = 5, c₂ = h + 16, giving c₁ = 3h + 28. Then first and second coordinates cancel, and the third cancels because it is half the first. These weights are not all zero since c₃ = 5. Hence dependence holds for every real h.


### 1.7.13 - Find h for dependence

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The third coordinate is -3 times the first for each displayed vector, regardless of h. Derive a relation from c₁ - 2c₂ + 3c₃ = 0, which gives c₁ = 2c₂ - 3c₃. The second equation becomes c₂ + (h - 15)c₃ = 0. Set c₃ = 1, then c₂ = 15 - h and c₁ = 27 - 2h. The first two sums vanish by construction, and the third is -3 times the first, so it vanishes too. Since the third weight is 1, dependence holds for all real h.


### 1.7.14 - Find h for dependence

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The first two coordinate equations of a zero combination are c₁ - 5c₂ + c₃ = 0 and -c₁ + 7c₂ + c₃ = 0. Adding gives 2c₂ + 2c₃ = 0, hence c₂ = -c₃ and c₁ = -6c₃. The third equation becomes 3(-6c₃) + 8(-c₃) + hc₃ = (h - 26)c₃ = 0. Nontrivial weights require h = 26. At that value (-6,-1,1) is a dependence relation; at any other value all weights vanish.


### 1.7.15 - Inspect four vectors in ℝ^2

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The collection is dependent because four vectors have only two entries each. In a 2 × 4 column matrix, at most two columns can have pivots, so Ax = 0 has at least two free weights. The too-many-vectors theorem proves dependence without calculating particular weights. Pairwise nonparallel directions would not make four plane vectors independent.


### 1.7.16 - Inspect the two vectors in ℝ^3

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The second vector (6,-3,9) is 3/2 times the first (4,-2,6). Consequently 3v₁ - 2v₂ = 0 has nonzero weights, proving dependence. The factor matches all three coordinates; matching only the first coordinate would not suffice.


### 1.7.17 - Inspect a collection containing zero

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The middle vector is zero. Give it coefficient 1 and the other two vectors coefficient 0: 0v₁ + 1v₂ + 0v₃ = 0. The weights are not all zero, so the collection is dependent regardless of the other entries.


### 1.7.18 - Inspect four vectors with two entries

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Four vectors in ℝ^2 must be dependent by the more-vectors-than-entries theorem. The homogeneous column system has four unknown weights but at most two pivots, so a free weight yields a nontrivial zero combination. No numerical row reduction is needed for this decision.


### 1.7.19 - Inspect whether the two vectors are multiples

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The first two coordinate ratios suggest a multiplier -1/4 from (-8,12,-4) to (2,-3,-1). That multiplier would make the third entry 1, not -1. Therefore the vectors are not scalar multiples. Both are nonzero, so the two-vector characterization proves they are linearly independent.


### 1.7.20 - Inspect the collection containing zero

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The third vector is zero. The weights (0,0,1) form a nontrivial zero combination. Hence the collection is dependent even if the first two vectors were independent. Independence is a property of the entire indexed collection.


### 1.7.21 - True/false: Having the trivial homogeneous solution proves independence

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** Every homogeneous system has the trivial solution. Independence requires it to be the only solution. The repeated columns (1,0),(1,0) give both the trivial weights and the nontrivial weights (1,-1).


### 1.7.22 - True/false: Two vectors are dependent exactly when they lie on an origin line

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** For nonzero vectors, lying on one origin line means scalar proportionality, the two-vector dependence criterion. If one or both are zero, the pair is dependent and a line through zero containing the other vector still exists.


### 1.7.23 - True/false: Every vector in a dependent set is a combination of the others

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** Take {0,(1,0)}. It is dependent because it contains zero, but (1,0) cannot be generated from zero. The correct characterization says at least one vector can be generated by the others.


### 1.7.24 - True/false: Fewer vectors than entries ensures independence

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** The two vectors (1,0,0),(2,0,0) have three entries each, yet are dependent since 2v₁ - v₂ = 0. The too-many-vectors theorem has no such converse.


### 1.7.25 - True/false: Any 4 × 5 matrix has dependent columns

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** It gives five vectors in ℝ^4. At most four coefficient pivots are possible, leaving a free weight in Ax = 0. The theorem therefore guarantees a nontrivial relation.


### 1.7.26 - True/false: Adding a vector in the span to an independent pair gives dependence

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** If z = ax + by, then ax + by - z = 0 is nontrivial because the coefficient on z is -1. This directly proves dependence of {x,y,z}.


### 1.7.27 - True/false: If x,y are independent and the triple is dependent, z is in their span

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** Take a nontrivial relation ax + by + cz = 0. If c were zero, independence of x,y would force a = b = 0, a contradiction. Thus c ≠ 0 and z = -(a/c)x - (b/c)y.


### 1.7.28 - True/false: A dependent collection in ℝ^n must have more than n vectors

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** A single zero vector is already dependent in ℝ^n for any positive n. Also two proportional nonzero vectors in ℝ^3 are dependent without exceeding three vectors. The size theorem is sufficient, not necessary.


### 1.7.29 - REF pattern for a 3 × 3 independent-column matrix

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Independence forces three column pivots. With three rows and three columns, the only pivot pattern is [p,*,*;0,p,*;0,0,p], where p means nonzero and * is arbitrary. There are no zero rows or skipped columns. Leading entries need not be 1 because only REF is requested.


### 1.7.30 - REF patterns for a dependent 2 × 2 matrix

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Dependence means fewer than two pivots. There may be zero pivots, giving the zero matrix, or one pivot in column 1, giving [p,*;0,0], or one pivot in column 2, giving [0,p;0,0]. These exhaust the options. The two-pivot pattern is excluded because it would force independence.


### 1.7.31 - REF when a₂ is not a multiple of a₁

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

One must separate a₁ = 0 from a₁ ≠ 0. If a₁ ≠ 0, the hypothesis makes the two columns independent, giving [p,*;0,p;0,0;0,0]. If a₁ = 0, the hypothesis says a₂ ≠ 0, and the REF pattern is [0,p;0,0;0,0;0,0]. This second case is why the wording is not automatically the same as saying neither vector is a multiple of the other.


### 1.7.32 - REF after adding a third vector outside an independent-pair span

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The independent pair gives two independent columns. If a₃ is outside their span, a relation c₁a₁ + c₂a₂ + c₃a₃ = 0 cannot have c₃ ≠ 0, since that would express a₃ in their span. If c₃ = 0, independence of the pair forces c₁ = c₂ = 0. Thus all three columns are independent and the 4 × 3 REF pattern is [p,*,*;0,p,*;0,0,p;0,0,0].


# Section 1.8 - Introduction to linear transformations


Original question pages follow. They preserve the exact wording, subparts, diagrams, and numerical data of the supplied exercise scans. Worked solutions begin immediately after these pages. A brief paraphrase at each answer identifies the task; consult the reproduced question for its full wording.


## Original exercises - source PDF page 11

@scan ex-11.png

@page


## Worked solutions


### 1.8.1 - Images under doubling

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

A = 2I₂ multiplies each input coordinate by 2. Thus T(1,-3) = (2,-6), and for v = (a,b), T(v) = (2a,2b). These are images, so the inputs are known and no system-solving step is needed. The rule is a dilation by factor 2 and preserves the origin.


### 1.8.2 - Images under a three-dimensional contraction

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The matrix is (1/2)I₃. Therefore T(1,0,-4) = (1/2,0,-2), and T(a,b,c) = (a/2,b/2,c/2). Each vector has three output entries because A has three rows. Scaling all coordinates by the same positive factor contracts toward the origin without reversing direction.


### 1.8.3 - Find a preimage of b and decide uniqueness

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

An input whose image is b solves Ax = b. The final pivot and parameter information decides whether such an input is unique.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "0", "-2", "-1"], ["-2", "1", "6", "7"], ["3", "-2", "-5", "-3"]], "bar": 3}

**Step 1: R2 ← R2 + (2)R1.** Add 2 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-2", "-1"], ["0", "1", "2", "5"], ["3", "-2", "-5", "-3"]], "bar": 3}

**Step 2: R3 ← R3 + (-3)R1.** Add -3 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-2", "-1"], ["0", "1", "2", "5"], ["0", "-2", "1", "0"]], "bar": 3}

**Step 3: R3 ← R3 + (2)R2.** Add 2 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-2", "-1"], ["0", "1", "2", "5"], ["0", "0", "5", "10"]], "bar": 3}

**Step 4: R3 ← (1/5)R3.** Multiply every entry of row 3, including any right-hand side, by 1/5. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "0", "-2", "-1"], ["0", "1", "2", "5"], ["0", "0", "1", "2"]], "bar": 3}

**Step 5: R1 ← R1 + (2)R3.** Add 2 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "3"], ["0", "1", "2", "5"], ["0", "0", "1", "2"]], "bar": 3}

**Step 6: R2 ← R2 + (-2)R3.** Add -2 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "3"], ["0", "1", "0", "1"], ["0", "0", "1", "2"]], "bar": 3}

**Read the equations.** x_1 = 3; x_2 = 1; x_3 = 2

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["3"], ["1"], ["2"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["-1"], ["7"], ["-3"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.8.4 - Find a preimage of b and decide uniqueness

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

An input whose image is b solves Ax = b. The final pivot and parameter information decides whether such an input is unique.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-3", "2", "6"], ["0", "1", "-4", "-7"], ["3", "-5", "-9", "-9"]], "bar": 3}

**Step 1: R3 ← R3 + (-3)R1.** Add -3 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "2", "6"], ["0", "1", "-4", "-7"], ["0", "4", "-15", "-27"]], "bar": 3}

**Step 2: R3 ← R3 + (-4)R2.** Add -4 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "2", "6"], ["0", "1", "-4", "-7"], ["0", "0", "1", "1"]], "bar": 3}

**Step 3: R1 ← R1 + (-2)R3.** Add -2 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "0", "4"], ["0", "1", "-4", "-7"], ["0", "0", "1", "1"]], "bar": 3}

**Step 4: R2 ← R2 + (4)R3.** Add 4 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-3", "0", "4"], ["0", "1", "0", "-3"], ["0", "0", "1", "1"]], "bar": 3}

**Step 5: R1 ← R1 + (3)R2.** Add 3 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "-5"], ["0", "1", "0", "-3"], ["0", "0", "1", "1"]], "bar": 3}

**Read the equations.** x_1 = -5; x_2 = -3; x_3 = 1

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["-5"], ["-3"], ["1"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["6"], ["-7"], ["-9"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.8.5 - Find a preimage of b and decide uniqueness

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

An input whose image is b solves Ax = b. The final pivot and parameter information decides whether such an input is unique.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-5", "-7", "-2"], ["-3", "7", "5", "-2"]], "bar": 3}

**Step 1: R2 ← R2 + (3)R1.** Add 3 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-5", "-7", "-2"], ["0", "-8", "-16", "-8"]], "bar": 3}

**Step 2: R2 ← (-1/8)R2.** Multiply every entry of row 2, including any right-hand side, by -1/8. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-5", "-7", "-2"], ["0", "1", "2", "1"]], "bar": 3}

**Step 3: R1 ← R1 + (5)R2.** Add 5 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "3", "3"], ["0", "1", "2", "1"]], "bar": 3}

**Read the equations.** x_1 + 3 x_3 = 3; x_2 + 2 x_3 = 1

The pivot columns are 1, 2. Thus x_1, x_2 are basic variables. x_3 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_3 = s with all parameters real. The complete coordinate answer is:

@eq x_1 = 3 - 3 s

@eq x_2 = 1 - 2 s

@eq x_3 = s

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1, where:

p =

@matrix {"a": [["3"], ["1"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["-3"], ["-2"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["0"], ["-1"], ["1"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["-2"], ["-2"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. Therefore A(p + s v_1) = A p + s A v_1 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.8.6 - Find a preimage of b and decide uniqueness

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

An input whose image is b solves Ax = b. The final pivot and parameter information decides whether such an input is unique.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-2", "1", "1"], ["3", "-4", "5", "9"], ["0", "1", "1", "3"], ["-3", "5", "-4", "-6"]], "bar": 3}

**Step 1: R2 ← R2 + (-3)R1.** Add -3 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-2", "1", "1"], ["0", "2", "2", "6"], ["0", "1", "1", "3"], ["-3", "5", "-4", "-6"]], "bar": 3}

**Step 2: R4 ← R4 + (3)R1.** Add 3 times row 1 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-2", "1", "1"], ["0", "2", "2", "6"], ["0", "1", "1", "3"], ["0", "-1", "-1", "-3"]], "bar": 3}

**Step 3: R2 ← (1/2)R2.** Multiply every entry of row 2, including any right-hand side, by 1/2. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "-2", "1", "1"], ["0", "1", "1", "3"], ["0", "1", "1", "3"], ["0", "-1", "-1", "-3"]], "bar": 3}

**Step 4: R3 ← R3 + (-1)R2.** Add -1 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-2", "1", "1"], ["0", "1", "1", "3"], ["0", "0", "0", "0"], ["0", "-1", "-1", "-3"]], "bar": 3}

**Step 5: R4 ← R4 + (1)R2.** Add 1 times row 2 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-2", "1", "1"], ["0", "1", "1", "3"], ["0", "0", "0", "0"], ["0", "0", "0", "0"]], "bar": 3}

**Step 6: R1 ← R1 + (2)R2.** Add 2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "3", "7"], ["0", "1", "1", "3"], ["0", "0", "0", "0"], ["0", "0", "0", "0"]], "bar": 3}

**Read the equations.** x_1 + 3 x_3 = 7; x_2 + x_3 = 3

The pivot columns are 1, 2. Thus x_1, x_2 are basic variables. x_3 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_3 = s with all parameters real. The complete coordinate answer is:

@eq x_1 = 7 - 3 s

@eq x_2 = 3 - s

@eq x_3 = s

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1, where:

p =

@matrix {"a": [["7"], ["3"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["-3"], ["-1"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["4"], ["2"], ["1"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["1"], ["9"], ["3"], ["-6"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. Therefore A(p + s v_1) = A p + s A v_1 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.8.7 - Domain and codomain for a 6 × 5 matrix

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

A has five columns, so its input must have five entries: a = 5. It has six rows, so its output has six entries: b = 6. Thus T: ℝ^5 → ℝ^6. This dimension statement says nothing yet about the range equaling the codomain.


### 1.8.8 - Matrix size for ℝ^4 into ℝ^5

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The input has four entries, requiring four matrix columns. The output has five entries, requiring five rows. Hence A must be 5 × 4. The inner dimensions in Ax are (5 × 4)(4 × 1), producing 5 × 1 as required.


### 1.8.9 - Find every input mapped to zero

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-4", "7", "-5", "0"], ["0", "1", "-4", "3", "0"], ["2", "-6", "6", "-4", "0"]], "bar": 4}

**Step 1: R3 ← R3 + (-2)R1.** Add -2 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-4", "7", "-5", "0"], ["0", "1", "-4", "3", "0"], ["0", "2", "-8", "6", "0"]], "bar": 4}

**Step 2: R3 ← R3 + (-2)R2.** Add -2 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-4", "7", "-5", "0"], ["0", "1", "-4", "3", "0"], ["0", "0", "0", "0", "0"]], "bar": 4}

**Step 3: R1 ← R1 + (4)R2.** Add 4 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-9", "7", "0"], ["0", "1", "-4", "3", "0"], ["0", "0", "0", "0", "0"]], "bar": 4}

**Read the equations.** x_1 - 9 x_3 + 7 x_4 = 0; x_2 - 4 x_3 + 3 x_4 = 0

The pivot columns are 1, 2. Thus x_1, x_2 are basic variables. x_3, x_4 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_3 = s, x_4 = t with all parameters real. The complete coordinate answer is:

@eq x_1 = 9 s - 7 t

@eq x_2 = 4 s - 3 t

@eq x_3 = s

@eq x_4 = t

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1 + t v_2, where:

p =

@matrix {"a": [["0"], ["0"], ["0"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["9"], ["4"], ["1"], ["0"]], "bar": null}

v_2 =

@matrix {"a": [["-7"], ["-3"], ["0"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["9"], ["4"], ["1"], ["0"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. Because p = 0, choosing a nonzero parameter gives a nontrivial homogeneous solution. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["0"], ["0"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. For direction v_2, multiplying by the original A gives the zero vector. Therefore A(p + s v_1 + t v_2) = A p + s A v_1 + t A v_2 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.8.10 - Find every input mapped to zero

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "1", "9", "2", "0"], ["1", "0", "3", "-4", "0"], ["0", "1", "2", "3", "0"], ["-2", "3", "0", "5", "0"]], "bar": 4}

**Step 1: R2 ← R2 + (-1)R1.** Add -1 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "1", "9", "2", "0"], ["0", "-1", "-6", "-6", "0"], ["0", "1", "2", "3", "0"], ["-2", "3", "0", "5", "0"]], "bar": 4}

**Step 2: R4 ← R4 + (2)R1.** Add 2 times row 1 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "1", "9", "2", "0"], ["0", "-1", "-6", "-6", "0"], ["0", "1", "2", "3", "0"], ["0", "5", "18", "9", "0"]], "bar": 4}

**Step 3: R2 ← (-1)R2.** Multiply every entry of row 2, including any right-hand side, by -1. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "1", "9", "2", "0"], ["0", "1", "6", "6", "0"], ["0", "1", "2", "3", "0"], ["0", "5", "18", "9", "0"]], "bar": 4}

**Step 4: R3 ← R3 + (-1)R2.** Add -1 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "1", "9", "2", "0"], ["0", "1", "6", "6", "0"], ["0", "0", "-4", "-3", "0"], ["0", "5", "18", "9", "0"]], "bar": 4}

**Step 5: R4 ← R4 + (-5)R2.** Add -5 times row 2 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "1", "9", "2", "0"], ["0", "1", "6", "6", "0"], ["0", "0", "-4", "-3", "0"], ["0", "0", "-12", "-21", "0"]], "bar": 4}

**Step 6: R3 ← (-1/4)R3.** Multiply every entry of row 3, including any right-hand side, by -1/4. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "1", "9", "2", "0"], ["0", "1", "6", "6", "0"], ["0", "0", "1", "3/4", "0"], ["0", "0", "-12", "-21", "0"]], "bar": 4}

**Step 7: R4 ← R4 + (12)R3.** Add 12 times row 3 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "1", "9", "2", "0"], ["0", "1", "6", "6", "0"], ["0", "0", "1", "3/4", "0"], ["0", "0", "0", "-12", "0"]], "bar": 4}

**Step 8: R4 ← (-1/12)R4.** Multiply every entry of row 4, including any right-hand side, by -1/12. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "1", "9", "2", "0"], ["0", "1", "6", "6", "0"], ["0", "0", "1", "3/4", "0"], ["0", "0", "0", "1", "0"]], "bar": 4}

**Step 9: R1 ← R1 + (-2)R4.** Add -2 times row 4 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "1", "9", "0", "0"], ["0", "1", "6", "6", "0"], ["0", "0", "1", "3/4", "0"], ["0", "0", "0", "1", "0"]], "bar": 4}

**Step 10: R2 ← R2 + (-6)R4.** Add -6 times row 4 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "1", "9", "0", "0"], ["0", "1", "6", "0", "0"], ["0", "0", "1", "3/4", "0"], ["0", "0", "0", "1", "0"]], "bar": 4}

**Step 11: R3 ← R3 + (-3/4)R4.** Add -3/4 times row 4 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "1", "9", "0", "0"], ["0", "1", "6", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "0"]], "bar": 4}

**Step 12: R1 ← R1 + (-9)R3.** Add -9 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "1", "0", "0", "0"], ["0", "1", "6", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "0"]], "bar": 4}

**Step 13: R2 ← R2 + (-6)R3.** Add -6 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "1", "0", "0", "0"], ["0", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "0"]], "bar": 4}

**Step 14: R1 ← R1 + (-1)R2.** Add -1 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "0", "0"], ["0", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "0"]], "bar": 4}

**Read the equations.** x_1 = 0; x_2 = 0; x_3 = 0; x_4 = 0

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["0"], ["0"], ["0"], ["0"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["0"], ["0"], ["0"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.8.11 - Is b = (-1,1,0) in the range?

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Range membership is equivalent to consistency of Ax = b. A solution gives a concrete preimage; a contradiction proves there is none.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-4", "7", "-5", "-1"], ["0", "1", "-4", "3", "1"], ["2", "-6", "6", "-4", "0"]], "bar": 4}

**Step 1: R3 ← R3 + (-2)R1.** Add -2 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-4", "7", "-5", "-1"], ["0", "1", "-4", "3", "1"], ["0", "2", "-8", "6", "2"]], "bar": 4}

**Step 2: R3 ← R3 + (-2)R2.** Add -2 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-4", "7", "-5", "-1"], ["0", "1", "-4", "3", "1"], ["0", "0", "0", "0", "0"]], "bar": 4}

**Step 3: R1 ← R1 + (4)R2.** Add 4 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-9", "7", "3"], ["0", "1", "-4", "3", "1"], ["0", "0", "0", "0", "0"]], "bar": 4}

**Read the equations.** x_1 - 9 x_3 + 7 x_4 = 3; x_2 - 4 x_3 + 3 x_4 = 1

The pivot columns are 1, 2. Thus x_1, x_2 are basic variables. x_3, x_4 have no leading pivots. Their values may be chosen arbitrarily; the pivot equations then determine the remaining entries. A zero row means 0 = 0 and imposes no additional restriction.

Set x_3 = s, x_4 = t with all parameters real. The complete coordinate answer is:

@eq x_1 = 3 + 9 s - 7 t

@eq x_2 = 1 + 4 s - 3 t

@eq x_3 = s

@eq x_4 = t

In vector form, assemble the constant entries into p and the coefficients of each parameter into a direction vector. Every solution is x = p + s v_1 + t v_2, where:

p =

@matrix {"a": [["3"], ["1"], ["0"], ["0"]], "bar": null}

v_1 =

@matrix {"a": [["9"], ["4"], ["1"], ["0"]], "bar": null}

v_2 =

@matrix {"a": [["-7"], ["-3"], ["0"], ["1"]], "bar": null}

For example, setting all parameters to 0 gives x = p. Setting s = 1 and all other parameters to 0 gives:

@matrix {"a": [["12"], ["5"], ["1"], ["0"]], "bar": null}

These are different because the selected free coordinate changes. Infinitely many real parameter values give infinitely many different solutions. 

**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["-1"], ["1"], ["0"]], "bar": null}

These entries equal the original right-hand sides, in order. For direction v_1, multiplying by the original A gives the zero vector. For direction v_2, multiplying by the original A gives the zero vector. Therefore A(p + s v_1 + t v_2) = A p + s A v_1 + t A v_2 = b for every parameter choice. Conversely, the pivot equations show that every solution has this form.


### 1.8.12 - Is b = (-1,3,-1,4) in the range?

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Solve Ax = b using the four supplied output entries. Do not infer membership merely because b has the right dimension.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "1", "9", "2", "-1"], ["1", "0", "3", "-4", "3"], ["0", "1", "2", "3", "-1"], ["-2", "3", "0", "5", "4"]], "bar": 4}

**Step 1: R2 ← R2 + (-1)R1.** Add -1 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "1", "9", "2", "-1"], ["0", "-1", "-6", "-6", "4"], ["0", "1", "2", "3", "-1"], ["-2", "3", "0", "5", "4"]], "bar": 4}

**Step 2: R4 ← R4 + (2)R1.** Add 2 times row 1 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "1", "9", "2", "-1"], ["0", "-1", "-6", "-6", "4"], ["0", "1", "2", "3", "-1"], ["0", "5", "18", "9", "2"]], "bar": 4}

**Step 3: R2 ← (-1)R2.** Multiply every entry of row 2, including any right-hand side, by -1. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "1", "9", "2", "-1"], ["0", "1", "6", "6", "-4"], ["0", "1", "2", "3", "-1"], ["0", "5", "18", "9", "2"]], "bar": 4}

**Step 4: R3 ← R3 + (-1)R2.** Add -1 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "1", "9", "2", "-1"], ["0", "1", "6", "6", "-4"], ["0", "0", "-4", "-3", "3"], ["0", "5", "18", "9", "2"]], "bar": 4}

**Step 5: R4 ← R4 + (-5)R2.** Add -5 times row 2 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "1", "9", "2", "-1"], ["0", "1", "6", "6", "-4"], ["0", "0", "-4", "-3", "3"], ["0", "0", "-12", "-21", "22"]], "bar": 4}

**Step 6: R3 ← (-1/4)R3.** Multiply every entry of row 3, including any right-hand side, by -1/4. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "1", "9", "2", "-1"], ["0", "1", "6", "6", "-4"], ["0", "0", "1", "3/4", "-3/4"], ["0", "0", "-12", "-21", "22"]], "bar": 4}

**Step 7: R4 ← R4 + (12)R3.** Add 12 times row 3 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "1", "9", "2", "-1"], ["0", "1", "6", "6", "-4"], ["0", "0", "1", "3/4", "-3/4"], ["0", "0", "0", "-12", "13"]], "bar": 4}

**Step 8: R4 ← (-1/12)R4.** Multiply every entry of row 4, including any right-hand side, by -1/12. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "1", "9", "2", "-1"], ["0", "1", "6", "6", "-4"], ["0", "0", "1", "3/4", "-3/4"], ["0", "0", "0", "1", "-13/12"]], "bar": 4}

**Step 9: R1 ← R1 + (-2)R4.** Add -2 times row 4 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "1", "9", "0", "7/6"], ["0", "1", "6", "6", "-4"], ["0", "0", "1", "3/4", "-3/4"], ["0", "0", "0", "1", "-13/12"]], "bar": 4}

**Step 10: R2 ← R2 + (-6)R4.** Add -6 times row 4 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "1", "9", "0", "7/6"], ["0", "1", "6", "0", "5/2"], ["0", "0", "1", "3/4", "-3/4"], ["0", "0", "0", "1", "-13/12"]], "bar": 4}

**Step 11: R3 ← R3 + (-3/4)R4.** Add -3/4 times row 4 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "1", "9", "0", "7/6"], ["0", "1", "6", "0", "5/2"], ["0", "0", "1", "0", "1/16"], ["0", "0", "0", "1", "-13/12"]], "bar": 4}

**Step 12: R1 ← R1 + (-9)R3.** Add -9 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "1", "0", "0", "29/48"], ["0", "1", "6", "0", "5/2"], ["0", "0", "1", "0", "1/16"], ["0", "0", "0", "1", "-13/12"]], "bar": 4}

**Step 13: R2 ← R2 + (-6)R3.** Add -6 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "1", "0", "0", "29/48"], ["0", "1", "0", "0", "17/8"], ["0", "0", "1", "0", "1/16"], ["0", "0", "0", "1", "-13/12"]], "bar": 4}

**Step 14: R1 ← R1 + (-1)R2.** Add -1 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "0", "-73/48"], ["0", "1", "0", "0", "17/8"], ["0", "0", "1", "0", "1/16"], ["0", "0", "0", "1", "-13/12"]], "bar": 4}

**Read the equations.** x_1 = -73/48; x_2 = 17/8; x_3 = 1/16; x_4 = -13/12

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["-73/48"], ["17/8"], ["1/16"], ["-13/12"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["-1"], ["3"], ["-1"], ["4"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.8.13 - Plot u,v and their images

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 111.

Reflection in the origin, equivalently a half-turn. Draw the inputs u = (5,2), v = (-2,4). Multiplying gives T(u) = (-5, -2) and T(v) = (2, -4). Each new arrow starts at zero and ends at its displayed coordinate. The following coordinate diagram shows both input and output arrows.

@customfig transform13


### 1.8.14 - Plot u,v and their images

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 111.

Uniform contraction by factor 1/2. Draw the inputs u = (5,2), v = (-2,4). Multiplying gives T(u) = (5/2, 1) and T(v) = (-1, 2). Each new arrow starts at zero and ends at its displayed coordinate. The following coordinate diagram shows both input and output arrows.

@customfig transform14


### 1.8.15 - Plot u,v and their images

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 111.

Projection onto the vertical x₂-axis; horizontal information is discarded. Draw the inputs u = (5,2), v = (-2,4). Multiplying gives T(u) = (0, 2) and T(v) = (0, 4). Each new arrow starts at zero and ends at its displayed coordinate. The following coordinate diagram shows both input and output arrows.

@customfig transform15


### 1.8.16 - Plot u,v and their images

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 111.

Reflection across the diagonal x₂ = x₁; the coordinates are swapped. Draw the inputs u = (5,2), v = (-2,4). Multiplying gives T(u) = (2, 5) and T(v) = (4, -2). Each new arrow starts at zero and ends at its displayed coordinate. The following coordinate diagram shows both input and output arrows.

@customfig transform16


### 1.8.17 - Use linearity for 3u,2v,3u + 2v

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Linearity preserves scalar multiplication, so T(3u) = 3T(u) = 3(2,1) = (6,3), and T(2v) = 2T(v) = 2(-1,3) = (-2,6). It also preserves addition, giving T(3u + 2v) = T(3u) + T(2v) = (6,3) + (-2,6) = (4,9). The weights stay the same on the output side; the original u,v coordinates do not replace their known images.


### 1.8.18 - Construct the image of w from the diagram

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 111.

The grid-free drawing indicates w = u + 2v: u reaches the upper-right point and two leftward v-displacements reach w on the vertical axis. The supplied selected solution confirms this geometric relation. By linearity, T(w) = T(u) + 2T(v). In the output picture, draw two copies of T(v) head to tail after T(u), or complete the parallelogram with sides T(u) and 2T(v). The resulting arrow is shown in the construction below. Exact numerical coordinates are not supplied and are not invented.

@customfig relation18


### 1.8.19 - Images determined by the two basis images

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Any x = (x₁,x₂) equals x₁e₁ + x₂e₂. Linearity gives T(x) = x₁(2,5) + x₂(-1,6) = (2x₁ - x₂,5x₁ + 6x₂). In particular, T(5,-3) = 5(2,5) - 3(-1,6) = (13,7). This derivation works for every x, not only the numerical example.


### 1.8.20 - Construct a matrix implementing the rule

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 111.

The input weights x₁,x₂ multiply v₁ = (-2,5), v₂ = (7,-3). Thus the standard matrix uses these as columns: A = [-2,7;5,-3]. Expanding Ax gives ( -2x₁ + 7x₂,5x₁ - 3x₂), which is exactly x₁v₁ + x₂v₂. Hence T(x) = Ax for every input, as required.


# Section 1.9 - The matrix of a linear transformation


Original question pages follow. They preserve the exact wording, subparts, diagrams, and numerical data of the supplied exercise scans. Worked solutions begin immediately after these pages. A brief paraphrase at each answer identifies the task; consult the reproduced question for its full wording.


## Original exercises - source PDF page 12

@scan ex-12.png

@page


## Worked solutions


### 1.9.1 - Standard matrix from two four-entry images

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The first column is T(e₁) = (2,1,2,1), and the second is T(e₂) = (-5,2,0,0). Therefore:

@matrix {"a": [["2", "-5"], ["1", "2"], ["2", "0"], ["1", "0"]], "bar": null}

There are four output entries and two input coordinates, so the size is 4 × 2. By linearity, multiplying this matrix by (x₁,x₂) gives x₁T(e₁) + x₂T(e₂), proving that it represents T.


### 1.9.2 - Standard matrix from three basis images

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 112.

Put T(e₁) = (1,3), T(e₂) = (4,2), and T(e₃) = (-5,4) into columns in that order:

@matrix {"a": [["1", "4", "-5"], ["3", "2", "4"]], "bar": null}

The result is 2 × 3. Each column records the response to one unit input, so the weighted column sum gives T(x) for every x by linearity.


### 1.9.3 - Counterclockwise rotation by 3π/2

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

A three-quarter counterclockwise turn sends e₁ to (0,-1) and e₂ to (1,0). Thus A = [0,1;-1,0]. Checking a general vector gives (x₂,-x₁), the same as a quarter-turn clockwise. The input images must be placed into columns, which fixes the signs.


### 1.9.4 - Clockwise rotation by π/4

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 112.

Let q = 1/√2. The image of e₁ is (q,-q), as the supplied hint states. Rotating e₂ by the same angle gives (q,q). Thus A = [q,q;-q,q] = (1/√2)[1,1;-1,1]. At e₁ it points down-right and at e₂ up-right, consistent with a clockwise quarter of a right angle.


### 1.9.5 - Vertical shear from its basis action

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The first column is T(e₁) = e₁ - 2e₂ = (1,-2), while the second is T(e₂) = e₂ = (0,1). Therefore A = [1,0;-2,1], giving T(x₁,x₂) = (x₁,-2x₁ + x₂). The vertical coordinate changes in proportion to the horizontal one, and the vertical axis stays fixed.


### 1.9.6 - Horizontal shear from its basis action

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 112.

The first column is unchanged e₁ = (1,0). The second is e₂ + 3e₁ = (3,1). Thus A = [1,3;0,1]. Multiplication gives (x₁ + 3x₂,x₂), so points on the horizontal axis remain fixed and other horizontal displacements are proportional to height.


### 1.9.7 - Rotation followed by horizontal reflection

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Let q = 1/√2. Rotation by -3π/4 has matrix [-q,q;-q,-q]. Reflecting afterward in the horizontal axis negates the second output coordinate, giving A = [-q,q;q,q]. Equivalently, e₁ goes first to (-q,-q), then to (-q,q), and e₂ goes to (q,-q), then (q,q). These final images are the columns, matching the supplied hint for T(e₁).


### 1.9.8 - Two successive reflections

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 112.

First reflect (x₁,x₂) to (x₁,-x₂), then swap coordinates across x₂ = x₁ to obtain (-x₂,x₁). Thus A = [0,-1;1,0]. The basis check e₁ ↦ e₂ and e₂ ↦ -e₁ confirms the columns. This action is a counterclockwise rotation by π/2.


### 1.9.9 - Horizontal shear followed by reflection in the negative diagonal

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The shear sends (x₁,x₂) to (x₁ - 3x₂,x₂), since e₂ becomes e₂ - 3e₁. Reflection in x₂ = -x₁ swaps and negates, giving (-x₂,-x₁ + 3x₂). Hence A = [0,-1;-1,3]. The multiplication order would be reflection matrix times shear matrix, since shear happens first.


### 1.9.10 - Vertical-axis reflection followed by a 3π/2 rotation

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Reflect first to (-x₁,x₂). Rotation by 3π/2 sends (a,b) to (b,-a), so the final output is (x₂,x₁). Thus A = [0,1;1,0], a reflection in x₂ = x₁. Tracing both basis vectors gives e₁ ↦ e₂ and e₂ ↦ e₁, confirming the matrix.


### 1.9.11 - Two axis reflections equal a rotation

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Horizontal-axis reflection gives (x₁,-x₂); subsequent vertical-axis reflection gives (-x₁,-x₂). This is -I₂ acting on x, a rotation through π radians (also -π modulo 2π). Both standard basis vectors reverse direction. Thus the two-step transformation and the half-turn agree on every vector, not just a sketch.


### 1.9.12 - Identify the rotation in Exercise 8

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Exercise 8 gives T(x₁,x₂) = (-x₂,x₁), with matrix [0,-1;1,0]. Comparing with [cos θ,-sin θ;sin θ,cos θ] yields cos θ = 0,sin θ = 1, so θ = π/2 counterclockwise modulo 2π. The basis-vector action also identifies the same quarter-turn directly.


### 1.9.13 - Sketch T(2,1) using the basis images

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Since (2,1) = 2e₁ + e₂, linearity gives T(2,1) = 2T(e₁) + T(e₂). Copy the left-pointing T(e₁) arrow twice, then append one T(e₂) arrow head to tail. Draw the final arrow from the original origin to the constructed endpoint. The supplied figure gives directions and relative lengths, not labeled numerical coordinates, so a vector-combination construction is the faithful answer.

@customfig relation13


### 1.9.14 - Sketch the image of (-1,3)

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The standard matrix columns are a₁,a₂, so T(-1,3) = -a₁ + 3a₂. Reverse a₁, then add three copies of a₂ using head-to-tail placement; draw the resultant from zero. Because a₁ points down-right, -a₁ points up-left; adding three up-right copies of a₂ gives the endpoint in the construction below. No unprovided numerical coordinates are assumed.

@customfig relation14


### 1.9.15 - Fill the 3 × 3 coefficient matrix

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Read the coefficient of each input in each output. The three outputs are 2x₁ - 3x₃,4x₁,x₁ - x₂ + x₃. Hence the matrix is:

@matrix {"a": [["2", "0", "-3"], ["4", "0", "0"], ["1", "-1", "1"]], "bar": null}

Each zero explicitly indicates an input missing from that output. Expanding the row-column products returns the original three output expressions for all x.


### 1.9.16 - Fill the 3 × 2 coefficient matrix

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 112.

The output coordinates are x₁ - 3x₂,-2x₁ + x₂,x₁. Therefore A is:

@matrix {"a": [["1", "-3"], ["-2", "1"], ["1", "0"]], "bar": null}

It has two columns for the two inputs and three rows for the three outputs. The rule equals Ax for all x by direct row expansion.


### 1.9.17 - Show linearity by finding an implementing matrix

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The first output is zero; the next three are adjacent input sums. Read their coefficients to obtain:

@matrix {"a": [["0", "0", "0", "0"], ["1", "1", "0", "0"], ["0", "1", "1", "0"], ["0", "0", "1", "1"]], "bar": null}

Multiplying this A by an arbitrary input gives exactly the stated outputs. Every matrix transformation preserves addition and scalar multiplication, so this identity proves that T is linear. Merely checking a few numerical inputs would not prove it.


### 1.9.18 - Show linearity by finding an implementing matrix

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 112.

The four outputs are 2x₂ - 3x₁,x₁ - 4x₂,0,x₂. Read their coefficients to obtain:

@matrix {"a": [["-3", "2"], ["1", "-4"], ["0", "0"], ["0", "1"]], "bar": null}

Multiplying this A by an arbitrary input gives exactly the stated outputs. Every matrix transformation preserves addition and scalar multiplication, so this identity proves that T is linear. Merely checking a few numerical inputs would not prove it.


### 1.9.19 - Show linearity by finding an implementing matrix

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The two outputs are x₁ - 5x₂ + 4x₃ and x₂ - 6x₃. Read their coefficients to obtain:

@matrix {"a": [["1", "-5", "4"], ["0", "1", "-6"]], "bar": null}

Multiplying this A by an arbitrary input gives exactly the stated outputs. Every matrix transformation preserves addition and scalar multiplication, so this identity proves that T is linear. Merely checking a few numerical inputs would not prove it.


### 1.9.20 - Show linearity by finding an implementing matrix

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 112.

The scalar output is 2x₁ + 3x₃ - 4x₄, interpreted as a one-entry column. Read their coefficients to obtain:

@matrix {"a": [["2", "0", "3", "-4"]], "bar": null}

Multiplying this A by an arbitrary input gives exactly the stated outputs. Every matrix transformation preserves addition and scalar multiplication, so this identity proves that T is linear. Merely checking a few numerical inputs would not prove it.


### 1.9.21 - Find x whose image is (3,8)

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Use the coefficients of T(x₁,x₂) = (x₁ + x₂,4x₁ + 5x₂) as the standard matrix, then solve the requested output equation.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "1", "3"], ["4", "5", "8"]], "bar": 2}

**Step 1: R2 ← R2 + (-4)R1.** Add -4 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "1", "3"], ["0", "1", "-4"]], "bar": 2}

**Step 2: R1 ← R1 + (-1)R2.** Add -1 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "7"], ["0", "1", "-4"]], "bar": 2}

**Read the equations.** x_1 = 7; x_2 = -4

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["7"], ["-4"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["3"], ["8"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.9.22 - Find x whose image is (-1,4,9)

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 112.

All three output entries must match, so the third equation is included even though the input has only two coordinates.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-2", "-1"], ["-1", "3", "4"], ["3", "-2", "9"]], "bar": 2}

**Step 1: R2 ← R2 + (1)R1.** Add 1 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-2", "-1"], ["0", "1", "3"], ["3", "-2", "9"]], "bar": 2}

**Step 2: R3 ← R3 + (-3)R1.** Add -3 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-2", "-1"], ["0", "1", "3"], ["0", "4", "12"]], "bar": 2}

**Step 3: R3 ← R3 + (-4)R2.** Add -4 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-2", "-1"], ["0", "1", "3"], ["0", "0", "0"]], "bar": 2}

**Step 4: R1 ← R1 + (2)R2.** Add 2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "5"], ["0", "1", "3"], ["0", "0", "0"]], "bar": 2}

**Read the equations.** x_1 = 5; x_2 = 3

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["5"], ["3"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["-1"], ["4"], ["9"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 1.9.23 - True/false: A linear map is determined by its action on identity columns

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** Every input is a combination of those standard basis columns. Linearity applies the same combination to their known images, so no other choices of outputs remain.


### 1.9.24 - True/false: Unique output for each input makes a mapping one-to-one

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** Every function already has a unique output for each input. One-to-one additionally prohibits two different inputs from sharing an output. The zero map is a function with unique output 0 for every input but is not one-to-one.


### 1.9.25 - True/false: Rotation about the origin is linear

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** Its standard matrix is [cos θ,-sin θ;sin θ,cos θ]. The rule equals this matrix times every input, and every matrix transformation is linear. The center being the origin matters.


### 1.9.26 - True/false: The standard matrix columns are images of standard basis columns

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** This is the standard-matrix construction: column j is T(e_j). Placing those images in columns makes Ax equal the linear combination prescribed by T on every input.


### 1.9.27 - True/false: Composing linear transformations may give a nonlinear map

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** For S,T linear, T(S(cu + dv)) = T(cS(u) + dS(v)) = cT(S(u)) + dT(S(v)). This holds for arbitrary u,v,c,d, so the composition is linear. Its matrix is the ordered product.


### 1.9.28 - True/false: Some linear maps ℝ^n → ℝ^m are not matrix transformations

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** The standard-matrix theorem gives A = [T(e₁) ... T(e_n)] and T(x) = Ax for all x. The statement restricts to these finite real coordinate spaces, where that representation always exists.


### 1.9.29 - True/false: A map is onto if each input has some output

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** That is a basic property of a function, not the onto condition. Onto requires every vector in the codomain to be attained. Projection (a,b) ↦ (a,0) is defined for every input but misses (0,1).


### 1.9.30 - True/false: The listed axis and origin reflections have diagonal ±1 form

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** Horizontal reflection is diag(1,-1), vertical reflection is diag(-1,1), and origin reflection is diag(-1,-1). All have zero off-diagonal entries and diagonal entries ±1, as the statement claims. This does not say every reflection, such as a diagonal-line reflection, has that form.


# Section 2.1 - Matrix operations


Original question pages follow. They preserve the exact wording, subparts, diagrams, and numerical data of the supplied exercise scans. Worked solutions begin immediately after these pages. A brief paraphrase at each answer identifies the task; consult the reproduced question for its full wording.


## Original exercises - source PDF page 13

@scan ex-13.png

@page


## Original exercises - source PDF page 14

@scan ex-14.png

@page


## Worked solutions


### 2.1.1 - Compute the four requested expressions

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**-2A:** scale every entry by -2:

@matrix {"a": [["-4", "0", "2"], ["-8", "6", "-4"]], "bar": null}

**B - 2A:** subtract twice each A entry from the corresponding B entry:

@matrix {"a": [["3", "-5", "3"], ["-7", "2", "-7"]], "bar": null}

**AC:** undefined, since A has three columns and C has two rows. **CD:** both factors are 2 × 2, so compute by row-column products:

The product has 2 rows and 2 columns. Each entry uses one row of the left factor and one column of the right factor.

@eq c_{11} = (1)(3) + (2)(-1) = 1

@eq c_{12} = (1)(5) + (2)(4) = 13

@eq c_{21} = (-2)(3) + (1)(-1) = -7

@eq c_{22} = (-2)(5) + (1)(4) = -6

Collect those entries in their row and column positions:

@matrix {"a": [["1", "13"], ["-7", "-6"]], "bar": null}

As a second interpretation, column j of the answer is A times column j of B: it is a linear combination of the columns of A using the entries of that column of B as weights.


### 2.1.2 - Compute the four requested expressions

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 113.

**A + 2B:** the two 2 × 3 sizes match, so scale B and add entrywise:

@matrix {"a": [["16", "-10", "1"], ["6", "-11", "-4"]], "bar": null}

**3C - E:** undefined because 3C is 2 × 2 but E is 2 × 1. **CB:** dimensions (2 × 2)(2 × 3) match; its calculation follows. **EB:** undefined because the one column of E does not match the two rows of B.

The product has 2 rows and 3 columns. Each entry uses one row of the left factor and one column of the right factor.

@eq c_{11} = (1)(7) + (2)(1) = 9

@eq c_{12} = (1)(-5) + (2)(-4) = -13

@eq c_{13} = (1)(1) + (2)(-3) = -5

@eq c_{21} = (-2)(7) + (1)(1) = -13

@eq c_{22} = (-2)(-5) + (1)(-4) = 6

@eq c_{23} = (-2)(1) + (1)(-3) = -5

Collect those entries in their row and column positions:

@matrix {"a": [["9", "-13", "-5"], ["-13", "6", "-5"]], "bar": null}

As a second interpretation, column j of the answer is A times column j of B: it is a linear combination of the columns of A using the entries of that column of B as weights.


### 2.1.3 - Compute 3I₂ - A and (3I₂)A

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The scalar matrix 3I₂ is [3,0;0,3]. Subtract A entrywise to get:

@matrix {"a": [["-1", "1"], ["-5", "5"]], "bar": null}

Multiplication by 3I₂ scales each row by 3, giving (3I₂)A = 3A:

@matrix {"a": [["12", "-3"], ["15", "-6"]], "bar": null}

Subtracting 3I₂ and multiplying by 3I₂ are different operations: the first changes only the matching diagonal entries by subtraction, while the second scales every entry.


### 2.1.4 - Compute A - 5I₃ and (5I₃)A

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 113.

Subtract 5 from each diagonal entry, leaving all off-diagonal entries unchanged:

@matrix {"a": [["4", "-1", "3"], ["-8", "2", "-3"], ["-4", "1", "3"]], "bar": null}

For multiplication, (5I₃)A = 5A, so every entry is scaled:

@matrix {"a": [["45", "-5", "15"], ["-40", "35", "-15"], ["-20", "5", "40"]], "bar": null}

The identity multiplication property explains the second result; direct row-column multiplication verifies it entry by entry.


### 2.1.5 - Compute AB by columns and row-column entries

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 114.

The product has 3 rows and 2 columns. Each entry uses one row of the left factor and one column of the right factor.

@eq c_{11} = (-1)(3) + (2)(-2) = -7

@eq c_{12} = (-1)(-4) + (2)(1) = 6

@eq c_{21} = (5)(3) + (4)(-2) = 7

@eq c_{22} = (5)(-4) + (4)(1) = -16

@eq c_{31} = (2)(3) + (-3)(-2) = 12

@eq c_{32} = (2)(-4) + (-3)(1) = -11

Collect those entries in their row and column positions:

@matrix {"a": [["-7", "6"], ["7", "-16"], ["12", "-11"]], "bar": null}

As a second interpretation, column j of the answer is A times column j of B: it is a linear combination of the columns of A using the entries of that column of B as weights.


### 2.1.6 - Compute AB by columns and row-column entries

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The product has 3 rows and 2 columns. Each entry uses one row of the left factor and one column of the right factor.

@eq c_{11} = (4)(1) + (-2)(4) = -4

@eq c_{12} = (4)(3) + (-2)(-1) = 14

@eq c_{21} = (-3)(1) + (0)(4) = -3

@eq c_{22} = (-3)(3) + (0)(-1) = -9

@eq c_{31} = (3)(1) + (5)(4) = 23

@eq c_{32} = (3)(3) + (5)(-1) = 4

Collect those entries in their row and column positions:

@matrix {"a": [["-4", "14"], ["-3", "-9"], ["23", "4"]], "bar": null}

As a second interpretation, column j of the answer is A times column j of B: it is a linear combination of the columns of A using the entries of that column of B as weights.


### 2.1.7 - Find the size of B

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 114.

A is 5 × 3, so B needs three rows for AB to exist. The product has seven columns, which must be the number of columns in B. Hence B is 3 × 7, giving (5 × 3)(3 × 7) = 5 × 7. The outside dimensions are a consequence of the row-column definition.


### 2.1.8 - How many rows does B have?

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

BC has three rows, and every column of BC is B times a column of C. The output row count is therefore B’s row count: B has three rows. The information does not determine B’s number of columns; it only requires that number to equal the number of rows of C. Inventing a particular inner dimension would go beyond the question.


### 2.1.9 - Choose k so AB = BA

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 114.

Multiplication gives AB = [23,-10 + 5k;-9,15 + k] and BA = [23,15;6 - 3k,15 + k]. Equality requires every corresponding entry to agree. The off-diagonal equations are -10 + 5k = 15 and -9 = 6 - 3k, each giving k = 5. At k = 5 the diagonal entries already match, so this value is both necessary and sufficient.


### 2.1.10 - Show AB = AC although B ≠ C

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The two products are shown separately below. Their equality does not permit cancellation of singular A. The matrices B and C are different, for example their top-left entries are 8 and 5.

The product has 2 rows and 2 columns. Each entry uses one row of the left factor and one column of the right factor.

@eq c_{11} = (2)(8) + (-3)(5) = 1

@eq c_{12} = (2)(4) + (-3)(5) = -7

@eq c_{21} = (-4)(8) + (6)(5) = -2

@eq c_{22} = (-4)(4) + (6)(5) = 14

Collect those entries in their row and column positions:

@matrix {"a": [["1", "-7"], ["-2", "14"]], "bar": null}

As a second interpretation, column j of the answer is A times column j of B: it is a linear combination of the columns of A using the entries of that column of B as weights.

The product has 2 rows and 2 columns. Each entry uses one row of the left factor and one column of the right factor.

@eq c_{11} = (2)(5) + (-3)(3) = 1

@eq c_{12} = (2)(-2) + (-3)(1) = -7

@eq c_{21} = (-4)(5) + (6)(3) = -2

@eq c_{22} = (-4)(-2) + (6)(1) = 14

Collect those entries in their row and column positions:

@matrix {"a": [["1", "-7"], ["-2", "14"]], "bar": null}

As a second interpretation, column j of the answer is A times column j of B: it is a linear combination of the columns of A using the entries of that column of B as weights.

Both products equal [1,-7;-2,14], while B ≠ C. The rows of A are proportional, so A is singular; a nonzero difference B - C can be sent to zero.


### 2.1.11 - Diagonal multiplication and a commuting example

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Right multiplication by D = diag(2,3,5) scales the first, second, third columns of A by 2,3,5, respectively. Left multiplication scales its rows by those factors. Thus AD and DA are:

@matrix {"a": [["2", "3", "5"], ["2", "6", "15"], ["2", "12", "25"]], "bar": null}

@matrix {"a": [["2", "2", "2"], ["3", "6", "9"], ["5", "20", "25"]], "bar": null}

For the final request choose B = 2I₃. It is neither I₃ nor zero, and AB = A(2I₃) = 2A = (2I₃)A = BA by the scalar and identity laws. This works for the stated A without claiming that every diagonal matrix commutes with it.


### 2.1.12 - Construct nonzero distinct columns of B with AB = 0

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

For A = [3,-6;-1,2], the homogeneous equation says x₁ = 2x₂ in both rows. Choose two distinct nonzero solution columns b₁ = (2,1), b₂ = (4,2). Then B = [2,4;1,2], and Ab₁ = (6 - 6,-2 + 2) = 0 while Ab₂ = (12 - 12,-4 + 4) = 0. Since AB = [Ab₁ Ab₂], the whole product is zero, although neither A nor B is zero.


### 2.1.13 - Write the displayed column array as a product

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Let R = [r₁ ... r_p], an n × p matrix. The matrix Q is m × n, so QR is m × p and its jth column is Qr_j. Hence [Qr₁ ... Qr_p] = Q[r₁ ... r_p]. These are the natural structural factors. To ensure literally that neither factor is an identity even in special cases, use (tQ)((1/t)R) instead: choose a nonzero t among 2,3,4 such that tQ and (1/t)R are not identity matrices. Each identity condition excludes at most one t, so such a choice always exists. Scalar factors cancel, leaving QR. This also handles any exceptional supplied Q or R that happens to be an identity.


### 2.1.14 - Economic interpretation of UQ

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

U has three rows for materials, labor, overhead and two columns for products B,C. Each q_j has two entries giving dollar outputs of those products in quarter j. Thus Uq_j is a three-entry vector of the corresponding quarter’s costs, in dollars, by cost category. For Q = [q₁ q₂ q₃ q₄], UQ is 3 × 4; entry i,j is the dollar cost in category i during quarter j. The numeric U from the referenced example is not supplied, but the question asks for interpretation, so no missing values are needed or invented.


### 2.1.15 - True/false: AB has columns a₁b₁ and a₂b₂

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** The correct columns are Ab₁ and Ab₂. A column vector a₁ cannot ordinarily multiply another column b₁ under the usual matrix rule because their inner dimensions do not match. Matrix multiplication applies the entire A to each B column.


### 2.1.16 - True/false: AB is one column Ab₁ + Ab₂ + Ab₃

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** For B with three columns, AB has three columns [Ab₁ Ab₂ Ab₃]. Adding them produces a single vector and loses the separate effects of three input coordinates. The dimensions alone distinguish these arrays.


### 2.1.17 - True/false: Columns of AB combine B columns using A-column weights

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** The product columns combine A’s columns using entries from the corresponding B column. For instance, Ab_j = b_{1j}a₁ + ... + b_{nj}a_n. Reversing A and B describes a different or undefined operation.


### 2.1.18 - True/false: Row 2 of AB is row 2 of A times B

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** The jth entry of that row is row₂(A) times column j of B, exactly the row-column definition of (AB)_{2j}. Collecting all such entries yields row₂(A)B.


### 2.1.19 - True/false: AB + AC = A(B + C)

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** Entry i,j on either side is Σ over k of a_{ik}(b_{kj} + c_{kj}). Distributing real-number multiplication makes it the sum of entries of AB and AC. Compatible sizes are assumed.


### 2.1.20 - True/false: A^T + B^T = (A + B)^T

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** Entry i,j of either side is a_{ji} + b_{ji}. Both transposed matrices have matching sizes since A and B must have equal sizes for the original sum.


### 2.1.21 - True/false: (AB)C = (AC)B

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** Associativity allows (AB)C = A(BC), not exchanging B and C. Let A = I₂, B = [1,1;0,1], C = [1,0;0,2]. Then BC = [1,2;0,2] while CB = [1,1;0,2], so the proposed equality fails.


### 2.1.22 - True/false: (AB)^T = A^T B^T

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** The correct order reverses: (AB)^T = B^T A^T. For the B,C in the previous counterexample, transposing BC gives [1,0;2,2], whereas B^T C^T = [1,0;1,2]. Thus even when both products exist, the stated order can fail.


### 2.1.23 - True/false: Transpose keeps the same multiplication order

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** Transposition interchanges row and column roles, reversing the factor order. The proof compares entries (AB)_{ji} with (B^T A^T)_{ij}; both equal Σ over k of a_{jk}b_{ki}. Keeping the order would generally give different terms.


### 2.1.24 - True/false: Transpose distributes over a sum

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** The i,j entry of (A + B)^T is a_{ji} + b_{ji}, exactly the i,j entry of A^T + B^T. No factor order issue arises because addition is entrywise.


### 2.1.25 - Recover the first two columns of B

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Column j of AB is Ab_j, so solve A times each unknown column against the corresponding supplied product column. The two full solves follow.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-2", "-1"], ["-2", "5", "6"]], "bar": 2}

**Step 1: R2 ← R2 + (2)R1.** Add 2 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-2", "-1"], ["0", "1", "4"]], "bar": 2}

**Step 2: R1 ← R1 + (2)R2.** Add 2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "7"], ["0", "1", "4"]], "bar": 2}

**Read the equations.** x_1 = 7; x_2 = 4

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["7"], ["4"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["-1"], ["6"]], "bar": null}

These entries equal the original right-hand sides, in order. 

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["1", "-2", "2"], ["-2", "5", "-9"]], "bar": 2}

**Step 1: R2 ← R2 + (2)R1.** Add 2 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-2", "2"], ["0", "1", "-5"]], "bar": 2}

**Step 2: R1 ← R1 + (2)R2.** Add 2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-8"], ["0", "1", "-5"]], "bar": 2}

**Read the equations.** x_1 = -8; x_2 = -5

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["-8"], ["-5"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["2"], ["-9"]], "bar": null}

These entries equal the original right-hand sides, in order. 

Thus b₁ = (7,4) and b₂ = (-8,-5). Direct checks: A(7,4) = (-1,6) and A(-8,-5) = (2,-9), the required first and second product columns. No other B column is requested.


### 2.1.26 - Equal first two columns of B

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

If b₁ = b₂, applying the same A to both gives Ab₁ = Ab₂. These are the first two columns of AB by definition, so they are equal. The conclusion is equality of columns, not necessarily zero columns. No invertibility assumption is needed because we are applying a function to equal inputs.


### 2.1.27 - Third B column equals the sum of the first two

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

If b₃ = b₁ + b₂, then A b₃ = A(b₁ + b₂) = Ab₁ + Ab₂ by matrix-vector linearity. Therefore column 3 of AB is the sum of columns 1 and 2. This preserves the actual input coefficients 1 and 1; it does not assert any relationship between A’s own numbered columns.


### 2.1.28 - Second B column is zero

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Column 2 of AB is Ab₂ = A0 = 0. Its length equals the number of rows of A. The result follows even when A is nonzero, because every weighted column contribution has coefficient zero. No information about the remaining product columns follows.


### 2.1.29 - Last product column zero but last B column nonzero

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Let b be the nonzero last column of B. The hypothesis gives Ab = 0. Thus Ax = 0 has a nontrivial solution, so the columns of A are linearly dependent. The relevant weights are the entries of b. The conclusion does not imply that any individual column of A is zero.


### 2.1.30 - Dependent B columns imply dependent AB columns

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Dependence gives a nonzero weight vector c such that Bc = 0. Associativity gives (AB)c = A(Bc) = A0 = 0. The same weights c remain nonzero, so they constitute a nontrivial dependence relation among the columns of AB. This is a proof for arbitrary compatible matrices, not a numerical example.


### 2.1.31 - A left inverse forces trivial homogeneous solutions

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Assume CA = I_n. If Ax = 0, left-multiply by C to get CAx = 0, hence I_n x = x = 0. Therefore the columns of A are independent. An m × n matrix cannot have n independent columns when n > m, since it would have more columns than row pivots. Thus A cannot have more columns than rows: n ≤ m.


### 2.1.32 - A right inverse forces existence for every b

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Assume AD = I_m. For any b ∈ ℝ^m choose x = Db. Then Ax = ADb = I_m b = b, constructing a solution for every b. Therefore A has a pivot in every row. An m × n matrix can have at most n pivots, so m ≤ n: A cannot have more rows than columns.


### 2.1.33 - Left and right inverses force equal dimensions and equality

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Let A be m × n, with CA = I_n and AD = I_m. The argument of Exercise 31 yields n ≤ m, while Exercise 32 yields m ≤ n, so m = n. Then use the compatible product CAD: C(AD) = CI_m = C, and (CA)D = I_nD = D. Associativity says these are equal, hence C = D. This proves both requested conclusions without assuming squareness at the start.


### 2.1.34 - Construct D with AD = I₃

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The columns of A span ℝ^3, so each e_j in ℝ^3 has some preimage d_j ∈ ℝ^n satisfying Ad_j = e_j. Solve those three systems and assemble D = [d₁ d₂ d₃], an n × 3 matrix. Then AD has columns [Ad₁ Ad₂ Ad₃] = [e₁ e₂ e₃] = I₃. The construction is valid even when A has more than three columns and the chosen preimages are not unique.


### 2.1.35 - Inner and outer products

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

For u = (-2,3,-4) and v = (a,b,c), u^T v = -2a + 3b - 4c and v^T u = -2a + 3b - 4c. These are scalars, or 1 × 1 matrices. The outer products retain all pairwise products:

@matrix {"a": [["-2a", "-2b", "-2c"], ["3a", "3b", "3c"], ["-4a", "-4b", "-4c"]], "bar": null}

@matrix {"a": [["-2a", "3a", "-4a"], ["-2b", "3b", "-4b"], ["-2c", "3c", "-4c"]], "bar": null}

The first displayed matrix is uv^T and the second is vu^T. For example, the (1,2) entry of uv^T is u₁v₂ = -2b. Both are 3 × 3, unlike the scalar inner products.


### 2.1.36 - Compare the general inner and outer products

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The scalar products agree: u^T v = Σ u_i v_i = Σ v_i u_i = v^T u, using commutativity of real multiplication. The outer products generally do not agree entrywise. Instead (uv^T)^T = vu^T by the product transpose law. For example u = (1,0), v = (0,1) give uv^T = [0,1;0,0] and vu^T = [0,0;1,0], which are transposes and are unequal.


### 2.1.37 - Prove left and right distributive laws

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

For left distributivity, entry i,j of A(B + C) is Σ over k of a_{ik}(b_{kj} + c_{kj}). Real distributivity turns this into Σ a_{ik}b_{kj} + Σ a_{ik}c_{kj}, the i,j entry of AB + AC. For right distributivity, entry i,j of (B + C)A is Σ (b_{ik} + c_{ik})a_{kj} = Σ b_{ik}a_{kj} + Σ c_{ik}a_{kj}, the i,j entry of BA + CA. The matrices on each side have the same size by the stated compatibility assumption. Agreement of every entry proves both identities.


### 2.1.38 - Prove the scalar-product identities

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

For any scalar r, entry i,j of (rA)B is Σ (r a_{ik})b_{kj} = r Σ a_{ik}b_{kj}. Entry i,j of A(rB) is Σ a_{ik}(r b_{kj}) = r Σ a_{ik}b_{kj}. That common value is entry i,j of r(AB). All arrays have the same product dimensions. Therefore (rA)B = A(rB) = r(AB), with no swapping of matrix factors.


### 2.1.39 - Prove I_m A = A

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Write A = [a₁ ... a_n]. Each column of I_m A is I_m a_j = a_j, using the permitted identity action on every vector in ℝ^m. Thus I_m A has exactly A’s columns and size, so it equals A. This column argument extends the vector identity to the whole matrix.


### 2.1.40 - Prove A I_n = A

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Column j of A I_n is Ae_j. Multiplying by e_j gives weight 1 to column j of A and weight 0 to all other columns, so Ae_j = a_j. Therefore A I_n = [a₁ ... a_n] = A. The identity size is n because it acts on A’s input coordinates.


### 2.1.41 - Prove transpose reverses a product

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Entry i,j of (AB)^T is (AB)_{ji} = Σ over k of a_{jk}b_{ki}. Entry i,j of B^T A^T is Σ over k of (B^T)_{ik}(A^T)_{kj} = Σ b_{ki}a_{jk}. Real multiplication commutes, so each summand agrees. If A is m × n and B is n × p, both arrays are p × m. Equal sizes and all equal entries prove (AB)^T = B^T A^T.


### 2.1.42 - Transpose the product ABx

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

View the vector x as a column matrix. Apply the product rule twice: (ABx)^T = x^T(AB)^T = x^T B^T A^T. For A m × n, B n × p, x p × 1, both sides are 1 × m. The reversal affects the entire ordered list of factors. One may regroup products, but must retain this reversed factor order.


### 2.1.43 - Cut-off matrix-program question

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The supplied page ends after asking to find program documentation and write commands, before identifying the operations to be documented. The missing list is essential to the task, so no specific commands or program are invented. A clearer scan of the continuation is needed. This book’s exact-arithmetic verification code is editable source, but it is not presented as an answer to the missing source exercise.


# Section 2.2 - The inverse of a matrix


Original question pages follow. They preserve the exact wording, subparts, diagrams, and numerical data of the supplied exercise scans. Worked solutions begin immediately after these pages. A brief paraphrase at each answer identifies the task; consult the reproduced question for its full wording.


## Original exercises - source PDF page 15

@scan ex-15.png

@page


## Original exercises - source PDF page 16

@scan ex-16.png

@page


## Worked solutions


### 2.2.1 - Find the inverse using the 2 × 2 formula

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 115.

The determinant is (8)(2) - (3)(5) = 1, which is nonzero. Swap the diagonal entries, negate the off-diagonal entries, and divide every entry by 1. The inverse is:

@matrix {"a": [["2", "-3"], ["-5", "8"]], "bar": null}

A direct product check follows. Reversing the factors also gives I₂.

The product has 2 rows and 2 columns. Each entry uses one row of the left factor and one column of the right factor.

@eq c_{11} = (8)(2) + (3)(-5) = 1

@eq c_{12} = (8)(-3) + (3)(8) = 0

@eq c_{21} = (5)(2) + (2)(-5) = 0

@eq c_{22} = (5)(-3) + (2)(8) = 1

Collect those entries in their row and column positions:

@matrix {"a": [["1", "0"], ["0", "1"]], "bar": null}

As a second interpretation, column j of the answer is A times column j of B: it is a linear combination of the columns of A using the entries of that column of B as weights.


### 2.2.2 - Find the inverse using the 2 × 2 formula

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The determinant is (3)(2) - (1)(7) = -1, which is nonzero. Swap the diagonal entries, negate the off-diagonal entries, and divide every entry by -1. The inverse is:

@matrix {"a": [["-2", "1"], ["7", "-3"]], "bar": null}

A direct product check follows. Reversing the factors also gives I₂.

The product has 2 rows and 2 columns. Each entry uses one row of the left factor and one column of the right factor.

@eq c_{11} = (3)(-2) + (1)(7) = 1

@eq c_{12} = (3)(1) + (1)(-3) = 0

@eq c_{21} = (7)(-2) + (2)(7) = 0

@eq c_{22} = (7)(1) + (2)(-3) = 1

Collect those entries in their row and column positions:

@matrix {"a": [["1", "0"], ["0", "1"]], "bar": null}

As a second interpretation, column j of the answer is A times column j of B: it is a linear combination of the columns of A using the entries of that column of B as weights.


### 2.2.3 - Find the inverse using the 2 × 2 formula

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The determinant is (8)(-3) - (3)(-7) = -3, which is nonzero. Swap the diagonal entries, negate the off-diagonal entries, and divide every entry by -3. The inverse is:

@matrix {"a": [["1", "1"], ["-7/3", "-8/3"]], "bar": null}

A direct product check follows. Reversing the factors also gives I₂.

The product has 2 rows and 2 columns. Each entry uses one row of the left factor and one column of the right factor.

@eq c_{11} = (8)(1) + (3)(-7/3) = 1

@eq c_{12} = (8)(1) + (3)(-8/3) = 0

@eq c_{21} = (-7)(1) + (-3)(-7/3) = 0

@eq c_{22} = (-7)(1) + (-3)(-8/3) = 1

Collect those entries in their row and column positions:

@matrix {"a": [["1", "0"], ["0", "1"]], "bar": null}

As a second interpretation, column j of the answer is A times column j of B: it is a linear combination of the columns of A using the entries of that column of B as weights.


### 2.2.4 - Find the inverse using the 2 × 2 formula

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The determinant is (3)(-4) - (-2)(7) = 2, which is nonzero. Swap the diagonal entries, negate the off-diagonal entries, and divide every entry by 2. The inverse is:

@matrix {"a": [["-2", "1"], ["-7/2", "3/2"]], "bar": null}

A direct product check follows. Reversing the factors also gives I₂.

The product has 2 rows and 2 columns. Each entry uses one row of the left factor and one column of the right factor.

@eq c_{11} = (3)(-2) + (-2)(-7/2) = 1

@eq c_{12} = (3)(1) + (-2)(3/2) = 0

@eq c_{21} = (7)(-2) + (-4)(-7/2) = 0

@eq c_{22} = (7)(1) + (-4)(3/2) = 1

Collect those entries in their row and column positions:

@matrix {"a": [["1", "0"], ["0", "1"]], "bar": null}

As a second interpretation, column j of the answer is A times column j of B: it is a linear combination of the columns of A using the entries of that column of B as weights.


### 2.2.5 - Verify the inverse from Exercise 1

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

An inverse must multiply with the original matrix to give the identity. Compute both orders, not entrywise reciprocals.

The product has 2 rows and 2 columns. Each entry uses one row of the left factor and one column of the right factor.

@eq c_{11} = (8)(2) + (3)(-5) = 1

@eq c_{12} = (8)(-3) + (3)(8) = 0

@eq c_{21} = (5)(2) + (2)(-5) = 0

@eq c_{22} = (5)(-3) + (2)(8) = 1

Collect those entries in their row and column positions:

@matrix {"a": [["1", "0"], ["0", "1"]], "bar": null}

As a second interpretation, column j of the answer is A times column j of B: it is a linear combination of the columns of A using the entries of that column of B as weights.

The product has 2 rows and 2 columns. Each entry uses one row of the left factor and one column of the right factor.

@eq c_{11} = (2)(8) + (-3)(5) = 1

@eq c_{12} = (2)(3) + (-3)(2) = 0

@eq c_{21} = (-5)(8) + (8)(5) = 0

@eq c_{22} = (-5)(3) + (8)(2) = 1

Collect those entries in their row and column positions:

@matrix {"a": [["1", "0"], ["0", "1"]], "bar": null}

As a second interpretation, column j of the answer is A times column j of B: it is a linear combination of the columns of A using the entries of that column of B as weights.


### 2.2.6 - Verify the inverse from Exercise 2

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

An inverse must multiply with the original matrix to give the identity. Compute both orders, not entrywise reciprocals.

The product has 2 rows and 2 columns. Each entry uses one row of the left factor and one column of the right factor.

@eq c_{11} = (3)(-2) + (1)(7) = 1

@eq c_{12} = (3)(1) + (1)(-3) = 0

@eq c_{21} = (7)(-2) + (2)(7) = 0

@eq c_{22} = (7)(1) + (2)(-3) = 1

Collect those entries in their row and column positions:

@matrix {"a": [["1", "0"], ["0", "1"]], "bar": null}

As a second interpretation, column j of the answer is A times column j of B: it is a linear combination of the columns of A using the entries of that column of B as weights.

The product has 2 rows and 2 columns. Each entry uses one row of the left factor and one column of the right factor.

@eq c_{11} = (-2)(3) + (1)(7) = 1

@eq c_{12} = (-2)(1) + (1)(2) = 0

@eq c_{21} = (7)(3) + (-3)(7) = 0

@eq c_{22} = (7)(1) + (-3)(2) = 1

Collect those entries in their row and column positions:

@matrix {"a": [["1", "0"], ["0", "1"]], "bar": null}

As a second interpretation, column j of the answer is A times column j of B: it is a linear combination of the columns of A using the entries of that column of B as weights.


### 2.2.7 - Use the inverse from Exercise 1 to solve

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 115.

The inverse is [2,-3;-5,8], so x = A^(-1)b = (2(2) - 3(-1), -5(2) + 8(-1)) = (7,-18). The following elimination and original-equation check independently validate the inverse-method answer.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["8", "3", "2"], ["5", "2", "-1"]], "bar": 2}

**Step 1: R1 ← (1/8)R1.** Multiply every entry of row 1, including any right-hand side, by 1/8. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "3/8", "1/4"], ["5", "2", "-1"]], "bar": 2}

**Step 2: R2 ← R2 + (-5)R1.** Add -5 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "3/8", "1/4"], ["0", "1/8", "-9/4"]], "bar": 2}

**Step 3: R2 ← (8)R2.** Multiply every entry of row 2, including any right-hand side, by 8. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "3/8", "1/4"], ["0", "1", "-18"]], "bar": 2}

**Step 4: R1 ← R1 + (-3/8)R2.** Add -3/8 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "7"], ["0", "1", "-18"]], "bar": 2}

**Read the equations.** x_1 = 7; x_2 = -18

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["7"], ["-18"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["2"], ["-1"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 2.2.8 - Use the inverse from Exercise 2 to solve

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The inverse is [-2,1;7,-3]. Thus A^(-1)b = (4 + 3,-14 - 9) = (7,-23). The reduction below and substitution verify the same answer from the original system.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["3", "1", "-2"], ["7", "2", "3"]], "bar": 2}

**Step 1: R1 ← (1/3)R1.** Multiply every entry of row 1, including any right-hand side, by 1/3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "1/3", "-2/3"], ["7", "2", "3"]], "bar": 2}

**Step 2: R2 ← R2 + (-7)R1.** Add -7 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "1/3", "-2/3"], ["0", "-1/3", "23/3"]], "bar": 2}

**Step 3: R2 ← (-3)R2.** Multiply every entry of row 2, including any right-hand side, by -3. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "1/3", "-2/3"], ["0", "1", "-23"]], "bar": 2}

**Step 4: R1 ← R1 + (-1/3)R2.** Add -1/3 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "7"], ["0", "1", "-23"]], "bar": 2}

**Read the equations.** x_1 = 7; x_2 = -23

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["7"], ["-23"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["-2"], ["3"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 2.2.9 - Solve four systems by inverse and simultaneous reduction

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The determinant of A = [1,2;5,12] is 12 - 10 = 2, so A^(-1) = [6,-1;-5/2,1/2]. Part (a): multiply each b column by this matrix. Part (b): the same answers arise by carrying all four right-hand sides through one reduction:

The starting matrix is:

@matrix {"a": [["1", "2", "-1", "1", "2", "3"], ["5", "12", "3", "-5", "6", "5"]], "bar": 2}

**Step 1: R2 ← R2 + (-5)R1.** Add -5 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "2", "-1", "1", "2", "3"], ["0", "2", "8", "-10", "-4", "-10"]], "bar": 2}

**Step 2: R2 ← (1/2)R2.** Multiply every entry of row 2, including any right-hand side, by 1/2. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "2", "-1", "1", "2", "3"], ["0", "1", "4", "-5", "-2", "-5"]], "bar": 2}

**Step 3: R1 ← R1 + (-2)R2.** Add -2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-9", "11", "6", "13"], ["0", "1", "4", "-5", "-2", "-5"]], "bar": 2}

The four input solutions are the columns of the final right block: (-9,4), (11,-5), (6,-2), and (13,-5). Checking with original A gives (-1,3),(1,-5),(2,6),(3,5), respectively. Thus all four systems are verified. The appended block has four columns, but it does not add four coefficient variables.


### 2.2.10 - Show AD = I forces D = A^(-1) when A is invertible

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Left-multiply AD = I by A^(-1). Associativity gives (A^(-1)A)D = A^(-1)I, hence I D = A^(-1) and D = A^(-1). The assumption that A is invertible provides the legal left multiplier. The proof does not cancel A informally.


### 2.2.11 - True/false: An inverse satisfies both AB = I and BA = I

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** These are the two defining identities for the inverse of a square matrix. Both hold for the unique inverse. A theorem may allow one to infer the other for square matrices, but that does not change the defining conditions.


### 2.2.12 - True/false: Inverse of a product keeps the factor order

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** For invertible A,B, (AB)^(-1) = B^(-1)A^(-1). Multiplying AB by this reverse-order candidate brings B beside B^(-1) and then A beside A^(-1). Keeping the order generally leaves uncancelled interleaved factors.


### 2.2.13 - True/false: A^(-1)B^(-1) is the inverse of AB

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** It is the inverse of BA. As a numerical check, take A = [1,1;0,1], B = [1,0;0,2]. Then (AB)^(-1) = [1,-1;0,1/2], whereas A^(-1)B^(-1) = [1,-1/2;0,1/2]. They are unequal.


### 2.2.14 - True/false: The inverse of A^(-1) is A

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** The same two identities AA^(-1) = I and A^(-1)A = I show that A undoes A^(-1) in both orders. Uniqueness then identifies its inverse as A.


### 2.2.15 - True/false: ab - cd ≠ 0 ensures a 2 × 2 inverse

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** The determinant is ad - bc. For A = [1,2;2,4], ab - cd = 2 - 8 = -6 ≠ 0, but ad - bc = 4 - 4 = 0. The columns are proportional, so this is a singular counterexample satisfying the stated inequality.


### 2.2.16 - True/false: ad = bc makes the 2 × 2 matrix singular

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** The determinant ad - bc is zero. If the first row is nonzero, (-b,a) is a nonzero homogeneous solution; if it is zero, a nonzero solution is obtained from the remaining row or any vector if both rows vanish. Thus the transformation cannot have a two-sided inverse.


### 2.2.17 - True/false: Invertibility ensures consistency for every b

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** For any b, choose x = A^(-1)b. Then Ax = AA^(-1)b = b, constructing a solution. The same inverse also proves uniqueness, although this statement asks only consistency.


### 2.2.18 - True/false: Row reducing A to identity proves invertibility

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** The elementary row operations have an invertible product E with EA = I. Applying them to I gives E, and A = E^(-1), so E = A^(-1). This is the Gauss-Jordan inverse theorem for square A.


### 2.2.19 - True/false: Every elementary matrix is invertible

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**True.** Its single row operation can be undone: swap again, scale by the reciprocal nonzero scalar, or add the opposite multiple of the retained row. The matrix for that reverse operation is its inverse.


### 2.2.20 - True/false: Operations reducing A to I also reduce A^(-1) to I

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

**False.** Their combined left multiplier is A^(-1), so applied to A^(-1) they give A^(-2), not generally I. For A = 2I, the reduction scales rows by 1/2; applying it to A^(-1) = (1/2)I gives (1/4)I. The actual theorem says the operations send I to A^(-1).


### 2.2.21 - Unique matrix solution of AX = B

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 115.

Existence: set X = A^(-1)B. Dimensions are (n × n)(n × p) = n × p, and AX = A(A^(-1)B) = (AA^(-1))B = B. Uniqueness: if Y is any matrix satisfying AY = B, left-multiply by A^(-1) to get Y = A^(-1)B = X. This proves every column system at once and does not require B to be square.


### 2.2.22 - Why [A B] reduction computes A^(-1)B

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Each elementary row operation left-multiplies every block by the same elementary matrix. Their total product E sends A to I, so EA = I and E = A^(-1). Consequently the final right block is X = EB = A^(-1)B. This explains why carrying B through elimination works directly without separately forming and multiplying the inverse. Dimensions permit any n × p right block B.


### 2.2.23 - Cancellation with invertible A and failure without it

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 115.

If AB = AC and A is invertible, left-multiply by A^(-1). Associativity gives B = C. In general this is false for singular A: take A = [1,0;0,0], B = [0,0;0,1], C = 0. Both products are zero, but B ≠ C. This counterexample satisfies matching dimensions and directly shows why invertibility matters.


### 2.2.24 - Cancel an invertible right factor

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

From (B - C)D = 0, multiply both sides on the right by D^(-1). This gives (B - C)(DD^(-1)) = 0D^(-1), so B - C = 0 and hence B = C. Left-multiplication would not put D beside its inverse in general. Only D needs to be invertible; B and C need not be square.


### 2.2.25 - Produce an inverse for ABC

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Choose D = C^(-1)B^(-1)A^(-1). Then (ABC)D = AB(CC^(-1))B^(-1)A^(-1) = A(BB^(-1))A^(-1) = I. Similarly D(ABC) = C^(-1)B^(-1)(A^(-1)A)BC = C^(-1)(B^(-1)B)C = I. Associativity permits these regroupings without moving factors. Thus D is the inverse by definition.


### 2.2.26 - B and AB invertible imply A invertible

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Let C = AB. Since B is invertible, right-multiplication yields A = CB^(-1). Both factors on the right are invertible, so A is invertible and its inverse is B C^(-1). Check A(B C^(-1)) = CB^(-1)B C^(-1) = I and (B C^(-1))A = B C^(-1)C B^(-1) = I. This produces the inverse rather than assuming cancellation alone proves it.


### 2.2.27 - Solve AB = BC for A

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 115.

Right-multiply by B^(-1) to obtain ABB^(-1) = BCB^(-1), hence A = BCB^(-1). Substituting back gives AB = BCB^(-1)B = BC, proving the formula meets the original equation. The factor order is essential; one cannot simplify to A = C unless an extra commuting relation is known.


### 2.2.28 - Solve A = PBP^(-1) for B

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Left-multiply by P^(-1) and right-multiply by P. The result is P^(-1)AP = P^(-1)PBP^(-1)P = B. Thus B = P^(-1)AP. Substituting into PBP^(-1) cancels the adjacent inverse pairs and returns A, validating the formula. Only P’s invertibility is needed for this rearrangement.


### 2.2.29 - Solve C^(-1)(A + X)B^(-1) = I

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Left-multiply by C, giving (A + X)B^(-1) = C. Right-multiply by B to obtain A + X = CB. Hence X = CB - A. This matrix always exists with the stated matching sizes; X itself need not be invertible. Substitution gives C^(-1)(CB)B^(-1) = I, so existence is proved and the reversible rearrangement also proves uniqueness.


### 2.2.30 - Solve (A - AX)^(-1) = X^(-1)B

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Part (a): left-multiply by X to obtain B = X(A - AX)^(-1). Both factors are invertible by the hypotheses, so B is invertible; indeed B^(-1) = (A - AX)X^(-1). Part (b): invert the original equality, preserving reverse order, to get A - AX = B^(-1)X. Rearrange to A = (A + B^(-1))X. Thus A + B^(-1) = AX^(-1), which is invertible since A and X are invertible. Therefore X = (A + B^(-1))^(-1)A. The proof of that new factor’s invertibility is necessary before using its inverse. Multiplying the formula equation back yields A - AX = B^(-1)X, and inversion recovers the original identity under the given assumptions.


### 2.2.31 - Why are columns independent when A is invertible?

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

If Ax = 0, left-multiplying by A^(-1) gives x = 0. Thus only the trivial weights combine the columns to zero, which is the definition of column independence. This directly connects invertibility to the homogeneous test without relying on a numerical reduction.


### 2.2.32 - Why do invertible columns span ℝ^n?

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

For every b ∈ ℝ^n, x = A^(-1)b exists and satisfies Ax = b. Hence every b is a linear combination of the columns, using the entries of that x as weights. By definition the columns span ℝ^n. Equivalently, the every-right-hand-side existence theorem gives a pivot in every row.


### 2.2.33 - Trivial homogeneous solution implies invertibility for square A

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Only the trivial solution of Ax = 0 means no free coefficient variables, so all n columns have pivots. A has n rows as well, so its RREF has n leading 1s, one per row and column, and is I_n. Thus A is row equivalent to I_n. The Gauss-Jordan inverse theorem then proves invertibility. The same conclusion would fail for a tall nonsquare matrix, so squareness is explicitly used.


### 2.2.34 - Every-right-hand-side existence implies invertibility for square A

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Solvability for each b ∈ ℝ^n gives a pivot in every row of A. There are n rows and n columns, hence n pivots and no free columns. Its RREF is I_n, so A is row equivalent to the identity and is invertible. A wide rectangular matrix can be onto without an ordinary two-sided inverse; the square hypothesis is required.


### 2.2.35 - Why ad - bc = 0 prevents a 2 × 2 inverse

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

If (a,b) ≠ (0,0), let x = (-b,a). It is nonzero and Ax = (-ab + ba,-cb + da) = (0,ad - bc) = 0. If a = b = 0 but (c,d) ≠ (0,0), choose x = (-d,c); both row products are zero and x is nonzero. If all entries are zero, choose x = (1,0). Thus every case supplies a nontrivial homogeneous solution in addition to x = 0. An inverse would force every such solution to zero by left multiplication, a contradiction.


### 2.2.36 - Prove the 2 × 2 formula works

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Put δ = ad - bc ≠ 0 and C = (1/δ)[d,-b;-c,a]. Then AC = (1/δ)[ad - bc,-ab + ba;cd - dc,-cb + da] = I₂. Likewise CA = (1/δ)[da - bc,db - bd;-ca + ac,-cb + ad] = I₂. Division is permitted because δ is nonzero. Both inverse identities hold, proving C = A^(-1) by definition.


### 2.2.37 - Show row operations equal elementary left products

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Part (a): row i of I selects row i of A in the product, so row_i(I)A = row_i(A). Part (b): swapping rows 1 and 2 of I₃ gives E = [0,1,0;1,0,0;0,0,1]. Its first row selects row 2 of A, second selects row 1, third selects row 3; therefore EA performs the stated interchange. Part (c): E = diag(1,1,5) has third row 5row₃(I), so row 3 of EA is 5row₃(A), with the other rows unchanged. Each claim follows from the same row-column rule, for arbitrary entries of A.


### 2.2.38 - Elementary matrix for row 3 minus four times row 1

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

Take E = [1,0,0;0,1,0;-4,0,1], obtained by that operation on I₃. The first two rows of EA reproduce rows 1 and 2 of A. Its third row is -4row₁(A) + row₃(A), since E’s third-row coefficients are -4,0,1. Thus EA is exactly the requested row replacement. Its inverse adds four times row 1 to row 3, confirming reversibility.


### 2.2.39 - Find the inverse by Gauss-Jordan elimination, if it exists

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The starting matrix is:

@matrix {"a": [["1", "2", "1", "0"], ["4", "7", "0", "1"]], "bar": 2}

**Step 1: R2 ← R2 + (-4)R1.** Add -4 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "2", "1", "0"], ["0", "-1", "-4", "1"]], "bar": 2}

**Step 2: R2 ← (-1)R2.** Multiply every entry of row 2, including any right-hand side, by -1. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "2", "1", "0"], ["0", "1", "4", "-1"]], "bar": 2}

**Step 3: R1 ← R1 + (-2)R2.** Add -2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-7", "2"], ["0", "1", "4", "-1"]], "bar": 2}

The left block is I. The right block is therefore A^(-1):

@matrix {"a": [["-7", "2"], ["4", "-1"]], "bar": null}

**Verification.** Multiplying in each order gives the identity:

@matrix {"a": [["1", "0"], ["0", "1"]], "bar": null}

The same elementary operations changed A into I and I into A^(-1). They amount to multiplication on the left by A^(-1), which explains why the procedure works.


### 2.2.40 - Find the inverse by Gauss-Jordan elimination, if it exists

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The starting matrix is:

@matrix {"a": [["5", "10", "1", "0"], ["4", "7", "0", "1"]], "bar": 2}

**Step 1: R1 ← (1/5)R1.** Multiply every entry of row 1, including any right-hand side, by 1/5. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "2", "1/5", "0"], ["4", "7", "0", "1"]], "bar": 2}

**Step 2: R2 ← R2 + (-4)R1.** Add -4 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "2", "1/5", "0"], ["0", "-1", "-4/5", "1"]], "bar": 2}

**Step 3: R2 ← (-1)R2.** Multiply every entry of row 2, including any right-hand side, by -1. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "2", "1/5", "0"], ["0", "1", "4/5", "-1"]], "bar": 2}

**Step 4: R1 ← R1 + (-2)R2.** Add -2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-7/5", "2"], ["0", "1", "4/5", "-1"]], "bar": 2}

The left block is I. The right block is therefore A^(-1):

@matrix {"a": [["-7/5", "2"], ["4/5", "-1"]], "bar": null}

**Verification.** Multiplying in each order gives the identity:

@matrix {"a": [["1", "0"], ["0", "1"]], "bar": null}

The same elementary operations changed A into I and I into A^(-1). They amount to multiplication on the left by A^(-1), which explains why the procedure works.


### 2.2.41 - Find the inverse by Gauss-Jordan elimination, if it exists

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 115.

The starting matrix is:

@matrix {"a": [["1", "0", "-2", "1", "0", "0"], ["-3", "1", "4", "0", "1", "0"], ["2", "-3", "4", "0", "0", "1"]], "bar": 3}

**Step 1: R2 ← R2 + (3)R1.** Add 3 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-2", "1", "0", "0"], ["0", "1", "-2", "3", "1", "0"], ["2", "-3", "4", "0", "0", "1"]], "bar": 3}

**Step 2: R3 ← R3 + (-2)R1.** Add -2 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-2", "1", "0", "0"], ["0", "1", "-2", "3", "1", "0"], ["0", "-3", "8", "-2", "0", "1"]], "bar": 3}

**Step 3: R3 ← R3 + (3)R2.** Add 3 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-2", "1", "0", "0"], ["0", "1", "-2", "3", "1", "0"], ["0", "0", "2", "7", "3", "1"]], "bar": 3}

**Step 4: R3 ← (1/2)R3.** Multiply every entry of row 3, including any right-hand side, by 1/2. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "0", "-2", "1", "0", "0"], ["0", "1", "-2", "3", "1", "0"], ["0", "0", "1", "7/2", "3/2", "1/2"]], "bar": 3}

**Step 5: R1 ← R1 + (2)R3.** Add 2 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "8", "3", "1"], ["0", "1", "-2", "3", "1", "0"], ["0", "0", "1", "7/2", "3/2", "1/2"]], "bar": 3}

**Step 6: R2 ← R2 + (2)R3.** Add 2 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "8", "3", "1"], ["0", "1", "0", "10", "4", "1"], ["0", "0", "1", "7/2", "3/2", "1/2"]], "bar": 3}

The left block is I. The right block is therefore A^(-1):

@matrix {"a": [["8", "3", "1"], ["10", "4", "1"], ["7/2", "3/2", "1/2"]], "bar": null}

**Verification.** Multiplying in each order gives the identity:

@matrix {"a": [["1", "0", "0"], ["0", "1", "0"], ["0", "0", "1"]], "bar": null}

The same elementary operations changed A into I and I into A^(-1). They amount to multiplication on the left by A^(-1), which explains why the procedure works.


### 2.2.42 - Find the inverse by Gauss-Jordan elimination, if it exists

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The starting matrix is:

@matrix {"a": [["1", "-2", "1", "1", "0", "0"], ["4", "-7", "3", "0", "1", "0"], ["-2", "6", "-4", "0", "0", "1"]], "bar": 3}

**Step 1: R2 ← R2 + (-4)R1.** Add -4 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-2", "1", "1", "0", "0"], ["0", "1", "-1", "-4", "1", "0"], ["-2", "6", "-4", "0", "0", "1"]], "bar": 3}

**Step 2: R3 ← R3 + (2)R1.** Add 2 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-2", "1", "1", "0", "0"], ["0", "1", "-1", "-4", "1", "0"], ["0", "2", "-2", "2", "0", "1"]], "bar": 3}

**Step 3: R3 ← R3 + (-2)R2.** Add -2 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "-2", "1", "1", "0", "0"], ["0", "1", "-1", "-4", "1", "0"], ["0", "0", "0", "10", "-2", "1"]], "bar": 3}

**Step 4: R1 ← R1 + (2)R2.** Add 2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "-1", "-7", "2", "0"], ["0", "1", "-1", "-4", "1", "0"], ["0", "0", "0", "10", "-2", "1"]], "bar": 3}

The left block cannot become the identity: it has fewer than 3 pivots. A is singular and has no inverse. A zero row in the left block alone is not a contradiction about the original entries; it shows a missing pivot and loss of reversibility of the transformation.


### 2.2.43 - Inverses of lower-triangular ones, then generalize

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

For the displayed 3 × 3 and 4 × 4 cases, use adjacent row differences, working from the bottom upward so the row being subtracted is still original. The resulting inverse calculations are:

The starting matrix is:

@matrix {"a": [["1", "0", "0", "1", "0", "0"], ["1", "1", "0", "0", "1", "0"], ["1", "1", "1", "0", "0", "1"]], "bar": 3}

**Step 1: R2 ← R2 + (-1)R1.** Add -1 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "1", "0", "0"], ["0", "1", "0", "-1", "1", "0"], ["1", "1", "1", "0", "0", "1"]], "bar": 3}

**Step 2: R3 ← R3 + (-1)R1.** Add -1 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "1", "0", "0"], ["0", "1", "0", "-1", "1", "0"], ["0", "1", "1", "-1", "0", "1"]], "bar": 3}

**Step 3: R3 ← R3 + (-1)R2.** Add -1 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "1", "0", "0"], ["0", "1", "0", "-1", "1", "0"], ["0", "0", "1", "0", "-1", "1"]], "bar": 3}

The left block is I. The right block is therefore A^(-1):

@matrix {"a": [["1", "0", "0"], ["-1", "1", "0"], ["0", "-1", "1"]], "bar": null}

**Verification.** Multiplying in each order gives the identity:

@matrix {"a": [["1", "0", "0"], ["0", "1", "0"], ["0", "0", "1"]], "bar": null}

The same elementary operations changed A into I and I into A^(-1). They amount to multiplication on the left by A^(-1), which explains why the procedure works.

The starting matrix is:

@matrix {"a": [["1", "0", "0", "0", "1", "0", "0", "0"], ["1", "1", "0", "0", "0", "1", "0", "0"], ["1", "1", "1", "0", "0", "0", "1", "0"], ["1", "1", "1", "1", "0", "0", "0", "1"]], "bar": 4}

**Step 1: R2 ← R2 + (-1)R1.** Add -1 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "0", "1", "0", "0", "0"], ["0", "1", "0", "0", "-1", "1", "0", "0"], ["1", "1", "1", "0", "0", "0", "1", "0"], ["1", "1", "1", "1", "0", "0", "0", "1"]], "bar": 4}

**Step 2: R3 ← R3 + (-1)R1.** Add -1 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "0", "1", "0", "0", "0"], ["0", "1", "0", "0", "-1", "1", "0", "0"], ["0", "1", "1", "0", "-1", "0", "1", "0"], ["1", "1", "1", "1", "0", "0", "0", "1"]], "bar": 4}

**Step 3: R4 ← R4 + (-1)R1.** Add -1 times row 1 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "0", "1", "0", "0", "0"], ["0", "1", "0", "0", "-1", "1", "0", "0"], ["0", "1", "1", "0", "-1", "0", "1", "0"], ["0", "1", "1", "1", "-1", "0", "0", "1"]], "bar": 4}

**Step 4: R3 ← R3 + (-1)R2.** Add -1 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "0", "1", "0", "0", "0"], ["0", "1", "0", "0", "-1", "1", "0", "0"], ["0", "0", "1", "0", "0", "-1", "1", "0"], ["0", "1", "1", "1", "-1", "0", "0", "1"]], "bar": 4}

**Step 5: R4 ← R4 + (-1)R2.** Add -1 times row 2 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "0", "1", "0", "0", "0"], ["0", "1", "0", "0", "-1", "1", "0", "0"], ["0", "0", "1", "0", "0", "-1", "1", "0"], ["0", "0", "1", "1", "0", "-1", "0", "1"]], "bar": 4}

**Step 6: R4 ← R4 + (-1)R3.** Add -1 times row 3 to row 4. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "0", "1", "0", "0", "0"], ["0", "1", "0", "0", "-1", "1", "0", "0"], ["0", "0", "1", "0", "0", "-1", "1", "0"], ["0", "0", "0", "1", "0", "0", "-1", "1"]], "bar": 4}

The left block is I. The right block is therefore A^(-1):

@matrix {"a": [["1", "0", "0", "0"], ["-1", "1", "0", "0"], ["0", "-1", "1", "0"], ["0", "0", "-1", "1"]], "bar": null}

**Verification.** Multiplying in each order gives the identity:

@matrix {"a": [["1", "0", "0", "0"], ["0", "1", "0", "0"], ["0", "0", "1", "0"], ["0", "0", "0", "1"]], "bar": null}

The same elementary operations changed A into I and I into A^(-1). They amount to multiplication on the left by A^(-1), which explains why the procedure works.

For the n × n matrix A with a_{ij} = 1 when i ≥ j and 0 otherwise, let B have diagonal 1, subdiagonal -1, and zeros elsewhere. In BA, row i for i ≥ 2 is row_i(A) - row_{i-1}(A) = e_i^T; row 1 is e₁^T, so BA = I. In AB, for j < n, column j is column_j(A) - column_{j+1}(A) = e_j; the final column is e_n. Thus AB = I as well, proving the guessed inverse for all n.


### 2.2.44 - Inverse of the lower-triangular matrix with column weights

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

The entries are a_{ij} = j for i ≥ j and 0 otherwise. Write A = LD with L the lower-triangular all-ones matrix from Exercise 43 and D = diag(1,2,...,n). Then A^(-1) = D^(-1)L^(-1): its diagonal is 1,1/2,...,1/n, its subdiagonal entry in row i is -1/i for i ≥ 2, and all other entries are zero. To verify BA = I, row i for i ≥ 2 is (row_i(A) - row_{i-1}(A))/i = e_i^T; row 1 is e₁^T. For AB, entry i,j is 1 on the diagonal; when i > j it is j(1/j) + (j + 1)(-1/(j + 1)) = 0; above the diagonal it is 0. Thus both products are I and the formula is proved, including the nonzero divisors.


### 2.2.45 - Find only the third inverse column

Independently derived and cross-checked against the selected supplied solution on Combined PDF page 116.

The third inverse column solves Ax = e₃. Carry only that right-hand side; the following solution is the required column, not the entire inverse.

Each coefficient column corresponds to one unknown; the column after the vertical divider records the right-hand sides. We use reversible row operations to reveal the constraints.

The starting matrix is:

@matrix {"a": [["-2", "-7", "-9", "0"], ["2", "5", "6", "0"], ["1", "3", "4", "1"]], "bar": 3}

**Step 1: R1 ← (-1/2)R1.** Multiply every entry of row 1, including any right-hand side, by -1/2. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "7/2", "9/2", "0"], ["2", "5", "6", "0"], ["1", "3", "4", "1"]], "bar": 3}

**Step 2: R2 ← R2 + (-2)R1.** Add -2 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "7/2", "9/2", "0"], ["0", "-2", "-3", "0"], ["1", "3", "4", "1"]], "bar": 3}

**Step 3: R3 ← R3 + (-1)R1.** Add -1 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "7/2", "9/2", "0"], ["0", "-2", "-3", "0"], ["0", "-1/2", "-1/2", "1"]], "bar": 3}

**Step 4: R2 ← (-1/2)R2.** Multiply every entry of row 2, including any right-hand side, by -1/2. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "7/2", "9/2", "0"], ["0", "1", "3/2", "0"], ["0", "-1/2", "-1/2", "1"]], "bar": 3}

**Step 5: R3 ← R3 + (1/2)R2.** Add 1/2 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "7/2", "9/2", "0"], ["0", "1", "3/2", "0"], ["0", "0", "1/4", "1"]], "bar": 3}

**Step 6: R3 ← (4)R3.** Multiply every entry of row 3, including any right-hand side, by 4. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "7/2", "9/2", "0"], ["0", "1", "3/2", "0"], ["0", "0", "1", "4"]], "bar": 3}

**Step 7: R1 ← R1 + (-9/2)R3.** Add -9/2 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "7/2", "0", "-18"], ["0", "1", "3/2", "0"], ["0", "0", "1", "4"]], "bar": 3}

**Step 8: R2 ← R2 + (-3/2)R3.** Add -3/2 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "7/2", "0", "-18"], ["0", "1", "0", "-6"], ["0", "0", "1", "4"]], "bar": 3}

**Step 9: R1 ← R1 + (-7/2)R2.** Add -7/2 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "3"], ["0", "1", "0", "-6"], ["0", "0", "1", "4"]], "bar": 3}

**Read the equations.** x_1 = 3; x_2 = -6; x_3 = 4

Every unknown is basic, so no arbitrary choices remain. There is exactly one solution:

@matrix {"a": [["3"], ["-6"], ["4"]], "bar": null}



**Verification in the original equations.** For p, the left-hand sides A p are:

@matrix {"a": [["0"], ["0"], ["1"]], "bar": null}

These entries equal the original right-hand sides, in order.


### 2.2.46 - Find only the second and third inverse columns

Independently derived teaching solution; no matching selected answer is present on Combined PDF pages 101-116.

They solve Ax = e₂ and Ay = e₃. Carry both target columns together through the same operations:

The starting matrix is:

@matrix {"a": [["-25", "-9", "-27", "0", "0"], ["546", "180", "537", "1", "0"], ["154", "50", "149", "0", "1"]], "bar": 3}

**Step 1: R1 ← (-1/25)R1.** Multiply every entry of row 1, including any right-hand side, by -1/25. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "9/25", "27/25", "0", "0"], ["546", "180", "537", "1", "0"], ["154", "50", "149", "0", "1"]], "bar": 3}

**Step 2: R2 ← R2 + (-546)R1.** Add -546 times row 1 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "9/25", "27/25", "0", "0"], ["0", "-414/25", "-1317/25", "1", "0"], ["154", "50", "149", "0", "1"]], "bar": 3}

**Step 3: R3 ← R3 + (-154)R1.** Add -154 times row 1 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "9/25", "27/25", "0", "0"], ["0", "-414/25", "-1317/25", "1", "0"], ["0", "-136/25", "-433/25", "0", "1"]], "bar": 3}

**Step 4: R2 ← (-25/414)R2.** Multiply every entry of row 2, including any right-hand side, by -25/414. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "9/25", "27/25", "0", "0"], ["0", "1", "439/138", "-25/414", "0"], ["0", "-136/25", "-433/25", "0", "1"]], "bar": 3}

**Step 5: R3 ← R3 + (136/25)R2.** Add 136/25 times row 2 to row 3. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "9/25", "27/25", "0", "0"], ["0", "1", "439/138", "-25/414", "0"], ["0", "0", "-1/69", "-68/207", "1"]], "bar": 3}

**Step 6: R3 ← (-69)R3.** Multiply every entry of row 3, including any right-hand side, by -69. The pivot becomes 1; the multiplier is nonzero, so this step is reversible.

@matrix {"a": [["1", "9/25", "27/25", "0", "0"], ["0", "1", "439/138", "-25/414", "0"], ["0", "0", "1", "68/3", "-69"]], "bar": 3}

**Step 7: R1 ← R1 + (-27/25)R3.** Add -27/25 times row 3 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "9/25", "0", "-612/25", "1863/25"], ["0", "1", "439/138", "-25/414", "0"], ["0", "0", "1", "68/3", "-69"]], "bar": 3}

**Step 8: R2 ← R2 + (-439/138)R3.** Add -439/138 times row 3 to row 2. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "9/25", "0", "-612/25", "1863/25"], ["0", "1", "0", "-433/6", "439/2"], ["0", "0", "1", "68/3", "-69"]], "bar": 3}

**Step 9: R1 ← R1 + (-9/25)R2.** Add -9/25 times row 2 to row 1. This cancels the entry in the pivot column while preserving the solutions. All other rows stay as displayed.

@matrix {"a": [["1", "0", "0", "3/2", "-9/2"], ["0", "1", "0", "-433/6", "439/2"], ["0", "0", "1", "68/3", "-69"]], "bar": 3}

The first three columns are now I₃. The fourth column is the second inverse column, and the fifth is the third inverse column. They are, respectively:

@matrix {"a": [["3/2"], ["-433/6"], ["68/3"]], "bar": null}

@matrix {"a": [["-9/2"], ["439/2"], ["-69"]], "bar": null}

Multiplying the original A by these columns gives e₂ and e₃ exactly, verifying the requested results. The first inverse column was not computed, as requested.


# Coverage and answer provenance

Every complete visible numbered question has an answer above. The two truncated entries explicitly identify what is missing. Some printed group headings refer to question numbers beyond the supplied page boundary; those unseen statements are excluded from the inventory, not filled in from an assumed edition.

For each answer labeled as cross-checked, the selected supplied solution on the stated physical PDF page supports the conclusion. The expanded derivations and intermediate operations are independently authored. Answers without that label were derived from the actual scanned data and definitions; they are not labeled as official textbook answers.

Source maps: Section 1.1 uses exercise PDF pages 1-2, 1.2 uses 3-4, 1.3 uses 5-6, 1.4 uses 7-8, 1.5 uses 9, 1.7 uses 10, 1.8 uses 11, 1.9 uses 12, 2.1 uses 13-14, and 2.2 uses 15-16. Source questions requiring a drawing have a coordinate plot or vector-construction diagram alongside their answer. Structural and proof questions are answered with explicit general arguments.

The editable CSV inventory records section, question number, source completeness, and selected-solution cross-check page. The computation log records exact-arithmetic assertions used by the authoring code. The textbook explains the shared methods at greater length; this volume applies them to the supplied questions.

