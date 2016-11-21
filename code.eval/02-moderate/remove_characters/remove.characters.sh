# Reuben Thorpe (2016), CodeEval [Remove Characters v1.0]
IFS=','

while read line || [[ -n "$line" ]]; do
    problem=($line)
    remove_chars=${problem[1]:1}

    echo "${problem[0]}" | tr --delete $remove_chars
done < $1
