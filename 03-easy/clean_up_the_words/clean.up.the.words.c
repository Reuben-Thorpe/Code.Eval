// Reuben Thorpe (2016), CodeEval [Clean Up Words v1.1]
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>


int main(int argc, const char * argv[]) {
  FILE *file = fopen(argv[1], "r");
  char line[1024];

  while (fgets(line, 1024, file)) {
    bool first_word = true;

    for (int i = 0; i < strlen(line); i++) {

      if (isalpha(line[i])) {

        if (first_word) {
          printf("%c", tolower(line[i]));
          first_word = false;
        }

        else if (!isalpha(line[i-1])) printf(" %c", tolower(line[i]));
        else printf("%c", tolower(line[i]));
      }
    }

  printf("\n");
  }

  return(0);
}

