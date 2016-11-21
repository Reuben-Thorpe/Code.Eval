#!/bin/bash
# Reuben Thorpe (2016), CodeEval [Array Absurdity v1.1]


while read line || [[ -n "$line" ]]; do
    IFS=';'
    parse=($line)
    IFS=','
    sequence=(${parse[1]})
    COUNTER=0

    while [  $COUNTER -lt ${parse[0]} ]; do
        num=${sequence[$COUNTER]}

        if [[ " ${sequence[@]:$(($COUNTER + 1))} " =~ " $num " ]]; then
                echo $num
        fi
        let COUNTER=COUNTER+1
    done


done < $1
