//Reuben Thorpe (2015) 2nd December Advent of Code C++11
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

int main() {
  int dim [3] , wrapper = 0, ribbon = 0;
  string numb, line;
  ifstream input("./input.txt");

  if (input.is_open()) {
    stringstream buffer,bline;
    buffer << input.rdbuf();
    input.close();

    while (getline(buffer, line)) {
      stringstream bline(line);
      for(int i = 0; getline(bline, numb, 'x'); i++) {
        dim[i] = stoi(numb);
      }
      sort(dim, dim+3);

      //Part 1
      wrapper += 2*(dim[0]*dim[1]) + 2*(dim[1]*dim[2]) + 2*(dim[2]*dim[0]);
      wrapper += dim[0]*dim[1];

      //Part 2
      ribbon += (2*dim[0] + 2*dim[1]) + (dim[0]*dim[1]*dim[2]);
    }
  }
  cout << "\nPart 1 = " << wrapper << "\n";
  cout << "Part 2 = " << ribbon << "\n\n";
  return 0;
}
