#!/bin/bash
# Reuben Thorpe (2016), CodeEval [First Non-Repeated Character v1.2]

while read line || [[ -n "$line" ]]; do
    for (( i=0; i<${#line}; i++ )); do
        char="${line:$i:1}"
        if [[ $(grep -o "$char" <<< "$line" | wc -l) -eq 1 ]]
            then
                echo $char
                break
        fi
    done
done < $1
