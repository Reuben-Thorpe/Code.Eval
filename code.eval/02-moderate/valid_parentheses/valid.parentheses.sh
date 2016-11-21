# Reuben Thorpe (2016), CodeEval [Valid Parentheses v1.0]

while read line || [[ -n "$line" ]]; do

    while [[ "$line" == *"()"* || "$line" == *"{}"* || "$line" == *"[]"* ]] ; do
        line=${line//()/}
        line=${line//[]/}
        line=${line//\{\}/}
    done

    if [[ $line ]] ; then
        echo False
    else
        echo True
    fi
done < $1
