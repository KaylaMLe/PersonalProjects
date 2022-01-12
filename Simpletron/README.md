# Simpletron
> Simulates low-level assembly programming with built-in classes in C++

* Language: C++

## Installation

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
<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki