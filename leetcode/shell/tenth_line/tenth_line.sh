#!/bin/bash

filename='file.txt'
lines=$(wc -l "$filename" | awk '{print $1}')

if [ "$lines" -lt 10 ]
then
    echo ''
else
    head -n 10 "$filename" | tail -n 1
fi
