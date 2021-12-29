import sys

T = int(sys.stdin.readline())

while T > 0:
    (x1, y1, xp, yp) = [int(x) for x in sys.stdin.readline().split()]
    T -= 1
    print('{} {}'.format(2 * xp - x1, 2 * yp - y1))