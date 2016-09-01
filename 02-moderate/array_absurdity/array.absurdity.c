// Reuben Thorpe (2016), CodeEval [Array Absurdity v1.3]
#include <stdio.h>

void parse_problem(FILE* in_file, int* arr, int* size);
int print_repeat_element(int* arr, int* size);


int main(int argc, const char* argv[]) {
  FILE* in_file = fopen(argv[1], "r");
  int size;

  while (fscanf(in_file, "%d;", &size) != EOF) {
    int arr[size];

    parse_problem(in_file, arr, &size);
    print_repeat_element(arr, &size);
  }

  return(0);
}


void parse_problem(FILE* in_file, int* arr, int* size) {
  // Parse CodeEval problem sets for "array absurdity".
  for (int i = 0; i < (*size - 1); i++) fscanf(in_file, "%d,", &arr[i]);
  fscanf(in_file, "%d\n", &arr[*size-1]);
}


int print_repeat_element(int* arr, int* size) {
  // Print the first repeat element in an array.
  for(int i = 0; i < *size; i++) {
    for(int j = i+1; j < *size; j++) {
      if(arr[i] == arr[j]) {
        printf("%d\n", arr[i]);
        break;
      }
    }
  }
}


