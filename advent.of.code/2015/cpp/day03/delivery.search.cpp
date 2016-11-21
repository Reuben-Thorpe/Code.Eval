//Reuben Thorpe (2015) 3rd December Advent of Code C++11
#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <sstream>

using namespace std;

void jump (char move, int pos[], set<string>& ledger){
  switch(move){
    case '<': --pos[0]; break;
    case '>': ++pos[0]; break;
    case '^': ++pos[1]; break;
    case 'v': --pos[1]; break;
    }
  ledger.insert(to_string(pos[0]) + ',' + to_string(pos[1]));
}


int main() {
  ifstream input("input.txt");
  set<string> ledger_1, ledger_2;

  if (input.is_open()){
    stringstream buffer;
    buffer << input.rdbuf();
    input.close();
    int position [2] = {0,0}, santa_position [2] = {0,0}, robot_position [2] = {0,0};
    char move;
    bool santa;

    while (buffer >> move){

      //Part 1
      jump(move, position, ledger_1);

      //Part 2
      if (santa){
        jump(move, santa_position, ledger_2);
        santa = false;
      }
      else{
        jump(move, robot_position, ledger_2);
        santa = true;
      }

    }

    cout << "\nPart 1 = " << ledger_1.size() << "\n";
    cout << "Part 2 = " << ledger_2.size() << "\n\n";
  }
  return 0;
}
