#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re

whole_taxo_level_order = ['kingdom','phylum','class','order','family']

def incremente_taxonomy(taxo_levels, taxo_level_abundances, taxo_level_order):
    taxo_level_abundances.setdefault('abundances',
        { 'all': 0, 'unassigned': 0, 'assigned': 0})
    taxo_level_abundances['abundances']['all'] += 1
    taxo_level_abundances.setdefault('subclades', {})
    if len(taxo_levels) == 0 :
        if len(taxo_level_order) == 0:
            taxo_level_abundances['abundances']['assigned'] += 1
        else:
            taxo_level_abundances['abundances']['unassigned'] += 1
    else:
        
        taxo = taxo_levels[0]
        taxo = taxo.split('__')[1]
        taxo = taxo.replace("_"," ")

        if taxo != '':
            taxo_level_abundances['subclades'].setdefault(taxo,{})
            taxo_level_abundances['subclades'][taxo] = incremente_taxonomy(
                taxo_levels[1:], taxo_level_abundances['subclades'][taxo],
                taxo_level_order[1:])
    return taxo_level_abundances

def extract_taxo_level_abundances(input_filepath):
    taxo_level_abundances = {}

    with open(input_filepath, 'r') as input_file:
        otu_nb = 0
        for line in input_file.readlines():
            split_line = line[:-1].split('\t')
            otu_nb += 1
            all_taxo = line[:-1].split('\t')[1]
            taxo_levels = all_taxo.split(';')[1:]
            taxo_level_abundances = incremente_taxonomy(taxo_levels, 
                taxo_level_abundances, whole_taxo_level_order[1:])

    return taxo_level_abundances, otu_nb

def get_precisely_assigned_otu_abundances(taxo_level_abundances):
    for taxo in taxo_level_abundances['subclades']:
        taxo_level_abundances['subclades'][taxo], assigned_otu_nb = get_precisely_assigned_otu_abundances(
            taxo_level_abundances['subclades'][taxo])
        taxo_level_abundances['abundances']['assigned'] += assigned_otu_nb
    return taxo_level_abundances, taxo_level_abundances['abundances']['assigned']

def write_taxo_levels(taxo_level_abundances, all_taxo_level_abundance_file, 
        graphlan2_formatted_file, taxo_levels_abundance_files, taxo_level_order, 
        previous_levels, info_type, normalization_value = None):
    abundance = 100*taxo_level_abundances['abundances'][info_type]
    if info_type != 'unassigned':
        abundance /= (1.*normalization_value)
    else:
        abundance /= (1.*taxo_level_abundances['abundances']['all'])
    
    all_taxo_level_abundance_file.write('\t'.join(previous_levels))
    all_taxo_level_abundance_file.write('\t'*len(taxo_level_order[1:]))
    all_taxo_level_abundance_file.write('\t' + str(abundance) + '\n')

    taxo_string = ''
    sep = ''
    for i in range(len(previous_levels)):
        taxo_string += sep + whole_taxo_level_order[i][0] + '__'
        taxo_string += previous_levels[i].replace('[','').replace(']','')
        sep = '|'
    graphlan2_formatted_file.write(taxo_string + '\t')
    graphlan2_formatted_file.write(str(abundance) + '\n')

    taxo_levels_abundance_files[taxo_level_order[0]].write(previous_levels[-1] + '\t')
    taxo_levels_abundance_files[taxo_level_order[0]].write(str(abundance) + '\n')

    if taxo_level_abundances.has_key('subclades'):
        for taxo in taxo_level_abundances['subclades']:
            if taxo == 'Thermi':
                taxo_name = 'Deinococcus-Thermus'
            else:
                taxo_name = taxo
            write_taxo_levels(taxo_level_abundances['subclades'][taxo], 
                all_taxo_level_abundance_file, graphlan2_formatted_file,
                taxo_levels_abundance_files, taxo_level_order[1:], 
                previous_levels + [taxo_name], info_type, normalization_value)

def write_abundances(taxo_level_abundances, output_dir, info_type, otu_nb = None):
    taxo_levels_abundance_files = {}
    all_taxo_level_abundance_file = open(output_dir + 
        '/all_taxo_level_' + info_type + '_abundance_file.txt', 'w')
    graphlan2_formatted_file = open(output_dir + 
        '/all_taxo_level_' + info_type + '_abundance_graphlan2_formatted_file.txt', 'w')
    graphlan2_formatted_file.write('#SampleID\tMetaphlan2_Analysis\n')

    for taxo_level in whole_taxo_level_order:
        taxo_levels_abundance_files[taxo_level] = open(output_dir + 
            '/' + taxo_level + '_' + info_type + '_abundance.txt', 'w')
        taxo_levels_abundance_files[taxo_level].write(taxo_level + '\t')
        taxo_levels_abundance_files[taxo_level].write('abundance\n')
        all_taxo_level_abundance_file.write(taxo_level + '\t')
    all_taxo_level_abundance_file.write('abundance\n')    

    for taxo in taxo_level_abundances['subclades']:
        write_taxo_levels(taxo_level_abundances['subclades'][taxo], 
            all_taxo_level_abundance_file, graphlan2_formatted_file, 
            taxo_levels_abundance_files, whole_taxo_level_order, [taxo], 
            info_type, otu_nb)

    for taxo_level_file in taxo_levels_abundance_files:
        taxo_levels_abundance_files[taxo_level_file].close()
    all_taxo_level_abundance_file.close()
    graphlan2_formatted_file.close()

def format_EBI_taxonomic_results(args):
    taxo_level_abundances, otu_nb = extract_taxo_level_abundances(
        args.ebi_taxonomic_results)
    taxo_level_abundances, assigned_otu_nb = get_precisely_assigned_otu_abundances(
        taxo_level_abundances)

    write_abundances(taxo_level_abundances, args.output_dir, 'all', otu_nb)
    write_abundances(taxo_level_abundances, args.output_dir, 'unassigned')
    write_abundances(taxo_level_abundances, args.output_dir, 'assigned', 
        assigned_otu_nb)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ebi_taxonomic_results', required=True)
    parser.add_argument('--output_dir', required=True)
    args = parser.parse_args()

    format_EBI_taxonomic_results(args)