N = int(input())
ratings = [int(input()) for __ in range(N)]

candies = [1] * N

for i in range(1, N):
    if ratings[i] > ratings[i - 1]:
        candies[i] = candies[i - 1] + 1

for i in reversed(range(N - 1)):
    if ratings[i] > ratings[i + 1]:
        candies[i] = max(candies[i], candies[i + 1] + 1)

print(sum(candies))