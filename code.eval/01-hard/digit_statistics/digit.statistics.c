// Reuben Thorpe (2016), CodeEval [Digit Statistics v1.2]
#include <stdio.h>

void digit_stats(int a, long int n);
void repeat_seq(int a, long int* seq);


int main(int argc, const char* argv[]) {
  FILE* file = fopen(argv[1], "r");
  int a;
  long int n;

  while (fscanf(file, "%d %ld\n", &a, &n) != EOF) {
    digit_stats(a, n);
  }
  return(0);
}


void digit_stats(int a, long int n) {
  /*
    Given the numbers "a" and "n" find out how many times each digit from zero
    to nine is the last digit of the number in a sequence
    [ a, a2, a3, ... an-1, an ].
  */

  long int cycle_span = 0;
  long int seq_pattern[10] = {0};
  repeat_seq(a, seq_pattern);

  for (int i = 0; i < 10; i++) cycle_span += seq_pattern[i];

  long int cycle_multiplier = n / cycle_span;
  long int cycle_m_remainder = n % cycle_span;

  for (int i = 0; i < 10; i++) seq_pattern[i] *= cycle_multiplier;

  if (cycle_m_remainder != 0) {
    long int m = a;
    for (int i = 0; i < cycle_m_remainder; i++) {
      seq_pattern[m] += 1;
      m *= a;
      m %= 10;
    }
  }

  for (int i = 0; i < 9; i++) {
    printf("%d: %ld, ", i, seq_pattern[i]);
  }
  printf("9: %ld\n", seq_pattern[9]);
}


void repeat_seq(int a, long int* seq) {
  /*
    Find all the last repeat digits of a square sequence.
  */
  long int m = a;

  while (seq[m] == 0) {
    seq[m] += 1;
    m *= a;
    m %= 10;
  }
}
