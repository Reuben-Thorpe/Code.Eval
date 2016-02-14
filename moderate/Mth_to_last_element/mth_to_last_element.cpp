// Reuben Thorpe (2016) mth to last element v1.1

#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <iterator>
#include <vector>

using namespace std;

int main(int argc, char* argv[]) {
    string line;
    int index = 0;
    vector<string> parse;
    ifstream file(argv[1]);

    while(getline(file, line)) {
        istringstream iss(line);
        copy(istream_iterator<string>(iss),
             istream_iterator<string>(),
             back_inserter(parse));

        index = stod(parse.back());
        parse.pop_back();
        index = parse.size() - index;
        if (index >= 0) {
            cout << parse[index] << "\n";
        }
        parse.clear();
    }

    return(0);
}
