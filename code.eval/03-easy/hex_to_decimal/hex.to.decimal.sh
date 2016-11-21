#!bin/bash
# Reuben Thorpe (2016), CodeEval [Hex To Decimal v1.1]

while read line || [[ -n "$line" ]]; do
    echo $((16#$line))
done < $1
