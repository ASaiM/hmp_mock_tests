#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
from Bio import SeqIO
from sets import Set


def test_ebi_seq_id(args):
    asaim_rrna_seq_ids = []
    for record in SeqIO.parse(args.asaim_rrna_seq, "fasta"):
        asaim_rrna_seq_ids.append(record.description.split(' ')[0])

    asaim_non_rrna_seq_ids = []
    for record in SeqIO.parse(args.asaim_non_rrna_seq, "fasta"):
        asaim_non_rrna_seq_ids.append(record.description.split(' ')[0])

    nb = {}
    nb['ebi_rrna_seq_nb'] = 0
    nb['ebi_rrna_seq_in_asaim_rrna'] = 0
    nb['ebi_rrna_seq_in_asaim_non_rrna'] = 0
    ebi_rrna_seq_not_in_asaim = []
    for record in SeqIO.parse(args.ebi_rrna_seq, "fasta"):
        ebi_rrna_seq_id = record.description.split(' ')[0]
        nb['ebi_rrna_seq_nb'] += 1
        if ebi_rrna_seq_id in asaim_rrna_seq_ids:
            nb['ebi_rrna_seq_in_asaim_rrna'] += 1
        elif ebi_rrna_seq_id in asaim_non_rrna_seq_ids:
            nb['ebi_rrna_seq_in_asaim_non_rrna'] += 1
        else:
            ebi_rrna_seq_not_in_asaim.append(record)

    return ebi_rrna_seq_not_in_asaim, nb


def check_hsp(pident, cov, evalue):
    return pident >= 98 and cov >= 98 and evalue <= 1e-16


def blast_comparison(ebi_rrna_seq_not_in_asaim):
    if not os.path.exists("tmp"):
        os.makedirs("tmp")

    #SeqIO.write(ebi_rrna_seq_not_in_asaim, "tmp/ebi_rrna_seq_not_in_asaim.fasta",
    #    "fasta")

    cmd = "makeblastdb "
    cmd += ' -in "' + args.asaim_rrna_seq + '"'
    cmd += ' -dbtype nucl'
    #os.system(cmd)
    cmd = "blastn "
    cmd += ' -db "' + args.asaim_rrna_seq + '"'
    cmd += " -query tmp/ebi_rrna_seq_not_in_asaim.fasta"
    cmd += " -out tmp/ebi_rrna_seq_not_in_asaim_report"
    cmd += ' -outfmt "6 qseqid sseqid pident qlen length evalue"'
    os.system(cmd)

    qseqids = Set([])
    with open("tmp/ebi_rrna_seq_not_in_asaim_report", "r") as blast_report:
        for line in blast_report.readlines():
            split_line = line[:-1].split('\t')
            #print split_line
            qseqid = split_line[0]
            pident = float(split_line[2])
            qlen = float(split_line[3])
            length = float(split_line[4])
            cov = 100*qlen/length
            evalue = float(split_line[5])

            if check_hsp(pident, cov, evalue):
                qseqids.add(qseqid)
    return len(qseqids)


def compare_ebi_asaim_rrna_sequences(args):
    print "\tComparison based on sequence id"
    ebi_rrna_seq_not_in_asaim, nb = test_ebi_seq_id(args)
    ebi_rrna_seq_not_in_asaim_nb = len(ebi_rrna_seq_not_in_asaim)

    print "\t\tPercentage of EBI rRNA sequences found in ASaiM rRNA sequences",
    print (100.*nb['ebi_rrna_seq_in_asaim_rrna'])/nb['ebi_rrna_seq_nb']
    print "\t\tPercentage of EBI rRNA sequences found in ASaiM non rRNA sequences",
    print (100.*nb['ebi_rrna_seq_in_asaim_non_rrna'])/nb['ebi_rrna_seq_nb']
    print "\t\tPercentage of EBI rRNA sequences not found in ASaiM sequences",
    print (100.*ebi_rrna_seq_not_in_asaim_nb)/nb['ebi_rrna_seq_nb']

    print "\tSearch of similarity between ",
    print "EBI rRNA sequences not found in ASaiM sequences and ",
    print "ASaiM rRNA sequences"
    new_ebi_rrna_seq_in_asaim_rrna = blast_comparison(ebi_rrna_seq_not_in_asaim)
    nb['ebi_rrna_seq_in_asaim_rrna'] += new_ebi_rrna_seq_in_asaim_rrna
    ebi_rrna_seq_not_in_asaim_nb -= new_ebi_rrna_seq_in_asaim_rrna

    print "\t\tPercentage of EBI rRNA sequences found in ASaiM rRNA sequences",
    print (100.*nb['ebi_rrna_seq_in_asaim_rrna'])/nb['ebi_rrna_seq_nb']
    print "\t\tPercentage of EBI rRNA sequences found in ASaiM non rRNA sequences",
    print (100.*nb['ebi_rrna_seq_in_asaim_non_rrna'])/nb['ebi_rrna_seq_nb']
    print "\t\tPercentage of EBI rRNA sequences not found in ASaiM sequences",
    print (100.*ebi_rrna_seq_not_in_asaim_nb)/nb['ebi_rrna_seq_nb']


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ebi_rrna_seq', required=True)
    parser.add_argument('--asaim_rrna_seq', required=True)
    parser.add_argument('--asaim_non_rrna_seq', required=True)
    args = parser.parse_args()

    compare_ebi_asaim_rrna_sequences(args)
