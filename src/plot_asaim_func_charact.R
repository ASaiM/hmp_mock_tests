args<-commandArgs(TRUE)

output_dir = args[1]

gene_families_abundances = read.table(paste(output_dir, '/10_more_abund_gene_families.txt', sep = ''), h = T, sep = '\t')

pdf(paste(output_dir,'/10_more_abund_gene_families.pdf',sep=''),width = 5, height = 5)
par(las=2)
par(mar=c(5,15,1,1))
col = c("lightblue","darkblue")
order = order(gene_families_abundances[,2], decreasing = T)
barplot(t(rev(gene_families_abundances[order,c(2,3)])), col= col, 
    xlab = "Relative abundances (%)", beside=TRUE, horiz=TRUE, 
    cex.axis = 0.8, cex.name = 0.8, names.arg = gene_families_abundances[,1])
legend("topright", legend = rev(c('SRR072233','SRR072232')), fill = rev(col), cex = 0.7)
dev.off()

pathways_abundances = read.table(paste(output_dir, '/10_more_abund_pathways.txt', sep = ''), h = T, sep = '\t')

pdf(paste(output_dir,'/10_more_abund_pathways.pdf',sep=''),width = 5, height = 5)
par(las=2)
par(mar=c(5,15,1,1))
col = c("lightblue","darkblue")
order = order(pathways_abundances[,2], decreasing = T)
barplot(t(rev(pathways_abundances[order,c(2,3)])), col= col, 
    xlab = "Relative abundances (%)", beside=TRUE, horiz=TRUE, 
    cex.axis = 0.8, cex.name = 0.7, names.arg = pathways_abundances[,1])
legend("topright", legend = rev(c('SRR072233','SRR072232')), fill = rev(col), cex = 0.7)
dev.off()