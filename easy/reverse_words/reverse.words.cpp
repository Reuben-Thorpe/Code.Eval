// Reuben Thorpe (2016), CodeEval [Reverse Words v1.0]
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;


int main (int argc, char* argv[]) {
  ifstream inFile(argv[1]);
  vector<string> capture;
  capture.reserve(50);
  string line, word;

  while(getline(inFile, line)) {
    istringstream iss(line);
    while(iss >> word) {
      capture.push_back(word);
    }

    for (int i = capture.size()-1; i > 0; i--) {
      cout << capture[i] << " ";
    }

    cout << capture[0] << '\n';
    capture.clear();
  }

  return(0);
}
