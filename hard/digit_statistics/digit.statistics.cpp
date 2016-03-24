// Reuben Thorpe (2016), CodeEval [Digit Statistics v1.0]
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

void digit_stats(int a, long int n);
vector<long int> repeat_seq(int a);


int main(int argc, char* argv[]) {
  ifstream in_file(argv[1]);
  int a;
  long int n;

  while (in_file.peek() != EOF && in_file >> a >> n) {
    digit_stats(a, n);
  }
  return(0);
}


void digit_stats(int a, long int n) {
  vector<long int> seq_pattern = repeat_seq(a);
  long int cycle_span = accumulate(seq_pattern.begin(), seq_pattern.end(), 0);
  long int cycle_multiplier = n / cycle_span;
  long int cycle_m_remainder = n % cycle_span;
  for (auto& value: seq_pattern) value*=cycle_multiplier;

  if (cycle_m_remainder != 0) {
    long int m = a;
    for (int i = 0; i < cycle_m_remainder; i++) {
      seq_pattern[m] += 1;
      m *= a;
      m %= 10;
    }
  }
  for (int i = 0; i < seq_pattern.size()-1; i++) {
    cout << i << ": " << seq_pattern[i] << ", ";
  }
  cout << seq_pattern.size()-1 << ": " << seq_pattern.back() << "\n";
}


vector<long int> repeat_seq(int a) {
  long int m = a;
  vector<long int> seq(10, 0);
  while (seq[m] == 0) {
    seq[m] += 1;
    m *= a;
    m %= 10;
  }
  return(seq);
}

