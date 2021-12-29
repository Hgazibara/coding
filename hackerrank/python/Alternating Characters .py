for t in range(int(input())):
    testcase = input()
    print(sum(map(lambda a,b: a==b, testcase[:-1], testcase[1:])))