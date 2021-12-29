import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		int testCases = Integer.parseInt(reader.readLine());
		
		while(testCases > 0) {
			int N = Integer.parseInt(reader.readLine());
			System.out.println(N * (N - 1) / 2);
			--testCases;
		}
    }
}