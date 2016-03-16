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

def concatenate_ebi_asaim_functional_results(args):
    workflow_file_path = "data/asaim_concatenate_all_go_slim_terms.ga"

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
    parser.add_argument('--sample1_dir', required=True)
    parser.add_argument('--sample2_dir', required=True)
    parser.add_argument('--sample1_name', required=True)
    parser.add_argument('--sample2_name', required=True)
    parser.add_argument('--output_dir', required=True)
    args = parser.parse_args()

    concatenate_ebi_asaim_functional_results(args)