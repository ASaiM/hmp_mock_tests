#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from Bio import SeqIO

def fill_distri(read_size, distri):
    if read_size < 50:
        distri['0-50'] += 1
    elif read_size < 100:
        distri['50-100'] += 1
    elif read_size < 150:
        distri['100-150'] += 1
    elif read_size < 200:
        distri['150-200'] += 1
    elif read_size < 250:
        distri['200-250'] += 1
    elif read_size < 300:
        distri['250-300'] += 1
    elif read_size < 350:
        distri['300-350'] += 1
    elif read_size < 400:
        distri['350-400'] += 1
    elif read_size < 450:
        distri['400-450'] += 1
    elif read_size < 500:
        distri['450-500'] += 1
    elif read_size < 550:
        distri['500-550'] += 1
    elif read_size < 600:
        distri['550-600'] += 1
    elif read_size < 650:
        distri['600-650'] += 1
    elif read_size < 700:
        distri['650-700'] += 1
    elif read_size < 750:
        distri['700-750'] += 1
    elif read_size < 800:
        distri['750-800'] += 1
    else:
        print "Read size > 800"
    return distri

def extract_read_sizes(args):
    distri = {}
    distri['0-50'] = 0
    distri['50-100'] = 0
    distri['100-150'] = 0
    distri['150-200'] = 0
    distri['200-250'] = 0
    distri['250-300'] = 0
    distri['300-350'] = 0
    distri['350-400'] = 0
    distri['400-450'] = 0
    distri['450-500'] = 0
    distri['500-550'] = 0
    distri['550-600'] = 0
    distri['600-650'] = 0
    distri['650-700'] = 0
    distri['700-750'] = 0
    distri['750-800'] = 0

    with open(args.read_size_file, "w") as read_size_file:
        for record in SeqIO.parse(args.fasta_file,"fasta"):
            read_size = len(record.seq)
            read_size_file.write(record.description.split(' ')[0] + '\t')
            read_size_file.write(str(read_size) + '\n')
            distri = fill_distri(read_size, distri)

    with open(args.read_size_distribution, "w") as read_size_distribution:
        read_size_distribution.write('0-50\t' + str(distri['0-50']) + '\n')
        read_size_distribution.write('50-100\t' + str(distri['50-100']) + '\n')
        read_size_distribution.write('100-150\t' + str(distri['100-150']) + '\n')
        read_size_distribution.write('150-200\t' + str(distri['150-200']) + '\n')
        read_size_distribution.write('200-250\t' + str(distri['200-250']) + '\n')
        read_size_distribution.write('250-300\t' + str(distri['250-300']) + '\n')
        read_size_distribution.write('300-350\t' + str(distri['300-350']) + '\n')
        read_size_distribution.write('350-400\t' + str(distri['350-400']) + '\n')
        read_size_distribution.write('400-450\t' + str(distri['400-450']) + '\n')
        read_size_distribution.write('450-500\t' + str(distri['450-500']) + '\n')
        read_size_distribution.write('500-550\t' + str(distri['500-550']) + '\n')
        read_size_distribution.write('550-600\t' + str(distri['550-600']) + '\n')
        read_size_distribution.write('600-650\t' + str(distri['600-650']) + '\n')
        read_size_distribution.write('650-700\t' + str(distri['650-700']) + '\n')
        read_size_distribution.write('700-750\t' + str(distri['700-750']) + '\n')
        read_size_distribution.write('750-800\t' + str(distri['750-800']) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--fasta_file', required=True)
    parser.add_argument('--read_size_file', required=True)
    parser.add_argument('--read_size_distribution', required=True)
    args = parser.parse_args()

    extract_read_sizes(args)
