#!/bin/bash

function launch_asaim_workflow {
    sample_name=$1
    python src/launch_asaim_workflow.py \
        --api_key "ee9664590ef964b6fc48fadd689e11bb" \
        --gi_url "http://172.21.23.6:8080/" \
        --sample_name $sample_name
}

echo "Launch ASaiM workflow"
echo "====================="
launch_asaim_workflow "SRR072232"
#launch_asaim_workflow "SRR072233"
echo ""