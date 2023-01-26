#include <fstream>
#include <vector>
#include <string>

std::vector<std::string> openTxtFile(std::ifstream &sourceFile);
void executeFile(std::vector<std::string> wholeFile);
std::string instructionFormat(std::string someWord);

class processor
{
public:
    void mov(int registerNumber, std::string value);

private:
    std::string registers[16];
};

class node
{
public:
    node(std::string newValue)
    {
        value = newValue;
        nodeType = "node"; // might not be necessary
    };

    std::string getNodeType();
    std::string getValue();
    std::vector<node> getChildNodes();
    void addChildNode(node newChild);

private:
    std::string nodeType;
    std::string value;
    std::vector<node> childNodes;
};