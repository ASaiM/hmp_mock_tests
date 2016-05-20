library(ade4)

args<-commandArgs(TRUE)

output_dir = args[1]

family_abundances = read.table(paste(output_dir, "/family_abundance.txt", sep = ''), h = T, sep = '\t', row.names = 1)
family_abundances[family_abundances == 0] = NA
#differences = cbind(family_abundances$ebi_abundance - family_abundances$expected,
#    family_abundances$asaim_abundance - family_abundances$expected)
#rownames(differences) = rownames(family_abundances)
#colnames(differences) = c("ebi", "asaim")

pdf(paste(output_dir, "/family_abundances.pdf", sep = ""),width = 5, height = 5)
par(las=2)
par(mar=c(5,10,1,1))
col = c("blue3","green3", "red")
order = order(family_abundances[,1], decreasing = TRUE)#c(12,15,1,5,6,7,10,14,4,8,9,11,16,18,2,3,13,17,19)
barplot(t(rev(family_abundances[order,])), 
    width = c(1,1,0.5), col= col, xlab = "Relative abundances in percentage", 
    beside=TRUE, horiz=TRUE, log = "x", cex.axis = 0.8, xlim = c(0.01, 50))
legend("topright", legend = rev(c('ASaiM','EBI','Mapping-based')), fill = rev(col), cex = 0.7)
dev.off()

species_abundances = read.table(paste(output_dir, "/species_abundance.txt", sep = ''), h = T, sep = '\t', row.names = 1)
species_abundances[species_abundances == 0] = NA
pdf(paste(output_dir, "/species_abundances.pdf", sep = ""))
par(las=2)
par(mar=c(5,16,1,1))
col = c("blue3","red")
order = order(species_abundances[,1], decreasing = TRUE)#c(1,5,6,12,17,7,10,14,16,18,4,8,9,11,19,21,2,3,13,15,20,22)
barplot(t(rev(species_abundances[order,c(1,3)])), width = c(1,0.5), col= col, 
    xlab = "Relative abundances in percentage",
    beside=TRUE, horiz=TRUE, log = "x", cex.axis = 0.8, xlim = c(0.01, 50))
legend("topright", legend = rev(c('ASaiM','Mapping-based')), fill = rev(col), cex = 0.75)
dev.off()

family_abundances = read.table(paste(output_dir, "/family_abundance.txt", sep = ''), h = T, sep = '\t', row.names = 1)
colnames(family_abundances) = c("Mapping-based", "EBI", "ASaiM")
observed_family_abundances = family_abundances[family_abundances[,2] > 0 & family_abundances[,3] >0, ]
family_abundances_pca = dudi.pca(observed_family_abundances, scannf = FALSE, nf = 2)


pdf(paste(output_dir, "/family_abundance_pca.pdf", sep = ''))
scatter(family_abundances_pca, clab.row = 0, posieig = "none", sub = paste('First axis (' ,
    round(100*family_abundances_pca$eig[1]/sum(family_abundances_pca$eig)), '%) - Second axis (', 
    round(100*family_abundances_pca$eig[2]/sum(family_abundances_pca$eig)),'%)', sep = ''))
dev.off()

print("Correlation between first axis and total abundance")
print(cor.test(family_abundances_pca$li[,1],apply(observed_family_abundances,1,sum)))