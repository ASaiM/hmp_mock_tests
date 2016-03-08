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