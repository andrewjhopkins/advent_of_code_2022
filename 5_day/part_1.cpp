#include <cctype>
#include <iostream>
#include <fstream>
#include <vector>
#include <stack>

using namespace std;
int main(int argc, char *argv[]) {

    if (argc < 2) {
        cout << "Usage: .exe <file input>\n";
        return 0;
    }

    vector<vector<char>> input;
    ifstream infile(argv[1]);

    string line;
    while (getline(infile, line)) {
      if (isdigit(line.at(1))) {
        break;
      }
      vector<char> lineChars;

      for (int i = 1; i < line.size(); i += 4) {
        lineChars.push_back(line.at(i));
      }
      input.push_back(lineChars);
    }

    vector<stack<char>> stacks;

    for (int i = 0 ; i < input[0].size(); i++) {
      stack<char> newStack;
      stacks.push_back(newStack);
    }

    for (int i = input.size() - 1; i >= 0; i--) {
      for (int j = 0; j < input[i].size(); j++) {

        if (isalpha(input[i][j])) {
          stacks[j].push(input[i][j]);
        }

      }
    }

    vector<vector<int>> moves;

    while (getline(infile, line)) {
      if (line.size() > 0 && line.at(0) == 'm') {
        vector<int> move;

        unsigned first = line.find("move ") + 4;
        unsigned last = line.find(" from");
        move.push_back(stoi(line.substr(first, last - first)));

        first = line.find("from ") + 5;
        last = line.find(" to");
        move.push_back(stoi(line.substr(first, last - first)));

        first = line.find("to ") + 3;
        move.push_back(stoi(line.substr(first, line.size())));

        moves.push_back(move);
      }
    }

    for (int i = 0; i < moves.size(); i++) {
      int amount = moves[i][0];
      int from = moves[i][1] - 1;
      int to = moves[i][2] - 1;

      for (int j = 0; j < amount; j++) {
        if (!stacks[from].empty()) {
          stacks[to].push(stacks[from].top());
          stacks[from].pop();
        }
      }
    }

    for (int i = 0; i < stacks.size(); i++) {
      cout << stacks[i].top();
    }
    cout << "\n";

    return 0;
}
