# Operation codes
> Prefix these to an address to form a word for the program to execute.

## Input/Output
| Basic function | Operation code | Description |
|----------------|-----------------|--------------|
| read               | 10                    | Reads user input into specified address |
| write              | 11                    | Writes user input into specified address |

## Load and Store
| Basic function | Operation code | Description |
|----------------|-----------------|--------------|
| load             | 20             | Loads word from specified address to the accumulator |
| store          | 21             | Stores word from the accumulator in the specified address |

## Arithmetic
| Basic function | Operation code | Description |
|----------------|----------------|-------------|
| add            | 30             | Adds word from the specified address to the word in the accumulator |
| subtract       | 31             | Subtracts word from the specified address from the word in the accumulator |
| divide         | 32             | Divides the word in the accumulator by the word in the specified address |
| multiply       | 33             | Multiplies the accumulator by the word from the specified location in memory |

## Program control
| Basic function | Operation code | Description |
|----------------|----------------|-------------|
| branch         | 40             | Unconditionally branches to the specified location in memory |
| branchneg      | 41             | Branches to the specified location in memory if the accumulator is negative |
| branchzero     | 42             | Branches to the specified location in memory if the accumulator is zero |
| halt           | 43             | End program execution |