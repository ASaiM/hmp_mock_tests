#!/usr/bin/env bash
. src/misc.sh


function launch_mapping_workflow {
    sample_name=$1
    result_dir="results/"$sample_name
    output_dir=$result_dir"/mapping"
    if [[ ! -d $output_dir ]]; then
        mkdir $output_dir
    fi

    python src/launch_mapping_workflow.py \
        --api_key $3 \
        --gi_url $2 \
        --sample_name $sample_name \
        --output_dir $output_dir

    Rscript src/compute_distance_targeted_mapping_abundance.R $output_dir"/20_join_two_datasets_on_data_7_and_data_19.tabular"
}
export -f launch_mapping_workflow

function format_mapping_results {
    python src/format_mapping_results.py \
        --mapping_results "results/"$1"/mapping/19_normalize_a_dataset_by_on_data_18_normalized_dataset.tabular" \
        --expected_taxonomy "data/expected_species_w_taxonomy.txt" \
        --output_dir "results/"$1"/mapping/"
}
export -f format_mapping_results

function run_graphlan_workflow {
    python src/run_graphlan_workflow.py \
        --taxonomy_file "results/"$1"/mapping/graphlan2_formatted_mapping_results.txt" \
        --output_dir "results/"$1"/mapping/graphlan_representations" \
        --api_key $3 \
        --gi_url $2
}
export -f run_graphlan_workflow

echo "Download reference genomes and extract some data"
echo "================================================"
cd data

if [[ ! -d "reference_genomes" ]]; then
    mkdir "reference_genomes"
fi

cd "reference_genomes"
python "../../src/donwload_extract_reference_genomes.py" \
    --exp_taxo_file "../expected_species_w_taxonomy.txt" \
    --protein_nb_file "../expected_species_w_protein_nb.txt"

if [[ -f "reference_genomes.fna.gz" ]]; then
    rm "reference_genomes.fna.gz"
fi
cat *.fna.gz > "reference_genomes.fna.gz"
cd ../../
echo ""

echo "Map raw sequences on references genomes and extract abundance information"
echo "========================================================================="
cat id.txt | parallel launch_mapping_workflow {} $asaim_galaxy_instance_url $api_key_on_asaim_galaxy_instance
echo ""

echo "Format mapping to get full taxonomy and nice representation"
echo "==========================================================="
cat id.txt | parallel format_mapping_results {}
echo ""

echo "Run workflow to get graphlan representations"
echo "============================================"
cat id.txt | parallel run_graphlan_workflow {} $asaim_galaxy_instance_url $api_key_on_asaim_galaxy_instance
echo ""
