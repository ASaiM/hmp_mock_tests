#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re
import time
from bioblend import galaxy

def create_history(name, gi):
    history_details = gi.histories.create_history(name)
    return history_details['id']

def upload_file(filepath, name, hist_id, gi, file_type):
    upload_file_details = gi.tools.upload_file(filepath, hist_id, 
        file_name = name, file_type = file_type)
    upload_file_job_id = upload_file_details['jobs'][0]['id']
    while str(gi.jobs.get_state(upload_file_job_id)) != 'ok':
        time.sleep(1)
    return upload_file_details['outputs'][0]['id']

def upload_files(input_filepaths, hist_id, gi, file_types = {}):
    datasets_id = {} 
    for input_name in input_filepaths:
        file_type = 'tabular'
        if file_types.has_key(input_name):
            file_type = file_types[input_name]
        datasets_id[input_name] = upload_file(input_filepaths[input_name], 
            input_name, hist_id, gi, file_type)
    return datasets_id

def import_workflow(workflow_file_path, gi):
    wf_details = gi.workflows.import_workflow_from_local_path(workflow_file_path)
    wf_id = wf_details['id']
    return wf_id, gi.workflows.show_workflow(wf_id)['inputs']

def check_history_state(gi, hist_id):
    hist_state = gi.histories.show_history(hist_id)['state_ids']
    state = len(hist_state['running']) > 0 
    state |= len(hist_state['queued']) > 0
    state |= len(hist_state['new']) > 0
    return state

def launch_workflow(wf_id, datamap, hist_id, gi, to_check_history_state = True):
    wf_invocation_details = gi.workflows.invoke_workflow(wf_id, datamap, history_id=hist_id)
    wf_invocation_id = wf_invocation_details['id']
    #wf_outputs = wf_invocation_details['outputs']

    if to_check_history_state:
        while check_history_state(gi, hist_id):
            time.sleep(1)

def create_input_datamap(wf_inputs, datasets_id):
    datamap = dict()
    for wf_input in wf_inputs.keys():
        input_name = str(wf_inputs[wf_input]['label'])
        if not datasets_id.has_key(input_name):
            raise ValueError(input_name + ' not found in datasets')
        datamap[wf_input] = { 'src':'hda', 'id': datasets_id[input_name]}
    return datamap

def get_hist_id(hist_name, gi):
    histories = gi.histories.get_histories()
    hist_id = None

    for history in histories:
        if history['name'] == hist_name:
            if hist_id != None:
                raise ValueError(hist_name, 'already found')
            hist_id = history['id']

    if hist_id == None:
        raise ValueError('No history found for', hist_name)
    return hist_id

def export_workflow_outputs(hist_id, output_dir, gi, to_purge = True):
    print "  Export history content of ", hist_id
    count = 1
    for dataset_id in gi.histories.show_history(hist_id)['state_ids']['ok']:
        dataset_name = str(gi.datasets.show_dataset(dataset_id)['name']).lower()
        dataset_name = dataset_name.replace(':', '')
        dataset_name = dataset_name.replace(' ','_')
        dataset_name = dataset_name.replace('/','_')
        dataset_name = str(count) + '_' + dataset_name
        extension = gi.datasets.show_dataset(dataset_id)['extension']
        if extension == None:
            extension = ''
        else:
            extension = '.' + str(extension)
        output_filepath = output_dir + '/' + dataset_name + extension
        count += 1
        gi.histories.download_dataset(hist_id, dataset_id, output_filepath, 
            use_default_filename=False)
    gi.histories.delete_history(hist_id, purge = to_purge)

def run_workflow(workflow_name, workflow_file_path, input_filepaths, gi,
        output_dir, export = True, purge_hist = True, delete_wf = True,
        to_check_history_state = True, file_types = {}):
    print "  Create an history for ", workflow_name, " and import input data"
    hist_id = create_history(workflow_name,gi)
    datasets_id = upload_files(input_filepaths, hist_id, gi, file_types)
    
    print "  Import workflow and launch it"
    wf_id, wf_inputs = import_workflow(workflow_file_path, gi)
    datamap = create_input_datamap(wf_inputs, datasets_id)
    launch_workflow(wf_id, datamap, hist_id, gi, to_check_history_state)

    if export:
        print "  Export workflow results"
        export_workflow_outputs(hist_id,output_dir,gi, purge_hist)

    if delete_wf:
        print "  Delete workflow"
        gi.workflows.delete_workflow(wf_id)

def connect_to_galaxy_instance(gi_url, api_key):
    print "  Connect to Galaxy instance on ", gi_url
    gi = galaxy.GalaxyInstance(url=gi_url, key=api_key)
    return gi
