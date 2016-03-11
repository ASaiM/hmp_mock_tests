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

function get_rRNA_sequences_number {
    sample_name=$1
    run_name=$2
    echo " $sample_name"
    echo "  5S sequences:"
    wget "https://www.ebi.ac.uk/metagenomics//projects/SRP004311/samples/"$run_name"/runs/"$sample_name"/results/versions/1.0/taxonomy/5S-rRNA-FASTA" >/dev/null 2>&1
    grep ">" "5S-rRNA-FASTA" | wc -l
    rm "5S-rRNA-FASTA"

    echo "  16S sequences:"
    wget "https://www.ebi.ac.uk/metagenomics//projects/SRP004311/samples/"$run_name"/runs/"$sample_name"/results/versions/1.0/taxonomy/16S-rRNA-FASTA" >/dev/null 2>&1
    grep ">" "16S-rRNA-FASTA" | wc -l
    rm "16S-rRNA-FASTA"

    echo "  23S sequences:"
    wget "https://www.ebi.ac.uk/metagenomics//projects/SRP004311/samples/"$run_name"/runs/"$sample_name"/results/versions/1.0/taxonomy/23S-rRNA-FASTA" >/dev/null 2>&1
    grep ">" "23S-rRNA-FASTA" | wc -l
    rm "23S-rRNA-FASTA"
}

function download_EBI_taxonomic_results {
    sample_name=$1
    run_name=$2
    echo " -- "$sample_name" -- "
    if [[ ! -d $sample_name ]]; then
        mkdir $sample_name
    fi 
    cd $sample_name
    if [[ ! -d "EBI_results" ]]; then
        mkdir "EBI_results"
    fi
    wget "https://www.ebi.ac.uk/metagenomics//projects/SRP004311/samples/"$run_name"/runs/"$sample_name"/results/versions/1.0/taxonomy/OTU-TSV"
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

echo "Get number of rRNA sequences"
echo "============================"
get_rRNA_sequences_number "SRR072232" "SRS121012"
get_rRNA_sequences_number "SRR072233" "SRS121011"
echo ""

echo "Download EBI taxonomic results"
echo "=============================="
if [[ ! -d results ]]; then
    mkdir results
fi
cd results 
download_EBI_taxonomic_results "SRR072232" "SRS121012"
download_EBI_taxonomic_results "SRR072233" "SRS121011"
cd ../
echo ""

echo "Format EBI taxonomic results"
echo "============================"
format_EBI_taxonomic_results "SRR072232"
format_EBI_taxonomic_results "SRR072233"
echo ""

