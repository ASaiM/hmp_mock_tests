#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re
import time
from bioblend import galaxy
import galaxy_api_commands

def asaim_functional_results_comparison(args):
    gi = galaxy_api_commands.connect_to_galaxy_instance(args.gi_url, args.api_key)

    for charac in ['gene_families', 'pathways']:

        raw_result_filepaths = {}
        taxo_related_result_filepaths = {}
        if charac == 'gene_families':
            raw_result_filepaths['First dataset'] = "results/" + args.first_dataset + "asaim_results/51_normalize_a_dataset_by_on_data_40_normalized_dataset.tabular" 
            raw_result_filepaths['Second dataset'] = "results/" + args.first_dataset + "asaim_results/51_normalize_a_dataset_by_on_data_40_normalized_dataset.tabular" 
            taxo_related_result_filepaths['First dataset'] = "results/" + args.first_dataset + "asaim_results/37_combine_metaphlan2_and_humann2_outputs_on_data_29_and_data_10_gene_family_abundances_related_to_genus_species_abundances.tabular"
            taxo_related_result_filepaths['Second dataset'] = "results/" + args.first_dataset + "asaim_results/37_combine_metaphlan2_and_humann2_outputs_on_data_29_and_data_10_gene_family_abundances_related_to_genus_species_abundances.tabular"
        else:
            raw_result_filepaths['First dataset'] = "results/" + args.first_dataset + "asaim_results/52_normalize_a_dataset_by_on_data_41_normalized_dataset.tabular" 
            raw_result_filepaths['Second dataset'] = "results/" + args.first_dataset + "asaim_results/52_normalize_a_dataset_by_on_data_41_normalized_dataset.tabular" 
            taxo_related_result_filepaths['First dataset'] = "results/" + args.first_dataset + "asaim_results/38_combine_metaphlan2_and_humann2_outputs_on_data_31_and_data_10_pathway_abundances_related_to_genus_species_abundances.tabular"
            taxo_related_result_filepaths['Second dataset'] = "results/" + args.first_dataset + "asaim_results/38_combine_metaphlan2_and_humann2_outputs_on_data_31_and_data_10_pathway_abundances_related_to_genus_species_abundances.tabular"

        workflow_file_path = "data/asaim_functional_result_comparison.ga"
        raw_output_dir = args.output_dir + '/raw_' + charac + '/'
        if not os.path.exists(raw_output_dir):
            os.makedirs(raw_output_dir)
        galaxy_api_commands.run_workflow('Raw ' + charac, workflow_file_path, 
            raw_result_filepaths, gi, raw_output_dir)

        workflow_file_path = "data/asaim_taxonomically_related_functional_result_comparison.ga"
        taxo_output_dir = args.output_dir + '/taxonomically_related_' + charac + '/'
        if not os.path.exists(taxo_output_dir):
            os.makedirs(taxo_output_dir)
        galaxy_api_commands.run_workflow('Taxonomically related ' + charac, 
            workflow_file_path, taxo_related_result_filepaths, gi, taxo_output_dir)

    for group in ['biological_process', 'cellular_component', 'molecular_function']:
        output_dir = args.output_dir + '/' + group
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        workflow_file_path = "data/asaim_taxonomically_related_functional_result_comparison.ga"

        input_filepath = {}

        if group == 'biological_process'
            input_filepath['First dataset'] = "results/" + args.first_dataset + "asaim_results/56_normalize_a_dataset_by_on_data_49_normalized_dataset.tabular" 
            input_filepath['Second dataset'] = "results/" + args.first_dataset + "asaim_results/56_normalize_a_dataset_by_on_data_49_normalized_dataset.tabular" 
        elif group == 'cellular_component':
            input_filepath['First dataset'] = "results/" + args.first_dataset + "asaim_results/57_normalize_a_dataset_by_on_data_50_normalized_dataset.tabular" 
            input_filepath['Second dataset'] = "results/" + args.first_dataset + "asaim_results/57_normalize_a_dataset_by_on_data_50_normalized_dataset.tabular" 
        elif group == 'molecular_function':
            input_filepath['First dataset'] = "results/" + args.first_dataset + "asaim_results/55_normalize_a_dataset_by_on_data_48_normalized_dataset.tabular" 
            input_filepath['Second dataset'] = "results/" + args.first_dataset + "asaim_results/55_normalize_a_dataset_by_on_data_48_normalized_dataset.tabular" 

        galaxy_api_commands.run_workflow(group, workflow_file_path, 
            input_filepath, gi, output_dir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gi_url', required=True)
    parser.add_argument('--api_key', required=True)
    parser.add_argument('--first_dataset', required=True)
    parser.add_argument('--second_dataset', required=True)
    parser.add_argument('--output_dir', required=True)
    args = parser.parse_args()

    asaim_functional_results_comparison(args)