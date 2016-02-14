#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>
#include <string>


const float PHI = 1.61803398874989484820;
const float SQRT5 = sqrt(5);

float fib(float n) {
    return(( (pow(PHI, n) - pow(-PHI, -n)) / SQRT5 ));
    }


int main(int argc, char* argv[]) {
  std::string line;
  std::ifstream file(argv[1]);
  std::stringstream buffer;
  buffer << file.rdbuf();
  while (getline(buffer, line)) {
    std::cout << fib(std::stod(line)) << "\n";
  }
  return 0;
}
