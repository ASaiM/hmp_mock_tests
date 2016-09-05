#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re
import time

def extract_mapping_gene_families(mapping_gene_family_filepath):
    mapping_gene_families = {}
    with open(mapping_gene_family_filepath, 'r') as mapping_gene_family_file:
        for line in mapping_gene_family_file.readlines()[1:]:
            split_line = line[:-1].split('\t')
            mapping_gene_families[split_line[0]] = float(split_line[2])
    return mapping_gene_families

def compare_asaim_mapping_gene_families(args):
    mapping_gene_families = extract_mapping_gene_families(args.mapping_gene_families)

    asaim_gene_families = 0
    similar_gene_families = []

    abund_sum = 0
    similar_gene_family_abund_sum = 0

    similar_gene_family_file = open(args.similar_gene_families, 'w')
    similar_gene_family_file.write('gene_family\tmapping_abund\tasaim_abund\n')
    asaim_specific_gene_family_file = open(args.asaim_specific_gene_families, 'w')

    with open(args.asaim_gene_families, 'r') as asaim_gene_family_file:
        for line in asaim_gene_family_file.readlines()[1:]:
            split_line = line[:-1].split('\t')
            asaim_gene_families += 1
            abund = 100*float(split_line[1])
            abund_sum += abund
            gene_family = split_line[0].split(':')[0]
            if gene_family in mapping_gene_families:
                similar_gene_family_file.write(gene_family + '\t')
                similar_gene_family_file.write(str(mapping_gene_families[gene_family]) + '\t')
                similar_gene_family_file.write(str(abund) + '\n')

                similar_gene_families.append(gene_family)
                similar_gene_family_abund_sum += abund
            else:
                asaim_specific_gene_family_file.write(gene_family + '\n')

    similar_gene_family_file.close()
    asaim_specific_gene_family_file.close()

    print "\tNumber of similar gene families:", len(similar_gene_families)
    print
    print "\tPercentage of ASaiM gene families similar to mapping gene families:",
    print (100.*len(similar_gene_families))/asaim_gene_families
    print "\tRelative abundance of ASaiM gene families similar to mapping gene families:",
    print similar_gene_family_abund_sum
    print

    mapping_similar_gene_families = 0
    mapping_gene_family_nb = 0
    similar_gene_family_abund_sum = 0

    for family in mapping_gene_families:
        mapping_gene_family_nb += 1
        if family in similar_gene_families:
            mapping_similar_gene_families += 1
            similar_gene_family_abund_sum += mapping_gene_families[family]

    print "\tPercentage of mapping gene families similar to ASaiM gene families:",
    print (100.*mapping_similar_gene_families)/mapping_gene_family_nb
    print "\tRelative abundance of ASaiM gene families similar to mapping gene families:",
    print similar_gene_family_abund_sum


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--asaim_gene_families', required=True)
    parser.add_argument('--mapping_gene_families', required=True)
    parser.add_argument('--similar_gene_families', required=True)
    parser.add_argument('--asaim_specific_gene_families', required=True)
    args = parser.parse_args()

    compare_asaim_mapping_gene_families(args)
