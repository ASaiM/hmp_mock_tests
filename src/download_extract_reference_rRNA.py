#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re
import time
import wget
import subprocess
import tarfile
from Bio import SeqIO

def extract_pos(line):
    start = int(line[3])
    stop = int(line[4])
    strand = line[6]
    return start, stop, strand


def extract_genome_part(genome, start, stop, strand):
    #if strand == '-':
    #    reverse_complement_genome = genome.reverse_complement()
    #    reverse_start = (genome_size-stop)
    #    reverse_stop = (genome_size-start+1)
    #    return reverse_complement_genome[reverse_start:reverse_stop]
    #else:
    return genome[start:stop]


def download_extract_reference_rRNA(exp_taxo_filepath, reference_rRNA_filepath,
    rRNA_nb_filepath):
    with open(exp_taxo_filepath, 'r') as exp_taxo_file:
        rRNA_nb_file = open(rRNA_nb_filepath, 'w')

        if not os.path.exists("tmp"):
            os.makedirs("tmp")
        os.chdir("tmp")

        rRNA_seq_records = []

        for line in exp_taxo_file.readlines():
            split_line = line[:-1].split('\t')

            sp_name = split_line[7]
            ftp_link = split_line[9]

            print sp_name
            rRNA_5S_genes = 0
            rRNA_16S_genes = 0
            rRNA_23S_genes = 0
            rRNA_genes = 0

            if sp_name != 'Acinetobacter baumannii':
                new_filename = sp_name.lower().replace(' ','_') + '.fna'

                filename = wget.download(ftp_link + '_rna_from_genomic.fna.gz')
                os.rename(filename, new_filename + ".gz")
                os.system("gunzip " + new_filename + ".gz")
                print

                for record in SeqIO.parse(new_filename,"fasta"):
                    if record.description.find("ribosomal") != -1:
                        rRNA_seq_records.append(record)
                        rRNA_genes += 1

                        if record.description.find("5S") != -1 :
                            rRNA_5S_genes += 1
                        elif record.description.find("16S")!= -1 :
                            rRNA_16S_genes += 1
                        elif record.description.find("23S")!= -1 :
                            rRNA_23S_genes += 1
                        #else:
                        #    raise ValueError("Unknown ribosomal gene")
            else:
                seq_filename = sp_name.lower().replace(' ','_') + '.fna'
                filename = wget.download(ftp_link + '_genomic.fna.gz')
                os.rename(filename, seq_filename)
                record_iterator = SeqIO.parse(seq_filename, "fasta")
                genome = next(record_iterator)

                new_filename = sp_name.lower().replace(' ','_') + '.gff'
                filename = wget.download(ftp_link + '_genomic.gff.gz')
                os.rename(filename, new_filename + ".gz")
                os.system("gunzip " + new_filename + ".gz")
                print

                with open(new_filename, "r") as gff_file:
                    for line in gff_file.readlines():
                        if line[0] == '#':
                            continue

                        split_line = line[:-1].split('\t')
                        if split_line[2] != 'rRNA':
                            continue

                        rRNA_genes += 1
                        start, stop, strand = extract_pos(split_line)
                        rRNA_seq_records.append(extract_genome_part(genome,
                            start, stop, strand))

                        if split_line[8].find("product=5S ribosomal RNA") != -1:
                            rRNA_5S_genes += 1
                        elif split_line[8].find("product=16S ribosomal RNA") != -1:
                            rRNA_16S_genes += 1
                        elif split_line[8].find("product=23S ribosomal RNA") != -1:
                            rRNA_23S_genes += 1

            rRNA_nb_file.write(sp_name + '\t')
            rRNA_nb_file.write(str(rRNA_5S_genes) + '\t')
            rRNA_nb_file.write(str(rRNA_16S_genes) + '\t')
            rRNA_nb_file.write(str(rRNA_23S_genes) + '\n')

        rRNA_nb_file.close()
        SeqIO.write(rRNA_seq_records, reference_rRNA_filepath, "fasta")
        os.chdir("../")
        os.system("rm -r tmp")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--exp_taxo_file', required=True)
    parser.add_argument('--reference_rRNA_file', required=True)
    parser.add_argument('--rRNA_nb_file', required=True)
    args = parser.parse_args()

    download_extract_reference_rRNA(args.exp_taxo_file,
        args.reference_rRNA_file, args.rRNA_nb_file)
