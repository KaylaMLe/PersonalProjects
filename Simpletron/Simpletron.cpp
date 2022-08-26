#include <fstream>
#include <iostream>
using namespace std;

int main()
{
    // asks the user to specify a file to run
    ifstream sourceFile;
    string sourceFilePath;

    while (!(sourceFile.is_open()))
    {
        cout << "Path to source file: ";
        cin >> sourceFilePath;
        sourceFile.open(sourceFilePath, std::fstream::in | std::fstream::out);
        cin.clear();
    }

    cout << "file opened";

    return 0;
}