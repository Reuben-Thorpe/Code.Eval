// Reuben Thorpe (2016), CodeEval [Fizz Buzz v1.0]
#include <iostream>
#include <fstream>

using namespace std;


void fizzBuzz(int X, int Y, int N) {
  // Print out fizz buzz values
  for(int i = 1; i <= N; i++) {
    bool flag = false;
    if (i % X == 0) {
      cout << "F";
      flag = true;
    }
    if (i % Y == 0) {
      cout << "B";
    }
    else if (!flag) {
      cout << i;
    }
    if (i < N) {cout << " ";}
  }
  cout << "\n";
}


int main(int argc, char* argv[]) {
  ifstream inFile(argv[1]);
  int X, Y, N;
  while(inFile >> X >> Y >> N) {
    fizzBuzz(X, Y, N);
  }
  return(0);
}

