// Reuben Thorpe (2016), CodeEval [Array Absurdity v1.2]
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;


int main(int argc, char* argv[]) {
  ifstream in_file(argv[1]);
  string line;

  while(getline(in_file, line)) {
    int N;
    int num;
    stringstream sstr(line);
    sstr >> N;
    sstr.ignore();

    vector<int> seq;
    seq.reserve(N-1);

    while(sstr >> num) {
      if (find(seq.begin(), seq.end(), num) != seq.end()) {
        cout << num << '\n';
        break;
      }
      else {
        seq.push_back(num);
        sstr.ignore();
      }
    }
  }

  return(0);
}
