// Reuben Thorpe (2016), CodeEval [Distinct Subsequence v1.1]
#include <iostream>
#include <fstream>
#include <vector>


using namespace std;
int gResult = 0;


vector<int> findIn(string inString, char match) {
  // Return a list of all positions char occures in string
  vector<int> indicies;
  for (int i = 0; i < inString.length(); i++) {
    if (inString[i] == match) {
      indicies.push_back(i);
    }
  }
  return(indicies);
}


void countSub(vector<vector<int>> freqArray, int depth, int cut) {
    // Counts the number of sub-sequences in the position matrix.
    // This function used global variable "gResult"
  if (depth == 0) {
    for (int i: freqArray[depth]) {
      countSub(freqArray, depth+1, i);
    }
  }
  else if (depth == freqArray.size()-1) {
    for (int i: freqArray[depth]) {
      if (i > cut) {
        gResult++;
      }
    }
  }
  else {
    for (int i: freqArray[depth]) {
      if (i > cut) {
        countSub(freqArray, depth+1, i);
      }
    }
  }
}


int main(int argc, char* argv[]) {
  // Generates position matrix, and calculates sub string frequency
  ifstream inFile(argv[1]);
  string seq, subSeq;

  while(getline(inFile, seq, ',') && getline(inFile, subSeq)) {
    vector<vector<int>> freqArray;

    for (char i: subSeq) {
      freqArray.push_back(findIn(seq, i));
    }

    countSub(freqArray, 0, 0);
    cout << gResult << "\n";
    gResult = 0;
  }
  return(0);
}
