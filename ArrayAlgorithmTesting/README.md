# Array algorithm testing
> Testing utilities for array sorting and selection algorithms

* Language: Java

Resources for writing the unsorted and sorted versions of lists of random
numbers to a text file and reading them back into arrays.

## Use
After compiling the .class file with the provided batch script or by using:

    javac .\ArrayAlgorithmTesting\testutils\source\TestReadWrite.java

you can create a text file with the original array in the first row and its
sorted version in the second row with the following command.

    java ArrayAlgorithmTesting.testutils.source [array length] [min value,
    inclusive] [max value, exclusive]

You can then import the test reading function to parse a test .txt and return
the original and sorted arrays concatenated with:

    import testutils.source.TestReadWrite;

ReadTest uses the test creation and reading functions to create a new test .txt,
read the arrays from it, and prints them to the terminal to visually show that
the test handling functions work properly.

## Release History
*Status: In progress*
* 1.0 (April 28, 2023)
  * Copied files from classwork and added a README with usage instructions