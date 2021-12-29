import sys
import re
import io

input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
N = input_stream.readline()
pattern = re.compile(r'http(?:s|)://[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*')
urls = set()

def strip_prefix(string, prefix):
    if string.startswith(prefix):
        string = string[len(prefix):]
    return string

def strip_prefixes(string, prefixes):
    for prefix in prefixes:
        string = strip_prefix(string, prefix)
    return string
    

for line in input_stream:
    for found in re.findall(pattern, line):
        # move both prefixes and everything after first /
        found = strip_prefixes(found, ['https://', 'http://', 'www.', 'ww2.'])
        if '/' in found:
            found = found[0:found.index('/')]
        urls.add(found)
        
print(';'.join(sorted(urls)))