// Reuben Thorpe (2016), CodeEval [String Permutations v1.1]
#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

int fac(int n) {
  // Compute factorial
  return (n == 1 || n == 0) ? 1 : fac(n - 1) * n;
}


int main(int argc, char* argv[]) {
  ifstream inFile(argv[1]);
  string line;

  while (inFile >> line) {
    int i = 0;
    int limit = fac(line.length());
    sort(line.begin(), line.end());

    do {
      cout << line << ',';
      i++;
    } while (next_permutation(line.begin(), line.end()) && i < limit-1);

    next_permutation(line.end(), line.begin());
    cout << line << '\n';
  }

  return(0);
}
