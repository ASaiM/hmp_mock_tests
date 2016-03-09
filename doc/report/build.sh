#!/usr/bin/env bash

cd doc/report/
pandoc -s report.md \
    -t latex \
    -o report.pdf \
    --template="bioinformatics_template.tex" \
    -N