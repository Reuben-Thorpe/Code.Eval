#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;

void parse_problem(string line, vector<char> &puzzle, int &N);
bool is_valid_sudoku(vector<char> &puzzle, int N);


int main(int argc, char* argv[]) {
  ifstream in_file(argv[1]);
  string line;

  while (getline(in_file, line)) {
    vector<char> puzzle;
    int N;

    parse_problem(line, puzzle, N);

    if (is_valid_sudoku(puzzle, N))  cout << "True\n";
    else cout << "False\n";
  }

  return(0);
}


void parse_problem(string line, vector<char> &puzzle, int &N) {
  // Parse CodeEval each set a time for Sudoku.
  stringstream sstr(line);
  char num;
  sstr >> N;
  sstr.ignore();
  puzzle.reserve(N*N);

  while (sstr >> num) {
    puzzle.push_back(num);
    sstr.ignore();
  }
}


bool is_valid_sudoku(vector<char> &puzzle, int N) {
  // Check whether a matrix is a valid sudoku entry, only valid for N={3, 9}.
  int quadrant_size;

  if (N == 9) quadrant_size = 3;
  else if (N == 4) quadrant_size = 2;

  vector<int> rowTrack(N, 0), colTrack(N, 0), boxTrack(N, 0);

  for (int i = 0; i < puzzle.size(); i++) {
    int row = i / N;
    int col = i - (row * N);
    int boxRow = row / quadrant_size;
    int boxCol = col / quadrant_size;
    int box = (boxRow*quadrant_size) + boxCol;

    int value = puzzle[i] - '0';

    int mask = 1 << value;

    if ((rowTrack[row] & mask)!=0) return(false);
    if ((colTrack[col] & mask)!=0) return(false);
    if ((boxTrack[box] & mask)!=0) return(false);

    rowTrack[row] += mask;
    colTrack[col] += mask;
    boxTrack[box] += mask;
  }	
  return(true);
}


