#!/bin/bash

function concatenate_ebi_asaim_taxonomic_results {
    sample_name=$1
    result_dir="results/"$sample_name
    output_dir=$result_dir"/concatenated_results"
    if [[ ! -d $output_dir ]]; then
        mkdir $output_dir
    fi

    python src/concatenate_ebi_asaim_taxonomic_results.py \
        --expected_taxonomy "data/expected_species_w_taxonomy.txt" \
        --asaim_result_dir $result_dir"/asaim_results" \
        --ebi_result_dir $result_dir"/EBI_results" \
        --output_dir $output_dir \
        --sample_name $sample_name
}

function plot_taxonomic_results {
    sample_name=$1
    Rscript src/plot_taxonomic_results.R \
        "results/"$sample_name"/concatenated_results"
}


echo "Concatenate EBI and ASaiM taxonomic results given expected taxonomy for each sample"
echo "==================================================================================="
concatenate_ebi_asaim_taxonomic_results "SRR072232"
concatenate_ebi_asaim_taxonomic_results "SRR072233"
echo ""

echo "Plot expected, EBI and ASaiM taxonomic results for each sample"
echo "=============================================================="
plot_taxonomic_results "SRR072232"
plot_taxonomic_results "SRR072233"
echo ""