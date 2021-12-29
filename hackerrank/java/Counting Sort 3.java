import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		HashMap<Integer, Integer> freqs = new HashMap<Integer, Integer>();
		int[] sums = new int[100];
		String input = reader.readLine();
		
		while((input = reader.readLine()) != null) {
			String[] in = input.split("\\s+");
			Integer key = Integer.parseInt(in[0]);
			freqs.put(key, freqs.containsKey(key) ? freqs.get(key) + 1 : 1);
		}
		
		for(int i = 0; i < 100; i++) {
			for(int j = 0; j <= i; j++) {
				sums[i] += freqs.containsKey(j) ? freqs.get(j) : 0;
			}
            System.out.format("%d ", sums[i]);
		}
    }
}