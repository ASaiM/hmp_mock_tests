library(ade4)
library(ape)
library(vegan)

args<-commandArgs(TRUE)

output_dir = args[1]

analyse_abundance <- function(data, data_type){
    colnames(data) = c("Mapping-\nbased", "EBI", "ASaiM")

    # PCOA on distance matrix
    data_dist = vegdist(t(data))
    data_dist_pcoa = pcoa(data_dist)
    colnames(data_dist_pcoa$vectors) = c(paste('First axis (' , round(100*data_dist_pcoa$values$Relative_eig[1]), '%)', sep = ""), paste('Second axis (',
        round(100*data_dist_pcoa$values$Relative_eig[2]),'%)', sep = ""))

    pdf(paste(output_dir, "/", data_type,"_pcoa.pdf", sep = ""))
    par(mar=c(5,5,1,1))
    biplot(data_dist_pcoa)
    dev.off()

    # PCA
    data_pca = dudi.pca(data, scannf = FALSE, nf = 2)
    pdf(paste(output_dir, "/", data_type,"_pca.pdf", sep = ''))
    scatter(data_pca, clab.row = 0, posieig = "none", sub = paste('First axis (' ,
        round(100*data_pca$eig[1]/sum(data_pca$eig)), '%) - Second axis (',
        round(100*data_pca$eig[2]/sum(data_pca$eig)),'%)', sep = ''))
    dev.off()

    # Barplot
    data[data == 0] = NA
    pdf(paste(output_dir, "/", data_type,".pdf", sep = ""),width = 5, height = 5)
    par(las=2)
    par(mar=c(5,10,1,1))
    col = c("blue3","green3", "red")
    order = order(data[,1], decreasing = TRUE)#c(12,15,1,5,6,7,10,14,4,8,9,11,16,18,2,3,13,17,19)
    barplot(t(rev(data[order,])),
        width = c(1,1,0.5), col= col, xlab = "Relative abundances in percentage",
        beside=TRUE, horiz=TRUE, log = "x", cex.axis = 0.8, xlim = c(0.01, 50))
    legend("topright", legend = rev(c('ASaiM','EBI','Mapping-based')), fill = rev(col), cex = 0.7)
    dev.off()

}

family_abundances = read.table(paste(output_dir, "/family_abundance.txt", sep = ''), h = T, sep = '\t', row.names = 1)
analyse_abundance(family_abundances, "family_abundance")

species_abundances = read.table(paste(output_dir, "/species_abundance.txt", sep = ''), h = T, sep = '\t', row.names = 1)
analyse_abundance(species_abundances, "species_abundance")
