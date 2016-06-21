#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re
import time
from bioblend import galaxy
import galaxy_api_commands


def run_graphlan_workflow(args):
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    workflow_file_path = "data/workflows/generate_graphlan_output.ga"
    gi = galaxy_api_commands.connect_to_galaxy_instance(args.gi_url, args.api_key)

    input_filepaths = {}
    input_filepaths['Taxonomy'] = args.taxonomy_file
    galaxy_api_commands.run_workflow('GraPhlAn representation', workflow_file_path,
        input_filepaths, gi, args.output_dir, export = True,
        delete = True, to_check_history_state = True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--taxonomy_file', required=True)
    parser.add_argument('--output_dir', required=True)
    parser.add_argument('--gi_url', required=True)
    parser.add_argument('--api_key', required=True)
    args = parser.parse_args()

    run_graphlan_workflow(args)
