#include <iostream>
#include <fstream>

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
      string firstPair = line.substr(0, line.find(','));
      string secondPair = line.substr(line.find(',') + 1, line.size());

      int firstLow = stoi(firstPair.substr(0, firstPair.find('-')));
      int firstHigh = stoi(firstPair.substr(firstPair.find('-') + 1, firstPair.size()));
      
      int secondLow = stoi(secondPair.substr(0, secondPair.find('-')));
      int secondHigh = stoi(secondPair.substr(secondPair.find('-') + 1, secondPair.size()));

      if (firstLow <= secondLow && firstHigh >= secondHigh || secondLow <= firstLow && secondHigh >= firstHigh) {
        output += 1;
      }
    }

    cout << output << "\n";
    return 0;
}
