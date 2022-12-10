#include <iostream>
#include <fstream>
#include <map>
#include <vector>


using namespace std;
int handleCycle(int i, int x, int &toFind, map<int, int> addMap, vector<int> &sums);

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
    int toFind = 20;

    vector<int> sums;

    while (getline(infile, line)) {

      if (line.at(0) == 'a') {
        int addValue = stoi(line.substr(line.find(" ") + 1, line.size()));
        addMap[i + 2] = addValue;
        i += 1;
        x = handleCycle(i, x, toFind, addMap, sums);

        i += 1;
        x = handleCycle(i, x, toFind, addMap, sums);
        
      }
      else {
        i += 1;
        x = handleCycle(i, x, toFind, addMap, sums);
      }
    }

    int output = 0;

    for (int i : sums) {
      output += i;
    }

    cout << output << "\n";

    return 0;
}

int handleCycle(int i, int x, int &toFind, map<int, int> addMap, vector<int> &sums) {
  int returnVal;
  

  if (addMap.find(i) != addMap.end()) {
    returnVal = x + addMap[i];
  }
  else {
    returnVal = x;
  }

  if (i == toFind) {
    sums.push_back(returnVal * i);
    toFind += 40;
  }

  return returnVal;
}
