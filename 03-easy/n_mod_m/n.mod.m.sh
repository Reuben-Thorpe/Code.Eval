# Reuben Thorpe (2016), CodeEval [N Mod M v1.0]

IFS=','

while read line || [[ -n "$line" ]]; do
    problem=($line)
    N=${problem[0]}
    M=${problem[1]}

    echo $((N - (N/M)*M))

done < $1
