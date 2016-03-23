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

    if workflow_name == 'biological_process':
        asaim_filename = '56_normalize_a_dataset_by_on_data_49_normalized_dataset.tabular'
    elif workflow_name == 'cellular_component':
        asaim_filename = '57_normalize_a_dataset_by_on_data_50_normalized_dataset.tabular'
    elif workflow_name == 'molecular_function':
        asaim_filename = '55_normalize_a_dataset_by_on_data_48_normalized_dataset.tabular'
    else:
        raise ValueError('Unknow workflow_name:' + workflow_name)

    input_filepaths['asaim'] = args.asaim_result_dir + '/' + asaim_filename
    input_filepaths['ebi'] = args.ebi_result_dir + '/' + workflow_name + '.txt'
    output_dir = args.output_dir + '/' + workflow_name
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    galaxy_api_commands.run_workflow(workflow_name, workflow_file_path, input_filepaths, 
        gi, output_dir)

def concatenate_ebi_asaim_functional_results(args):
    workflow_file_path = "data/asaim_concatenate_go_slim_terms.ga"

    gi = galaxy_api_commands.connect_to_galaxy_instance(args.gi_url, args.api_key)
    print 
    for term in ['biological_process', 'cellular_component', 'molecular_function']:
        print " ", term
        launch_concatenation(term, workflow_file_path, gi, args)
        print 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gi_url', required=True)
    parser.add_argument('--api_key', required=True)
    parser.add_argument('--asaim_result_dir', required=True)
    parser.add_argument('--ebi_result_dir', required=True)
    parser.add_argument('--output_dir', required=True)
    args = parser.parse_args()

    concatenate_ebi_asaim_functional_results(args)