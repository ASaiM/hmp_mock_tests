#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from Bio import SeqIO

def fill_assignations(assignations, assignation_lineage):
    assignation = assignation_lineage[0].split('__')[-1].replace('_',' ')
    assignations.setdefault(assignation, {'nb': 0, 'subassignations': {}})
    assignations[assignation]['nb'] += 1
    if len(assignation_lineage) > 1:
        assignations[assignation]['subassignations'] = fill_assignations(
            assignations[assignation]['subassignations'],
            assignation_lineage[1:])
    return assignations


def write_assignations(assignations, formatted_assignation_file, seq_nb, space,
    expected_species, exp_species_abundance):
    for assignation in assignations:
        abundance = 100.*assignations[assignation]['nb']/(1.*seq_nb)
        to_write = space + assignation + ': '
        to_write += str(abundance)
        to_write += ' %'
        formatted_assignation_file.write(to_write + '\n')

        if assignation.lower().replace(' ','_') == expected_species:
            if exp_species_abundance != 0:
                print expected_species, 'found twice'
            exp_species_abundance = abundance

        if assignations[assignation]['subassignations']:
            exp_species_abundance = write_assignations(assignations[assignation]['subassignations'],
                formatted_assignation_file, seq_nb, space + '\t',
                expected_species, exp_species_abundance)

    return exp_species_abundance

def analyze_metaphlan2_output(args):
    seq_nb = 0
    for record in SeqIO.parse(args.sequence_file, "fasta"):
        seq_nb += 1

    assignations = {}
    with open(args.metaphlan2_output, 'r') as metaphlan2_output_file:
        for line in metaphlan2_output_file.readlines()[1:]:
            assignation_lineage = line[:-1].split('\t')[1].split('|')
            assignations = fill_assignations(assignations, assignation_lineage)

    exp_species_abundance = 0
    with open(args.formatted_assignations, 'w') as formatted_assignation_file:
        exp_species_abundance = write_assignations(assignations,
            formatted_assignation_file, seq_nb, '', args.expected_species, 0)

    with open(args.exp_species_abundance_file,'a') as exp_species_abundance_file:
        exp_sp = args.expected_species.replace("_", " ").title()
        exp_species_abundance_file.write(exp_sp + '\t')
        exp_species_abundance_file.write(str(exp_species_abundance) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--metaphlan2_output', required=True)
    parser.add_argument('--sequence_file', required=True)
    parser.add_argument('--formatted_assignations', required=True)
    parser.add_argument('--expected_species', required=True)
    parser.add_argument('--exp_species_abundance_file', required=True)
    args = parser.parse_args()

    analyze_metaphlan2_output(args)
