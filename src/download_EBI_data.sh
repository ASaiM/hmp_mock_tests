#!/bin/bash

function download_unarchive {
    sample_name=$1
    if [[ ! -f $sample_name".fastq" ]]; then
        echo " -- "$sample_name" -- "
        wget "ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR072/"$sample_name"/"$sample_name".fastq.gz"
        gunzip $sample_name".fastq.gz"
        echo ""
    fi
}

function download_EBI_taxonomic_results {
    sample_name=$1
    echo " -- "$sample_name" -- "
    if [[ ! -d $sample_name ]]; then
        mkdir $sample_name
    fi 
    cd $sample_name
    if [[ ! -d "EBI_results" ]]; then
        mkdir "EBI_results"
    fi
    wget $2
    mv "OTU-TSV" "EBI_results/taxonomic_assignation.tsv"
    cd ../
    echo ""
}

function format_EBI_taxonomic_results {
    sample_name=$1
    python src/format_EBI_taxonomic_results.py \
        --ebi_taxonomic_results "results/"$sample_name"/EBI_results/taxonomic_assignation.tsv" \
        --output_dir "results/"$sample_name"/EBI_results/"
}

echo "Download input datasets"
echo "======================="
cd data
download_unarchive "SRR072232"
download_unarchive "SRR072233"
cd ../
echo ""

echo "Download EBI taxonomic results"
echo "=============================="
if [[ ! -d results ]]; then
    mkdir results
fi
cd results 
download_EBI_taxonomic_results "SRR072232" \
    "https://www.ebi.ac.uk/metagenomics//projects/SRP004311/samples/SRS121012/runs/SRR072232/results/versions/1.0/taxonomy/OTU-TSV"
download_EBI_taxonomic_results "SRR072233" \
    "https://www.ebi.ac.uk/metagenomics//projects/SRP004311/samples/SRS121011/runs/SRR072233/results/versions/1.0/taxonomy/OTU-TSV"
cd ../
echo ""

echo "Format EBI taxonomic results"
echo "============================"
format_EBI_taxonomic_results "SRR072232"
format_EBI_taxonomic_results "SRR072233"
echo ""