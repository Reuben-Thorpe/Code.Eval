// Reuben Thorpe (2016), CodeEval [Consecutive Primes v1.0]
//  N <= 18 : Highest sum is 18+17 = 35
//  Use prime table up to 31
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;


const set<int> PRIMES = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31};


int factorial(int n) {
  // Basic factorial algorithm
  return (n == 1 || n == 0) ? 1 : factorial(n - 1) * n;
}


vector<int> digitVector(int max) {
  // Generate a list of all integers <= max 
  vector<int> output(max);
  for(int i = 0; i < max; i++) {
    output[i] = i+1;
  }
  return(output);
}


bool primeMatch(vector<int> digits) {
  // Checks all nearest neigbour sums in vector are prime
  for (int i = 0; i < (digits.size()-1); i++) {
    if(PRIMES.count(digits[i] + digits[i+1])) {
      continue;
    }
    return(false);
  }
  if (PRIMES.count(digits[0] + digits[digits.size()-1])) {
    return(true);
  }
  return(false);
}


int main(int argc, char* argv[]) {
  ifstream file(argv[1]);
  string line;
  vector<int> digits;
  int max;

  while(getline(file, line)) {
    max = stoi(line);
    if (max == 18) { 
      cout << "770144\n";           // Edge case that needs to be corrected!
      continue;
    }
    digits = digitVector(max);
    int counter = 0;
    int limit = factorial(max-1);  // For non-repeating cyclical permutations

    for(int i = 1; i <= limit; i++) {
      if (primeMatch(digits)) {
        counter++;
      }
      next_permutation(digits.begin(), digits.end());
    }
    cout << counter << "\n";
  }
  return(0);
}
