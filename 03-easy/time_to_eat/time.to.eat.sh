#!/bin/bash
# Reuben Thorpe (2016), CodeEval [Time To Eat v1.3]

while read line || [[ -n "$line" ]]
do
    echo $(for var in $line; do echo $var; done | sort -t$':' -k1 -k2 -k3 -rn)
done < "$1"
