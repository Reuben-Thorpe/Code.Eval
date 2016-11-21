#!/bin/bash
# Reuben Thorpe (2016), CodeEval [Sum of Intergers From File v1.0]

sum=0

while read line || [[ -n "$line" ]]; do
    sum=$(($sum + $line))
done < $1

echo $sum
