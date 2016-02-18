// Reuben Thorpe (2016), CodeEval [Trick Or Treat v1.1]
// [key] vamp = 3, zomb = 4, witch = 5
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <iterator>

using namespace std;


vector<string> split(string line) {
  // Splits string by whitespaces, returns vector<string>
  istringstream iss(line);
  vector<string> parse;
  copy(istream_iterator<string>(iss),
       istream_iterator<string>(),
       back_inserter(parse));
  return(parse);
}

void calculate(vector<int>& data) {
  // Calculates the share value from parsed values
  int result = 0;
  for(int i = 0; i < 3; i++) {
      result += data[i]*(i+3);
  }
  result *= data[3];

  result = result/(data[0] + data[1] + data[2]);
  cout << result << "\n";

}


int main(int argc, char* argv[]) {
  ifstream file(argv[1]);
  string line;
  vector<string> parse; 
  while(getline(file, line)) {
    parse = split(line);
    vector<int> values = {0,0,0,0};
    int i = 1;
    for(int ii = 0; i < 3; i++) {
      values[ii] = stoi(parse[i].substr(0, parse[i].size()-1));
      i += 2;
    }
    values[3] = stoi(parse[7]);
    calculate(values);
  }
  return(0);
}
