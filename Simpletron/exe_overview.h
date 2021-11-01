#ifndef EXE_OVERVIEW_H
#define EXE_OVERVIEW_H

namespace runtime
{
	class processes
	{
	public:
		int execute(int memory[], int accumulator, int instructionCounter, int instructionRegister, int operationCode, int operand);
		bool matherror(int memory[], int accumulator, int operationCode, int operand);
		void memdump(int memory[], int accumulator, int instructionCounter, int instructionRegister, int operationCode, int operand);
	};
}
#endif // !EXE_OVERVIEW_H