#!/bin/sh
cat popular-names.txt | tr '\t' ' ' > 11-tr.txt

expand -t 1 popular-names.txt > 11-expand.txt
