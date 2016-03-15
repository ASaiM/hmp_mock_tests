#!/bin/bash

function export_asaim_workflow_outputs {
    sample_name=$1
    python src/export_history_datasets.py \
        --api_key $3 \
        --gi_url $2 \
        --sample_name $sample_name \
        --output_dir "results/"$sample_name"/asaim_results/" 
}

function extract_unassigned_clades_perc {
    sample_name=$1
    read_number=`grep -o ">" results/$sample_name/asaim_results/vsearch_dereplication_on_data_6.fasta | wc -l`
    python src/extract_unassigned_clades_perc.py \
        --metaphlan_output "results/"$sample_name"/asaim_results/profile_of_communities_on_data_8_(metaphlan).txt" \
        --read_number $read_number \
        --unassigned_clade_output_file "results/"$sample_name"/asaim_results/unassigned_clade_perc.txt"
}

function compare_humann2_output {
    charact_output_dir=$4"/"$1
    if [[ ! -d $charact_output_dir ]]; then
        mkdir $charact_output_dir
    fi
    python src/compare_humann2_output.py \
        --gi_url $2 \
        --api_key $3 \
        --characteristics $1 \
        --sample_name "SRR072232" \
        --sample_name "SRR072233" \
        --output_dir $charact_output_dir
}

echo "Export ASaiM workflow outputs"
echo "============================="
export_asaim_workflow_outputs "SRR072232" $1 $2
export_asaim_workflow_outputs "SRR072233" $1 $2
echo ""

echo "Extract percentage of unassigned clades with MetaPhlAn output"
echo "============================================================="
extract_unassigned_clades_perc "SRR072232"
extract_unassigned_clades_perc "SRR072233"
echo ""

echo "Extract more abundant gene families and pathways and plot comparison"
echo "===================================================================="
output_dir="results/concatenated_samples"
if [[ ! -d $output_dir ]]; then
    mkdir $output_dir
fi
echo "Gene families"
echo "-------------"
compare_humann2_output "gene_families"  $1 $2 $output_dir 
echo "Pathways"
echo "--------"
compare_humann2_output "pathways"  $1 $2 $output_dir