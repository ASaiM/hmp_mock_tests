#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re
import wget
import subprocess
import tarfile
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def extract_pos(line):
    start = int(line[3])
    stop = int(line[4])
    strand = line[6]
    return start, stop, strand


def extract_genome_part(genome, start, stop, strand, gene_id):
    #if strand == '-':
    #    reverse_complement_genome = genome.reverse_complement()
    #    reverse_start = (genome_size-stop)
    #    reverse_stop = (genome_size-start+1)
    #    return reverse_complement_genome[reverse_start:reverse_stop]
    #else:
    record = SeqRecord(genome.seq[start:stop])
    record.id = gene_id
    record.description = gene_id
    return record


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
            else:
                new_filename = sp_name.lower().replace(' ','_') + '.gff'
                filename = wget.download(ftp_link + '_genomic.gff.gz')
                os.rename(filename, new_filename + ".gz")
                os.system("gunzip " + new_filename + ".gz")
                print

                os.system("gunzip ../reference_genomes/acinetobacter_baumannii.fna.gz")
                record_iterator = SeqIO.parse(
                    "../reference_genomes/acinetobacter_baumannii.fna",
                    "fasta")
                genome = next(record_iterator)

                with open(new_filename, "r") as gff_file:
                    for line in gff_file.readlines():
                        if line[0] == '#':
                            continue

                        split_line = line[:-1].split('\t')
                        if split_line[2] != 'rRNA':
                            continue

                        gene_id = split_line[8].split("Dbxref=GeneID:")[1]
                        gene_id = gene_id.split(';')[0]
                        gene_id = split_line[0] + ' ' + gene_id

                        rRNA_genes += 1
                        start, stop, strand = extract_pos(split_line)
                        rRNA_seq_records.append(extract_genome_part(genome,
                            start, stop, strand, gene_id))

                        if split_line[8].find("product=5S ribosomal RNA") != -1:
                            rRNA_5S_genes += 1
                        elif split_line[8].find("product=16S ribosomal RNA") != -1:
                            rRNA_16S_genes += 1
                        elif split_line[8].find("product=23S ribosomal RNA") != -1:
                            rRNA_23S_genes += 1
                os.system("gzip ../reference_genomes/acinetobacter_baumannii.fna")

            rRNA_nb_file.write(sp_name + '\t')
            rRNA_nb_file.write(str(rRNA_5S_genes) + '\t')
            rRNA_nb_file.write(str(rRNA_16S_genes) + '\t')
            rRNA_nb_file.write(str(rRNA_23S_genes) + '\n')

        rRNA_nb_file.close()

        os.chdir("../")
        os.system("rm -r tmp")

        output_handle = open(reference_rRNA_filepath, "w")
        SeqIO.write(rRNA_seq_records, output_handle, "fasta")
        output_handle.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--exp_taxo_file', required=True)
    parser.add_argument('--reference_rRNA_file', required=True)
    parser.add_argument('--rRNA_nb_file', required=True)
    args = parser.parse_args()

    download_extract_reference_rRNA(args.exp_taxo_file,
        args.reference_rRNA_file, args.rRNA_nb_file)
