N = int(input())
marks_column = input().split().index('MARKS')
marks = [int(input().split()[marks_column]) for _ in range(N)]
print(sum(marks) / len(marks))
