// Reuben Thorpe (2016), CodeEval [Happy Numbers v1.3]
#include <iostream>
#include <fstream>
#include <set>
#include <math.h>

using namespace std;

int sum_sqr_digits(int n);


int main(int argc, char* argv[]) {
  ifstream in_file(argv[1]);
  set<int> unhappy_seq = {4, 16, 37, 58, 89, 145, 42, 20};
  int sqr_sum;

  while(in_file >> sqr_sum) {
    in_file.ignore();
    sqr_sum = sum_sqr_digits(sqr_sum);

    while (true) {

      if (sqr_sum == 1) {
        cout << "1\n";
        break;
      }

      else if (unhappy_seq.find(sqr_sum) != unhappy_seq.end()) {
        cout << "0\n";
        break;
      }

      else {
        sqr_sum = sum_sqr_digits(sqr_sum);
      }
    }

  }
  return(0);
}


int sum_sqr_digits(int n) {
  // Sum the square of the digits of an intiger.
  int s = 0;

  while (n != 0) {
    s += pow(n % 10, 2);
    n /= 10;
  }
  return(s);
}
