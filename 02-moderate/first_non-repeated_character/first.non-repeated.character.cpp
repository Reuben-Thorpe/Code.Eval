// Reuben Thorpe (2016), CodeEval [First Non-Repeated Character v1.1]
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;


int main(int argc, char* argv[]) {
  ifstream in_file(argv[1]);
  string line;

  while(getline(in_file, line)) {
    for (auto c: line) {
      if (count(line.begin(), line.end(), c) == 1) {
        cout << c << '\n';
        break;
      }
    }
  }

  return(0);
}
