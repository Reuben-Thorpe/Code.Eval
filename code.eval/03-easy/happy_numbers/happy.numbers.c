// Reuben Thorpe (2016), CodeEval [Happy Numbers v1.1]
#include <stdio.h>
#include <stdbool.h>
#include <math.h>

int sum_sqr_digits(int n);
bool is_value_in_array(int val, int *arr, int size);


int main(int argc, const char * argv[]) {
  FILE *in_file = fopen(argv[1], "r");
  int unhappy_seq[] = {4, 16, 37, 58, 89, 145, 42, 20};
  int unhappy_seq_size = sizeof(unhappy_seq)/sizeof(unhappy_seq[0]);
  int num, sqr_sum;

  while (fscanf(in_file, "%d\n", &num) != EOF) {;
    sqr_sum = sum_sqr_digits(num);

    while (true) {

      if (sqr_sum == 1) {
        printf("1\n");
        break;
      }

      else if (is_value_in_array(sqr_sum, unhappy_seq, unhappy_seq_size)) {
        printf("0\n");
        break;
      }

      else {
        sqr_sum = sum_sqr_digits(sqr_sum);
      }
    }
  }

  return(0);
}


int sum_sqr_digits(int n) {
  // Sum the square of the digits of an intiger.
  int s = 0;
  int x;

  while (n != 0) {
    x = (n % 10);
    s += x*x;
    n /= 10;
  }
  return(s);
}


bool is_value_in_array(int val, int *arr, int size) {
  // Returns true if 'val' is found in the array.
  int i;
  for (i=0; i < size; i++) {
    if (arr[i] == val) {
      return(true);
    }
  }
  return(false);
}


