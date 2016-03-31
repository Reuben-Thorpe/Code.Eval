// Reuben Thorpe (2016), CodeEval [Hex To Decimal v1.0]
#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;


int main(int argc, char* argv[]) {
  ifstream inFile(argv[1]);
  string line;

  while(getline(inFile, line)) {
    stringstream ss;
    int num;
    ss.str(line);
    ss >> std::hex >> num;
    cout << num << '\n';
  }
  return(0);
}
