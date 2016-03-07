#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re
import time
from bioblend import galaxy

def launch_asaim_workflow(args):
    workflow_file_path = "data/asaim_galaxy_workflow.ga"
    input_data_file = "data/" + args.sample_name + ".fastq"

    print "  Connect to Galaxy instance on ", args.gi_url
    gi = galaxy.GalaxyInstance(url=args.gi_url, key=args.api_key)

    print "  Create an history for ", args.sample_name, " and import input data"
    history_details = gi.histories.create_history(args.sample_name)
    hist_id = history_details['id']
    upload_file_details = gi.tools.upload_file(input_data_file, hist_id)
    upload_file_job_id = upload_file_details['jobs'][0]['id']
    while str(gi.jobs.get_state(upload_file_job_id)) != 'ok':
        time.sleep(1)

    print "  Import workflow and launch it"
    wf_details = gi.workflows.import_workflow_from_local_path(workflow_file_path)
    wf_id = wf_details['id']
    wf = gi.workflows.show_workflow(wf_id)
    wf_input_id = wf['inputs'].keys()[0]
    dataset_id = gi.histories.show_history(hist_id, contents=False)['state_ids']['ok'][0]
    datamap = dict()
    datamap[wf_input_id] = { 'src':'hda', 'id':dataset_id }
    wf_invocation_details = gi.workflows.run_workflow(wf_id, datamap, 
        history_id=hist_id)
    wf_invocation_id = wf_invocation_details['id']
    wf_outputs = wf_invocation_details['outputs']
    
    print "  Wait while workflow is running and export output datasets when generated"
    output_dir_path = "results/" + args.sample_name + "/asaim_results/" 
    if not os.path.exists(output_dir_path):
        os.mkdir(output_dir_path)
    for dataset_id in wf_outputs:
        while str(gi.datasets.show_dataset(dataset_id)['state']) != 'ok':
            time.sleep(1)
            print dataset_id, gi.datasets.show_dataset(dataset_id)['state']
        gi.histories.download_dataset(hist_id, dataset_id, output_dir_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gi_url', required=True)
    parser.add_argument('--api_key', required=True)
    parser.add_argument('--sample_name', required=True)
    args = parser.parse_args()

    launch_asaim_workflow(args)
    