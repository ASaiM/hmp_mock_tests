#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re

def init_exp_taxo(split_line, exp_taxo_w_abund, exp_taxo_order, exp_abundance):
    taxo_name = split_line[0].lower()
    taxo_name = taxo_name.replace(' ','-')
    if len(exp_taxo_order) > 0:
        sub_taxons = exp_taxo_order[0].lower()
        exp_taxo_w_abund.setdefault(taxo_name, 
            {'abundances' : {'ebi': 0, 'asaim': 0, 'expected': 0}, sub_taxons: {}})
        exp_taxo_w_abund[taxo_name]['abundances']['expected'] += exp_abundance
        exp_taxo_w_abund[taxo_name][sub_taxons] = init_exp_taxo(split_line[1:],
            exp_taxo_w_abund[taxo_name][sub_taxons], exp_taxo_order[1:], exp_abundance)
    else:
        exp_taxo_w_abund.setdefault(taxo_name, 
            {'abundances' : {'ebi': 0, 'asaim': 0, 'expected': 0}})
        exp_taxo_w_abund[taxo_name]['abundances']['expected'] += exp_abundance

    return exp_taxo_w_abund

def extract_expected_taxonomy(expected_taxonomy_filepath, sample_name):
    exp_taxo_w_abund = {}
    exp_taxo_w_abund['kingdom'] = {}
    with open(expected_taxonomy_filepath, 'r') as expected_taxonomy_file:
        expected_taxonomy_file_content = expected_taxonomy_file.readlines()
        exp_taxo_order = expected_taxonomy_file_content[0][:-1].split('\t')[:-2]
        for line in expected_taxonomy_file_content[1:]:
            split_line = line[:-1].split('\t')

            if sample_name == 'SRR072232':
                exp_abund = 100*float(split_line[-2])/5566000
            elif sample_name == 'SRR072233':
                exp_abund = 100*float(split_line[-1])/2200000
            else:
                raise ValueError('Unknow sample name:', sample_name)

            exp_taxo_w_abund['kingdom'] = init_exp_taxo(split_line[1:-2], 
                exp_taxo_w_abund['kingdom'], exp_taxo_order[2:], 
                exp_abund)
    return exp_taxo_w_abund

def fill_one_taxo_abundance(exp_taxo_w_abund, taxo, abundance, taxo_order, 
    result_type, unexpected_clade_file):
    if len(taxo) == 0 or taxo[0] == '':
        if exp_taxo_w_abund['abundances'][result_type] != 0:
            print exp_taxo_w_abund
            raise ValueError("Abundance already fill in")
        exp_taxo_w_abund['abundances'][result_type] = abundance
    elif taxo_order[0] != 'strains':
        taxo_name = taxo[0].lower()
        taxo_name = taxo_name.replace(' ','-')
        taxo_level = taxo_order[0]
        if not exp_taxo_w_abund[taxo_level].has_key(taxo_name):
            unexpected_clade_file.write('|'.join(taxo) + '\t')
            unexpected_clade_file.write(result_type + '\t')
            unexpected_clade_file.write(taxo_order[0] + '\t')
            unexpected_clade_file.write(str(abundance) + '\n')
        else:
            exp_taxo_w_abund[taxo_level][taxo_name] = fill_one_taxo_abundance(
                exp_taxo_w_abund[taxo_level][taxo_name], taxo[1:],
                abundance, taxo_order[1:], result_type, unexpected_clade_file)
    return exp_taxo_w_abund

def fill_taxo_abund(exp_taxo_w_abund, result_filepath, result_type, 
    unexpected_clade_file):
    with open(result_filepath, 'r') as result_file:
        result_file_content = result_file.readlines()
        taxo_order = result_file_content[0][:-1].split('\t')
        for line in result_file_content[1:]:
            split_line = line[:-1].split('\t')
            abundance = float(split_line[-1])
            exp_taxo_w_abund = fill_one_taxo_abundance(exp_taxo_w_abund, 
                split_line[:-1], abundance, taxo_order, result_type, 
                unexpected_clade_file)
    return exp_taxo_w_abund

