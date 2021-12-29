import sys
import re

all_lines = [line.replace('\n', '') for line in sys.stdin.readlines()]

# number of sentences and sentences themselves
N = int(all_lines[0])
sentences = all_lines[1:N+1]

# number of words and words itself
T = int(all_lines[N+1])
words = all_lines[N+2:]

for word in words:
    counter = 0
    for sentence in sentences:
        counter += len(re.findall('(?:(?<=[^a-zA-Z_])|(?<=^))'+word+'(?=[^a-zA-Z_]|$)', sentence))
    print(counter)