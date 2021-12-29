import collections

a_size, b_size = map(int, input().split())

a_words = collections.defaultdict(list)

for i in range(a_size):
    word = input()
    a_words[word].append(i + 1)

for i in range(b_size):
    word = input()
    
    if word in a_words:
        print(' '.join(map(str, a_words[word])))
    else:
        print(-1)
