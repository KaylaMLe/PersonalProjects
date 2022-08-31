#include "simpletron-processing.h"
#include <fstream>
#include <string>
#include <vector>
#include <iostream>

std::vector<std::string> openTxtFile(std::ifstream &sourceFile)
{
    std::string thisLine;
    std::vector<std::string> wholeFile;

    while (getline(sourceFile, thisLine))
    {
        wholeFile.push_back(thisLine);
    }

    return wholeFile;
}

void executeFile(std::vector<std::string> wholeFile)
{
    processor thisProcessor;

    for (int i = 0; i < wholeFile.size(); i++)
    {
        // in a line, finds the first substring before the first space
        int firstSpace = wholeFile[i].find_first_of(' ');
        std::string instruction = wholeFile[i].substr(0, firstSpace);
        std::string args = wholeFile[i].substr(firstSpace + 1, wholeFile[i].length() - (firstSpace + 1));

        // TODO: is a switch-case like series of if statements optimal here?
        if (instruction == "mov")
        {
            int firstDigit = findFirst('r', args) + 1;
            int firstComma = args.find_first_of(',');

            // TODO: implement mov
        }
    }
}

// case-insensitive version of find_first_of for a single char
// still returns std::string::npos if a match isn't found
int findFirst(char thisChar, std::string searchInHere)
{
    int firstInd = searchInHere.find_first_of(thisChar);

    if (firstInd == std::string::npos)
    {
        if (isupper(thisChar))
        {
            firstInd = searchInHere.find_first_of(tolower(thisChar));
        }
        else if (islower(thisChar))
        {
            firstInd = searchInHere.find_first_of(toupper(thisChar));
        }
    }

    return firstInd;
}