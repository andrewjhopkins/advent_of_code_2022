#include <iostream>
#include <fstream>

using namespace std;
void checkAndAddNewMax(int ongoing, int max[]);

int main(int argc, char *argv[]) {

    if (argc < 2) {
        cout << "Usage: .exe <file input>\n";
        return 0;
    }

    ifstream infile(argv[1]);

    int max[3] = {0, 0, 0};
    int ongoing = 0;

    string line;
    while (getline(infile, line)) {
        if (line.size() != 0) {
            ongoing += stoi(line);
        }
        else {
            checkAndAddNewMax(ongoing, max);
            ongoing = 0;
        }
    }

    checkAndAddNewMax(ongoing, max);

    int output = 0;
    for (int i : max) {
        output += i;
    }

    cout << output << "\n";

    return 0;
}

void checkAndAddNewMax(int ongoing, int max[]) {
    int position = -1;
    for (int i = 2; i >= 0; i--) {
        if (ongoing >= max[i]) {
            position = i;
            break;
        }
    }

    if (position == -1) {
        return;
    }

    for(int i = 0; i < position; i++) {
        max[i] = max[i + 1];
    }

    max[position] = ongoing;
    return;
}
