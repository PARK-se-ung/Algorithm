import sys
input = sys.stdin.readline

p = 1000000007

def inv(x):
    num = 1
    b = p - 2
    while b > 0:
        if b % 2 == 1:
            num = (num * x) % p
        b //= 2
        x = (x ** 2) % p
    return num

fac = [1] * 4000001

for i in range(1, 4000001):
    fac[i] = (fac[i - 1] * i) % p

for _ in range(int(input())):
    n, k = map(int, input().split(' '))
    print((fac[n] * inv(fac[k]) * inv(fac[n - k])) % p)