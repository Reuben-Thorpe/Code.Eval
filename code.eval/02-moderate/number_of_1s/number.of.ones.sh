#!bin/bash
# Reuben Thorpe (2016), CodeEval [Number of Ones v1.2]

while read line || [[ -n "$line" ]]; do
     echo "obase=2;$line" | bc | grep -o "1" | wc -l
done < $1
