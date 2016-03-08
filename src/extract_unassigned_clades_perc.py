#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re

def fill_taxonomy(taxo_levels, taxo_level_abundances, read_nb):
    taxo = taxo_levels[0]
    taxo = taxo.split('__')[1]
    taxo = taxo.replace("_"," ")
    taxo_level_abundances.setdefault(taxo, {})
    taxo_level_abundances[taxo].setdefault('subclades_read_nb', 0)
    taxo_level_abundances[taxo].setdefault('read_nb', 0)
    taxo_level_abundances[taxo].setdefault('subclades', {})
    if len(taxo_levels) > 1:
        taxo_level_abundances[taxo]['subclades'] = fill_taxonomy(taxo_levels[1:], 
            taxo_level_abundances[taxo]['subclades'], read_nb)
        if len(taxo_levels) == 2:
            taxo_level_abundances[taxo]['subclades_read_nb'] += read_nb
    else:
        taxo_level_abundances[taxo]['read_nb'] += read_nb
    return taxo_level_abundances

def write_unassigned_perc(unassigned_clades_perc, output_file, previous_level):
    print unassigned_clades_perc.keys()
    unassigned_perc = unassigned_clades_perc['subclades_read_nb']/unassigned_clades_perc['read_nb']
    unassigned_perc = 100*(1-unassigned_perc)
    output_file.write('\t'.join(previous_level) + '\t')
    output_file.write(str(unassigned_perc) + '\n')
    for taxo in unassigned_clades_perc['subclades']:
        write_unassigned_perc(unassigned_clades_perc['subclades'][taxo], 
            output_file, previous_level + [taxo])

def extract_unassigned_clades_perc(args):
    unassigned_clades_perc = {}
    unassigned_clades_perc['read_nb'] = 0
    unassigned_clades_perc['subclades_read_nb'] = int(args.read_number)
    unassigned_clades_perc['subclades'] = {}
    with open(args.metaphlan_output, 'r') as input_file:
        file_content = input_file.readlines()

        read_nb = int(file_content[-1][:-1].split(' ')[-1])
        unassigned_clades_perc['read_nb'] = read_nb

        for line in file_content[2:-1]:
            split_line = line[:-1].split('\t')
            taxo = split_line[0].split('|')
            read_nb = int(split_line[-1])
            unassigned_clades_perc['subclades'] = fill_taxonomy(taxo, 
                unassigned_clades_perc['subclades'], read_nb)

    print unassigned_clades_perc

    with open(args.unassigned_clade_output_file, 'w') as output_file:
        write_unassigned_perc(unassigned_clades_perc, output_file, [], 
            )

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--metaphlan_output', required=True)
    parser.add_argument('--read_number', required=True)
    parser.add_argument('--unassigned_clade_output_file', required=True)
    args = parser.parse_args()

    extract_unassigned_clades_perc(args)