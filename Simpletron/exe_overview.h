#ifndef EXE_OVERVIEW_H
#define EXE_OVERVIEW_H

namespace runtime
{
	class processes
	{
	public:
		int execute(int memory[], int accumulator, int PC, int instructionRegister, int operationCode, int operand);
		void updateFlags(int accumulator);
		bool matherror(int memory[], int accumulator, int operationCode, int operand);
		void memdump(int memory[], int accumulator, int PC, int instructionRegister, int operationCode, int operand);
	private:
		bool CPSR[4]{ false };// negative zero carry overflow
	};
}
#endif // !EXE_OVERVIEW_H