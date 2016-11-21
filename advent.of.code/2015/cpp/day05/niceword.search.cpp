//Reuben Thorpe (2015) 5th December Advent of Code C++11
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <array>

using namespace std;


int countSubstring(const string& str, const string& sub) {
  //count non-overlapping occurrences of substring in string
  int count = 0;
  for (size_t offset = str.find(sub); offset != string::npos;
              offset = str.find(sub, offset + sub.length())) {
    ++count;
  }
  return count;
}


int main() {
  int niceword_1 = 0, niceword_2 = 0;
  ifstream input("./input.txt");

  if (input.is_open()) {
    stringstream buffer_1, buffer_2;
    buffer_1 << input.rdbuf();
    input.seekg(0,input.beg);
    buffer_2 << input.rdbuf();
    input.close();
    string rule_1 = "aeiou", line;
    array<string,4> rule_3 = {"ab", "cd", "pq", "xy"};

    //Part 1
    while (getline(buffer_1, line)) {
      bool flag_1 = false, flag_2 = false, flag_3 = true;
      int vowels = 0;

      //Part 1.1
      for (int i = 0; i < rule_1.length(); i++) {
        vowels += count(line.begin(), line.end(), rule_1[i]);
        if (vowels >= 3) {
          flag_1 = true;
          break;
        }
      }
      if (!flag_1) {continue;}

      //Part 1.2
      for (int i = 0; i < (line.length()-1); i++) {
        if (line[i] == line[i+1]) {
          flag_2 = true;
          break;
        }
      }
      if (!flag_2) {continue;}

      //Part 1.3
      for (int i = 0; i < rule_3.size(); i++) {
        if (line.find(rule_3[i]) != string::npos) {
          flag_3 = false;
          break;
        }
      }
      if (!flag_3) {continue;}

      ++niceword_1;
    }

    //Part 2
    while (getline(buffer_2, line)) {
      bool flag_1 = false, flag_2 = false;
      string rule_1;

      //Part 2.1
      for (int i = 0; i < line.length()-1; i++) {
        rule_1 = string(1, line[i]) + string(1, line[i+1]);
        if (countSubstring(line, rule_1) >= 2) {
          flag_1 = true;
          break;
        }
      }
      if (!flag_1) {continue;}

      //Part 2.2
      for (int i =0; i < line.length()-2; i++) {
        if (line[i] == line[i+2]) {
          flag_2 = true;
          break;
        }
      }
      if (!flag_2) {continue;}

      ++niceword_2;
    }

  }
  cout << "\nPart 1 = " << niceword_1 << "\n";
  cout << "Part 2 = " << niceword_2 << "\n\n";
  return 0;
}
