import sys

N = sys.stdin.readline()
counter = 0

for tweet in sys.stdin:
    if 'hackerrank' in tweet.lower():
        counter += 1
        
print(counter)