// Reuben Thorpe (2016), CodeEval [Decode Numbers v1.1]
#include <iostream>
#include <fstream>
#include <vector>


using namespace std;


int decode_permutations(string number_string) {
  // Dynamic programming solution to the possible decoding problem

  int n = number_string.size();
  vector<int> count(n + 1);
  count[0] = 1;
  count[1] = 1;

  for (int i = 2; i <= n; i++) {

    if (number_string[i-1] > '0') {
      count[i] = count[i-1];
    }

    if (number_string[i-2] < '2' || (number_string[i-2] == '2' && number_string[i-1] < '7')) {
      count[i] += count[i-2];
    }
  }

  return(count[n]);

}


int main(int argc, char* argv[]) {

  ifstream in_file(argv[1]);
  string line;

  while (getline(in_file, line)) {
    cout << decode_permutations(line) << '\n';
  }

  return(0);
}


