import sys
input = sys.stdin.readline

f = list(map(int, input().split()))
fa, fb = map(int, input().split())

f_inv = [0] * 10
for i in range(10):
    f_inv[f[i]] = i

def func(x, f):
    digit = 1
    result = 0
    while x > 0:
        result += f[x % 10] * digit
        x //= 10
        digit *= 10
    
    return result

print(func(func(fa, f_inv) + func(fb, f_inv), f))