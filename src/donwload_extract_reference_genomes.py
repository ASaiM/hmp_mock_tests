#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import re
import time
import wget
import subprocess

def donwload_extract_reference_genomes(exp_taxo_filepath, protein_nb_filepath):
    with open(exp_taxo_filepath, 'r') as exp_taxo_file:
        with open(protein_nb_filepath, 'w') as protein_nb_file:
            for line in exp_taxo_file.readlines():
                split_line = line[:-1].split('\t')
                
                sp_name = split_line[7]
                ftp_link = split_line[9]

                print sp_name

                filename = wget.download(ftp_link + '_genomic.fna.gz')
                os.rename(filename, sp_name.lower().replace(' ','_') + '.fna.gz')

                command = 'curl -s -L ' + ftp_link + '_protein.faa.gz'
                command += ' | zgrep "^>" | wc -l'
                prot_nb = subprocess.check_output(command, shell=True, 
                    stderr=subprocess.STDOUT)  
                prot_nb = prot_nb.replace(' ','')
                prot_nb = prot_nb.replace('\n','')
                protein_nb_file.write(sp_name + '\t' + prot_nb + '\n')

                print 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--exp_taxo_file', required=True)
    parser.add_argument('--protein_nb_file', required=True)
    args = parser.parse_args()

    donwload_extract_reference_genomes(args.exp_taxo_file, args.protein_nb_file)

