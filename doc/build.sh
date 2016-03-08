#!/usr/bin/env bash

pandoc -s doc/report.md \
    -t latex \
    -o doc/report.pdf \
    --filter pandoc-fignos