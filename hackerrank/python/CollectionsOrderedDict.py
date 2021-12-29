import collections

N = int(input())
items = collections.OrderedDict()

for n in range(N):
    item, price = input().rsplit(maxsplit=1)
    
    if item in items:
        items[item] += int(price)
    else:
        items[item] = int(price)

for item in items:
    print('{} {}'.format(item, items[item]))
