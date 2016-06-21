#!/usr/bin/env bash
. src/misc.sh

if [ ! -d "logs" ]; then
    mkdir "logs"
fi

echo "##############################################################"
echo "# Get the input datasets and EBI result data and format them #"
echo "##############################################################"
./src/download_format_EBI_data.sh > logs/download_format_EBI_data

echo "###########################################################"
echo "# Get reference genomes and mapped input datasets on them #"
echo "###########################################################"
./src/download_extract_map_reference_genomes.sh > logs/download_extract_map_reference_genomes &

echo "##########################################################################"
echo "# Launch ASaiM workflow on both datasets (this task takes several hours) #"
echo "##########################################################################"
function launch_asaim_workflow {
    sample_name=$1
    python src/launch_asaim_workflow.py \
        --api_key $3 \
        --gi_url $2 \
        --sample_name $sample_name \
        > "logs/launch_asaim_workflow_"$1
}
export -f launch_asaim_workflow

cat id.txt | parallel launch_asaim_workflow {} $asaim_galaxy_instance_url $api_key_on_asaim_galaxy_instance
echo ""
