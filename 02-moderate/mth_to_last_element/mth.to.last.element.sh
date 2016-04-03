#!bin/bash
# Reuben Thorpe (2016), CodeEval [Mth To Last Element v1.1]


while read -r line || [[ -n "$line" ]]; do
    IFS=' ' read -ra ARRY <<< "$line"
    length=${#ARRY[@]}
    last_pos=$((length - 1))
    N=$(($length - ${ARRY[${last_pos}]} - 1))

    if [[ $N -ge 0 ]]; then
        echo ${ARRY[${N}]}
    fi

done < $1
