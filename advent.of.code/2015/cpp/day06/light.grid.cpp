// Reuben Thorpe (2015) 5th December Advent of Code C++11
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <array>

using namespace std;

int main() {
  ifstream input("./input.txt");

  if (input.is_open()) {
    stringstream buffer;
    buffer << input.rdbuf();
    input.close();
    }

  //cout << "\nPart 1 = " << niceword_1 << "\n";
  //cout << "Part 2 = " << niceword_2 << "\n\n";
  return 0;
}