def write_taxo_levels(exp_taxo_w_abund, all_taxo_level_abundance_file, 
        taxo_level_files, taxo_level_order, previous_levels):
    if exp_taxo_w_abund.has_key('abundances'):  
        abundances = exp_taxo_w_abund['abundances']
        all_taxo_level_abundance_file.write('\t'.join(previous_levels))
        all_taxo_level_abundance_file.write('\t'*len(taxo_level_order[1:]))
        all_taxo_level_abundance_file.write('\t' + str(abundances['expected']) )
        all_taxo_level_abundance_file.write('\t' + str(abundances['ebi']) )
        all_taxo_level_abundance_file.write('\t' + str(abundances['asaim']) + '\n')

        taxo_level_files[taxo_level_order[0]].write(previous_levels[-1])
        taxo_level_files[taxo_level_order[0]].write('\t' + str(abundances['expected']))
        taxo_level_files[taxo_level_order[0]].write('\t' + str(abundances['ebi']))
        taxo_level_files[taxo_level_order[0]].write('\t' + str(abundances['asaim']) + '\n')

    if len(taxo_level_order) > 1:
        for taxo in exp_taxo_w_abund[taxo_level_order[1]]:
            taxo_name = taxo.replace('-',' ').capitalize()
            write_taxo_levels(exp_taxo_w_abund[taxo_level_order[1]][taxo], 
                all_taxo_level_abundance_file, taxo_level_files, 
                taxo_level_order[1:], previous_levels + [taxo_name])

def concatenate_ebi_asaim_taxonomic_results(args):
    exp_taxo_w_abund = extract_expected_taxonomy(args.expected_taxonomy, 
        args.sample_name)

    unexpected_clade_file = open(args.output_dir + '/unexpected_clades.txt', 
        'w')

    asaim_result_filepath = args.asaim_result_dir 
    asaim_result_filepath += '/14_format_metaphlan2_on_data_10_abundances_for_all_taxonomic_levels.tabular'
    exp_taxo_w_abund = fill_taxo_abund(exp_taxo_w_abund, asaim_result_filepath, 
        'asaim', unexpected_clade_file)

    ebi_result_filepath = args.ebi_result_dir 
    ebi_result_filepath += '/all_taxo_level_assigned_abundance_file.txt'
    exp_taxo_w_abund = fill_taxo_abund(exp_taxo_w_abund, ebi_result_filepath, 
        'ebi', unexpected_clade_file)

    unexpected_clade_file.close()

    taxo_level_order = ['domain','kingdom','phylum','class','order','family','genus','species']
    taxo_level_files = {}
    all_taxo_level_abundance_file = open(args.output_dir + '/all_taxo_level_abundance.txt', 'w')
    for level in taxo_level_order:
        taxo_level_files[level] = open(args.output_dir + '/' + level + '_abundance.txt','w')
        taxo_level_files[level].write(level + '\t')
        taxo_level_files[level].write('expected\tebi_abundance\tasaim_abundance\n')
        all_taxo_level_abundance_file.write(level + '\t')
    all_taxo_level_abundance_file.write('expected\tebi_abundance\tasaim_abundance\n')

    write_taxo_levels(exp_taxo_w_abund, all_taxo_level_abundance_file, 
        taxo_level_files, taxo_level_order, [''])

    for level in taxo_level_order:
        taxo_level_files[level].close()
    all_taxo_level_abundance_file.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--expected_taxonomy', required=True)
    parser.add_argument('--asaim_result_dir', required=True)
    parser.add_argument('--ebi_result_dir', required=True)
    parser.add_argument('--output_dir', required=True)
    parser.add_argument('--sample_name', required=True)
    args = parser.parse_args()

    concatenate_ebi_asaim_taxonomic_results(args)