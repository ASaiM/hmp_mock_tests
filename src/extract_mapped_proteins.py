#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import pysam


def extract_refseq_uniref50_mapping(args):
    refseq_uniref50_mapping = {}
    with open(args.refseq_uniref50_mapping_file) as refseq_uniref50_mapping_file:
        for line in refseq_uniref50_mapping_file.readlines():
            split_line = line[:-1].split('\t')
            refseq_uniref50_mapping.setdefault(split_line[0], split_line[1])
    return refseq_uniref50_mapping


def extract_uniref50_abundance(args, refseq_uniref50_mapping, log_file):
    uniref50_abundance = {}
    samfile = pysam.AlignmentFile(args.mapping_file,"rb")
    total_count = 0
    non_mapped_seq = []
    with open(args.reference_protein_file) as ref_prot_file:
        for line in ref_prot_file.readlines()[1:]:
            split_line = line[:-1].split('\t')
            org = split_line[0]
            genome_seq_id = split_line[1]
            ref_seq_id = split_line[2]
            start = int(split_line[3])
            stop = int(split_line[4])

            if genome_seq_id in non_mapped_seq:
                continue

            if samfile.get_tid(genome_seq_id) == -1:
                string = genome_seq_id + ' for ' + org
                string += ' is not a mapped sequence'
                log_file.write(string + '\n')
                non_mapped_seq.append(genome_seq_id)
                continue

            count = samfile.count(reference = genome_seq_id, start = start,
                end = stop, until_eof = True)

            if count == 0:
                continue

            if not refseq_uniref50_mapping.has_key(ref_seq_id):
                string = ref_seq_id
                string += ' not found in RefSeq - UniRef50 mapping'
                log_file.write(string + '\n')
                continue

            uniref50_id = refseq_uniref50_mapping[ref_seq_id]
            uniref50_abundance.setdefault(uniref50_id,
                {'total': 0, 'per_species': {}})

            uniref50_abundance[uniref50_id]['total'] += count
            uniref50_abundance[uniref50_id]['per_species'].setdefault(org,
                0)
            uniref50_abundance[uniref50_id]['per_species'][org] += count
            total_count += count
    return uniref50_abundance, total_count


def analyze_mapping_info(args):
    log_file = open(args.log, 'w')

    refseq_uniref50_mapping = extract_refseq_uniref50_mapping(args)
    uniref50_abundance, total_count = extract_uniref50_abundance(args,
        refseq_uniref50_mapping, log_file)
    with open(args.uniref50_abund_file, 'w') as abund_file:
        abund_file.write('uniref50_id\tmapped_count\trelative_mapped_count\n')

        with open(args.uniref50_abund_per_sp_file, 'w') as abund_per_sp_file:
            abund_per_sp_file.write('uniref50_id\tspecies\t')
            abund_per_sp_file.write('mapped_count\trelative_mapped_count\n')

            for uniref50_id in uniref50_abundance:
                count = uniref50_abundance[uniref50_id]['total']
                relative_count = 100*count/(1.*total_count)
                abund_file.write(uniref50_id + '\t')
                abund_file.write(str(count) + '\t')
                abund_file.write(str(relative_count) + '\n')

                for sp in uniref50_abundance[uniref50_id]['per_species']:
                    count = uniref50_abundance[uniref50_id]['per_species'][sp]
                    relative_count = 100*count/(1.*total_count)
                    abund_per_sp_file.write(uniref50_id + '\t')
                    abund_per_sp_file.write(sp + '\t')
                    abund_per_sp_file.write(str(count) + '\t')
                    abund_per_sp_file.write(str(relative_count) + '\n')
    log_file.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mapping_file', required=True)
    parser.add_argument('--reference_protein_file', required=True)
    parser.add_argument('--refseq_uniref50_mapping_file', required=True)
    parser.add_argument('--uniref50_abund_file', required=True)
    parser.add_argument('--uniref50_abund_per_sp_file', required=True)
    parser.add_argument('--log', required=True)
    args = parser.parse_args()

    analyze_mapping_info(args)
