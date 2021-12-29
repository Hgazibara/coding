/* Sample program illustrating input/output methods */
import java.util.*;
import java.io.*;

class Solution{
    public static void main( String args[] ) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		
		// First line of input
		String[] NK = reader.readLine().split("\\s+");
		int N = Integer.parseInt(NK[0]);
		int K = Integer.parseInt(NK[1]);
		
		// Second line of input
		String[] cs = reader.readLine().split("\\s+");
		int[] costs = new int[N];
		for(int i = 0; i < N; i++) {
			costs[i] = Integer.parseInt(cs[i]);
		}
		
		Arrays.sort(costs);
		int[] flowersPerPerson = new int[K];
		int totalCost = 0;
		
		// Compute
		for(int i = N - 1; i >= 0; --i) {
			int min = Integer.MAX_VALUE;
			int cost = 0;
			int person = 0;
			
			for(int j = 0; j < K; ++j) {
				cost = (flowersPerPerson[j] + 1) * costs[i];
				if(cost < min) {
					min = cost;
					person = j;
				}
			}
			
			flowersPerPerson[person] += 1;
			totalCost += cost;
		}
		
		System.out.println(totalCost);
    }
}