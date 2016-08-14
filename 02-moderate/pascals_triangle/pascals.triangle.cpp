// Reuben Thorpe (2016), CodeEval [Pascals Triangle v1.1]
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> parse_problem(ifstream &in_file);
vector<string> generate_pascals_triangle(int depth);
void print_problem(int depth, vector<string> &master_triangle);


int main(int argc, char* argv[]) {
  ifstream in_file(argv[1]);
  int num;
  vector<string> master_triangle;
  master_triangle.reserve(20);
  vector<int> problem_set = parse_problem(in_file);

  int max_value = *max_element(problem_set.begin(), problem_set.end());

  master_triangle = generate_pascals_triangle(max_value);

  for(auto num: problem_set) {
    print_problem(num, master_triangle);
  }
  return(0);
}


vector<int> parse_problem(ifstream &in_file) {
  // Parse CodeEval problem set for Pascals Triangle.
  int num;
  vector<int> problem_set;
  problem_set.reserve(20);

  while (in_file >> num) {
    problem_set.push_back(num);
    in_file.ignore();
  }

  return(problem_set);
}


void print_problem(int depth, vector<string> &master_triangle) {
  // Print a problem set in the correct format.
  for (int i = 0; i < (depth - 1); i++) {
    cout << master_triangle[i];
  }

  cout << master_triangle[depth-1].substr(0, master_triangle[depth-1].size() - 1);
  cout << '\n';
}


vector<string> generate_pascals_triangle(int depth) {
  // Generate a Pascals Triangle of depth n.
  vector<string> pascals_triangle;
  pascals_triangle.reserve(depth);

  for (int n = 0; n < depth; n++) {
    vector<int> line = {1};
    line.reserve(n);

    for (int k = 0; k < n; k++) {
      line.push_back(line[k] * (n-k) / (k+1));
    }

    string formated_line;
    for (auto num: line) {
      formated_line += to_string(num) + " ";
    }

    pascals_triangle.push_back(formated_line);
  }

  return(pascals_triangle);
}
