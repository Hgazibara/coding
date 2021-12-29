T = int(input())
numbers_d = {
    0: True,
    1: True,
    2: True,
    3: True,
    5: True,
    8: True
}
numbers_l = [0,1,1,2,3,5,8]

def is_fibo(number, numbers_l, numbers_d):
    if number in numbers_d:
        return True
    else:
        if number < numbers_l[-1]:
            return False
        else:
            next = numbers_l[-1] + numbers_l[-2]
            numbers_l.append(next)
            numbers_d[next] = True
            
            if next == number:
                return True
            else:
                return is_fibo(number, numbers_l, numbers_d)

while T > 0:
    N = int(input())
    print('IsFibo' if is_fibo(N, numbers_l, numbers_d) else 'IsNotFibo')
    T -= 1