// Reuben Thorpe (2016), CodeEval [Point In Circle v1.1]
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <math.h>

using namespace std;

float distance(float x1, float y1, float x2, float y2);


int main(int argc, char* argv[]) {
  ifstream in_file(argv[1]);
  string line;
  float center_x, center_y, radius, point_x, point_y;
  cout << boolalpha;

  while(getline(in_file, line)) {

    sscanf(line.c_str(),
           "Center: (%f, %f); Radius: %f; Point: (%f, %f)",
           &center_x, &center_y, &radius, &point_x, &point_y);

    cout << (distance(center_x, center_y, point_x, point_y) < radius) << '\n';
  }

  return(0);
}


float distance(float x1, float y1, float x2, float y2) {
  // Measure the distance between two points.
  return(sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2)));
}
