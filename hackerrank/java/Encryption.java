import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static class Encoder {
		
		public static char[][] createRectangle(String message) {
			int messageLength = message.length();
			int dimensions[] = findDimensions(message);
			char[][] rectangle = new char[dimensions[0]][dimensions[1]];
			
			int iter = 0;
			
			for(int i = 0; i < dimensions[0]; ++i) {
				for(int j = 0; j < dimensions[1]; ++j) {
					if(iter == messageLength) { break; }
					rectangle[i][j] = message.charAt(iter);
					iter += 1;
				}
			}
			
			return rectangle;
		}
		
		public static String encode(String message) {
			StringBuilder output = new StringBuilder();
			char[][] rectangle = createRectangle(message);
			
			for(int j = 0, cols = rectangle[0].length; j < cols; ++j) {
				for(int i = 0, rows = rectangle.length; i < rows; ++i) {
					if(rectangle[i][j] != '\0') {
						output.append(rectangle[i][j]);
					}
				}
				output.append(' ');
			}
			
			return output.toString();
		}
		
		public static int[] findDimensions(String message) {
			int messageLength = message.length();
			int lower = (int)Math.floor(Math.sqrt(messageLength));
			int upper = (int)Math.ceil(Math.sqrt(messageLength));
			int[] dimensions = new int[2];
			boolean found = false;
			
			for(int i = lower; i <= upper; ++i) {
				for(int j = lower; j <= upper; ++j) {
					if(i*j >= messageLength) {
						dimensions[0] = i;
						dimensions[1] = j;
						found = true;
						break;
					}
				}
				if(found == true) { break; }
			}
			
			return dimensions;
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		System.out.println(Encoder.encode(reader.readLine()));
	}
}