#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
from Bio import SeqIO

def compare_raw_and_ref_sortmerna_results(args):
    raw_rrna_seq = []
    for record in SeqIO.parse(args.raw_rrna_seq, "fasta"):
        raw_rrna_seq.append(record.description.split(' ')[0])

    ref_rrna_seq = 0
    raw_ref_rrna_seq = 0
    for record in SeqIO.parse(args.ref_rrna_seq, "fasta"):
        seq_id = record.description.split(' ')[0]
        ref_rrna_seq += 1
        if seq_id in raw_rrna_seq:
            raw_ref_rrna_seq += 1

    print "\tNumber of rRNA sequences (SortMeRNA db):", len(raw_rrna_seq)
    print "\tNumber of rRNA sequences (reference seq db):", ref_rrna_seq
    print "\tNumber of rRNA sequences found with SortMeRNA found also with",
    print " reference rRNA sequence db:", raw_ref_rrna_seq
    print "\tProportion of rRNA sequences found with SortMeRNA found also with",
    print " reference rRNA sequence db:", raw_ref_rrna_seq/(1.*len(raw_rrna_seq))
    print "\tProportion of rRNA sequences found with rRNA sequence found also with",
    print " SortMeRNA sequence db:", raw_ref_rrna_seq/(1.*ref_rrna_seq)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--raw_rrna_seq', required=True)
    parser.add_argument('--ref_rrna_seq', required=True)
    args = parser.parse_args()

    compare_raw_and_ref_sortmerna_results(args)
