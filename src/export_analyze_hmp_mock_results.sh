#!/usr/bin/env bash
. src/misc.sh

echo "###############################################################"
echo "# Export ASaiM workflow outputs (when the workflows are done) #"
echo "###############################################################"
function export_asaim_workflow_outputs {
    sample_name=$1
    python src/export_history_datasets.py \
        --api_key $3 \
        --gi_url $2 \
        --sample_name $sample_name \
        --output_dir "results/"$sample_name"/asaim_results/"
}
export -f export_asaim_workflow_outputs

function extract_unassigned_clades_perc {
    sample_name=$1
    read_number=`grep -o ">" results/$sample_name/asaim_results/8_vsearch_dereplication_on_data_6.fasta | wc -l`
    python src/extract_unassigned_clades_perc.py \
        --metaphlan_output "results/"$sample_name"/asaim_results/9_profile_of_communities_on_data_8_(metaphlan).txt" \
        --read_number $read_number \
        --unassigned_clade_output_file "results/"$sample_name"/asaim_results/unassigned_clade_perc.txt"
}
export -f extract_unassigned_clades_perc

function run_graphlan_workflow {
    python src/run_graphlan_workflow.py \
        --taxonomy_file "results/"$1"/asaim_results/10_profile_of_communities_on_data_8_(metaphlan).tabular" \
        --output_dir "results/"$1"/asaim_results/graphlan_representations" \
        --api_key $3 \
        --gi_url $2
}
export -f run_graphlan_workflow

echo "Export ASaiM workflow outputs"
echo "============================="
cat id.txt | parallel export_asaim_workflow_outputs {} $asaim_galaxy_instance_url $api_key_on_asaim_galaxy_instance
echo ""

echo "Extract percentage of unassigned clades with MetaPhlAn output"
echo "============================================================="
cat id.txt | parallel extract_unassigned_clades_perc {}
echo ""

echo "Run workflow to get graphlan representations"
echo "============================================"
cat id.txt | parallel run_graphlan_workflow {} $asaim_galaxy_instance_url $api_key_on_asaim_galaxy_instance
echo ""

echo "Compare functional resuls, taxonomically-related functional results and GO slim terms"
echo "====================================================================================="
output_dir="results/concatenated_asaim_results/functional_results"
if [[ ! -d $output_dir ]]; then
    mkdir -p $output_dir
fi
python src/compare_asaim_functional_results.py \
    --gi_url $asaim_galaxy_instance_url \
    --api_key $api_key_on_asaim_galaxy_instance \
    --first_dataset "SRR072232" \
    --second_dataset "SRR072233" \
    --output_dir $output_dir

echo "Compute correlation and plot additional representation for taxonomically-related functional results"
echo "==================================================================================================="
output_dir="results/SRR072232/additional_results"
if [[ ! -d $output_dir ]]; then
    mkdir -p $output_dir
fi
output_dir="results/SRR072233/additional_results"
if [[ ! -d $output_dir ]]; then
    mkdir -p $output_dir
fi
Rscript src/compute_plot_correlation.R


echo "###############################################################"
echo "# Concatenate results (EBI one and ASaiM one) to compare them #"
echo "###############################################################"
function concatenate_ebi_asaim_taxonomic_results {
    sample_name=$1
    result_dir="results/"$sample_name
    output_dir=$result_dir"/concatenated_results"
    if [[ ! -d $output_dir ]]; then
        mkdir $output_dir
    fi

    python src/concatenate_ebi_asaim_taxonomic_results.py \
        --expected_taxonomy $result_dir"/mapping/formatted_mapping_results.txt" \
        --asaim_result_dir "results/"$sample_name"/asaim_results" \
        --ebi_result_dir $result_dir"/EBI_results" \
        --output_dir $output_dir
}
export -f concatenate_ebi_asaim_taxonomic_results

function plot_taxonomic_results {
    sample_name=$1
    Rscript src/plot_taxonomic_results.R \
        "results/"$sample_name"/concatenated_results"
}
export -f plot_taxonomic_results

function concatenate_go_slim_terms {
    output_dir="results/concatenated_go_slim_terms/"
    if [[ ! -d $output_dir ]]; then
        mkdir $output_dir
    fi

    python src/concatenate_go_slim_terms.py \
        --gi_url $1 \
        --api_key $2 \
        --output_dir $output_dir
    Rscript src/plot_go_slim_pca.R
}
export -f concatenate_go_slim_terms

echo "Concatenate EBI and ASaiM taxonomic results given expected taxonomy for each sample"
echo "==================================================================================="
cat id.txt | parallel concatenate_ebi_asaim_taxonomic_results {}
echo ""

echo "Plot expected, EBI and ASaiM taxonomic results for each sample"
echo "=============================================================="
cat id.txt | parallel plot_taxonomic_results {}
echo ""

echo "Concatenate EBI and ASaiM GO slim terms results"
echo "==============================================="
concatenate_go_slim_terms $asaim_galaxy_instance_url $api_key_on_asaim_galaxy_instance
echo ""
