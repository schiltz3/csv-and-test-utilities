#!/bin/bash
# Converts the txt file saved from Unico GUI to a CSV by replacing all whitespace with commas
# Run script with txt file to convert as the argument

# Creat new filepath for output csv with same name as input txt
output=$(sed -E 's/\.txt/\.csv/g' <<< "$1")

cat $1 | \
# remove first 2 lines to conform to standard SVG format
	sed '1,2d' | \
# remove returns from file
	sed -E 's/\r//g' | \
# Replace contiguous whitespace with one comma from 2 to $
	sed -E '2,$ s/\s+/\,/g' | \
# Insert specific commas on line 3
	sed -E '1s/\]\s+/\]\,/g' | \
# Remove trailing whitespace at the end of line 3
	sed -E '1s/\s+$//g' | \
# Suposed to remove commas at the end of a line
	sed -E 's/[,\s+]+$//g' \
> $output

