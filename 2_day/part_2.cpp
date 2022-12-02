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

    map<char, string> moveGuide;
    moveGuide = {{'A', "rock"}, {'X', "rock"}, {'B', "paper"}, {'Y', "paper"}, {'C', "scissors"}, {'Z', "scissors"}};

    map<string, string> loseGuide;
    loseGuide = {{"rock", "scissors"}, {"paper", "rock"}, {"scissors", "paper"}};

    map<string, string> winGuide;
    winGuide = {{"rock", "paper"}, {"paper", "scissors"}, {"scissors", "rock"}};

    map<string, int> score;
    score = {{"rock", 1}, {"paper", 2}, {"scissors", 3}};

    int output = 0;

    string line;
    while (getline(infile, line)) {

      if (line.size() > 0) {
        char oponent = line.at(0);
        char ending = line.at(2);

        string player;

        if (ending == 'X') {
          player = loseGuide[moveGuide[oponent]];
          output += score[player];
        }
        else if (ending == 'Y') {
          output += score[moveGuide[oponent]] + 3;
        }
        else {
          player = winGuide[moveGuide[oponent]];
          output += score[player] + 6;
        }
      }
    }

    cout << output << "\n";
    return 0;
}
