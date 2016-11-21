// Reuben Thorpe (2016), CodeEval [Compare Points v1.2]
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

string get_heading(long int& O, long int& P, long int& Q, long int& R);


int main (int argc, const char* argv[]) {
    ifstream in_file(argv[1]);
    long int O, P, Q, R;

    while (in_file >> O >> P >> Q >> R) {

        cout << get_heading(O, P, Q, R) << '\n';
    }
    return(0);
}


string get_heading(long int& O, long int& P, long int& Q, long int& R) {
    /*
    Generate the heading from one gps coordinate to the second. The second
    coordinate is transformed with the first so that its origin become
    (0,0). The cardinal direction is then simple to extrapolate.
    */

    long int x = Q - O;
    long int y = R - P;
    string heading;

    if (y > 0) heading += 'N';
    else if (y < 0) heading += 'S';

    if (x > 0) heading += 'E';
    else if (x < 0) heading += 'W';

    return((heading.size() == 0) ? "here" : heading);
}
