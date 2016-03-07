#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re

def incremente_taxonomy(taxo_levels, taxo_level_abundances):
    if len(taxo_levels) == 0:
        taxo_level_abundances.setdefault('Unassigned',0)
        taxo_level_abundances['Unassigned'] += 1
        return taxo_level_abundances

    taxo = taxo_levels[0]
    taxo = taxo.split('__')[1]
    taxo = taxo.replace("_"," ")

    if taxo != '':
        taxo_level_abundances.setdefault(taxo,{})
        taxo_level_abundances[taxo].setdefault('All', 0)
        taxo_level_abundances[taxo]['All'] += 1
        taxo_level_abundances[taxo] = incremente_taxonomy(taxo_levels[1:],
            taxo_level_abundances[taxo])
    return taxo_level_abundances

def write_taxo_levels(taxo_level_abundances, all_taxo_level_abundance_file, 
        taxo_levels_abundance_files, taxo_level_order, previous_levels, otu_nb):
    if taxo_level_abundances.has_key('All'):
        abundance = 100*taxo_level_abundances['All']/(1.*otu_nb)
        
        all_taxo_level_abundance_file.write('\t'.join(previous_levels))
        all_taxo_level_abundance_file.write('\t'*len(taxo_level_order[1:]))
        all_taxo_level_abundance_file.write('\t' + str(abundance) + '\n')

        taxo_levels_abundance_files[taxo_level_order[0]].write(previous_levels[-1] + '\t')
        taxo_levels_abundance_files[taxo_level_order[0]].write(str(abundance) + '\n')

    for taxo in taxo_level_abundances:
        if taxo != 'All' and taxo != 'Unassigned':
            write_taxo_levels(taxo_level_abundances[taxo], 
                all_taxo_level_abundance_file,
                taxo_levels_abundance_files, taxo_level_order[1:], 
                previous_levels + [taxo], otu_nb)

def format_EBI_taxonomic_results(args):
    taxo_level_abundances = {}

    with open(args.ebi_taxonomic_results, 'r') as input_file:
        otu_nb = 0
        for line in input_file.readlines():
            split_line = line[:-1].split('\t')
            otu_nb += 1
            all_taxo = line[:-1].split('\t')[1]
            taxo_levels = all_taxo.split(';')[1:]
            taxo_level_abundances = incremente_taxonomy(taxo_levels, 
                taxo_level_abundances)

    taxo_levels_abundance_files = {}
    taxo_levels_abundance_files['kingdom'] = open(args.kingdom_abundance_file, 'w')
    taxo_levels_abundance_files['phylum'] = open(args.phylum_abundance_file, 'w')
    taxo_levels_abundance_files['class'] = open(args.class_abundance_file, 'w')
    taxo_levels_abundance_files['order'] = open(args.order_abundance_file, 'w')
    taxo_levels_abundance_files['family'] = open(args.family_abundance_file, 'w')
    all_taxo_level_abundance_file = open(args.all_taxo_level_abundance_file, 'w')

    taxo_level_order = ['domain','kingdom','phylum','class','order','family']
    for taxo_level in taxo_level_order[1:]:
        taxo_levels_abundance_files[taxo_level].write(taxo_level + '\t')
        taxo_levels_abundance_files[taxo_level].write('abundance\n')
        all_taxo_level_abundance_file.write(taxo_level + '\t')
    all_taxo_level_abundance_file.write('abundance\n')    

    write_taxo_levels(taxo_level_abundances, all_taxo_level_abundance_file, 
        taxo_levels_abundance_files, taxo_level_order, [], otu_nb)

    for taxo_level_file in taxo_levels_abundance_files:
        taxo_levels_abundance_files[taxo_level_file].close()
    all_taxo_level_abundance_file.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ebi_taxonomic_results', required=True)
    parser.add_argument('--all_taxo_level_abundance_file', required=True)
    parser.add_argument('--kingdom_abundance_file', required=True)
    parser.add_argument('--phylum_abundance_file', required=True)
    parser.add_argument('--class_abundance_file', required=True)
    parser.add_argument('--order_abundance_file', required=True)
    parser.add_argument('--family_abundance_file', required=True)
    args = parser.parse_args()

    format_EBI_taxonomic_results(args)