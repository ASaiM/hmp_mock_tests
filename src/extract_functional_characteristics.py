#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re

def extract_abundances(filepath, nb_charact_to_extract):
    abundances = {}
    more_abund_charact = []
    abund_sum = 0
    with open(filepath, 'r') as abundance_file:
        for line in abundance_file.readlines()[1:]:
            split_line = line[:-1].split('\t')
            charact_id = split_line[0]
            abund = float(split_line[1])
            abundances[charact_id] = abund
            abund_sum += abund

            if len(more_abund_charact) < nb_charact_to_extract:
                more_abund_charact.append(charact_id)
            else:
                best_pos = None
                for i in range(len(more_abund_charact)-1,-1,-1):
                    if abundances[more_abund_charact[i]] < abund:
                        best_pos = i
                    else:
                        break
                if best_pos != None:
                    more_abund_charact = more_abund_charact[:best_pos]
                    more_abund_charact += [charact_id]
                    more_abund_charact += more_abund_charact[best_pos:-1]
    return abundances, more_abund_charact

def format_characteristic_name(name):
    formatted_name = name
    if formatted_name.find(':') != -1:
        formatted_name = formatted_name.split(':')[1][1:]
    formatted_name = formatted_name.replace('/',' ')
    formatted_name = formatted_name.replace('-',' ')
    formatted_name = formatted_name.replace("'",'')
    if formatted_name.find('(') != -1 and formatted_name.find(')') != -1:
        open_bracket = formatted_name.find('(')
        close_bracket = formatted_name.find(')')+1
        formatted_name = formatted_name[:open_bracket] + formatted_name[close_bracket:]
    return formatted_name

def write_more_abundant_charat(abundances,more_abund_charact, output_filepath):
    with open(output_filepath,'w') as output_file:
        output_file.write('\t')
        output_file.write('\t'.join(abundances.keys()) + '\n')

        for mac in more_abund_charact:
            formatted_mac = format_characteristic_name(mac)
            output_file.write(formatted_mac)
            for sample in abundances:
                abund = abundances[sample].get(mac, 0)
                output_file.write('\t' + str(abund))
            output_file.write('\n')

def extract_similar_characteristics(abundances):
    sim_characteristics = set()
    for sample in abundances.keys()[1:]:
        s

def extract_functional_characteristics(args):
    abundances = {}
    more_abund_charact = []

    for i in range(len(args.sample_name)):
        abundances[args.sample_name[i]], mac = extract_abundances(args.charact_input_file[i],
            args.most_abundant_characteristics_to_extract)
        more_abund_charact += mac

    write_more_abundant_charat(abundances, list(set(more_abund_charact)), 
        args.more_abund_output_file)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--sample_name', required=True, action='append')
    parser.add_argument('--charact_input_file', required=True, action='append')
    parser.add_argument('--most_abundant_characteristics_to_extract', required=True,
        type = int)
    parser.add_argument('--more_abund_output_file', required=True)
    args = parser.parse_args()

    if len(args.sample_name) != len(args.charact_input_file):
        raise ValueError("Same number of values (in same order) are expected for --sample_name and --charact_input_file")

    extract_functional_characteristics(args)