import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		
		int testCases = Integer.parseInt(reader.readLine());
		
		String line;
		while((line = reader.readLine()) != null) {
			int N = Integer.parseInt(line);
			System.out.println(N + 1);
		}
    }
}