// Reuben Thorpe (2016), CodeEval [Fibonacci Series v1.0]
#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

const float PHI = 1.61803398874989484820;
const float SQRT5 = sqrt(5);


float fib(float n) {
  return(((pow(PHI, n) - pow(-PHI, -n)) / SQRT5));
  }


int main(int argc, char* argv[]) {
  string line;
  ifstream file(argv[1]);
  while (getline(file, line)) {
    cout << fib(stod(line)) << "\n";
  }
  return 0;
}
