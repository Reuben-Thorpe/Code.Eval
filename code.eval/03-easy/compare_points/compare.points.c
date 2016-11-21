// Reuben Thorpe (2016), CodeEval [Compare Points v1.1]
#include <stdio.h>
#include <string.h>

void get_heading(char cardinal_string[4], long int* O, long int* P, long int* Q, long int* R);


int main (int argc, const char* argv[]) {
  FILE* in_file = fopen(argv[1], "r");
  char cardinal_string[4];
  long int O, P, Q, R;

  while (fscanf(in_file, "%ld %ld %ld %ld\n", &O, &P, &Q, &R) != EOF) {
    get_heading(cardinal_string, &O, &P, &Q, &R);
    printf("%s\n", cardinal_string);

  }

  return(0);
}


void get_heading(char cardinal_string[4], long int* O, long int* P, long int* Q, long int* R) {
  /*
    Generate the heading from one gps coordinate to the second. The second
    coordinate is transformed with the first so that its origin become
    (0,0). The cardinal direction is then simple to extrapolate.
  */
  memset(cardinal_string, 0, 4);
  int index = 0;

  long int x = *Q - *O;
  long int y = *R - *P;

  if (y > 0) cardinal_string[index++] = 'N';
  else if (y < 0) cardinal_string[index++] = 'S';

  if (x > 0) cardinal_string[index] = 'E';
  else if (x < 0) cardinal_string[index] = 'W';

  if (strlen(cardinal_string) == 0) strcpy(cardinal_string, "here");
}
