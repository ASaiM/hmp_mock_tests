#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import wget

def extract_ref_proteins(feature_table_filepath, reference_protein_file, genome):
    with open(feature_table_filepath, 'r') as feature_table_file:
        for line in feature_table_file.readlines():
            split_line = line[:-1].split('\t')
            if split_line[0] == 'CDS':
                genome_id = split_line[6]
                start = split_line[7]
                stop = split_line[8]
                ref_seq_id = split_line[11]
                if ref_seq_id != '':
                    reference_protein_file.write(genome + '\t')
                    reference_protein_file.write(genome_id + '\t')
                    reference_protein_file.write(ref_seq_id + '\t')
                    reference_protein_file.write(start + '\t')
                    reference_protein_file.write(stop + '\n')

def download_format_reference_proteins(args):
    with open(args.exp_taxo_file, 'r') as exp_taxo_file:
        with open(args.reference_protein_file, 'w') as reference_protein_file:
            reference_protein_file.write('organism_name\tgenome_seq_id\t')
            reference_protein_file.write('cds_ref_seq_id\tstart\tstop\n')

            for line in exp_taxo_file.readlines():
                split_line = line[:-1].split('\t')

                sp_name = split_line[7]
                ftp_link = split_line[9]

                print sp_name

                new_filename = sp_name.lower().replace(' ','_') + '._feature_table.txt'
                filename = wget.download(ftp_link + '_feature_table.txt.gz')
                os.rename(filename, new_filename + '.gz')
                os.system("gunzip " + new_filename + ".gz")

                extract_ref_proteins(new_filename, reference_protein_file,
                    sp_name)

                os.system("rm " + new_filename)

                print

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--exp_taxo_file', required=True)
    parser.add_argument('--reference_protein_file', required=True)
    args = parser.parse_args()

    download_format_reference_proteins(args)
