#include <iostream>
#include <fstream>
#include <vector>

using namespace std;
int main(int argc, char *argv[]) {

    if (argc < 2) {
        cout << "Usage: .exe <file input>\n";
        return 0;
    }

    vector<vector<int>> map;

    ifstream infile(argv[1]);

    string line;
    while (getline(infile, line)) {

      vector<int> row;
      for (int i = 0; i < line.size(); i++) {
        row.push_back(line.at(i) - '0');
      }
      map.push_back(row);
    }

    int output = (map.size() * 2) + ((map[0].size() - 2) * 2);

    for (int row = 1; row < map.size() - 1; row++) {
      for (int col = 1; col < map[row].size() - 1; col++) {

        bool rowPlus = true;
        bool rowMinus = true;
        bool colPlus = true;
        bool colMinus = true;

        for (int i = row + 1; i < map.size(); i++) {
          if (map[i][col] >= map[row][col]) {
            rowPlus = false;
            break;
          }
        }

        for (int i = row - 1; i >= 0; i--) {
          if (map[i][col] >= map[row][col]) {
            rowMinus = false;
            break;
          }
        }

        for (int i = col + 1; i < map[0].size(); i++) {
          if (map[row][i] >= map[row][col]) {
            colPlus = false;
            break;
          }
        }

        for (int i = col - 1; i >= 0; i--) {
          if (map[row][i] >= map[row][col]) {
            colMinus = false;
            break;
          }
        }

        if (rowPlus || rowMinus || colPlus || colMinus) {
          output += 1;
        }
      }
    }

    cout << output << "\n";
    return 0;
}
