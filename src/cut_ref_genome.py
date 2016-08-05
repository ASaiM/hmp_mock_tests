#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import numpy as np
import random
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def cut_seq(genome, size_min, size_max, nb):
    starts = np.random.random_integers(0, len(genome.seq), nb)
    lengths = np.random.random_integers(size_min, size_max, nb)
    reads = []
    for i in range(nb):
        start = starts[i]
        stop = start + lengths[i]
        record = SeqRecord(genome.seq[start:stop])
        record.id = str(i)
        record.description = "Cut genome of size " + str(stop-start)
        reads.append(record)
    return reads


def cut_ref_genome(args):
    record_iterator = SeqIO.parse(args.ref_genome_seq, "fasta")
    genome = next(record_iterator)

    reads = []
    with open(args.read_size_distribution, 'r') as read_size_distribution:
        for line in read_size_distribution.readlines():
            split_line = line[:-1].split('\t')
            nb = int(split_line[1])
            interval = split_line[0].split('-')
            interval_min = int(interval[0])
            interval_max = int(interval[1])
            reads += cut_seq(genome, interval_min, interval_max, nb)

    random.shuffle(reads)

    output_handle = open(args.cut_ref_genome, "w")
    SeqIO.write(reads, output_handle, "fasta")
    output_handle.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ref_genome_seq', required=True)
    parser.add_argument('--read_size_distribution', required=True)
    parser.add_argument('--cut_ref_genome', required=True)
    args = parser.parse_args()

    cut_ref_genome(args)
