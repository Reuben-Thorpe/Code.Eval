// Reuben Thorpe (2016), CodeEval [Decimal To Binary v1.0]
#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <bitset>

using namespace std;

int main(int argc, char* argv[]) {
  ifstream inFile(argv[1]);
  string binary;
  int num;
  cout << fixed << setprecision(0);

  while (inFile >> num) {
    binary = bitset<32>(num).to_string();
    cout << count(binary.begin(), binary.end(), '1') << '\n';
  }

  return(0);
}
