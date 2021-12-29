import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		Pattern hyperlink = Pattern.compile("<a\\b[^>]*>(.*?)<\\/a>");
		Pattern title = Pattern.compile(">(.*?)<");
		Pattern link = Pattern.compile("href=\"(.*?)\"");
		String line;
		
		int lines = Integer.parseInt(reader.readLine());
		
		while((line = reader.readLine()) != null) {
			Matcher matcher = hyperlink.matcher(line);
			
			while(matcher.find()) {
				Matcher m1 = title.matcher(matcher.group());
				Matcher m2 = link.matcher(matcher.group());
				
				String titleMatch = "";
				String linkMatch = "";
				
				while(m1.find()) {
					String found = m1.group(1);
					if(found.length() > titleMatch.length()) {
						titleMatch = found;
					}
				}
				
				while(m2.find()) {
					String found = m2.group(1);
					if(found.length() > linkMatch.length()) {
						linkMatch = found;
					}
				}
				
				System.out.format("%s,%s\n", linkMatch.trim(), titleMatch.trim());
			}
		}
	}
}