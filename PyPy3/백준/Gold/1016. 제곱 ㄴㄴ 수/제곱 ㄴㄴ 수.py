import sys
input = sys.stdin.readline

m, M = map(int, input().split(' '))
square_free = [1] * (M - m + 1)

def func(x):
    square = x ** 2
    residue = m % square
    if  residue == 0:
        return m
    else:
        return (m // square + 1) * square

n = 2
while n ** 2 <= M:
    for i in range(func(n), M + 1, n ** 2):
        square_free[i - m] = 0
    n += 1
print(sum(square_free))
