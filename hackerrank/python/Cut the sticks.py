N = int(input())
lengths = [int(x) for x in input().split()]

while any([x != 0 for x in lengths]):
    print(sum([1 for x in lengths if x != 0]))
    min_x = min([x for x in lengths if x != 0])
    lengths = [x - min_x if x != 0 else 0 for x in lengths]