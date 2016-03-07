#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re
import time
from bioblend import galaxy

def search_history(histories, history_name):
    hist_id = None
    for history in histories:
        if history['name'] == history_name:
            hist_id = history['id']

    if hist_id == None:
        raise ValueError('No history found for', history_name)

    return hist_id

def export_history_datasets(args):
    print "  Connect to Galaxy instance on ", args.gi_url
    gi = galaxy.GalaxyInstance(url=args.gi_url, key=args.api_key)

    print "  Get history id"
    histories = gi.histories.get_histories()
    hist_id = search_history(histories, args.sample_name)
    output_dir_path = "results/" + args.sample_name + "/asaim_results/" 
    if not os.path.exists(output_dir_path):
        os.mkdir(output_dir_path)

    print "  Export history datasets"
    for dataset_id in gi.histories.show_history(hist_id)['state_ids']['ok']:
        gi.histories.download_dataset(hist_id, dataset_id, output_dir_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gi_url', required=True)
    parser.add_argument('--api_key', required=True)
    parser.add_argument('--sample_name', required=True)
    args = parser.parse_args()

    export_history_datasets(args)