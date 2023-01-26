#include "simpletron-processing.h"
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main()
{

    ifstream sourceFile;
    string sourceFilePath{""};
    // asks the user to specify a file to run until a valid txt file is given
    while (!(sourceFile.is_open()) || sourceFilePath.length() < 3 || sourceFilePath.substr(sourceFilePath.length() - 4, 4) != ".txt")
    {
        cout << "Path to source file: ";
        cin >> sourceFilePath;
        sourceFile.open(sourceFilePath, std::fstream::in | std::fstream::out);
        cin.clear();
    }

    vector<string> opened = openTxtFile(sourceFile);
    sourceFile.close();
    executeFile(opened);

    return 0;
}