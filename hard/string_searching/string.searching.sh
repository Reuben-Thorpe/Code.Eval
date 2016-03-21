#!bin/bash
# Reuben Thorpe (2016), CodeEval [String Searching v1.1]


while read -r line || [[ -n "$line" ]]; do
    IFS=',' read -ra ARRY <<< "$line"
    string="${ARRY[0]}"
    s_string="${ARRY[1]}"


    if [[ $s_string == " " ]]; then
        echo "true"
    elif [[ $string == *$s_string* ]]; then
        echo "true"
    else
        echo "false"
    fi

done < $1
