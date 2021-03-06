# Simpletron
> Simulates low-level assembly programming with built-in classes in C++

* Language: C++

## Installation
* The pre-compiled executable is compatible with Windows.*
With GCC on Windows, Mac OS X, and Unix systems:

```sh
g++ Simpletron.cpp exe_overview.cpp -o Simpletron
```

## Usage example

![Entering words into Simpletron](https://i.imgur.com/EwnH9Si.png)
![Simpletron execution and memory dump](https://i.imgur.com/ViNrCtn.png)

Enter operation codes (see ``OperationCodes`` for a full list) and target addresses into the terminal to initialize a program. After execution, all register and memory values are displayed.

## Release History
*Status: In progress*
* 1.0 (October 26, 2021)
    * First version: basic program structure and functions present
* 1.1 (October 31, 2021)
    * Separated main file into Simpletron.cpp and appropriate header files
* 1.2 (November 10, 2021)
	* Added CPSR flags and checks them to branch. Also added branchoverflow
* 1.21 (January 8, 2022)
	* Hotfix: Latest version now compiles without error
* 1.22 (January 11, 2022)
	* Additional bug fixes: Words are now properly stored without causing an early memdump.
* 1.3 (January 16, 2022)
	* Overflows trigger an alert without ending execution. Flags are properly updated.
* 1.4 (January 17, 2022)
	* End of execution memdump now also written into a file