import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static class CostElement implements Comparable<CostElement> {
		
		public int index;
		public int value;
		
		public CostElement(int index, int value) {
			this.index = index;
			this.value = value;
		}

		@Override
		public int compareTo(CostElement o) {
			return this.value - o.value;
		}
		
		@Override
		public String toString() {
			return String.format("%d ", value);
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		int testCases = Integer.parseInt(reader.readLine());

		while(testCases > 0) {
			int money = Integer.parseInt(reader.readLine());
			int flavoursCount = Integer.parseInt(reader.readLine());
			String[] flavours = reader.readLine().split("\\s+");
			CostElement[] costs = new CostElement[flavoursCount];
			
			for(int i = 0; i < flavoursCount; ++i) {
				costs[i] = new CostElement(i, Integer.parseInt(flavours[i]));
			}
			
			Arrays.sort(costs);
			
			for(int i = 0, limit = flavoursCount - 1; i < limit; ++i) {
				int cost = money - costs[i].value;
				int index = Arrays.binarySearch(costs, i+1, flavoursCount, new CostElement(0, cost));
				if(index >= 0) {
					int left = costs[i].index + 1;
					int right = costs[index].index + 1;
					System.out.format("%d %d\n", Math.min(left, right), Math.max(left, right));
					break;
				}
			}
			
			testCases--;
		}
	}
}