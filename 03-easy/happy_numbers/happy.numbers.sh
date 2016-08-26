# Reuben Thorpe (2016), CodeEval [Happy Numbers v1.2]

declare -a unhappy_seq=(4 16 37 58 89 145 42 20)


function sum_sqr_digits { # <int>
    # Sum the sqaurs of the digits of an intiger.
    local s=0
    local n=$1

    while [[ $n != 0 ]]; do
        s=$(( s + (n % 10)**2 ))
        n=$((n/10))
    done

  echo $s
}


function scan_array { # <element> <array>
    # Return true if element found in array, otherwise return false.
    local element=$1
    local arr=($@)
    arr=${arr[@]:1}

    for i in ${arr[@]} ; do
        if [ $i == $element ] ; then
            echo 1
            break
        fi
    done
    return 0
}


while read line || [[ -n "$line" ]]; do
    sqr_sum=$(sum_sqr_digits $line)

    while [[ true ]]; do

        if [[ $sqr_sum == 1 ]]; then
            echo "1"
            break

        elif [[ $(scan_array $sqr_sum ${unhappy_seq[@]}) ]]; then
            echo "0"
            break

        else
            sqr_sum=$(sum_sqr_digits $sqr_sum)
        fi

    done

done < $1
