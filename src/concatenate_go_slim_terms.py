#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re
import time
from bioblend import galaxy
import galaxy_api_commands

def launch_concatenation(workflow_name,workflow_file_path, gi, args):
    input_filepaths = {}
    filepath = workflow_name + '/normalize_a_dataset_by_on_data_8_normalized_dataset.tabular'
    input_filepaths[args.sample1_name] = args.sample1_dir + '/' + filepath
    input_filepaths[args.sample2_name] = args.sample2_dir + '/' + filepath
    output_dir = args.output_dir + '/' + workflow_name
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    galaxy_api_commands.run_workflow(workflow_name, workflow_file_path, input_filepaths, 
        gi, output_dir)

def concatenate_go_slim_terms(args):
    workflow_file_path = "data/workflows/go_slim_term_comparison.ga"

    gi = galaxy_api_commands.connect_to_galaxy_instance(args.gi_url, args.api_key)
    print 

    for group in ['biological_process', 'cellular_component', 'molecular_function']:
        output_dir = args.output_dir + '/' + group
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        input_filepath = {}

        if group == 'biological_process':
            input_filepath['SRR072232_asaim'] = "previous_results/SRR072232/asaim_results/56_normalize_a_dataset_by_on_data_49_normalized_dataset.tabular" 
            input_filepath['SRR072233_asaim'] = "previous_results/SRR072233/asaim_results/56_normalize_a_dataset_by_on_data_49_normalized_dataset.tabular" 
        elif group == 'cellular_component':
            input_filepath['SRR072232_asaim'] = "previous_results/SRR072232/asaim_results/57_normalize_a_dataset_by_on_data_50_normalized_dataset.tabular" 
            input_filepath['SRR072233_asaim'] = "previous_results/SRR072233/asaim_results/57_normalize_a_dataset_by_on_data_50_normalized_dataset.tabular" 
        elif group == 'molecular_function':
            input_filepath['SRR072232_asaim'] = "previous_results/SRR072232/asaim_results/55_normalize_a_dataset_by_on_data_48_normalized_dataset.tabular" 
            input_filepath['SRR072233_asaim'] = "previous_results/SRR072233/asaim_results/55_normalize_a_dataset_by_on_data_48_normalized_dataset.tabular" 

        input_filepath['SRR072232_ebi'] = "results/SRR072232/EBI_results/" + group + ".txt" 
        input_filepath['SRR072233_ebi'] = "results/SRR072233/EBI_results/" + group + ".txt" 

        galaxy_api_commands.run_workflow(group, workflow_file_path, 
            input_filepath, gi, output_dir)
        print

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gi_url', required=True)
    parser.add_argument('--api_key', required=True)
    parser.add_argument('--output_dir', required=True)
    args = parser.parse_args()

    #concatenate_go_slim_terms(args)