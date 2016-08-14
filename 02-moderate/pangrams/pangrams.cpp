// Reuben Thorpe (2016), CodeEval [Pangrams v1.1]
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

string missing_lowercase_ascii_alpha(string line, string &alpha_lower);


int main(int argc, char* argv[]) {
  ifstream in_file(argv[1]);
  string line;
  string alpha_lower = "abcdefghijklmnopqrstuvwxyz";

  while (getline(in_file, line)) {
  cout << missing_lowercase_ascii_alpha(line, alpha_lower) << '\n';
  }

  return(0);
}


string missing_lowercase_ascii_alpha(string line, string &alpha_lower) {
  // Determin what letters from the lowercase ascii are missing from the string.

  transform(line.begin(), line.end(), line.begin(), ::tolower);
  sort(line.begin(), line.end());
  auto last = unique(line.begin(), line.end());
  line.erase(last, line.end());
  line.erase(line.begin(), line.begin()+1);

  string solution;

  set_difference(alpha_lower.begin(), alpha_lower.end(), line.begin(),
                 line.end(), back_inserter(solution));

  if (solution.empty()) return("NULL");
  else return(solution);

}


