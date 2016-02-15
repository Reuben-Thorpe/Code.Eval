// Reuben Thorpe (2016), CodeEval [Trick Or Treat v1.1]
// [key] vamp = 3, zomb = 4, witch = 5
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <iterator>
#include <string>

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
  // Calculates the share value from parsed data
  int result = 0;
  result += data[0]*3;
  result += data[1]*4;
  result += data[2]*5;
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
    vector<int> data = {0,0,0,0};
    data[0] = stoi(parse[1].substr(0, parse[1].size()-1));
    data[1] = stoi(parse[3].substr(0, parse[3].size()-1));
    data[2] = stoi(parse[5].substr(0, parse[5].size()-1));
    data[3] = stoi(parse[7]);
    calculate(data);
  }
  return(0);
}
