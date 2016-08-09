#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

def extract_refseq_uniref50_mapping(args):
    with open(args.refseq_uniref50_mapping_file, 'w') as refseq_uniref50_mapping_file:
        with open(args.uniprot_mapping_file, 'r') as uniprot_mapping_file:
            for line in uniprot_mapping_file.readlines():
                split_line = line[:-1].split('\t')
                ref_seq_id = split_line[3]
                uniref50_id = split_line[9]
                refseq_uniref50_mapping_file.write(ref_seq_id + '\t')
                refseq_uniref50_mapping_file.write(uniref50_id + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--uniprot_mapping_file', required=True)
    parser.add_argument('--refseq_uniref50_mapping_file', required=True)
    args = parser.parse_args()

    extract_refseq_uniref50_mapping(args)
