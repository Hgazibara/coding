N = int(input())
records = {}

while N > 0:
    name, grades = input().strip().split(' ', 1)
    records[name] = [float(grade) for grade in grades.split()]
    N -= 1
    
target = input().strip()
print('{0:.2f}'.format(sum(records[target]) / len(records[target])))