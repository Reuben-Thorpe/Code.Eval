// Reuben Thorpe (2016), CodeEval [Find The Highest Score v1.0]
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;


int main(int argc, char* argv[]) {
  ifstream inFile(argv[1], ios::binary);
  vector<int> high_score;
  high_score.reserve(20);   // Maximum number of categories

  while (inFile.peek() != EOF) {
    int num;
    string row;
    stringstream row_stream;

    // Calculates the number of catagories and populate the high_score

    getline(inFile, row, '|');
    row_stream.str(row);
    while (row_stream >> num) high_score.push_back(num);
    int colN = high_score.size();

    // Compare to the rest of the column values, keep the highest

    while (true) {

      for (int j = 0; j < colN; j++) {
        inFile >> num;
        if (num > high_score[j]) high_score[j] = num;
      }

      if (inFile.peek() == '\n' || inFile.peek() == EOF) {
        inFile.ignore(3, '\n');
        break;
      }

      else inFile.ignore(3, '|');
    }

    for (auto i: high_score) cout << i << " ";
    cout << "\n";
    high_score.clear();
  }

  return(0);
}
