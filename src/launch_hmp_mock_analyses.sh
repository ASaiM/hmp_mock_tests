#!/usr/bin/env bash
. src/misc.sh

echo "##############################################################"
echo "# Get the input datasets and EBI result data and format them #"
echo "##############################################################"
./src/download_format_EBI_data.sh

echo "###########################################################"
echo "# Get reference genomes and mapped input datasets on them #"
echo "###########################################################"
./src/download_extract_map_reference_genomes.sh

echo "##########################################################################"
echo "# Launch ASaiM workflow on both datasets (this task takes several hours) #"
echo "##########################################################################"
./src/launch_asaim_workflow.sh


echo "###############################################################"
echo "# Export ASaiM workflow outputs (when the workflows are done) #"
echo "###############################################################"
./src/export_asaim_workflow_outputs.sh

echo "###############################################################"
echo "# Concatenate results (EBI one and ASaiM one) to compare them #"
echo "###############################################################"
./src/concatenate_results.sh