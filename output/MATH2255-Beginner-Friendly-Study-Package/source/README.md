# Editable MATH 2255 sources

Edit the two MATH2255-*.md manuscripts, then run:

    python3 build_math2255.py

Install the Python dependencies reportlab, pypdf, Pillow and pdfplumber if they are not available. The renderer currently uses macOS font paths near the middle of build_math2255.py; change those paths for another operating system. The source/scans folder preserves the 16 supplied exercise page images used inside the workbook. There is no HTML output or browser dependency.

The manuscripts are the editable deliverables. The author_textbook.py and author_workbook.py programs reproduce their initial content and exact computations; running those programs regenerates the manuscripts and will replace manual edits. Run qa_math2255.py to repeat the recorded mathematical and inventory checks. Mathematical assertions use Python Fraction and do not depend on floating-point rounding.

Extended Markdown blocks:

- @matrix followed by JSON has an array a and optional bar column index. Fractions such as "3/2" are typeset vertically. The bar index counts coefficient columns.
- @eq introduces a centered equation. x_1 and A^(-1) become subscript and superscript notation in the PDF.
- @figure and @customfig name the vector diagrams implemented in the renderer.
- @scan inserts an original exercise page from scans/.
- @toc inserts a generated linked table of contents, and @page requests a page break.

Source provenance: Heli-exam_prep_Combined.pdf and Exercises_Merged.pdf supplied by the user. The manuscript source-correspondence chapters and exercise-inventory.csv record section/question mappings and selected-answer cross-checks. Two source questions are truncated (1.2.41, 2.1.43); their absent continuations remain explicitly flagged. The inverse example on lecture PDF page 98 has conflicting first-row entries; both actual matrices are distinguished and solved in the textbook.

These materials include no exam cheat sheet and make no assertion about permitted examination reference-sheet rules.
