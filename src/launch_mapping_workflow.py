#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re
import time
from bioblend import galaxy
import galaxy_api_commands

def launch_mapping_workflow(args):
    workflow_file_path = "data/workflows/mapping_workflow.ga"
    gi = galaxy_api_commands.connect_to_galaxy_instance(args.gi_url, args.api_key)

    input_filepaths = {}
    input_filepaths['raw sequences'] = "data/" + args.sample_name + ".fastq"
    input_filepaths['reference genomes'] = "data/reference_genomes/reference_genomes.fna.gz"
    input_filepaths['Expected ribosomal rna operon counts'] = "data/" + args.sample_name + "_expected_ribosomal_rna_operon_counts.txt"

    file_types = {}
    file_types['raw sequences'] = "fastqsanger"
    file_types['reference genomes'] = "fasta"
    file_types['Expected ribosomal rna operon counts'] = "tabular"

    galaxy_api_commands.run_workflow('Mapping for ' + args.sample_name, 
        workflow_file_path, input_filepaths, gi, args.output_dir, 
        file_types = file_types)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gi_url', required=True)
    parser.add_argument('--api_key', required=True)
    parser.add_argument('--sample_name', required=True)
    parser.add_argument('--output_dir', required=True)
    args = parser.parse_args()

    launch_mapping_workflow(args)