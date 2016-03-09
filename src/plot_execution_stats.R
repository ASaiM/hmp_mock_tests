args<-commandArgs(TRUE)

output_dir = args[1]

execution_time = read.table(paste(output_dir, '/execution_time.txt', sep = ''), 
    sep = "\t", h = T)
execution_time$start = strptime(execution_time$start, "%Y-%m-%d %H:%M:%OS")
execution_time$stop = strptime(execution_time$stop, "%Y-%m-%d %H:%M:%OS")
time_diff = execution_time$stop - execution_time$start
time_diff_in_min = as.numeric(time_diff)/60
time_diff_in_h = time_diff_in_min/60
min = 60*(as.numeric(time_diff_in_h) %% 1)
formatted_time_diff_in_h = paste(floor(time_diff_in_h),"h", min, sep = '')

time_diff_matrix = cbind.data.frame(time_diff, time_diff_in_min, time_diff_in_h, formatted_time_diff_in_h)
colnames(time_diff_matrix) = c('diff_s','diff_min','diff_h', 'formatted_time_diff_in_h')
row.names(time_diff_matrix) = execution_time$process
print(time_diff_matrix)