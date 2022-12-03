#include <iostream>
#include <fstream>
#include <map>
#include <unordered_set>

using namespace std;
int main(int argc, char *argv[]) {

    if (argc < 2) {
        cout << "Usage: .exe <file input>\n";
        return 0;
    }

    int output = 0;
    ifstream infile(argv[1]);

    string line;
    int lineNum = 0;
    map<char, int> frequency;

    while (getline(infile, line)) {
      if (lineNum % 3 == 0) {
        frequency.clear();
      }

      lineNum += 1;
      unordered_set<char> seen;

      for (int i = 0; i < line.size(); i++) {
        char letter = line.at(i);

        if (seen.find(letter) == seen.end()) {
          seen.insert(letter);
          frequency[letter] += 1;

          if (frequency[letter] == 3) {
            // uppercase
            if (int(letter) <= 90) {
              output += (int(letter) - 64 + 26);
            } 
            // lowercase
            else {
              output += (int(letter) - 96);
            }
            break;
          }
        }
      }
    }

    cout << output << "\n";
    return 0;
}
