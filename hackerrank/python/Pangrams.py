import collections
import string

counter = collections.Counter(c.lower() for c in input().rstrip())

for key in string.ascii_lowercase + ' ':
    if not key in counter:
        print('not pangram')
        break
else:
    print('pangram')