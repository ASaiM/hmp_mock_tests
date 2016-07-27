#!/usr/bin/env bash
. src/misc.sh

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
    echo " -- $sample_name -- "
    if [[ ! -d $sample_name ]]; then
        mkdir $sample_name
    fi
    cd $sample_name
    if [[ ! -d "EBI_results" ]]; then
        mkdir "EBI_results"
    fi

    echo "  5S sequences:"
    wget "https://www.ebi.ac.uk/metagenomics//projects/SRP004311/samples/"$run_name"/runs/"$sample_name"/results/versions/1.0/taxonomy/5S-rRNA-FASTA" >/dev/null 2>&1
    grep ">" "5S-rRNA-FASTA" | wc -l
    mv "5S-rRNA-FASTA" "EBI_results/5S_rRNA.fasta"
    cat "EBI_results/5S_rRNA.fasta" > "EBI_results/rRNA.fasta"

    echo "  16S sequences:"
    wget "https://www.ebi.ac.uk/metagenomics//projects/SRP004311/samples/"$run_name"/runs/"$sample_name"/results/versions/1.0/taxonomy/16S-rRNA-FASTA" >/dev/null 2>&1
    grep ">" "16S-rRNA-FASTA" | wc -l
    mv "16S-rRNA-FASTA" "EBI_results/16S_rRNA.fasta"
    cat "EBI_results/16S_rRNA.fasta" >> "EBI_results/rRNA.fasta"

    echo "  23S sequences:"
    wget "https://www.ebi.ac.uk/metagenomics//projects/SRP004311/samples/"$run_name"/runs/"$sample_name"/results/versions/1.0/taxonomy/23S-rRNA-FASTA" >/dev/null 2>&1
    grep ">" "23S-rRNA-FASTA" | wc -l
    mv "23S-rRNA-FASTA" "EBI_results/23S_rRNA.fasta"
    cat "EBI_results/23S_rRNA.fasta" >> "EBI_results/rRNA.fasta"

    cd ../
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
export -f format_EBI_taxonomic_results

function run_graphlan_workflow {
    python src/run_graphlan_workflow.py \
        --taxonomy_file "results/"$1"/EBI_results/all_taxo_level_assigned_abundance_graphlan2_formatted_file.txt" \
        --output_dir "results/"$1"/EBI_results/graphlan_representations" \
        --api_key $3 \
        --gi_url $2
}
export -f run_graphlan_workflow

function download_EBI_functional_results {
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
    wget "https://www.ebi.ac.uk/metagenomics//projects/SRP004311/samples/"$run_name"/runs/"$sample_name"/results/versions/1.0/function/GOSlimAnnotations"
    mv "GOSlimAnnotations" "EBI_results/go_slim_annotations.csv"
    cd ../
    echo ""
}
export -f download_EBI_functional_results

function format_EBI_functional_results {
    sample_name=$1
    python src/format_EBI_functional_results.py \
        --ebi_functional_results "results/"$sample_name"/EBI_results/go_slim_annotations.csv" \
        --output_dir "results/"$sample_name"/EBI_results/"
}
export -f format_EBI_functional_results

if [[ ! -d results ]]; then
    mkdir results
fi

echo "Download input datasets"
echo "======================="
cd data
download_unarchive "SRR072232"
download_unarchive "SRR072233"
cd ../
echo ""

echo "Get number of rRNA sequences"
echo "============================"
cd results
get_rRNA_sequences_number "SRR072232" "SRS121012"
get_rRNA_sequences_number "SRR072233" "SRS121011"
cd ../
echo ""

echo "Download EBI taxonomic results"
echo "=============================="
cd results
download_EBI_taxonomic_results "SRR072232" "SRS121012"
download_EBI_taxonomic_results "SRR072233" "SRS121011"
cd ../
echo ""

echo "Format EBI taxonomic results"
echo "============================"
cat id.txt | parallel format_EBI_taxonomic_results {}
echo ""

echo "Run workflow to get graphlan representations"
echo "============================================"
cat id.txt | parallel run_graphlan_workflow {} $asaim_galaxy_instance_url $api_key_on_asaim_galaxy_instance
echo ""

echo "Download EBI functional results"
echo "==============================="
cd results
download_EBI_functional_results "SRR072232" "SRS121012"
download_EBI_functional_results "SRR072233" "SRS121011"
cd ../
echo ""

echo "Format EBI functional results"
echo "============================="
cat id.txt | parallel format_EBI_functional_results {}
echo ""
