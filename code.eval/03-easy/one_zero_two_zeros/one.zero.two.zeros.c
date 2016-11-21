// Reuben Thorpe (2016), CodeEVal [One Zero Two Zeros v1.1]
#include <stdio.h>

// Constants
const int UN_INT_BIT_SIZE = sizeof(unsigned int) * 8;

// Functions
int one_zero_two_zero(unsigned int unset_count, unsigned int series_limit);
unsigned int count_zero_bits(unsigned int value);


int main(int argc, const char* argv[]) {

  unsigned int unset_count, series_limit;
  FILE* in_file = fopen(argv[1], "r");

  while (fscanf(in_file, "%d %d\n", &unset_count, &series_limit) != EOF) {
    printf("%d\n", one_zero_two_zero(unset_count, series_limit));
  }

  return 0;
}


int one_zero_two_zero(unsigned int unset_count, unsigned int series_limit) {
  /*
    Find the number of reverse popcount values of a series which are the same
    as a given value.
  */

  int sum = 0;

  for (int i = 1; i <= series_limit; i++) {
    if (count_zero_bits(i) == unset_count) sum++;
  }

  return sum;
}


unsigned int count_zero_bits(unsigned int value) {
  /* 
    This function is implimentation specific to GNU gcc.
    It counts the number of 0-bits in an int, removing the leading zeros.
  */
 
  return (UN_INT_BIT_SIZE - __builtin_clz(value) - __builtin_popcount(value));
}
