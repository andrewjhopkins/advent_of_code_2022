#include <iostream>
#include <fstream>
#include <cmath>
#include <map>
#include <string>

using namespace std;
int main(int argc, char *argv[]) {

    if (argc < 2) {
        cout << "Usage: .exe <file input>\n";
        return 0;
    }

    map<string, int> output;

    ifstream infile(argv[1]);

    int hx = 0;
    int hy = 0;

    int tx = 0;
    int ty = 0;

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

        hx += xAdder;
        hy += yAdder;

        if (round(sqrt(pow((hx - tx), 2) + pow((hy - ty), 2))) > 1) {
          if (hx == tx) {
            if (hy > ty) {
              ty += 1;
            }
            else {
              ty -= 1;
            }
          }
          else if (hy == ty) {
            if (hx > tx) {
              tx += 1;
            }
            else {
              tx -= 1;
            }
          }

          else if (hx > tx && hy > ty) {
            tx += 1;
            ty += 1;
          }
          else if (hx > tx && hy < ty) {
            tx += 1;
            ty -= 1;
          }
          else if (hx < tx && hy > ty) {
            tx -= 1;
            ty += 1;
          }
          else if (hx < tx && hy < ty) {
            tx -= 1;
            ty -= 1;
          }
        }

        string key = to_string(tx) + " " + to_string(ty);
        output[key] = 0;
      }
    }

    cout << output.size() << "\n";
    return 0;
}
