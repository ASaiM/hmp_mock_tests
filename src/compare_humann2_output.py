#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re
import time
from bioblend import galaxy
import galaxy_api_commands

def compare_humann2_output(args):
    workflow_file_path = "data/asaim_compare_normalized_characteristics_abundances.ga"

    input_filepaths  = {}
    if args.characteristics == 'gene_families':
        humann2_filename = "51_normalize_a_dataset_by_on_data_40_normalized_dataset.tabular" 
        combined_humann2_metaphlan2_filename = "37_combine_metaphlan2_and_humann2_outputs_on_data_29_and_data_10_gene_family_abundances_related_to_genus_species_abundances.tabular"
    else:
        humann2_filename = "52_normalize_a_dataset_by_on_data_41_normalized_dataset.tabular" 
        combined_humann2_metaphlan2_filename = "38_combine_metaphlan2_and_humann2_outputs_on_data_31_and_data_10_pathway_abundances_related_to_genus_species_abundances.tabular"

    for sample_name in args.sample_name:
        filepath = "results/" + sample_name + "/asaim_results/" + humann2_filename
        input_filepaths[sample_name + '_humann2'] = filepath
        filepath = "results/" + sample_name + "/asaim_results/" + combined_humann2_metaphlan2_filename
        input_filepaths[sample_name + '_combined_humann2_metaphlan2'] = filepath

    gi = galaxy_api_commands.connect_to_galaxy_instance(args.gi_url, args.api_key)
    galaxy_api_commands.run_workflow(args.characteristics, workflow_file_path, 
        input_filepaths, gi, args.output_dir)

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