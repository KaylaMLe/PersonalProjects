package testutils;

import java.util.Arrays;

import testutils.source.TestReadWrite;


/**
 * test class for verifying test interpretation capabilities
 */
public class ReadTest {
    /**
     * creates a test and prints out the arrays read from the text files
     * 
     * @param args test arr length, min element value, and max element value
     */
    public static void main(String[] args) {
        Integer length = args.length < 1 ? 10 : Integer.parseInt(args[0]);
        Integer minElem = args.length < 2 ? 0 : Integer.parseInt(args[1]);
        Integer maxElem = args.length < 3 ? 10 : Integer.parseInt(args[2]);

        String testFileName = TestReadWrite.make_test(length, minElem, maxElem);

        Integer[] readArr = TestReadWrite.read_test(testFileName);

        Integer[] testArr = new Integer[readArr.length / 2];
        System.arraycopy(readArr, 0, testArr, 0, testArr.length);

        Integer[] ansArr = new Integer[testArr.length];
        System.arraycopy(readArr, ansArr.length, ansArr, 0, ansArr.length);

        System.out.println(Arrays.toString(testArr));
        System.out.println(Arrays.toString(ansArr));
    }
}
