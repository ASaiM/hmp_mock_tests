#!/bin/bash

function launch_asaim_workflow {
    sample_name=$1
    python src/launch_asaim_workflow.py \
        --api_key $3 \
        --gi_url $2 \
        --sample_name $sample_name
}

echo "Launch ASaiM workflow"
echo "====================="
launch_asaim_workflow "SRR072232" $1 $2
launch_asaim_workflow "SRR072233" $1 $2
echo ""