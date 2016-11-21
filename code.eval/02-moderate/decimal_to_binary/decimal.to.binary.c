// Reuben Thorpe (2016), CodeEval [Decimal To Binary v1.4]
#include <stdio.h>

long decimal_to_binary(long n);


int main (int argc, const char* argv[]) {
  FILE *file = fopen(argv[1], "r");
  long decimal;

  while (fscanf(file, "%ld\n", &decimal) != EOF) {
    printf("%ld\n", decimal_to_binary(decimal));
  }

  return(0);
}


long decimal_to_binary(long n) {
  // Function to convert a decinal number to binary number.
    int remainder; 
    long binary = 0, i = 1;

    while(n != 0) {
        remainder = n%2;
        n = n/2;
        binary= binary + (remainder*i);
        i = i*10;
    }
    return binary;
}
