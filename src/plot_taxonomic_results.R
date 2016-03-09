args<-commandArgs(TRUE)

output_dir = args[1]

family_abundances = read.table(paste(output_dir, "/family_abundance.txt", sep = ''), h = T, sep = '\t', row.names = 1)
family_abundances[family_abundances == 0] = NA
#differences = cbind(family_abundances$ebi_abundance - family_abundances$expected,
#    family_abundances$asaim_abundance - family_abundances$expected)
#rownames(differences) = rownames(family_abundances)
#colnames(differences) = c("ebi", "asaim")

pdf(paste(output_dir, "/family_abundances.png", sep = ""),width = 5, height = 5)
par(las=2)
par(mar=c(5,9,1,1))
col = c("blue3","green3", "red")
order = c(12,15,1,5,6,7,10,14,4,8,9,11,16,18,2,3,13,17,19)
barplot(t(rev(family_abundances[order,])), 
    width = c(1,1,0.5), col= col, xlab = "Relative abundances in percentage", 
    beside=TRUE, horiz=TRUE, log = "x", cex.names=0.7, cex.axis = 0.8)
legend("topright", legend = rev(c('ASaiM','EBI','Expected')), fill = rev(col), cex = 0.75)
dev.off()

species_abundances = read.table(paste(output_dir, "/species_abundance.txt", sep = ''), h = T, sep = '\t', row.names = 1)
species_abundances[species_abundances == 0] = NA
png(paste(output_dir, "/species_abundances.png", sep = ""))
par(las=2)
par(mar=c(5,12,1,1))
col = c("blue3","red")
order = c(1,5,6,12,17,7,10,14,16,18,4,8,9,11,19,21,2,3,13,15,20,22)
barplot(t(rev(species_abundances[order,c(1,3)])), width = c(1,0.5), col= col, 
    xlab = "Relative abundances in percentage",
    beside=TRUE, horiz=TRUE, log = "x", cex.names=0.7, cex.axis = 0.8)
legend("topright", legend = rev(c('ASaiM','Expected')), fill = rev(col), cex = 0.75)
dev.off()
