package testutils.source;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.time.format.DateTimeFormatter;
import java.time.LocalDateTime;
import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;


/**
 * handles testing functions, including test generation and reading into arrays
 */
public class TestReadWrite {
    /**
     * parses command line args for test generation
     * 
     * @param args test arr length, min element value, and max element value
     */
    public static void main(String args[]) {
        Integer length = args.length < 1 ? 10 : Integer.parseInt(args[0]);
        Integer minElem = args.length < 2 ? 0 : Integer.parseInt(args[1]);
        Integer maxElem = args.length < 3 ? 10 : Integer.parseInt(args[2]);

        TestReadWrite.make_test(length, minElem, maxElem);
    }

    /**
     * generates a random integer array and its sorted version then writes both
     * to a text file
     * 
     * @param length length of the test array
     * @param minElem minimum value of elements (inclusive)
     * @param maxElem maximum value of elements (exclusive)
     * 
     * @return the path to the file generated
     * 
     * @throws IOException if an error occurs during file creation, writing, or
     * closing
     */
    public static String make_test(
            Integer length, Integer minElem, Integer maxElem) {
        Integer[] unsortedElems = make_int_arr(length, minElem, maxElem);
        
        // Array sorting is in ascending order by default
        Integer[] sortedElems = unsortedElems.clone();
        Arrays.sort(sortedElems);

        DateTimeFormatter ymdhms = DateTimeFormatter.ofPattern(
            "yyyyMMddHHmmss");
        LocalDateTime now = LocalDateTime.now();

        String name = String.format(
            "./testarr/test%d_%s.txt", length, ymdhms.format(now));

        try {
            FileWriter newTest = new FileWriter(name);

            newTest.write(int_arr_to_str(unsortedElems) + '\n');
            newTest.write(int_arr_to_str(sortedElems));

            newTest.close();
        } catch(IOException e) {
            System.out.println(e);
            return "";
        }

        return name;
    }

    // generates an integer array of the given specifications 
    private static Integer[] make_int_arr(
        Integer length, Integer minElem, Integer maxElem) {
        Integer[] unsortedInts = new Integer[length];
        Random nextInList = new Random();

        for (int i = 0; i < length; i++){
            unsortedInts[i]
                = nextInList.nextInt(maxElem - minElem) + minElem;
        }

        return unsortedInts;
    }

    // converts an integer array to a space seperated string
    private static String int_arr_to_str(Integer[] arr) {
        String strList = "";

        for (int i = 0; i < arr.length; i++) {
            strList += Integer.toString(arr[i]) + ' ';
        }

        return strList.trim();
    }

    /**
     * reads a test text file and returns the initial test and sorted solution
     * 
     * @param pathToTest the filepath to the .txt of the test
     * @return an array containing the elements of the test followed by the
     * same elements in order
     */
    public static Integer[] read_test(String pathToTest) {
        String testLine;
        String solutionLine;

        try {
            File testFile = new File(pathToTest);
            Scanner reader = new Scanner(testFile);

            testLine = reader.nextLine();
            solutionLine = reader.nextLine();

            reader.close();
        } catch (FileNotFoundException e) {
            System.out.println(e);
            return new Integer[0];
        }

        String[] testArr = testLine.split("\s", 0);
        String[] solutionArr = solutionLine.split("\s", 0);
        Integer[] returnArr = new Integer[testArr.length * 2];

        for (int i = 0; i < returnArr.length; i++) {
            returnArr[i] = i < testArr.length ? Integer.parseInt(testArr[i])
                : Integer.parseInt(solutionArr[i - solutionArr.length]);
        }

        return returnArr;
    }
}