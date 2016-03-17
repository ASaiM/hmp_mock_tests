#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re
import time
from bioblend import galaxy
import galaxy_api_commands

def export_history_datasets(args):
    if not os.path.exists(args.output_dir):
        os.mkdir(args.output_dir)

    gi = galaxy_api_commands.connect_to_galaxy_instance(args.gi_url, args.api_key)
    hist_id = galaxy_api_commands.get_hist_id(args.sample_name, gi)
    galaxy_api_commands.export_workflow_outputs(hist_id, args.output_dir, gi)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gi_url', required=True)
    parser.add_argument('--api_key', required=True)
    parser.add_argument('--sample_name', required=True)
    parser.add_argument('--output_dir', required=True)
    args = parser.parse_args()

    export_history_datasets(args)