// Reuben Thorpe (2016), CodeEval [Odd Numbers v1.0]
#include <stdio.h>


int main() {
  int i;
  for (i = 1; i < 100; i++) {
    if (i % 2 != 0) {
      printf("%d\n", i);
    }

  }
  return(0);
}
