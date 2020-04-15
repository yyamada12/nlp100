#!/bin/sh

cut -f 1 popular-names.txt | sort | uniq -c | sort -r | sed "s/^ *[0-9]* //g" > 19-cut-uniq-sort.txt