// Reuben Thorpe (2016), CodeEval [Email Validation v1.1]
// This currently does not work in gcc 4.8 but is a complete solution in 4.9
#include <iostream>
#include <fstream>
#include <regex>

using namespace std;


int main(int argc, char* argv[]) {
  cout << std::boolalpha;
  ifstream in_file(argv[1]);
  string line;
  regex email_validation(R"(^"[a-z|A-Z|0-9|_|-|+|.|@]+"|[a-z|A-Z|0-9|_|-|+|.?]*@{1}[a-z|0-9]+\.{1}[a-z|0-9|-]+\.?[a-z|0-9|-]{2,})");


  while (getline(in_file, line)) {
    cout << regex_match(line, email_validation) << '\n';
  }

  return(0);
}
