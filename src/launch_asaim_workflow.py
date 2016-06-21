#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re
import time
from bioblend import galaxy
import galaxy_api_commands

def launch_asaim_workflow(args):
    workflow_file_path = "data/workflows/asaim_main_workflow.ga"
    gi = galaxy_api_commands.connect_to_galaxy_instance(args.gi_url, args.api_key)

    input_filepaths = {'raw sequences': "data/" + args.sample_name + ".fastq"}
    file_types = {'raw sequences': "fastq"}
    galaxy_api_commands.run_workflow(args.sample_name, workflow_file_path, input_filepaths,
        gi, '', export = False, file_types = file_types, to_check_history_state = False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gi_url', required=True)
    parser.add_argument('--api_key', required=True)
    parser.add_argument('--sample_name', required=True)
    args = parser.parse_args()

    launch_asaim_workflow(args)
