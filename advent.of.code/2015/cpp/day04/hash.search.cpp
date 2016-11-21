//Reuben Thorpe (2015) 4th December Advent of Code c++11
#include <iostream>
#include <string>
#include "md5.h"

using namespace std;

bool startsWith(string input, string check) {
  //checks begining of string
  return !input.compare(0, check.length(), check);
}

int main() {
  string key = "bgvyzdsv", part1 = "00000", part2 = "000000", input;
  bool flag_1 = false, flag_2 = false;
  int i = 0;
  cout << "\n";

  while (true) {
    input = md5(key+to_string(i));
    //Part 1
    if (startsWith(input, part1) && !flag_1) {
      cout << "Part 1 = " << i << "\n";
      flag_1 = true;
      if (flag_2) {break;}
    }
    //Part 2
    if (startsWith(input, part2) && !flag_2) {
      cout << "Part 2 = " << i << "\n";
      flag_2 = true;
      if (flag_1) {break;}
    }
    ++i;
  }

  cout << "\n";
  return 0;
}
