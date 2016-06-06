#!/usr/bin/env bash
image_update=true
if $image_update ; then
    echo "Get last version of each images..."

    SRR072232_result_dir="results/SRR072232/"
    SRR072233_result_dir="results/SRR072233/"
    concatenated_results_dir="results/concatenated_asaim_results/functional_results/"

    # Taxonomic results
    ## Mapping
    cp "results/SRR072232/mapping/22_plot_grouped_barplot_on_data_20_pdf_barplot.pdf" \
        "doc/images/SRR072232/mapping_expectation_barplot.pdf"
    cp "results/SRR072233/mapping/22_plot_grouped_barplot_on_data_20_pdf_barplot.pdf" \
        "doc/images/SRR072233/mapping_expectation_barplot.pdf"
    cp "results/SRR072232/mapping/23_plot_barplot_on_data_21_pdf_barplot.pdf" \
        "doc/images/SRR072232/ratio_mapping_expectation_barplot.pdf"
    cp "results/SRR072233/mapping/23_plot_barplot_on_data_21_pdf_barplot.pdf" \
        "doc/images/SRR072233/ratio_mapping_expectation_barplot.pdf"

    cp "results/SRR072232/concatenated_results/species_abundances.pdf" \
        "doc/images/SRR072232/species_abundances.pdf"
    cp "results/SRR072233/concatenated_results/species_abundances.pdf" \
        "doc/images/SRR072233/species_abundances.pdf"
    cp "results/SRR072232/concatenated_results/family_abundances.pdf" \
        "doc/images/SRR072232/concatenated_family_abundances.pdf"
    cp "results/SRR072233/concatenated_results/family_abundances.pdf" \
        "doc/images/SRR072233/concatenated_family_abundances.pdf"
    cp "results/SRR072232/concatenated_results/family_abundance_pcoa.pdf" \
        "doc/images/SRR072232/concatenated_family_abundance_pcoa.pdf"
    cp "results/SRR072233/concatenated_results/family_abundance_pcoa.pdf" \
        "doc/images/SRR072233/concatenated_family_abundance_pcoa.pdf"
        cp "results/SRR072232/concatenated_results/species_abundance_pcoa.pdf" \
            "doc/images/SRR072232/concatenated_species_abundance_pcoa.pdf"
        cp "results/SRR072233/concatenated_results/species_abundance_pcoa.pdf" \
            "doc/images/SRR072233/concatenated_species_abundance_pcoa.pdf"

    # Functional results
    ## Only ASaiM
    cp "results/concatenated_asaim_results/functional_results/raw_gene_families/7_plot_generic_x-y_plot_on_data_7_pdf_x-y_plot.pdf" \
        "doc/images/concatenated_asaim_results/functional_results/raw_gene_families.pdf"
    cp "results/concatenated_asaim_results/functional_results/raw_pathways/7_plot_generic_x-y_plot_on_data_7_pdf_x-y_plot.pdf" \
        "doc/images/concatenated_asaim_results/functional_results/raw_pathways.pdf"

    cp "results/concatenated_asaim_results/functional_results/taxonomically_related_gene_families/23_plot_generic_x-y_plot_on_data_22_pdf_x-y_plot.pdf" \
        "doc/images/concatenated_asaim_results/functional_results/taxonomically_related_gene_families.pdf"
    cp "results/concatenated_asaim_results/functional_results/taxonomically_related_pathways/23_plot_generic_x-y_plot_on_data_22_pdf_x-y_plot.pdf" \
        "doc/images/concatenated_asaim_results/functional_results/taxonomically_related_pathways.pdf"

    cp "results/concatenated_asaim_results/functional_results/biological_process/10_plot_grouped_barplot_on_data_9_pdf_barplot.pdf" \
        "doc/images/concatenated_asaim_results/functional_results/biological_process.pdf"
    cp "results/concatenated_asaim_results/functional_results/molecular_function/10_plot_grouped_barplot_on_data_9_pdf_barplot.pdf" \
        "doc/images/concatenated_asaim_results/functional_results/molecular_function.pdf"
    cp "results/concatenated_asaim_results/functional_results/cellular_component/10_plot_grouped_barplot_on_data_9_pdf_barplot.pdf" \
        "doc/images/concatenated_asaim_results/functional_results/cellular_component.pdf"

    # Concatenated GO slim terms
    cp "results/concatenated_go_slim_terms/biological_process_pca.pdf" \
        "doc/images/concatenated_go_slim_terms/biological_process_pca.pdf"
    cp "results/concatenated_go_slim_terms/cellular_component/24_plot_grouped_barplot_on_data_23_pdf_barplot.pdf" \
        "doc/images/concatenated_go_slim_terms/cellular_component_barplot.pdf"
    cp "results/concatenated_go_slim_terms/cellular_component_pca.pdf" \
        "doc/images/concatenated_go_slim_terms/cellular_component_pca.pdf"
    cp "results/concatenated_go_slim_terms/molecular_function_pca.pdf" \
        "doc/images/concatenated_go_slim_terms/molecular_function_pca.pdf"
fi


cd doc/report/

echo "Compile report"
pandoc -s report.md \
    -t latex \
    -o report.pdf \
    --template="bioinformatics_template.tex" \
    --bibliography="references.bib" \
    --csl="bioinformatics.csl" \
    -N
