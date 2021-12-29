import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static final int MOD = 1234567;
    
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		int testCases = Integer.parseInt(reader.readLine());
		
		while(testCases > 0) {
			long ways = 1;
			int N = Integer.parseInt(reader.readLine());
			int[] towns = new int[N - 1];
			String[] inputs = reader.readLine().split("\\s+");
			
			for(int i = 0; i < (N - 1); i++) {
				towns[i] = Integer.parseInt(inputs[i]);
				ways = ((ways % MOD) * (towns[i] % MOD)) % MOD;
			}
			
			System.out.println(ways % MOD);
            --testCases;
		}
    }
}