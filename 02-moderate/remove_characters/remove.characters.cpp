// Reuben Thorpe (2016), CodeEval [Remove Characters v1.2]
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>

using namespace std;


int main(int argc, char* argv[]) {
  ifstream in_file(argv[1]);
  string line;

  while (getline(in_file, line)) {
    stringstream sstr(line);
    string sentence, remove_chars;
    getline(sstr, sentence, ',');
    sstr >> remove_chars;

    for (auto n: remove_chars) {
      sentence.erase(remove(sentence.begin(),
                            sentence.end(), n),
                            sentence.end());
    }

    cout << sentence << '\n';
  }

  return(0);
}
