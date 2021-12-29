for t in range(int(input())):
    N, K = [int(x) for x in input().split()]
    times = [int(x) for x in input().split()]
    print('YES' if len([x for x in times if x <= 0]) < K else 'NO')