#include "simpletron-processing.h"
#include <fstream>
#include <string>

std::string openTxtFile(std::ifstream &sourceFile)
{
    std::string thisLine;
    std::string wholeFile;

    while (getline(sourceFile, thisLine))
    {
        wholeFile += thisLine;
    }

    return wholeFile;
}