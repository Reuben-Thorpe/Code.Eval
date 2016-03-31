// Reuben Thorpe (2016), CodeEval [As Quick As A Flash v1.1]
#include <iostream>
#include <sstream>
#include <vector>
#include <fstream>

using namespace std;

int q_sort_pivots(vector<int> seq, int begin, int end);
void swap(int& a, int& b);


int main(int argc, char* argv[]) {
  ifstream inFile(argv[1]);
  vector<int> seq;
  seq.reserve(30); // Maximum number of elements
  int num, N;
  string line;

  while (getline(inFile, line)) {
    stringstream ss;
    ss.str(line);
    while (ss >> num) seq.push_back(num);
    N = seq.size() - 1;
    cout << q_sort_pivots(seq, 0, N) << "\n";
    seq.clear();
  }

  return(0);
}


int q_sort_pivots(vector<int> seq, int begin, int end) {
  if (begin < end) {
    int pivot = seq[begin];
    int pivot_pos = begin;
    int left = begin+1;
    int right = end;

    while (left < right) {
      while (left < right && seq[right] >= pivot) right--;

      if (seq[right] < pivot) {
        swap(seq[pivot_pos], seq[right]);
        pivot_pos = right;
      }

      if (left < right) {
        while (left < right && seq[left] <= pivot) left++;

        if (seq[left] > pivot) {
          swap(seq[pivot_pos], seq[left]);
          pivot_pos = left;
        }
      }
    }

    return(1 + q_sort_pivots(seq, begin, pivot_pos-1) +
           q_sort_pivots(seq, pivot_pos+1, end));
  }
  else return(0);
}


void swap(int& a, int& b) {
  int tmp = a;
  a = b;
  b = tmp;
}
