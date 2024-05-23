import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;


class Result {

    /*
     * Complete the 'getShrunkArray' function below.
     *
     * The function is expected to return a STRING_ARRAY.
     * The function accepts following parameters:
     *  1. STRING_ARRAY inputArray
     *  2. INTEGER burstLength
     */
     
    static class Pair {
    String str;
    int count;

    Pair (String str, int count) {
        this.str = str;
        this.count = count;
    }
}


    public static List<String> getShrunkArray(List<String> inputArray, int burstLength) {

    int n = inputArray.size();
    List<String> outputArray = new ArrayList<String>();
    
    Stack<Pair> stk = new Stack<Pair>();

    int count = 1;
    for (int i = 0; i < n; i++) {
        if (stk.isEmpty()) {
            stk.push(new Pair(inputArray.get(i), 1));
        }
        else if ((stk.peek().str).equals(inputArray.get(i))) {
            count = stk.peek().count + 1;
            stk.push(new Pair(inputArray.get(i), count));
            if (count >= burstLength) {
                while (count-- > 0) {
                    stk.pop();
                }
            }
        }
        else {
            stk.push(new Pair(inputArray.get(i), 1));
        }
    }
    for (int i = 0; i < stk.size(); i++) {
        outputArray.add(stk.get(i).str);
    }

    return outputArray;
    }
}
public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int inputArrayCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<String> inputArray = new ArrayList<>();

        for (int i = 0; i < inputArrayCount; i++) {
            String inputArrayItem = bufferedReader.readLine();
            inputArray.add(inputArrayItem);
        }

        int burstLength = Integer.parseInt(bufferedReader.readLine().trim());

        List<String> result = Result.getShrunkArray(inputArray, burstLength);

        for (int i = 0; i < result.size(); i++) {
            bufferedWriter.write(result.get(i));

            if (i != result.size() - 1) {
                bufferedWriter.write("\n");
            }
        }

        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
