# MATH 2255 · Beginner-Friendly Study Reader

An offline linear algebra study reader based on the supplied Lakehead University course material. It includes 18 content sections, all 339 numbered exercise entries, 337 complete teaching solutions, worked calculations, visual lessons, and a downloadable two-page cheat sheet.

## Open the reader

Download [the standalone HTML](output/MATH2255-Beginner-Friendly-Study-Reader-Final.html) and open the saved file in your browser. Its content, mathematical font, illustrations, question images, and PDF are embedded, so it works offline.

- [Complete study package and editable sources](output/MATH2255-Beginner-Friendly-Study-Package.zip)
- [Two-sided cheat-sheet PDF](output/pdf/MATH2255-Two-Sided-Cheat-Sheet.pdf)
- [Full editing and rebuild instructions](reader/README.md)
- [Content revision and validation record](reader/qa/beginner/VALIDATION-SUMMARY.md)

The two original truncated questions, **1.2.41 and 2.1.43**, remain clearly flagged. Their missing continuations are not invented.

## Project files

- `reader/`: standalone HTML builder, native MathML renderer, interface, lesson authoring modules, diagrams, and validation tools.
- `source/`: original editable manuscripts, source scans, exercise inventory, and earlier mathematical checks.
- `source/teaching/`: canonical revised teaching records, complete updated Markdown exports, and editable SVG illustrations.
- `output/`: finished reader, PDF, downloadable source package, and delivery manifest. The extracted package is also retained.
- Root PDF and DOCX files: supplied course and exercise source documents.

## Rebuild

From this repository's root:

```sh
python3 reader/build_reader.py
python3 reader/validate_reader.py
```

Reading and building the standalone HTML require no online services. The build uses Python's standard library. Extended validation and manuscript exports use `lxml`, `pypdf`, and `pdfplumber`; see [the detailed README](reader/README.md).

The latest revision preserves all 598 original row operations and adds explicit entry arithmetic, staged matrix products, parameter examples, question-specific proof explanations, and canonical practice answers shared between chapter disclosures and the answer collection.
