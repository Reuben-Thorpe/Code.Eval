// Reuben Thorpe (2016), CodeEval [Black Card v1.0]
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

void parse_problem(FILE* in_file, char names[11][100], int* turns);
const char* black_card(char names[11][100], int* turns);
void compress(char names[11][100], int* length);


int main(int argc, const char* argv[]) {
  FILE* in_file = fopen(argv[1], "r");
  char names[11][100];
  int turns;

  while (!feof(in_file)) {
    parse_problem(in_file, names, &turns);
    printf("%s\n", black_card(names, &turns));
  }

  return(0);
}


const char* black_card(char names[11][100], int* turns) {
  // Determin which entry is the "black card".

  int length;

  for (int i = 0; i < 11; i++) {
    if (strlen(names[i]) == 0) {
      length = i;
      break;
    }
  }

  while (length != 1) {
    names[(*turns % length) - 1][0] = '\0';
    length--;
    compress(names, &length);
  }
  return(names[0]);
}


void compress(char names[11][100], int* length) {
  /*
  Compress array by finding a single empty entry and trainslating the
  remaining entries towards the head of the array.
  */

  for (int i = 0; i < 11; i++) {
    if (strlen(names[i]) == 0) {
      for (int j = i; j < *length; j++) {
        strcpy(names[j], names[j+1]);
      }
      names[*length][0] = '\0';
    }
  }
}


void parse_problem(FILE* in_file, char names[11][100], int* turns) {
  // Parse CodeEval problem set "Black Cards".

  memset(names, 0, sizeof(char)*11*100);
  char tmp_string[100];

  for (int i = 0; i < 11; i++ ) {
    fscanf(in_file, "%s ", &tmp_string);
    if (tmp_string[0] == '|') break;
    else strcpy(names[i], tmp_string);
  }

  fscanf(in_file, "%i\n", turns);
}
