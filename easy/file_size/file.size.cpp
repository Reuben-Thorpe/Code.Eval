// Reuben Thorpe (2016), CodeEval [File Size v1.1]
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char* argv[]) {
  ifstream inFile(argv[1], ios::binary | ios::ate);
  cout << inFile.tellg() << '\n';
  return(0);
}
