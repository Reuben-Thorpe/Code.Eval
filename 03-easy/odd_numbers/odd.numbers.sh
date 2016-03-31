#!bin/bash
# Reuben Thorpe (2016), CodeEval [Odd Numbers v1.2]

COUNTER=1

while [ $COUNTER -lt 100 ]; do
  echo $COUNTER
  let COUNTER+=2
done
