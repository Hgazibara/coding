import sys
import re

patterns = {
    'C': [
        r'#include .*?',
        r'int main',
        r'scanf',
        r'printf',
        r'#define'
    ],
    'Java': [
        r'import .*?;',
        r'class',
        r'public|protected|private',
        r'throws',
        r'String\[\] args'
    ],
    'Python': [
        r'import [^;]+$',
        r'# .*?'
        r'\[.*?:.*?\]',
        r'print .*?',
        r'find'
    ]
}

snippet = sys.stdin.read()
counters = {'C': 0, 'Java': 0, 'Python': 0}

for lang in patterns:
    for pattern in patterns[lang]:
        counters[lang] += len(re.findall(pattern, snippet))
        
print(sorted(counters.items(), key=lambda t:t[1], reverse=True)[0][0])