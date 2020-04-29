#!/bin/sh
echo 'train.txt'
cut -f 5 train.txt | sort | uniq -c
echo ''

echo 'valid.txt'
cut -f 5 valid.txt | sort | uniq -c
echo ''

echo 'test.txt'
cut -f 5 test.txt | sort | uniq -c
