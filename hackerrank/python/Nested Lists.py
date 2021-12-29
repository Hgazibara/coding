N = int(input())

grades = {}

while N > 0:
    name, grade = input(), float(input())
    grades[grade] = grades.get(grade, []) + [name]
    N -= 1
    
target = sorted(grades.keys())[1]
print('\n'.join(sorted(grades[target])))