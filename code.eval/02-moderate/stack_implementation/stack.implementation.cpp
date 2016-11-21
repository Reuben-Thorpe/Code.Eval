#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;


int main(int argc, char* argv[]) {
  ifstream in_file(argv[1]);
  string in_line;

  while (getline(in_file, in_line)) {
    vector<int> word_space;
    int num;
    istringstream sstr(in_line);

    while (sstr >> num) {
      word_space.push_back(num);
    }

    reverse(word_space.begin(), word_space.end());

    for(int i = 0; i < word_space.size(); i+=2) {
      cout << word_space[i] << ' ';
    }
    cout << '\n';
  }

  return(0);
}
