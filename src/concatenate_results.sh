#!/usr/bin/env bash
. src/misc.sh

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


function concatenate_ebi_asaim_functional_results {
    sample_name=$1
    result_dir="results/"$sample_name
    output_dir=$result_dir"/concatenated_results"
    if [[ ! -d $output_dir ]]; then
        mkdir $output_dir
    fi

    python src/concatenate_ebi_asaim_functional_results.py \
        --asaim_result_dir $result_dir"/asaim_results" \
        --ebi_result_dir $result_dir"/EBI_results" \
        --output_dir $output_dir \
        --gi_url $2 \
        --api_key $3
}

function concatenate_both_samples_functional_results {
    output_dir="results/concatenated_samples/"
    python src/concatenate_both_samples_functional_results.py \
        --gi_url $1 \
        --api_key $2 \
        --sample1_dir "results/SRR072232/concatenated_results" \
        --sample2_dir "results/SRR072233/concatenated_results" \
        --sample1_name "SRR072232" \
        --sample2_name "SRR072233" \
        --output_dir $output_dir
    Rscript src/plot_go_slim_pca.R
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

echo "Concatenate EBI and ASaiM functional results (GO slim terms)"
echo "============================================================"
echo "SRR072232"
echo "---------"
concatenate_ebi_asaim_functional_results "SRR072232" $asaim_galaxy_instance_url $api_key_on_asaim_galaxy_instance
echo "SRR072233"
echo "---------"
concatenate_ebi_asaim_functional_results "SRR072233" $asaim_galaxy_instance_url $api_key_on_asaim_galaxy_instance
echo ""
echo "All samples"
echo "-----------"
concatenate_both_samples_functional_results $asaim_galaxy_instance_url $api_key_on_asaim_galaxy_instance
echo ""