#!bin/bash
# Reuben Thorpe (2016), CodeEval [Decimal To Binary v1.4]

while read line || [[ -n "$line" ]]; do
     echo "obase=2;$line" | bc
done < $1
