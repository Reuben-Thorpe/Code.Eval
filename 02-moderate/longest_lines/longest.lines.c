// Reuben Thorpe (2016), CodeEval [Longest Lines v1.2]
#include <stdio.h>
#include <string.h>


int main(int argc, const char *argv[]) {
  FILE *file = fopen(argv[1], "r");
  char line[1024];
  char string_array[40][1024];
  int n = 0, keep = 0;

  fscanf(file, "%d\n", &keep);

  while (fgets(line, 1024, file)) {
    n++;

    for (int i = 0; i < n; i++) {

      if (strlen(string_array[i]) < strlen(line)) {

        for (int j = n; j >= i; j--) {
          strcpy(string_array[j], string_array[j-1]);
        }

        strcpy(string_array[i], line);
        break;
      }
    }
  }

  for (int i = 0; i < keep; i++) {
    printf("%s", string_array[i]);
  }

  return(0);
}
