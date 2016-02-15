#!/bin/bash
filename=$1

while read -r line
do
  for i in `seq 1 10`;
  do
    step2 $line
  done

done < "$filename"


function step1 {
  n=$((10#$1))

}


function step2 {
  n=$((10#$1))
  #n+=2000
  return $n

}
