# Reuben Thorpe (2016), CodeEval [Fibonacci Series v1.1]

SQRT_5=$(echo "sqrt(5)" | bc -l)
PHI=1.61803398874989484820


fib() {
    printf "%.0f\n" $(echo "((($PHI^$1)-(-$PHI)^(-$1))/$SQRT_5)" | bc -l)
}


while read line || [[ -n "$line" ]]; do
   fib $line
done < $1
