#include "simpletron-processing.h"
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cmath>

int findFirst(char thisChar, std::string searchInHere);
std::vector<std::string> strToVector(std::string wholeString, std::string limiters);

std::string node::getNodeType()
{
    return nodeType;
}

std::string node::getValue()
{
    return value;
}

std::vector<node> node::getChildNodes()
{
    return childNodes;
}

void node::addChildNode(node newChild)
{
    childNodes.push_back(newChild);
}

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

// case-insensitive version of find_first_of for a single alphabetic char
// still returns std::string::npos if a match isn't found
int findFirst(char thisChar, std::string searchInHere)
{
    int firstInd = searchInHere.find_first_of(thisChar);

    if (firstInd == std::string::npos && isalpha(thisChar))
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

node parseInstruction(std::string codeLine)
{
    codeLine.erase(std::remove_if(codeLine.begin(), codeLine.end(), !isalnum));
    std::vector<std::string> lineParts = strToVector(codeLine, " ");

    node root = node(lineParts[0]);
    root.addChildNode(node(lineParts[1]));
    root.addChildNode(node(lineParts[2]));
}

std::vector<std::string> strToVector(std::string wholeString, std::string limiters)
{
    std::vector<std::string> wordsList;
    int wordBegin{0};
    int wordEnd = wholeString.find_first_of(limiters);
    // while there is another limiter in the string, find and add the next word
    while (wordEnd != std::string::npos)
    {
        std::string thisWord = wholeString.substr(wordBegin, wordEnd - wordBegin);

        if (thisWord.length() > 0)
        {
            wordsList.push_back(thisWord);
        }

        wordBegin = wordEnd++;
        wordEnd = wholeString.find_first_of(limiters, wordBegin);
    }
    // if there is a word at the end of the string, add it to the list
    if (wordBegin + 1 < wholeString.length())
    {
        wordsList.push_back(wholeString.substr(wordBegin));
    }

    return wordsList;
}

std::string instructionFormat(std::string someWord)
{
    if (someWord == "mo")
}
