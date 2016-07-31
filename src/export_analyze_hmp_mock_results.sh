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
function analyze_rDNA_sequences {
  sample_name=$1
  echo "$sample_name"
  echo "----------"

  echo "Extract proportion of eukaryotic rRNA sequences in ASaiM results"
  python src/extract_eukaryotic_rRNA_seq_prop.py \
    --sortmerna_euk_db "data/sortmerna_euk.fasta" \
    --asaim_rrna_blast_report "results/"$sample_name"/asaim_results/12_alignments_on_data_7_(blast).tabular"
  echo ""

  echo "Compare EBI rRNA sequences and ASaiM rRNA sequences"
  python src/compare_ebi_asaim_rrna_sequences.py \
    --ebi_rrna_seq "results/"$sample_name"/EBI_results/rRNA.fasta" \
    --asaim_rrna_seq "results/"$sample_name"/asaim_results/10_aligned_reads_on_data_7_(fasta).fasta" \
    --asaim_non_rrna_seq "results/"$sample_name"/asaim_results/11_rejected_reads_on_data_7_(fasta).fasta"
  echo ""

  echo "Check ASaiM rRNA sequences"

  echo "  Run SortMeRNA (same parameters) with reference rRNA sequences"
  reference_rRNAs_dir="data/reference_rRNAs/"
  sortmerna \
    --ref $reference_rRNAs_dir"/reference_rRNAs.fasta",$reference_rRNAs_dir"/reference_rRNAs.idx" \
    --reads "results/"$sample_name"/asaim_results/7_vsearch_dereplication_on_data_5.fasta" \
    --aligned "results/"$sample_name"/supp_results/aligned_ref_rrna" \
    --fastx \
    --blast "1 cigar qcov qstrand" \
    --best 1 \
    --min_lis 2 \
    -e 1.0 \
    --match 2 \
    --mismatch -3 \
    --gap_open 5 \
    --gap_ext 2 \
    -N -3

  echo "  Compare results to the one obtained with ASaiM"
  python src/compare_raw_and_ref_sortmerna_results.py \
    --raw_rrna_seq "results/"$sample_name"/asaim_results/10_aligned_reads_on_data_7_(fasta).fasta"\
    --ref_rrna_seq "results/"$sample_name"/supp_results/aligned_ref_rrna.fasta"


}

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

echo "Analyze rDNA sequences"
echo "======================"
supp_results="results/SRR072232/supp_results/"
if [[ ! -d $supp_results ]]; then
  mkdir -p $supp_results
fi

supp_results="results/SRR072233/supp_results/"
if [[ ! -d $supp_results ]]; then
  mkdir -p $supp_results
fi

echo "Download SortMeRNA eukaryotic databases"
echo "---------------------------------------"
cd "data/"
wget "https://raw.githubusercontent.com/biocore/sortmerna/master/rRNA_databases/silva-euk-18s-id95.fasta"
cat "silva-euk-18s-id95.fasta" > "sortmerna_euk.fasta"
rm "silva-euk-18s-id95.fasta"
wget "https://raw.githubusercontent.com/biocore/sortmerna/master/rRNA_databases/silva-euk-28s-id98.fasta"
cat "silva-euk-28s-id98.fasta" >> "sortmerna_euk.fasta"
rm "silva-euk-28s-id98.fasta"
cd ../
echo ""

echo "Prepare reference rRNA databases to be usable by SortMeRNA"
echo "----------------------------------------------------------"
reference_rRNAs_dir="data/reference_rRNAs/"
indexdb_rna \
  --ref $reference_rRNAs_dir"/reference_rRNAs.fasta",$reference_rRNAs_dir"/reference_rRNAs.idx" \
  --max_pos 10000 \
  -L 18

echo "Analyze rDNA sequences"
echo "----------------------"
analyze_rDNA_sequences "SRR072232"
analyze_rDNA_sequences "SRR072233"
echo ""

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
