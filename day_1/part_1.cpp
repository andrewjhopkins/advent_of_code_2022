#include <iostream>
#include <fstream>

using namespace std;
int main(int argc, char *argv[]) {

    if (argc < 2) {
        cout << "Usage: .exe <file input>\n";
        return 0;
    }

    ifstream infile(argv[1]);

    int output = 0;
    int ongoing = 0;

    string line;
    while (getline(infile, line)) {
        if (line.size() != 0) {
            ongoing += stoi(line);
        }
        else {
            output = max(output, ongoing);
            ongoing = 0;
        }
    }

    output = max(output, ongoing);

    cout << output << "\n";
    return 0;
}
