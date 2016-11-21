# Reuben Thorpe (2016), CodeEval [String Rotation v1.1]
IFS=','

while read line || [[ -n "$line" ]]; do
    problem=($line)
    string=${problem[0]}
    rotation=${problem[1]}
    size=${#rotation}
    result="False"

    for ((i=0; i<=size; i++))
    do

    if [[ ${rotation:$i:1} == ${string:0:1} ]]
        then
            match=${rotation:$i:$((size - i))}${rotation:0:$i}

            if [[ $match == $string ]]
                then
                    result="True"
                    break
            fi
    fi
    done
    echo $result


done < $1
