library(ade4)

get_data <- function(type){
    input_filepath = paste('results/concatenated_samples/',type, 
        '/normalize_a_dataset_by_on_data_6_normalized_dataset.tabular', sep = '')

    l = list()
    l$data = read.table(input_filepath, sep = '\t')
    l$extracted_data = l$data[,c(3,4,5,6)]
    row.names(l$extracted_data) = l$data[,1]
    colnames(l$extracted_data) = c('SRR072232 (ASaiM)', 'SRR072232 (EBI)', 'SRR072233 (ASaiM)', 'SRR072233 (EBI)')

    l$pca <- dudi.pca(l$extracted_data, scannf = FALSE, nf = 2)
    l$order_1 = order(abs(l$pca$li[,1]),decreasing = T)
    l$order_axis1 = l$pca$li[l$order_1,]
    l$go_names_axis1 = l$data[l$order_1,2]

    l$order_2 = order(abs(l$pca$li[,2]),decreasing = T)
    l$order_axis2 = l$pca$li[l$order_2,]
    l$go_names_axis2 = l$data[l$order_2,2]
    return(l)
}

type = 'biological_process'
bp = get_data(type)
pdf(paste('results/concatenated_samples/', type, '/pca.pdf', sep = ''))
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
cc = get_data(type)
pdf(paste('results/concatenated_samples/', type, '/pca.pdf', sep = ''))
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
mf = get_data(type)
pdf(paste('results/concatenated_samples/', type, '/pca.pdf', sep = ''))
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