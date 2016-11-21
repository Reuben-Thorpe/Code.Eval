//Reuben Thorpe (2015) 1st December Advent of Code C++11
#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int main() {
  int floor = 0, index;
  ifstream input("./input.txt");

  if (input.is_open()) {
    stringstream buffer;
    buffer << input.rdbuf();
    input.close();
    bool flag = false;
    char step;

    //Part 1
    while (buffer >> step) {
      switch(step) {
        case '(': ++floor; break;
        case ')': --floor; break;
      }
      //Part 2
      if (!flag && floor == -1) {
        index = buffer.tellg();
        flag = true;
      }
    }

  }
  cout << "\nPart 1 = " << floor << endl;
  cout << "Part 2 = " << index << "\n\n";
  return 0;

}
