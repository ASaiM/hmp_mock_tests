#!/usr/bin/env bash
. src/misc.sh

echo "Download reference genomes and extract some data"
echo "================================================"
cd data

if [[ ! -d "reference_genomes" ]]; then
    mkdir "reference_genomes"
fi

cd "reference_genomes"
python ../../src/donwload_extract_reference_genomes.py \
    --exp_taxo_file ../expected_species_w_taxonomy.txt \
    --protein_nb_file ../expected_species_w_protein_nb.txt
cd ../../
echo ""
