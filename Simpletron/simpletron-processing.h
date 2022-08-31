#include <fstream>
#include <vector>
#include <string>

std::vector<std::string> openTxtFile(std::ifstream &sourceFile);
void executeFile(std::vector<std::string> wholeFile);

class processor
{
public:
    void mov(int registerNumber, std::string value);

private:
    std::string registers[16];
};