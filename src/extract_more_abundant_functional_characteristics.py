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
    print abund_sum
    return abundances, more_abund_charact

def extract_more_abundant_functional_characteristics(args):
    abundances = {}
    more_abund_charact = []

    base_name_file = ''
    if args.functional_characteristics == 'gene_families':
        base_name_file = "normalized_table_for______________data_17_(humann2).tsv"
    elif args.functional_characteristics == 'pathways':
        base_name_file = "normalized_table_for______________data_19_(humann2).tsv"
    else :
        raise ValueError('Unknown functional characteristics')

    for sample in args.sample_name:
        abundance_filepath = "results/" + sample + "/asaim_results/" + base_name_file
        abundances[sample], mac = extract_abundances(abundance_filepath,
            args.number_of_characteristics_to_extract)
        more_abund_charact += mac

    more_abund_charact = list(set(more_abund_charact))
    with open(args.output_file,'w') as output_file:
        output_file.write(args.functional_characteristics + '\t')
        output_file.write('\t'.join(args.sample_name) + '\n')

        for mac in more_abund_charact:
            formatted_mac = mac
            if formatted_mac.find(':') != -1:
                formatted_mac = formatted_mac.split(':')[1][1:]
            formatted_mac = formatted_mac.replace('/',' ')
            formatted_mac = formatted_mac.replace('-',' ')
            formatted_mac = formatted_mac.replace("'",'')

            if formatted_mac.find('(') != -1 and formatted_mac.find(')') != -1:
                open_bracket = formatted_mac.find('(')
                close_bracket = formatted_mac.find(')')+1
                formatted_mac = formatted_mac[:open_bracket] + formatted_mac[close_bracket:]
            output_file.write(formatted_mac)
            for sample in args.sample_name:
                abund = abundances[sample].get(mac, 0)
                output_file.write('\t' + str(abund))
            output_file.write('\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--sample_name', required=True, action='append')
    parser.add_argument('--functional_characteristics', required=True, 
        choices=['gene_families', 'pathways'])
    parser.add_argument('--number_of_characteristics_to_extract', required=True,
        type = int)
    parser.add_argument('--output_file', required=True)
    args = parser.parse_args()

    extract_more_abundant_functional_characteristics(args)