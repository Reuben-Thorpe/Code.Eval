// Reuben Thorpe (2016), CodeEval [Decimal To Binary v1.0]
#include <iostream>
#include <fstream>
#include <iomanip>
#include <bitset>

using namespace std;

int main(int argc, char* argv[]) {
  ifstream inFile(argv[1]);
  int num;
  cout << fixed << setprecision(0);

  while (inFile >> num) {
    cout << stod(bitset<32>(num).to_string()) << '\n';
  }

  return(0);
}
