import sys
import re

all_lines = [x.replace('\n', '') for x in sys.stdin.readlines()]

# input lines
N = int(all_lines[0])
lines = all_lines[1:N+1]

# test cases
T = int(all_lines[N+1])
words = all_lines[N+2:]

for word in words:
	words_sum = 0
	for line in lines:
		words_sum += len(re.findall(word, line)) + len(re.findall(word.replace('ze', 'se'), line))
	print(words_sum)