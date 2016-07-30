// Reuben Thorpe (2016), CodeEval [Distinc Triangels v1.1]
/*
 Parts of this code where re-written in python from the link below
 http://www.geeksforgeeks.org/number-of-triangles-in-a-undirected-graph/
*/

#include <bits/stdc++.h>
#include <fstream>
#include <vector>

using namespace std;


void multiply_sqr_matrix(vector<vector<int>> A, vector<vector<int>> B, vector<vector<int>>& C) {
  // Utility function for matrix multiplication
  int V = A[0].size();

  for (int i = 0; i < V; i++) {
    for (int j = 0; j < V; j++) {
      for (int k = 0; k < V; k++) {
        C[i][j] += A[i][k]*B[k][j];
      }
    }
  }
}


int get_trace(vector< vector<int> > graph) {
  // Utility function to calculate trace of a matrix (sum of diagnonal elements)
  int trace = 0;
  int V = graph[0].size();

  for (int i = 0; i < V; i++) {
    trace += graph[i][i];
  }
  return(trace);
}


int triangles_in_graph(vector< vector<int> > graph) {
  // Utility function for calculating number of triangles in graph
  int vertices = graph[0].size();
  vector< vector<int> > aux2;
  aux2.reserve(vertices);
  vector< vector<int> > aux3;
  aux3.reserve(vertices);

  // Initialising aux matrices with 0
  int count = 0;
  vector<int> empty_set(vertices, 0);

  while (count < vertices) {
    aux2.push_back(empty_set);
    aux3.push_back(empty_set);
    count++;
  }

  // aux2 is now graph^2
  multiply_sqr_matrix(graph, graph, aux2);

  // aux3 is now graph^3
  multiply_sqr_matrix(graph, aux2, aux3);

  int trace = get_trace(aux3);
  return(trace / 6);
}

vector< vector<int> > parse_line(string line) {
  // Parse each line of the codeEval problem set, convert to adj matrix.
  stringstream ss;
  ss.str(line);

  int x, y, V, count = 0;
  ss >> V;
  vector< vector<int> > result;
  vector<int> empty_set(V, 0);

  while (count < V) {
    result.push_back(empty_set);
    count++;
  }

  ss.ignore(10, ';');
  while (ss >> x >> y) {
    //cout << x << " : " << y << "\n";
    result[x][y] = result[y][x] = 1;
    ss.ignore(2, ',');
  }

  return(result);

}


int main (int argc, char* argv[]) {

  ifstream in_file(argv[1]);
  vector< vector<int> > graph;
  string line;

  while (getline(in_file, line)){
    graph = parse_line(line);
    cout << triangles_in_graph(graph) << "\n";
  }

  return(0);
}

