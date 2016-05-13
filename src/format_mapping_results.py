#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re
import time
from bioblend import galaxy
import galaxy_api_commands

whole_taxo_level_order = ['kingdom','phylum','class','order','family', 'genus','species']


def extract_taxo(expected_taxonomy, taxonomy):
    taxo = expected_taxonomy[0]
    if len(expected_taxonomy) > 1:
        taxonomy.setdefault(taxo, {'abundances':0, 'subclades': {}})
        taxonomy[taxo]['subclades'] = extract_taxo(expected_taxonomy[1:], 
            taxonomy[taxo]['subclades'])
    else:
        taxonomy.setdefault(taxo, {'abundances':0})
    return taxonomy

def check_taxo_in_mapping_results(taxo, mapping_names):
    for name in mapping_names:
        split_name = name.split(' ')
        if taxo.find(split_name[0]) != -1 and taxo.find(split_name[1]) != -1:
            return name
    return None

def fill_taxonomy(sub_taxonomy, mapping_results):
    abund_sum = 0
    for taxo in sub_taxonomy:
        name = check_taxo_in_mapping_results(taxo, mapping_results.keys())
        if name != None :
            sub_taxonomy[taxo]['abundances'] += float(mapping_results[name])

        if sub_taxonomy[taxo].has_key('subclades'):
            sub_taxonomy[taxo]['subclades'], abundances = fill_taxonomy(sub_taxonomy[taxo]['subclades'],
                mapping_results)
            sub_taxonomy[taxo]['abundances'] += abundances

        abund_sum += sub_taxonomy[taxo]['abundances']
    return sub_taxonomy, abund_sum

def write_taxonomy_abundance(taxonomy, higher_levels, tab_output_results, output_results):
    for taxo in taxonomy:
        whole_taxo = higher_levels + [taxo]
        remaining_taxo = [''] * (len(whole_taxo_level_order) - len(whole_taxo))

        tab_output_results.write('\t'.join(whole_taxo) + '\t')
        tab_output_results.write('\t'.join(remaining_taxo) + '\t')
        tab_output_results.write(str(taxonomy[taxo]['abundances']) + '\n')

        taxo_string = ''
        sep = ''
        for i in range(len(whole_taxo)):
            taxo_string += sep + whole_taxo_level_order[i][0] + '__'
            taxo_string += whole_taxo[i]
            sep = '|'
        output_results.write(taxo_string + '\t')
        output_results.write(str(taxonomy[taxo]['abundances']) + '\n')

        if taxonomy[taxo].has_key('subclades'):
            write_taxonomy_abundance(taxonomy[taxo]['subclades'], whole_taxo, 
                tab_output_results, output_results)
    
def format_mapping_results(args):
    mapping_results = {}
    with open(args.mapping_results, 'r') as mapping_results_file:
        for line in mapping_results_file.readlines():
            split_line = line[:-1].split('\t')
            mapping_results[split_line[0]] = split_line[1]

    taxonomy = {}
    with open(args.expected_taxonomy, 'r') as expected_taxonomy_file:
        for line in expected_taxonomy_file.readlines():
            split_line = line[:-1].split('\t')
            taxonomy = extract_taxo(split_line[1:(1+len(whole_taxo_level_order))], taxonomy)

    taxonomy, abund = fill_taxonomy(taxonomy, mapping_results)

    with open(args.output_dir  + "formatted_mapping_results", "w") as tab_output_results:
        for taxo_level in whole_taxo_level_order:
            tab_output_results.write(taxo_level + '\t')
        tab_output_results.write('abundances\n')

        with open(args.output_dir + "graphlan2_formatted_mapping_results", "w") as output_results:
            output_results.write('#SampleID\tMetaphlan2_Analysis\n')

            write_taxonomy_abundance(taxonomy, [], 
                tab_output_results, output_results)

    if not os.path.exists(args.output_dir + "/graphlan_generation"):
        os.makedirs(args.output_dir + "/graphlan_generation")

    workflow_file_path = "data/workflows/generate_graphlan_output.ga"
    gi = galaxy_api_commands.connect_to_galaxy_instance(args.gi_url, args.api_key)

    input_filepaths = {}
    input_filepaths['Taxonomy'] = args.output_dir + "graphlan2_formatted_mapping_results"
    galaxy_api_commands.run_workflow('GraPhlAn representation', workflow_file_path, 
        input_filepaths, gi, args.output_dir + "/graphlan_generation")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mapping_results', required=True)
    parser.add_argument('--expected_taxonomy', required=True)
    parser.add_argument('--gi_url', required=True)
    parser.add_argument('--api_key', required=True)
    parser.add_argument('--output_dir', required=True)
    args = parser.parse_args()

    format_mapping_results(args)