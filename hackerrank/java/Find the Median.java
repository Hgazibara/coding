import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(reader.readLine());
		int[] numbers = new int[N];
		String[] inputNumbers = reader.readLine().split("\\s+");
		
		for(int i = 0; i < N; ++i) {
			numbers[i] = Integer.parseInt(inputNumbers[i]);
		}
		
		Arrays.sort(numbers);
		System.out.println(numbers[N/2]);
    }
}