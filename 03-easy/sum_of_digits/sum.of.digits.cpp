// Reuben Thorpe (2016), CodeEval [Sum of Digits v1.1]

#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;


int main(int argc, char* argv[]) {
  ifstream in_file(argv[1]);
  string line;
  char digit;

  while (getline(in_file, line)) {
    int sum = 0;
    stringstream ss;
    ss.str(line);

    while (ss >> digit) {
      sum += digit - '0';
    }

    cout << sum << '\n';
  }

  return(0);
}
