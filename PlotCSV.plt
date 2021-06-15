# use in the format from within gnuplot:
# call 'PlotCSV.plt' '<ReletivePath/to/something.csv>' <Index of first Column to plot> <Index of last Column to plot>

set datafile separator comma

set autoscale xy

set xlabel "Sample"
set ylabel "Raw LSB"

set title sprintf("%s",ARGV[1])
set title font "Sans,14"
set terminal wxt size 1500, 600

set key autotitle columnhead width 2
plot for [i=ARGV[2]:ARGV[3]] ARGV[1] skip 1 using ($0):i w lines 
pause -1

