/* Sample program illustrating input and output */

import java.util.*;
import java.io.*;

class Solution{
    public static class SortedList {
		private int[] elements;
		private int size;
		
		private static final int MAX_SIZE = 100000;
		
		public SortedList() {
			elements = new int[MAX_SIZE];
		}
		
		public void add(int element) {
			elements[size] = element;
			
			// Move element to the correct position
            int i = size - 1;
            while(i >= 0 && elements[i] > element){
                elements[i + 1] = elements[i];
                i = i - 1;
            }
            elements[i + 1] = element;
            size += 1;
		}
		
		public int find(int element) {
			return size < 1 ? -1 : Arrays.binarySearch(elements, 0, size, element);
		}
		
		public int get(int position) throws IndexOutOfBoundsException {
			return elements[position];
		}
		
		public void remove(int element) {
			int position = find(element);
			
			if(position < 0) {
				 throw new IllegalArgumentException("Element not found");
			}
			
			// Move all elements to fill the space
			elements[position] = 0;
			for(int i = position + 1; i < size; ++i) {
				int tmp = elements[i];
				elements[i] = elements[i-1];
				elements[i-1] = tmp;
			}
			size -= 1;
			
			if(size == 0) {
				 throw new IllegalArgumentException("List is empty");
			}
		}
		
		public int size() {
			return size;
		}
		
		@Override
		public String toString() {
			StringBuilder output = new StringBuilder();
			
			for(int i = 0; i < size; ++i) {
				output.append(elements[i]);
			}
			
			return output.toString();
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(reader.readLine().trim());
		SortedList sortedList = new Solution.SortedList();
		
		for(int i = 0; i < N; ++i) {
			String[] input = reader.readLine().split("\\s+");
			Integer number = Integer.parseInt(input[1].trim());
			
			if(input[0].trim().equals("r")) {
				 try{
					sortedList.remove(number);
					 printMedian(sortedList);
				 } catch(IllegalArgumentException e) {
					System.out.println("Wrong!");
				 }
			} else {
				sortedList.add(number);
				 printMedian(sortedList);
			}
		}
	}
	
	public static void printMedian(SortedList sortedList) {
		int size = sortedList.size();
		
		if(size % 2 == 0) {
			int right = size / 2;
			int left = right - 1;
			double calc = sortedList.get(left)/2. + sortedList.get(right)/2.;
			
			if(calc == (int)calc) {
				System.out.println((int)calc);
			} else {
				System.out.println(String.format("%f", calc).replaceAll("0*$", ""));
			}
			
		} else {
			System.out.println(sortedList.get(size / 2));
		}
	}
}