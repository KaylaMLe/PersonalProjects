# Simpletron
> Simulates low-level assembly programming with built-in classes in C++

* Language: C++

## Installation
With GCC on Windows and Unix systems:

```sh
g++ Simpletron.cpp exe_overview.cpp -o Simpletron
```

## Release History
*Status: In progress*
* 1.0 (October 26, 2021)
   * First version: basic program structure and functions present
* 1.1 (October 31, 2021)
  * Separated main file into Simpletron.cpp and appropriate header files
* 1.20 (November 10, 2021)
  * Added CPSR flags and checks them to branch. Also added branchoverflow
* 1.21 (January 8, 2022)
  * Hotfix: Latest version now compiles without error
* 1.22 (January 11, 2022)
  * Additional bug fixes: Words are now properly stored without causing an early memdump.
* 1.3 (January 16, 2022)
  * Overflows trigger an alert without ending execution. Flags are properly updated.
* 1.4 (January 17, 2022)
  * End of execution memdump now also written into a file
* 2.0 (August 26, 2022)
  * Started some major fixes to better align with the project's goal and use better software engineering practices
* 2.01 (August 31, 2022)
  * Implemented text file processing to better ease use and testing. I'm going to shift focus to creating an abstract syntax tree to help build an understanding of how ARM assembly is compiled (compiled? executed?) and make implementing features of ARM assembly easier.