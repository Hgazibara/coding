import sys
import re
import io

input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
N = input_stream.readline()
pattern = re.compile(r'([a-zA-Z0-9_]+(?:\.[a-zA-Z0-9_]+)*@[a-zA-Z0-9_]+(?:\.[a-zA-Z0-9]+)*)')
emails = set()

for line in input_stream:
    for found in re.findall(pattern, line):
        emails.add(found)
        
print(';'.join(sorted(emails)))