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

start = execution_time[execution_time$process == 'all', ]$start
stop = execution_time[execution_time$process == 'all', ]$stop

execution_stats = read.table('results/formatted_stat_for_46720.txt', sep = ' ')
execution_stats$V5 = strptime(paste(execution_stats$V1, execution_stats$V2), "%Y-%m-%d %H:%M:%OS")

interesting_time_range = execution_stats[execution_stats$V5 >= start & execution_stats$V5 <= stop,]
print("%CPU")
print(min(interesting_time_range$V3))
print(mean(interesting_time_range$V3))
print(max(interesting_time_range$V3))
print("Size")
print(min(interesting_time_range$V4))
print(mean(interesting_time_range$V4))
print(max(interesting_time_range$V4))