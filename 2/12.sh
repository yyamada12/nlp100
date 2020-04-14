#!/bin/sh

cut -f 1 -d $'\t' popular-names.txt > col1-cut.txt
cut -f 2 -d $'\t' popular-names.txt > col2-cut.txt
