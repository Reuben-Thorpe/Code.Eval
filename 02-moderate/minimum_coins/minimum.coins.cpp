// Reuben Thorpe (2016), CodeEval [Minimum Coins v1.1]
#include <iostream>
#include <fstream>

using namespace std;


int main(int argc, char* argv[]) {
  ifstream in_file(argv[1]);
  int num;

  while (in_file >> num) {
    int num_coins;
    num_coins = num / 5;
    num %= 5;
    num_coins += num / 3;
    num %= 3;
    num_coins += num;
    cout << num_coins << '\n';
  }

  return(0);
}
