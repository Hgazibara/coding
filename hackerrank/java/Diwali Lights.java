import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static final int MOD = 100000;
    
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		int testCases = Integer.parseInt(reader.readLine());
		
		while(testCases > 0) {
			int N = Integer.parseInt(reader.readLine());
			long ways = 1;
			
			for(int i = N; i > 0; i--) {
				ways = (ways * 2) % MOD;
			}
			
			System.out.println(ways - 1);
			--testCases;
		}
    }
}