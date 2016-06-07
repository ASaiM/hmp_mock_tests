library(ade4)
library(ape)
library(vegan)

args<-commandArgs(TRUE)

input_filepath = args[1]

data = read.table(input_filepath, sep = '\t', row.names = 1)
new_data = data[,c(1,3)]

print(vegdist(t(new_data)))
