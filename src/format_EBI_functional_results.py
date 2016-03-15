#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re

def extract_abundances_go_slim(input_filepath):
    go_slim_terms = {}
    with open(input_filepath, 'r') as input_file:
        for line in input_file.readlines():
            split_line = line[:-1].split('","')
            category = split_line[2]
            go_id = split_line[0][1:]
            go_name = split_line[1]
            abundance = int(split_line[3][:-1])
            go_slim_terms.setdefault(category, {'abundance':0, 'sub_terms': {}})
            go_slim_terms[category]['abundance'] += abundance
            go_slim_terms[category]['sub_terms'].setdefault(go_id, 
                {'name': go_name, 'abundance': abundance})
    return go_slim_terms

def write_relative_abundances(go_slim_terms, output_filepath):
    with open(output_filepath,'w') as output_file:
        output_file.write('GO id\tGO name\tAbundance\n')
        for sub_term in go_slim_terms['sub_terms']:
            output_file.write(sub_term + '\t')
            output_file.write(go_slim_terms['sub_terms'][sub_term]['name'] + '\t')
            relative_abundance = 100.*go_slim_terms['sub_terms'][sub_term]['abundance']
            relative_abundance /= go_slim_terms['abundance']
            output_file.write(str(relative_abundance) + '\n')

def format_EBI_functional_results(args):
    go_slim_terms = extract_abundances_go_slim(args.ebi_functional_results)
    for term in go_slim_terms:
        output_filepath = args.output_dir + '/' + term + '.txt'
        write_relative_abundances(go_slim_terms[term], output_filepath)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ebi_functional_results', required=True)
    parser.add_argument('--output_dir', required=True)
    args = parser.parse_args()

    format_EBI_functional_results(args)