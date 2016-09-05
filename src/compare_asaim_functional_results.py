#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re
import time
from bioblend import galaxy
import galaxy_api_commands

filepaths =  = {'gene_families': {}, 'pathways': {}, 'go_slim': {}}
filepaths['gene_families']['raw'] = "/asaim_results/51_normalize_a_dataset_by_on_data_39_normalized_dataset.tabular"
filepaths['gene_families']['taxo_related'] = "/asaim_results/37_combine_metaphlan2_and_humann2_outputs_on_data_29_and_data_10_gene_family_abundances_related_to_genus_species_abundances.tabular"
filepaths['pathways']['raw'] = "/asaim_results/52_normalize_a_dataset_by_on_data_41_normalized_dataset.tabular"
filepaths['pathways']['taxo_related'] = "/asaim_results/38_combine_metaphlan2_and_humann2_outputs_on_data_31_and_data_10_pathway_abundances_related_to_genus_species_abundances.tabular"
filepaths['go_slim']['biological_process'] = "/asaim_results/56_normalize_a_dataset_by_on_data_49_normalized_dataset.tabular"
filepaths['go_slim']['cellular_component'] = "/asaim_results/57_normalize_a_dataset_by_on_data_50_normalized_dataset.tabular"
filepaths['go_slim']['molecular_function'] = "/asaim_results/55_normalize_a_dataset_by_on_data_48_normalized_dataset.tabular"

def compare_simple_func_results(args, gi):
    for charac in ['gene_families', 'pathways']:
        raw_result_filepaths = {}
        raw_result_filepaths['First dataset'] = "results/" +
        raw_result_filepaths['First dataset'] += args.first_dataset
        raw_result_filepaths['First dataset'] += filepaths[charac]['raw']

        raw_result_filepaths['Second dataset'] = "results/" +
        raw_result_filepaths['Second dataset'] += args.second_dataset
        raw_result_filepaths['Second dataset'] += filepaths[charac]['raw']

        taxo_related_result_filepaths = {}
        taxo_related_result_filepaths['First dataset'] = "results/" +
        taxo_related_result_filepaths['First dataset'] += args.first_dataset
        taxo_related_result_filepaths['First dataset'] += filepaths[charac]['taxo_related']

        taxo_related_result_filepaths['Second dataset'] = "results/" +
        taxo_related_result_filepaths['Second dataset'] += args.second_dataset
        taxo_related_result_filepaths['Second dataset'] += filepaths[charac]['taxo_related']

        workflow_file_path = "data/workflows/asaim_functional_result_comparison.ga"
        raw_output_dir = args.output_dir + '/raw_' + charac + '/'
        if not os.path.exists(raw_output_dir):
            os.makedirs(raw_output_dir)
        galaxy_api_commands.run_workflow('Raw ' + charac, workflow_file_path,
            raw_result_filepaths, gi, raw_output_dir)
        print

        workflow_file_path = "data/workflows/asaim_taxonomically_related_functional_result_comparison.ga"
        taxo_output_dir = args.output_dir + '/taxonomically_related_' + charac + '/'
        if not os.path.exists(taxo_output_dir):
            os.makedirs(taxo_output_dir)
        galaxy_api_commands.run_workflow('Taxonomically related ' + charac,
            workflow_file_path, taxo_related_result_filepaths, gi, taxo_output_dir,
            purge_hist = True, delete_wf = True,to_check_history_state = True)
        print


def compare_go_slim_term_results(args, gi):
    for group in ['biological_process', 'cellular_component', 'molecular_function']:
        output_dir = args.output_dir + '/' + group
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        workflow_file_path = "data/workflows/asaim_go_slim_term_comparison.ga"

        input_filepath = {}
        input_filepath[group]

        input_filepath['First dataset'] = "results/" + args.first_dataset +
        input_filepath['First dataset'] += filepaths['go_slim'][group]
        input_filepath['Second dataset'] = "results/" + args.second_dataset +
        input_filepath['Second dataset'] += filepaths['go_slim'][group]

        galaxy_api_commands.run_workflow(group, workflow_file_path,
            input_filepath, gi, output_dir)
        print

def compare_asaim_functional_results(args):
    gi = galaxy_api_commands.connect_to_galaxy_instance(args.gi_url, args.api_key)
    compare_simple_func_results(args, gi)
    compare_go_slim_term_results(args, gi)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gi_url', required=True)
    parser.add_argument('--api_key', required=True)
    parser.add_argument('--first_dataset', required=True)
    parser.add_argument('--second_dataset', required=True)
    parser.add_argument('--output_dir', required=True)
    args = parser.parse_args()

    compare_asaim_functional_results(args)
