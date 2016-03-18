// Reuben Thorpe (2016), CodeEval [As Quick As A Flash v1.1]
#include <iostream>
#include <sstream>
#include <vector>
#include <fstream>

using namespace std;


class qSort {

  public:
    int pivot_count = 0;
    qSort(vector<int>& seq);

  private:
    void quick_sort(vector<int> seq, int begin, int end);
    void swap(int& a, int& b);

};


int main(int argc, char* argv[]) {
  ifstream inFile(argv[1]);
  vector<int> seq;
  seq.reserve(30); // Maximum number of elements
  int num;
  string line;

  while (getline(inFile, line)) {
    stringstream ss;
    ss.str(line);
    while (ss >> num) seq.push_back(num);
    cout << qSort(seq).pivot_count << "\n";
    seq.clear();
  }

  return(0);
}


qSort::qSort(vector<int>& seq) {
  int N = seq.size() - 1;
  quick_sort(seq, 0, N);
}


void qSort::quick_sort(vector<int> seq, int begin, int end) {
  if (begin < end) {
    pivot_count += 1;
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

    quick_sort(seq, begin, pivot_pos-1);
    quick_sort(seq, pivot_pos+1, end);
  }
}

void qSort::swap(int& a, int& b) {
  int tmp = a;
  a = b;
  b = tmp;
}
