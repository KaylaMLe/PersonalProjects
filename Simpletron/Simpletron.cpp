#include "exe_overview.h"
#include <iostream>
#include <iomanip>
#include <array>
using namespace runtime;

const size_t MEM_SIZE{ 100 };
processes prcs;

int main()
{
    int memory[MEM_SIZE]{0};

    // registers
    int accumulator{ 0 };
    int instructionRegister{ 0 };
    int instructionCounter{ 0 };
    int operationCode{ 0 };
    int operand{ 0 };

    std::cout << "*** Welcome to Simpletron! ***\n"
        << "*** Please enter your program one instruction ***\n\a"
        << "*** (or data word) at a time. I will type the ***\n"
        << "*** location number and a question mark (?). ***\n"
        << "*** You then type the word for that location. ***\n"
        << "*** Type the sentinel -99999 to stop entering ***\n"
        << "*** your program. ***\n" << std::endl;

    std::cout << std::setfill('0');

    for (int i{ 0 }; i < MEM_SIZE; i++) {
        do {
            // adds leading zero to digits
            std::cout << std::setw(2);
            std::cout << i;
            std::cout << std::setw(0);
            std::cout << " ? ";

            std::cin.clear();// allows iteration
            std::cin >> memory[i];
        } while ((memory[i] < -9999 || memory[i] > +9999) && memory[i] != -99999);

        // stop loading
        if (memory[i] == -99999) {
            memory[i] = 0;// code not stored
            std::cout << "\n*** Program loading completed ***\n" << "*** Program execution begins ***\n" << std::endl;
            prcs.execute(memory, accumulator, instructionCounter, instructionRegister, operationCode, operand);
            return 0;
        }
    }

    std::cout << "\n*** Program loading completed ***\n" << "*** Program execution begins ***\n" << std::endl;
    prcs.execute(memory, accumulator, instructionCounter, instructionRegister, operationCode, operand);
    return 0;
}