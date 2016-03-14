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

function extract_functional_characteristics {
    characteristics=$1
    filename=$2
    charact_nb=$3
    output_dir=$4
    more_abund_output_file=$output_dir"/"$charact_nb"_more_abund_"$characteristics".txt"
    python src/extract_functional_characteristics.py \
        --sample_name "SRR072232" \
        --sample_name "SRR072233" \
        --charact_input_file "results/SRR072232/asaim_results/"$filename \
        --charact_input_file "results/SRR072233/asaim_results/"$filename \
        --most_abundant_characteristics_to_extract $charact_nb \
        --more_abund_output_file $more_abund_output_file
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
extract_functional_characteristics "gene_families" \
    "normalized_table_for______________data_17_(humann2).tsv" 10 $output_dir 
extract_functional_characteristics "pathways" \
    "normalized_table_for______________data_19_(humann2).tsv" 10 $output_dir
Rscript src/plot_more_abund_func_charact.R $output_dir
