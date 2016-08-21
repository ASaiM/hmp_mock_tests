#!/usr/bin/env bash
. src/misc.sh

function download_ref_genomes_and_data {
    cd data

    echo "Reference genomes"
    echo "-----------------"
    if [[ ! -d "reference_genomes" ]]; then
        mkdir "reference_genomes"
    fi

    cd "reference_genomes"
    python "../../src/download_extract_reference_genomes.py" \
        --exp_taxo_file "../expected_species_w_taxonomy.txt" \
        --protein_nb_file "../expected_species_w_protein_nb.txt"

    if [[ -f "reference_genomes.fna.gz" ]]; then
        rm "reference_genomes.fna.gz"
    fi
    cat *.fna.gz > "reference_genomes.fna.gz"
    cd ../
    echo ""

    echo "Reference rRNA sequences"
    echo "------------------------"
    if [[ ! -d "reference_rRNAs" ]]; then
        mkdir "reference_rRNAs"
    fi

    python "../src/download_extract_reference_rRNA.py" \
        --exp_taxo_file "expected_species_w_taxonomy.txt" \
        --reference_rRNA_file "reference_rRNAs/reference_rRNAs.fasta" \
        --rRNA_nb_file "expected_species_w_rRNA_nb.txt"

    echo "Reference proteins"
    echo "------------------"

    python "../src/download_format_reference_proteins.py" \
        --exp_taxo_file "expected_species_w_taxonomy.txt" \
        --reference_protein_file "reference_protein.txt"

    cd ../
}

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

function download_extract_refseq_uniref50_mapping {
    echo "Download and format RefSeq UniRef50 mapping"
    echo "-------------------------------------------"
    wget "ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/idmapping/idmapping_selected.tab.gz"
    gunzip "idmapping_selected.tab.gz"
    python src/extract_refseq_uniref50_mapping.py \
        --uniprot_mapping_file "idmapping_selected.tab" \
        --refseq_uniref50_mapping_file "data/refseq_uniref50_mapping.txt" \
        --reference_protein_file "data/reference_protein.txt"
    rm "idmapping_selected.tab"
    echo ""
}

function extract_mapped_proteins {
    echo $1
    samtools index "results/"$1"/mapping/4_map_with_bwa-mem_on_data_3_and_data_1_(mapped_reads_in_bam_format).bam"
    python src/extract_mapped_proteins.py \
        --mapping_file "results/"$1"/mapping/4_map_with_bwa-mem_on_data_3_and_data_1_(mapped_reads_in_bam_format).bam" \
        --reference_protein_file "data/reference_protein.txt" \
        --refseq_uniref50_mapping_file "data/refseq_uniref50_mapping.txt" \
        --uniref50_abund_file "results/"$1"/mapping/uniref50_abundance.txt" \
        --uniref50_abund_per_sp_file "results/"$1"/mapping/uniref50_abundance_per_species.txt" \
        --log "results/"$1"/mapping/uniref50_abundance_log.txt"
}
export -f extract_mapped_proteins

echo "Download reference genomes and extract some data"
echo "================================================"
download_ref_genomes_and_data

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

echo "Extract information on mapped proteins, UniRef50 gene families, GO slim terms"
echo "============================================================================="
download_extract_refseq_uniref50_mapping

echo "Extract mapped proteins and UniRef50 gene family abundances"
echo "-----------------------------------------------------------"
extract_mapped_proteins SRR072232
extract_mapped_proteins SRR072233
echo ""
