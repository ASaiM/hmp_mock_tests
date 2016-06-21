plot_nb <- function(data, output_file){
    xlim = c(0, max(c(data[,'7'], data[,5])))

    pdf(output_file)
    par(mar=c(5,5,1,1))
    plot(data[,'7'], data[,5], xlab = 'Median protein number', 
        ylab = 'Number of found gene families', pch = 21, xlim = xlim, ylim = xlim)
    dev.off()
}

plot_diff_nb <- function(data, output_file){
    pdf(output_file)
    par(mar=c(5,5,1,1))
    plot(data[,1], (data[,5]-data[,'7']), xlab = 'Relative abundance of species (percentage)', 
        ylab = 'Difference between observed gene family number and expected protein number', 
        pch = 21, log = 'x')
    abline(h = 0, col = 'blue')
    dev.off()
}

compute_correlation <- function(data, col1, col2, name){
    print(paste("Correlation: ", name))
    print(cor.test(data[,col1],data[,col2]))
}

expected_species_protein_nb_median = read.table("data/expected_species_w_protein_nb.txt", 
    sep = "\t", row.names = 1)
row.names(expected_species_protein_nb_median) = gsub(" ", "_", row.names(expected_species_protein_nb_median))

SRR072232_gene_families = read.table('results/SRR072232/asaim_results/53_group_on_data_45.tabular',
    sep = '\t', row.names = 1)
SRR072232_gene_families[,'7'] = expected_species_protein_nb_median[row.names(SRR072232_gene_families),]
compute_correlation(SRR072232_gene_families, 1, 2, "SRR072232, species abundances vs mean gene family abundances")
#compute_correlation(SRR072232_gene_families, 1, 5, "SRR072232, species abundances vs gene family number")
compute_correlation(SRR072232_gene_families, '7', 5, "SRR072232, prot number vs gene family number")
plot_nb(SRR072232_gene_families, 'results/SRR072232/additional_results/plot_prot_nb_gene_family_number.pdf')
plot_diff_nb(SRR072232_gene_families, 'results/SRR072232/additional_results/plot_diff_prot_nb_gene_family_number.pdf')

SRR072233_gene_families = read.table('results/SRR072233/asaim_results/53_group_on_data_45.tabular',
    sep = '\t', row.names = 1)
SRR072233_gene_families[,'7'] = expected_species_protein_nb_median[row.names(SRR072233_gene_families),]
compute_correlation(SRR072233_gene_families, 1, 3, "SRR072233, species abundances vs mean gene family abundances")
#compute_correlation(SRR072233_gene_families, 1, 5, "SRR072233, species abundances vs gene family number")
compute_correlation(SRR072233_gene_families, '7', 5, "SRR072233, prot number vs gene family number")
plot_nb(SRR072233_gene_families, 'results/SRR072233/additional_results/plot_prot_nb_gene_family_number.pdf')
plot_diff_nb(SRR072233_gene_families, 'results/SRR072233/additional_results/plot_diff_prot_nb_gene_family_number.pdf')

SRR072232_pathways = read.table('results/SRR072232/asaim_results/54_group_on_data_47.tabular',
    sep = '\t', row.names = 1)
compute_correlation(SRR072232_pathways, 1, 2, "SRR072232, species abundances vs mean pathway abundances")
#compute_correlation(SRR072232_pathways, 1, 5, "SRR072232, species abundances vs pathway number")

SRR072233_pathways = read.table('results/SRR072233/asaim_results/54_group_on_data_47.tabular',
    sep = '\t', row.names = 1)
compute_correlation(SRR072233_pathways, 1, 2, "SRR072233, species abundances vs mean pathway abundances")
#compute_correlation(SRR072233_pathways, 1, 5, "SRR072233, species abundances vs pathway number")

#concatenated_gene_families = read.table('results/concatenated_samples/gene_families/41_compute_on_data_40.tabular',
#    sep = '\t', row.names = 1)
#compute_correlation(concatenated_gene_families, 1, 5, "SRR072233, species abundances vs mean gene family abundances")
#compute_correlation(concatenated_gene_families, 1, 2, "SRR072232, species abundances vs gene family number")

#concatenated_pathways = read.table('results/concatenated_samples/pathways/41_compute_on_data_40.tabular',
#    sep = '\t', row.names = 1)
#compute_correlation(concatenated_pathways, 1, 5, "SRR072233, species abundances vs mean pathway abundances")
