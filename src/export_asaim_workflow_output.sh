#!/usr/bin/env bash
. src/misc.sh

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
    read_number=`grep -o ">" results/$sample_name/asaim_results/8_vsearch_dereplication_on_data_6.fasta | wc -l`
    python src/extract_unassigned_clades_perc.py \
        --metaphlan_output "results/"$sample_name"/asaim_results/9_profile_of_communities_on_data_8_(metaphlan).txt" \
        --read_number $read_number \
        --unassigned_clade_output_file "results/"$sample_name"/asaim_results/unassigned_clade_perc.txt"
}

function functional_results_comparison {
    charact_output_dir=$4"/"$1
    if [[ ! -d $charact_output_dir ]]; then
        mkdir $charact_output_dir
    fi
    python src/asaim_functional_results_comparison.py \
        --gi_url $2 \
        --api_key $3 \
        --characteristics $1 \
        --first_dataset "SRR072232" \
        --second_dataset "SRR072233" \
        --output_dir $charact_output_dir
}

echo "Export ASaiM workflow outputs"
echo "============================="
export_asaim_workflow_outputs "SRR072232" $asaim_galaxy_instance_url $api_key_on_asaim_galaxy_instance
export_asaim_workflow_outputs "SRR072233" $asaim_galaxy_instance_url $api_key_on_asaim_galaxy_instance
echo ""

echo "Extract percentage of unassigned clades with MetaPhlAn output"
echo "============================================================="
extract_unassigned_clades_perc "SRR072232"
extract_unassigned_clades_perc "SRR072233"
echo ""

echo "Compare functional resuls, taxonomically-related functional results and GO slim terms"
echo "====================================================================================="
output_dir="results/concatenated_samples/functional_results"
if [[ ! -d $output_dir ]]; then
    mkdir $output_dir
fi
python src/asaim_functional_results_comparison.py \
    --gi_url $2 \
    --api_key $3 \
    --first_dataset "SRR072232" \
    --second_dataset "SRR072233" \
    --output_dir $output_dir 