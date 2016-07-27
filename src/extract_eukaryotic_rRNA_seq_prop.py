#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from Bio import SeqIO


def extract_eukaryotic_rRNA_seq_prop(args):
    sortmerna_euk_seq_id = []
    for record in SeqIO.parse(args.sortmerna_euk_db, "fasta"):
        sortmerna_euk_seq_id.append(record.description[:-1].split(' ')[0])

    with open(args.asaim_rrna_blast_report, 'r') as asaim_rrna_blast_report:
        rrna_seq_nb = 0
        euk_rrna_seq_nb = 0
        for line in asaim_rrna_blast_report.readlines():
            sortmerna_seq_id = line[:-1].split('\t')[1]
            rrna_seq_nb += 1
            if sortmerna_seq_id in sortmerna_euk_seq_id:
                euk_rrna_seq_nb += 1

    print "\tNumber of rRNA sequences", rrna_seq_nb
    print "\tNumber of eukaryotic rRNA sequences", euk_rrna_seq_nb
    print "\tPercentage of eukaryotic sequences in rRNA sequences",
    print (100.*euk_rrna_seq_nb)/rrna_seq_nb

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--sortmerna_euk_db', required=True)
    parser.add_argument('--asaim_rrna_blast_report', required=True)
    args = parser.parse_args()

    extract_eukaryotic_rRNA_seq_prop(args)
