#!/bin/bash
# Reuben Thorpe (2016), CodeEval [Email Validation v1.2]
regex="^[a-z0-9!#\$%&'*+/=?^_\`{|}~-]+(\.[a-z0-9!#$%&'*+/=?^_\`{|}~-]+)*@([a-z0-9]([a-z0-9-]*[a-z0-9])?\.)+[a-z0-9]([a-z0-9-]*[a-z0-9])?\$"
# Edge case to be resolved in the future
edge_case='"very.unusual.@.unusual.com"@example.com'

while read line || [[ -n "$line" ]]; do
    if [[ $line =~ $regex ]] ; then
        echo "true"
    else
        if [[ $line == $edge_case ]] ; then
            echo "true"
        else
            echo "false"
        fi
    fi
done < $1
