#!/bin/sh

read N
line_num=$(cat popular-names.txt | wc -l | tr -d ' ')
if [ $N -gt $line_num ];then
    exit 1
fi
line_num_per_file_small=$((line_num / N))
line_num_per_file_large=$((line_num_per_file_small + 1))
large_file_num=$((line_num % N))

line_num_large=$(($line_num_per_file_large * $large_file_num))
line_num_small=$(($line_num - $line_num_large))
head -$line_num_large popular-names.txt > large.txt
tail -$line_num_small popular-names.txt > small.txt

# use gnu-split for macOS
gsplit --additional-suffix=.txt\
    --numeric-suffixes=0\
    -l $line_num_per_file_large\
    large.txt\
    16-split-
gsplit --additional-suffix=.txt\
    --numeric-suffixes=$large_file_num\
    -l $line_num_per_file_small\
    small.txt\
    16-split-

rm large.txt small.txt