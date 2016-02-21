// Reuben Thorpe (2016), CodeEval [String Mask v1.0]
#include <iostream>
#include <fstream>

using namespace std;


char upperCase(char in) {
  // Converts DEC char to upper case
  return(in- 32);
}


int main(int argc, char* argv[]) {
  ifstream inFile(argv[1]);
  string word, binary;

  while(inFile >> word && inFile >> binary) {
    for(auto i = 0; i < word.length(); i++) {
      if (binary[i] == '1') {
        cout << upperCase(word[i]);
      }
      else {
        cout << word[i];
      }
    }
    cout << "\n";
  }
  return(0);
}

