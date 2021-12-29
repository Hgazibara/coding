import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static String genSequence(int number, int repetitions) {
		StringBuilder builder = new StringBuilder();
		
		for(int i = 0; i < repetitions; ++i) {
			builder.append(number);
		}
		
		return builder.toString();
	}
	
	public static boolean isValid(int threes, int fives) {
		return (threes % 5 == 0) && (fives % 3 == 0);
	}
	
	public static void main(String[] args) 
			throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		int testCases = Integer.parseInt(reader.readLine());
		
		while(testCases > 0) {
			int digits = Integer.parseInt(reader.readLine());
			int threes = 0;
			int fives = digits;
			
			for(int i = 0; i < digits; ++i) {
				if(isValid(threes, fives)) {
					break;
				}
				++threes;
				--fives;
			}
			
			if(isValid(threes, fives)) {
				System.out.format("%s%s\n", genSequence(5, fives), genSequence(3, threes));
			} else {
				System.out.println(-1);
			}
			
			testCases--;
		}
	}
}