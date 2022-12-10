#include <iostream>
#include <fstream>
#include <map>
#include <vector>


using namespace std;
int handleCycle(int i, int x, map<int, int> addMap, vector<char> &pixels);

int main(int argc, char *argv[]) {

    if (argc < 2) {
        cout << "Usage: .exe <file input>\n";
        return 0;
    }

    ifstream infile(argv[1]);

    map<int, int> addMap;

    string line;
    int i = 1;
    int x = 1;

    vector<char> pixels;

    while (getline(infile, line)) {
      if (line.at(0) == 'a') {
        int addValue = stoi(line.substr(line.find(" ") + 1, line.size()));
        addMap[i + 2] = addValue;
        i += 1;
        x = handleCycle(i, x, addMap, pixels);

        i += 1;
        x = handleCycle(i, x, addMap, pixels);
      }
      else {
        i += 1;
        x = handleCycle(i, x, addMap, pixels);
      }
    }

    return 0;
}

int handleCycle(int i, int x, map<int, int> addMap, vector<char> &pixels) {
  int returnVal;

  if (addMap.find(i) != addMap.end()) {
    returnVal = x + addMap[i];
  }
  else {
    returnVal = x;
  }

  if (pixels.size() >= x - 1 && pixels.size() <= x + 1) {
    pixels.push_back('#');
  }
  else {
    pixels.push_back('.');
  }

  if (pixels.size() == 40) {
    for (char i : pixels) {
      cout << i;
    }
    cout << "\n";
    pixels.clear();
  }

  return returnVal;
}
