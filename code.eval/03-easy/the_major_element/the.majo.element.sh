# Reuben Thorpe (2016), CodeEval [The Majo Element v1.0]

while read line || [[ -n "$line" ]]; do
    IFS=','
    seq=($line)
    L=${#seq[@]}
    N=$((L / 2))

    unset IFS
    result=($(echo "${seq[@]}" | tr ' ' '\n' | sort | uniq -c -d | sort -nr | head -n1))


    if [[ $N -lt ${result[0]} ]]; then
        echo ${result[1]}
    else
        echo None
    fi

done < $1
