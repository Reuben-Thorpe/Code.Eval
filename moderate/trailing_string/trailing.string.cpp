// Reuben Thorpe (2016), CodeEval [Trailing String v1.0]
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>

using namespace std;


bool test_match(string line) {
  // Test if last commma deliminated string in a new line is also at the end
  // of the new line from which it came.
  stringstream ss;
  ss >> noskipws;
  string B;
  char A;
  reverse(line.begin(), line.end());
  ss.str(line);
  getline(ss, B, ',');

  for (int i = 0; i < B.length(); i++) {
    ss >> A;
    if (A == B[i]) {
      continue;
    }
    else {
      return(false);
    }
  }
  return(true);
}


int main(int argc, char* argv[]) {
  ifstream inFile(argv[1]);
  string line;

  while(inFile.peek() != EOF && getline(inFile, line)) {
    if (test_match(line)) cout << "1\n";
    else cout << "0\n";
  }
  return(0);
}
