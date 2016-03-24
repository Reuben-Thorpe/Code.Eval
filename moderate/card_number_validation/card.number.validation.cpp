// Reuben Thorpe (2016), CodeEval [Card Number Validation v1.0]
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;


int luhn(long int n);


int main(int argc, char* argv[]) {
  ifstream in_file(argv[1]);
  long int card_number;
  string line;

  while (getline(in_file, line)) {
    line.erase(remove(line.begin(), line.end(), ' '),line.end());
    card_number = stol(line);
    cout << luhn(card_number) << '\n';
  }

  return(0);
}


int luhn(long int n) {
  // Mod 10 checksum by Hans Peter Luhn (1896-1964)
  int l_sum = 0;

  while (n) {
    int r = n % 100;
    n /= 100;
    int z = r % 10;
    r = r / 10*2;
    l_sum += r/10 + r%10 + z;
  }

  if (0 == l_sum%10) return(1);
  else return(0);
}

