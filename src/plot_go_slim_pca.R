library(ade4)
library(ape)
library(vegan)

get_data <- function(type){
    input_filepath = paste('results/concatenated_go_slim_terms/',type,
        '/23_normalize_a_dataset_by_on_data_22_normalized_dataset.tabular', sep = '')

    l = list()
    l$data = read.table(input_filepath, sep = '\t', h = F)

    l$extracted_data = l$data[,c(3,4,5,6)]
    row.names(l$extracted_data) = l$data[,1]
    colnames(l$extracted_data) = c('SRR072232\nwith ASaiM', 'SRR072232\nwith EBI', 'SRR072233\nwith ASaiM', 'SRR072233\nwith EBI')

    l$pca <- dudi.pca(l$extracted_data, scannf = FALSE, nf = 2)
    l$order_1 = order(abs(l$pca$li[,1]),decreasing = T)
    l$order_axis1 = l$pca$li[l$order_1,]
    l$go_names_axis1 = l$data[l$order_1,2]

    l$order_2 = order(abs(l$pca$li[,2]),decreasing = T)
    l$order_axis2 = l$pca$li[l$order_2,]
    l$go_names_axis2 = l$data[l$order_2,2]

    #print("Correlation of first axis with total abundance")
    #print(cor.test(l$pca$li[,1],apply(l$extracted_data,1,sum)))

    l$dist = vegdist(t(l$extracted_data))
    l$dist_pcoa = pcoa(l$dist)

    print(l$dist)

    colnames(l$dist_pcoa$vectors)[c(1,2)] = c(paste('First axis (' , round(100*l$dist_pcoa$values$Relative_eig[1]), '%)', sep = ""),
        paste('Second axis (', round(100*l$dist_pcoa$values$Relative_eig[2]),'%)', sep = ""))

    pdf(paste('results/concatenated_go_slim_terms/', type, "_pcoa.pdf", sep = ""))
    par(mar=c(5,5,1,1))
    biplot(l$dist_pcoa)
    dev.off()

    return(l)
}


type = 'biological_process'
print(type)
bp = get_data(type)
pdf(paste('results/concatenated_go_slim_terms/', type, '_pca.pdf', sep = ''))
scatter(bp$pca, clab.row = 0, posieig = "none", sub = paste('First axis (' ,
    round(100*bp$pca$eig[1]/sum(bp$pca$eig)), '%) - Second axis (',
    round(100*bp$pca$eig[2]/sum(bp$pca$eig)),'%)', sep = ''))
text(bp$order_axis1[1,1],bp$order_axis1[1,2], label = bp$go_names_axis1[1], pos = 4)
text(bp$order_axis1[2,1],bp$order_axis1[2,2], label = bp$go_names_axis1[2], pos = 3)
text(bp$order_axis1[3,1],bp$order_axis1[3,2], label = bp$go_names_axis1[3], pos = 3)
text(bp$order_axis1[4,1],bp$order_axis1[4,2], label = bp$go_names_axis1[4], pos = 2)

text(bp$order_axis2[1,1],bp$order_axis2[1,2], label = bp$go_names_axis2[1], pos = 3)
text(bp$order_axis2[2,1],bp$order_axis2[2,2], label = bp$go_names_axis2[2], pos = 3)
text(bp$order_axis2[4,1],bp$order_axis2[4,2], label = bp$go_names_axis2[4], pos = 3)
dev.off()

type = 'cellular_component'
print(type)
cc = get_data(type)
pdf(paste('results/concatenated_go_slim_terms/', type, '_pca.pdf', sep = ''))
scatter(cc$pca, clab.row = 0, posieig = "none", sub = paste('First axis (' ,
    round(100*cc$pca$eig[1]/sum(cc$pca$eig)), '%) - Second axis (',
    round(100*cc$pca$eig[2]/sum(cc$pca$eig)),'%)', sep = ''))
text(cc$order_axis1[1,1],cc$order_axis1[1,2], label = cc$go_names_axis1[1], pos = 4)
text(cc$order_axis1[2,1],4.1, label = cc$go_names_axis1[2], pos = 1)
text(cc$order_axis1[3,1],-2.3, label = cc$go_names_axis1[3], pos = 3)
#text(cc$order_axis1[4,1],cc$order_axis1[4,2], label = cc$go_names[4], pos = 3)
#text(cc$order_axis1[5,1],cc$order_axis1[5,2], label = cc$go_names[5], pos = 3)
dev.off()

type = 'molecular_function'
print(type)
mf = get_data(type)
pdf(paste('results/concatenated_go_slim_terms/', type, '_pca.pdf', sep = ''))
scatter(mf$pca, clab.row = 0, posieig = "none", sub = paste('First axis (' ,
    round(100*mf$pca$eig[1]/sum(mf$pca$eig)), '%) - Second axis (',
    round(100*mf$pca$eig[2]/sum(mf$pca$eig)),'%)', sep = ''))
text(mf$order_axis1[1,1],mf$order_axis1[1,2], label = mf$go_names_axis1[1], pos = 4)
text(mf$order_axis1[2,1],mf$order_axis1[2,2], label = mf$go_names_axis1[2], pos = 1)
text(mf$order_axis1[3,1],mf$order_axis1[3,2], label = mf$go_names_axis1[3], pos = 3)
text(mf$order_axis1[4,1],mf$order_axis1[4,2], label = mf$go_names_axis1[4], pos = 2)
text(mf$order_axis1[5,1],mf$order_axis1[5,2], label = mf$go_names_axis1[5], pos = 3)
text(mf$order_axis1[6,1],mf$order_axis1[6,2], label = mf$go_names_axis1[6], pos = 3)
text(mf$order_axis1[7,1],mf$order_axis1[7,2], label = mf$go_names_axis1[7], pos = 3)
dev.off()
