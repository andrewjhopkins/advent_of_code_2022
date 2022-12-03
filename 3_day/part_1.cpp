#include <iostream>
#include <fstream>
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
    while (getline(infile, line)) {
      unordered_set<char> set;
    
      for (int i = 0; i < line.size() / 2; i++) {
        set.insert(line.at(i));
      }

      for (int i = line.size() / 2; i < line.size(); i++) {
        if(set.find(line.at(i)) != set.end()) {
          char letter = line.at(i);

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

    cout << output << "\n";
    return 0;
}
