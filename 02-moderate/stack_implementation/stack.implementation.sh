#!/bin/bash
# Reuben Thorpe (2016), CodeEval [Stack Implementation v1.1]


while read line || [[ -n "$line" ]]; do
    array=($line)
    final_array=()

    end=$((${#array[@]} - 1))

    for i in $(eval echo {$end..0..2})
        do
            final_array+=(${array[$i]})
    done

    echo ${final_array[@]}

done < $1
