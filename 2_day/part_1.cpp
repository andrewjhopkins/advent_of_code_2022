#include <iostream>
#include <fstream>
#include <map>

using namespace std;
int main(int argc, char *argv[]) {

    if (argc < 2) {
        cout << "Usage: .exe <file input>\n";
        return 0;
    }

    ifstream infile(argv[1]);

    map<char, char> moveGuide;
    moveGuide = {{'X', 'A'}, {'Y', 'B'}, {'Z', 'C'}};

    map<char, char> winGuide;
    winGuide = {{'X', 'C'}, {'Y', 'A'}, {'Z', 'B'}};

    map<char, int> score;
    score = {{'X', 1}, {'Y', 2}, {'Z', 3}};

    int output = 0;

    string line;
    while (getline(infile, line)) {

      if (line.size() > 0) {
        char oponent = line.at(0);
        char player = line.at(2);

        output += score[player];

        if (moveGuide[player] == oponent) {
          output += 3;
        }
        else if (winGuide[player] == oponent) {
          output += 6;
        }
      }
    }

    cout << output << "\n";
    return 0;
}
