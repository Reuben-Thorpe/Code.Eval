// Reuben Thorpe (2016), CodeEval [Time To Eat v1.2]
#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

int main(int argc, char* argv[]) {
  ifstream inFile(argv[1]);
  string date;
  vector<string> dates;
  dates.reserve(20);  // max(N) = 20

  while(inFile.peek() != EOF) {

    while ((inFile.peek() != '\n') && inFile >> date) {
      dates.push_back(date);
    }

    sort(dates.begin(), dates.end());
    reverse(dates.begin(), dates.end());

    for(auto i: dates) {
      cout << i << " ";
    }
    cout << '\n';

    inFile.get(); // Removes '/n' from istream
    dates.clear();
  }
  return(0);
}
