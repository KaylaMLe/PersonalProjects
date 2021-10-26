#include <iostream>
#include <iomanip>
#include <array>

int execute(int memory[], int accumulator, int instructionCounter, int instructionRegister, int operationCode, int operand);
bool matherror(int memory[], int accumulator, int operationCode, int operand);
void memdump(int memory[], int accumulator, int instructionCounter, int instructionRegister, int operationCode, int operand);

const size_t MEM_SIZE{ 100 };

int main()
{
    int memory[MEM_SIZE]{ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

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
            execute(memory, accumulator, instructionCounter, instructionRegister, operationCode, operand);
            return 0;
        }
    }

    std::cout << "\n*** Program loading completed ***\n" << "*** Program execution begins ***\n" << std::endl;
    execute(memory, accumulator, instructionCounter, instructionRegister, operationCode, operand);
    return 0;
}
// execute sml
// return codes
//// 0: normal run
//// 1: invalid operation code
//// 2: integer underflow
//// 3: integer overflow
//// 4: divide by 0
int execute(int memory[], int accumulator, int instructionCounter, int instructionRegister, int operationCode, int operand) {
    // all possible operation codes
    enum validCode{read = 10, write = 11, // io
        load = 20, store = 21, // load store
        add = 30, subtract = 31, divide = 32, multiply = 33, // math
        branch = 40, branchneg = 41, branchzero = 42, halt = 43};// transfer of control
    
    while (instructionCounter < MEM_SIZE) {
        instructionRegister = memory[instructionCounter];
        operand = instructionRegister % 100;

        // "a specific location in memory" = memory[operand]
        switch (operationCode = instructionRegister / 100) {
        // input output
        case read:
            std::cout << "? ";
            std::cin.clear();
            std::cin >> memory[operand];
            
            // error catch
            if (memory[operand] < -9999) {
                std::cout << "\n*** Integer underflow at " << std::setw(2) << std::noshowpos << operand << " ***\n" 
                    << "*** Simpletron execution abnormally terminated ***\n" << std::endl;
                memdump(memory, accumulator, instructionCounter, instructionRegister, operationCode, operand);
                return 2;
            }

            if (memory[operand] > 9999) {
                std::cout << "\n*** Integer overflow at " << std::setw(2) << std::noshowpos << operand << " ***\n"
                    << "*** Simpletron execution abnormally terminated ***\n" << std::endl;
                memdump(memory, accumulator, instructionCounter, instructionRegister, operationCode, operand);
                return 3;
            }

            instructionCounter++;
            break;
        case write:
            std::cout << std::setw(2) << std::noshowpos << operand << ": " << std::setw(5) << std::showpos << std::internal << memory[operand] << std::endl;
            instructionCounter++;
            break;
        // load and store
        case load:
            accumulator = memory[operand];
            instructionCounter++;
            break;
        case store:
            memory[operand] = accumulator;
            instructionCounter++;
            break;
        // arithmetic
        case add:
            accumulator += memory[operand];
            instructionCounter++;

            if (matherror(memory, accumulator, operationCode, operand)) {
                memdump(memory, accumulator, instructionCounter, instructionRegister, operationCode, operand);
                return 3;
            }

            break;
        case subtract:
            accumulator -= memory[operand];
            instructionCounter++;

            if (matherror(memory, accumulator, operationCode, operand)) {
                memdump(memory, accumulator, instructionCounter, instructionRegister, operationCode, operand);
                return 2;
            }

            break;
        case divide:
            accumulator /= memory[operand];
            instructionCounter++;

            if (matherror(memory, accumulator, operationCode, operand)) {
                memdump(memory, accumulator, instructionCounter, instructionRegister, operationCode, operand);
                return 4;
            }

            break;
        case multiply:
            accumulator *= memory[operand];
            instructionCounter++;

            if (matherror(memory, accumulator, operationCode, operand)) {
                memdump(memory, accumulator, instructionCounter, instructionRegister, operationCode, operand);
                return 2;
            }

            break;
        // transfer of control
        case branch:
            instructionCounter = operand;
            break;
        case branchneg:
            if (accumulator < 0) {
                instructionCounter = operand;
            }
            break;
        case branchzero:
            if (accumulator == 0) {
                instructionCounter = operand;
            }
            break;
        case halt:
            std::cout << "\n*** Simpletron execution terminated ***\n" << std::endl;
            memdump(memory, accumulator, instructionCounter, instructionRegister, operationCode, operand);
            return 0;
        // invalid op code error
        default:
            std::cout << "\n*** Invalid operation code ***\n" << "*** Simpletron execution abnormally terminated ***\n" << std::endl;
            memdump(memory, accumulator, instructionCounter, instructionRegister, operationCode, operand);
            return 1;
        }
    }
}

// checks for errors in arithmetic operations
bool matherror(int memory[], int accumulator, int operationCode, int operand) {
    if (accumulator < -9999) {// too low
        std::cout << "\n*** Accumulator underflow at " << std::setw(2) << std::noshowpos << operand << " ***\n" 
            << "*** Simpletron execution abnormally terminated ***\n" << std::endl;
        return true;
    }
    else if (accumulator > 9999) {// too high
        std::cout << "\n*** Accumulator overflow at " << std::setw(2) << std::noshowpos << operand << " ***\n"
            << "*** Simpletron execution abnormally terminated ***\n" << std::endl;
        return true;
    }
    else if (operationCode == 32 && memory[operand] == 0) {// divide by zero
        std::cout << "\n*** Attempt to divide by zero at " << std::setw(2) << std::noshowpos << operand << " ***\n" 
            << "*** Simpletron execution abnormally terminated ***\n" << std::endl;
        return true;
    }
    else {
        return false;
    }
}

// displays registries and memory
void memdump(int memory[], int accumulator, int instructionCounter, int instructionRegister, int operationCode, int operand) {
    std::cout << "REGISTER:\n" << "accumulator\t\t" << std::setw(5) << std::showpos << std::internal << accumulator << std::endl
        << "instructionCounter\t" << std::setw(2) << std::noshowpos << instructionCounter << std::endl
        << "instructionRegister\t" << std::setw(5) << std::showpos << instructionRegister << std::endl
        << "operationCode\t\t" << std::setw(2) << std::noshowpos << operationCode << std::endl
        << "operand\t\t\t" << std::setw(2) << std::noshowpos << operand << std::endl << std::endl;

    std::cout << "MEMORY:\n" << "\t0" << "\t1" << "\t2" << "\t3" << "\t4" << "\t5" << "\t6" << "\t7" << "\t8" << "\t9" << std::endl;

    for (int i{ 0 }; i < 10; i++) {// ten rows
        std::cout << std::setw(0) << std::noshowpos << i * 10 << "\t";

        for (int j{ 0 }; j < 10; j++) {// ten columns
            std::cout << std::setw(5) << std::showpos << std::internal << memory[j + (i * 10)] << "\t";// column plus row
        }

        std::cout << std::endl;
    }
}