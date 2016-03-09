#!/usr/bin/env bash

cd doc
pandoc -s report.md \
    -t latex \
    -o report.pdf \
    --template="bioinformatics_template.tex" \
    -N

#pandoc -s doc/report.md \
#    -t docx \
#    -o doc/report.docx \
#    --filter pandoc-fignos \
#    --reference-docx="doc/cabios_word_temp/MS Word Template Bioinformatics.dotx" \
#    --template="doc/cabios_word_temp/MS Word Template Bioinformatics.dotx"
