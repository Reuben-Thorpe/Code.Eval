// Reuben Thorpe (2016), CodeEval [Longest Lines v1.2]
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char* argv[]) {
    string line;
    ifstream file(argv[1]);
    getline(file, line);
    int n = stod(line);
    vector<string> results(n+1, "");
    results.pop_back();
    auto it = results.begin();

    while(getline(file, line)) {
        for (int i = 0; i < n; i++) {
            if (results[i].length() < line.length()) {
                results.insert(it+i, line);
                results.pop_back();
                break;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        cout << results[i] << "\n";
    }

    return(0);
}
