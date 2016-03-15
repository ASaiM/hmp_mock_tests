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
    if args.characteristics == 'gene_families':
        filename = "normalized_table_for______________data_17_(humann2).tsv" 
    else:
        filename = "normalized_table_for______________data_19_(humann2).tsv" 

    print "  Connect to Galaxy instance on ", args.gi_url
    gi = galaxy.GalaxyInstance(url=args.gi_url, key=args.api_key)

    print "  Create an history for ", args.characteristics, " and import input data"
    history_details = gi.histories.create_history(args.characteristics)
    hist_id = history_details['id']
    datasets_id = {}
    for sample_name in args.sample_name:
        filepath = "results/" + sample_name + "/asaim_results/" + filename        
        upload_file_details = gi.tools.upload_file(filepath, hist_id, 
            file_name = sample_name)
        datasets_id[sample_name] = upload_file_details['outputs'][0]['id']
        #print gi.datasets.show_dataset(upload_file_details['outputs'][0]['id'])
        upload_file_job_id = upload_file_details['jobs'][0]['id']
        while str(gi.jobs.get_state(upload_file_job_id)) != 'ok':
            time.sleep(1)

    print "  Import workflow and launch it"
    wf_details = gi.workflows.import_workflow_from_local_path(workflow_file_path)
    wf_id = wf_details['id']
    wf = gi.workflows.show_workflow(wf_id)
    datamap = dict()

    for wf_input in wf['inputs'].keys():
        name = str(wf['inputs'][wf_input]['label'])
        if not datasets_id.has_key(name):
            raise ValueError(name + ' not found in datasets')
        datamap[wf_input] = { 'src':'hda', 'id': datasets_id[name]}

    wf_invocation_details = gi.workflows.run_workflow(wf_id, datamap, history_id=hist_id)
    wf_invocation_id = wf_invocation_details['id']
    wf_outputs = wf_invocation_details['outputs']

    while check_history_state(gi, hist_id):
        time.sleep(1)

    print "  Export workflow results"
    for dataset_id in gi.histories.show_history(hist_id)['state_ids']['ok']:
        name = str(gi.datasets.show_dataset(dataset_id)['name']).lower()
        name = name.replace(':', '')
        name = name.replace(' ','_')
        extension = gi.datasets.show_dataset(dataset_id)['extension']
        if extension == None:
            extension = ''
        else:
            extension = '.' + str(extension)
        output_filepath = args.output_dir + '/' + name + extension
        gi.histories.download_dataset(hist_id, dataset_id, output_filepath, 
            use_default_filename=False)

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