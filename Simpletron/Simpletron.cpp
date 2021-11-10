// TODO:
// overflow but not crash
// display CPSR when memdumping
// Warning	C4715	'runtime::processes::execute': not all control paths return a value
// implement carry flag
// optimize opcode checking during execution (impractical and slow to check an entire case/switch of every code)
// rework to register 0 - 16
// use string-based words (enumerate?)
// enable reading/writing to files (.s or .txt?)

#include "exe_overview.h"
#include <iostream>
#include <iomanip>
#include <array>
using namespace runtime;

const size_t MEM_SIZE{ 100 };
processes prcs;

int main()
{
    int memory[MEM_SIZE]{ 0 };

    // registers
    int accumulator{ 0 }, int instructionRegister{ 0 }, int PC{ 0 }, int operationCode, int operand{ 0 };

    std::cout << "\a*** Welcome to Simpletron! ***\n"// note the \a
        << "*** Please enter your program one instruction ***\n"
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
        } while ((memory[i] < -9999 || memory[i] > +9999) && memory[i] != -99999);// if not a four digit integer, re-prompt

        // stop loading when memory[i] == -99999
        memory[i] = 0;// stop code not stored
        std::cout << "\n*** Program loading completed ***\n" << "*** Program execution begins ***\n" << std::endl;
        prcs.execute(memory, accumulator, PC, instructionRegister, operationCode, operand);
        return 0;
    }

    std::cout << "\n*** Program loading completed ***\n" << "*** Program execution begins ***\n" << std::endl;
    prcs.execute(memory, accumulator, PC, instructionRegister, operationCode, operand);
    return 0;
}