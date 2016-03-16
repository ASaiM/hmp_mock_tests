#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re
import time
from bioblend import galaxy

def check_history_state(gi, hist_id):
    state = len(gi.histories.show_history(hist_id)['state_ids']['running']) > 0 
    state |= len(gi.histories.show_history(hist_id)['state_ids']['queued']) > 0
    return state

def compare_humann2_output(args):
    workflow_file_path = "data/asaim_compare_normalized_" 
    workflow_file_path += args.characteristics + "_abundances.ga"

    input_filepaths  = {}
    if args.characteristics == 'gene_families':
        filename = "normalize_a_dataset_by_on_data_17_normalized_dataset.tabular" 
    else:
        filename = "normalize_a_dataset_by_on_data_19_normalized_dataset.tabular" 
    for sample_name in args.sample_name:
        filepath = "results/" + sample_name + "/asaim_results/" + filename
        input_filepaths[sample_name] = filepath

    gi = galaxy_api_commands.connect_to_galaxy_instance(args.gi_url, args.api_key)
    galaxy_api_commands.run_workflow(args.sample_name, workflow_file_path, input_filepaths, 
        gi, args.output_dir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gi_url', required=True)
    parser.add_argument('--api_key', required=True)
    parser.add_argument('--characteristics', required=True, 
        choices=['gene_families', 'pathways'])
    parser.add_argument('--sample_name', required=True, action='append')
    parser.add_argument('--output_dir', required=True)
    args = parser.parse_args()

    compare_humann2_output(args)