#include <iostream>
#include <fstream>
#include <cmath>
#include <map>
#include <string>
#include <vector>

using namespace std;
int main(int argc, char *argv[]) {

    if (argc < 2) {
        cout << "Usage: .exe <file input>\n";
        return 0;
    }

    map<string, int> output;

    ifstream infile(argv[1]);

    vector<int> x{0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    vector<int> y{0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

    string line;
    while (getline(infile, line)) {
      char instruction = line.at(0);
      int magnitude = stoi(line.substr(line.find(" ") + 1, line.size()));

      int xAdder = 0;
      int yAdder = 0;

      switch (instruction) {
        case 'R':
          xAdder = 1;
          break;
        case 'L':
          xAdder = -1;
          break;
        case 'U':
          yAdder = 1;
          break;
        case 'D':
          yAdder = -1;
          break;
      }

      for (int i = 0; i < magnitude; i++) {

        x[0] += xAdder;
        y[0] += yAdder;

        for (int i = 0; i < x.size() - 1; i++) {
          if (round(sqrt(pow((x[i] - x[i + 1]), 2) + pow((y[i] - y[i + 1]), 2))) > 1) {
            if (x[i] == x[i + 1]) {
              if (y[i] > y[i + 1]) {
                y[i + 1] += 1;
              }
              else {
                y[i + 1] -= 1;
              }
            }
            else if (y[i] == y[i + 1]) {
              if (x[i] > x[i + 1]) {
                x[i + 1] += 1;
              }
              else {
                x[i + 1] -= 1;
              }
            }

            else if (x[i] > x[i + 1] && y[i] > y[i + 1]) {
              x[i + 1] += 1;
              y[i + 1] += 1;
            }
            else if (x[i] > x[i + 1] && y[i] < y[i + 1]) {
              x[i + 1] += 1;
              y[i + 1] -= 1;
            }
            else if (x[i] < x[i + 1] && y[i] > y[i + 1]) {
              x[i + 1] -= 1;
              y[i + 1] += 1;
            }
            else if (x[i] < x[i + 1] && y[i] < y[i + 1]) {
              x[i + 1] -= 1;
              y[i + 1] -= 1;
            }
          }
        }

        string key = to_string(x[x.size() - 1]) + " " + to_string(y[y.size() - 1]);
        output[key] = 0;
      }
    }

    cout << output.size() << "\n";
    return 0;
}

