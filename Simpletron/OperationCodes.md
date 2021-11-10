# Operation codes
> Prefix these to an address to form a word for the program to execute.

## Input/Output
| Basic function | Operation code | Description |
|----------------|----------------|-------------|
| read           | 10             | Reads user input into an address |
| write          | 11             | Writes user input into an address |

## Load and Store
| Basic function | Operation code | Description |
|----------------|----------------|-------------|
| load           | 20             | Loads word from an address to the accumulator |
| store          | 21             | Stores word from the accumulator to an address |

## Arithmetic
| Basic function | Operation code | Description |
|----------------|----------------|-------------|
| add            | 30             | Adds word from an address to the word in the accumulator |
| subtract       | 31             | Subtracts word from an address from the word in the accumulator |
| divide         | 32             | Divides the word in the accumulator by the word in an address |
| multiply       | 33             | Multiplies the accumulator by the word from the specified location in memory |

## Program control
| Basic function | Operation code | Description |
|----------------|----------------|-------------|
| branch         | 40             | Unconditionally branches |
| branchneg      | 41             | Branches if the negative flag is true |
| branchzero     | 42             | Branches if the zero flag is true |
| branchcarry    | 43             | Branches if the carry flag is true |
| branchoverflow | 44             | Branches if the overflow flag is true |
| halt           | 45             | End program execution |