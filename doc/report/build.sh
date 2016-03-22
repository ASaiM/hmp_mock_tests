#!/usr/bin/env bash

SRR072232_result_dir="results/SRR072232/"
SRR072233_result_dir="results/SRR072233/"
concatenated_results_dir="results/concatenated_samples/"

cp $SRR072232_result_dir"/asaim_results/43_graphlan_on_data_33_image.png" \
    "doc/images/SRR072232/graphlan.png"
cp $SRR072233_result_dir"/asaim_results/43_graphlan_on_data_33_image.png" \
    "doc/images/SRR072233/graphlan.png"

cp $SRR072232_result_dir"/concatenated_results/species_abundances.pdf" \
    "doc/images/SRR072232/species_abundances.pdf"
cp $SRR072233_result_dir"/concatenated_results/species_abundances.pdf" \
    "doc/images/SRR072233/species_abundances.pdf"
cp $SRR072232_result_dir"/concatenated_results/family_abundances.pdf" \
    "doc/images/SRR072232/concatenated_family_abundances.pdf"
cp $SRR072233_result_dir"/concatenated_results/family_abundances.pdf" \
    "doc/images/SRR072233/concatenated_family_abundances.pdf"

cp $SRR072232_result_dir"/asaim_results/60_plot_generic_x-y_plot_on_data_53_pdf_x-y_plot.pdf" \
    "doc/images/SRR072232/gene_family_nb.pdf"
cp $SRR072232_result_dir"/asaim_results/58_plot_generic_x-y_plot_on_data_53_pdf_x-y_plot.pdf" \
    "doc/images/SRR072232/mean_gene_family_abundance.pdf"
cp $SRR072232_result_dir"/asaim_results/62_plot_generic_x-y_plot_on_data_54_pdf_x-y_plot.pdf" \
    "doc/images/SRR072232/pathway_nb.pdf"
cp $SRR072232_result_dir"/asaim_results/61_plot_generic_x-y_plot_on_data_54_pdf_x-y_plot.pdf" \
    "doc/images/SRR072232/mean_pathway_abundance.pdf"
cp $SRR072232_result_dir"/asaim_results/plot_prot_nb_gene_family_number.pdf" \
    "doc/images/SRR072232/gene_family_nb_protein_nb.pdf"
cp $SRR072232_result_dir"/asaim_results/plot_diff_prot_nb_gene_family_number.pdf" \
    "doc/images/SRR072232/diff_prot_nb_gene_family_number.pdf"

cp $SRR072233_result_dir"/asaim_results/plot_diff_prot_nb_gene_family_number.pdf" \
    "doc/images/SRR072233/diff_prot_nb_gene_family_number.pdf"

cp $SRR072232_result_dir"/asaim_results/64_plot_barplot_on_data_55_pdf_barplot.pdf" \
    "doc/images/SRR072232/molecular_functions.pdf"
cp $SRR072232_result_dir"/asaim_results/65_plot_barplot_on_data_56_pdf_barplot.pdf" \
    "doc/images/SRR072232/biological_processes.pdf"
cp $SRR072232_result_dir"/asaim_results/66_plot_barplot_on_data_57_pdf_barplot.pdf" \
    "doc/images/SRR072232/cellular_components.pdf"

cp $concatenated_results_dir"/gene_families/15_similar_charact_x_y_plot.pdf" \
    "doc/images/concatenated_samples/gene_families_SRR072232_SRR072233.pdf" 
cp $concatenated_results_dir"/pathways/15_similar_charact_x_y_plot.pdf" \
    "doc/images/concatenated_samples/pathways_SRR072232_SRR072233.pdf" 

cp $concatenated_results_dir"/gene_families/36_plot_diff_orga_abund_diff_charact_nb.pdf" \
    "doc/images/concatenated_samples/gene_family_nb.pdf" 
cp $concatenated_results_dir"/gene_families/42_plot_diff_orga_abund_diff_charat_mean_abund.pdf" \
    "doc/images/concatenated_samples/mean_gene_family_abundance.pdf" 
cp $concatenated_results_dir"/pathways/37_plot_diff_orga_abund_diff_charact_nb.pdf" \
    "doc/images/concatenated_samples/pathway_nb.pdf" 
cp $concatenated_results_dir"/pathways/42_plot_diff_orga_abund_diff_charat_mean_abund.pdf" \
    "doc/images/concatenated_samples/mean_pathway_abundance.pdf" 

cp $concatenated_results_dir"/biological_process/plot_grouped_barplot_on_data_7_pdf_barplot.pdf" \
    "doc/images/concatenated_samples/biological_process_barplot.pdf"
cp $concatenated_results_dir"/biological_process/pca.pdf" \
    "doc/images/concatenated_samples/biological_process_pca.pdf"
cp $concatenated_results_dir"/molecular_function/plot_grouped_barplot_on_data_7_pdf_barplot.pdf" \
    "doc/images/concatenated_samples/molecular_function_barplot.pdf"
cp $concatenated_results_dir"/molecular_function/pca.pdf" \
    "doc/images/concatenated_samples/molecular_function_pca.pdf"
cp $concatenated_results_dir"/cellular_component/plot_grouped_barplot_on_data_7_pdf_barplot.pdf" \
    "doc/images/concatenated_samples/cellular_component_barplot.pdf"
cp $concatenated_results_dir"/cellular_component/pca.pdf" \
    "doc/images/concatenated_samples/cellular_component_pca.pdf"


cd doc/report/

pandoc -s report.md \
    -t latex \
    -o report.pdf \
    --template="bioinformatics_template.tex" \
    --bibliography="references.bib" \
    --csl="bioinformatics.csl" \
    -N