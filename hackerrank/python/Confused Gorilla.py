def get_pairs(x, N):
	if N % 2 == 0 and x == N//2:
		return [(x, x)]
	else:
		return [(x, N - x), (N - x, x)]


for t in range(int(input())):
	N = int(input())
	
	for x in range(N//2 + 1):
		for x, y in get_pairs(x, N):
			print('{0} {1}'.format(x, y))