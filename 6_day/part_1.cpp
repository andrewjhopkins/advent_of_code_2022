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

    string line;
    getline(infile, line);

    int window_start = 0;

    map<char, int> charIndex;

    for (int window_end = 0; window_end < line.size(); window_end++) {
      char currentChar = line.at(window_end);

      if (charIndex.find(currentChar) != charIndex.end() && charIndex[currentChar] >= window_start) {
        window_start = charIndex[currentChar] + 1;
      }

      charIndex[currentChar] = window_end;

      if ((window_end - window_start + 1) == 4) {
        cout << window_end + 1 << "\n";
        return 0;
      }
    }

    return 0;
}
