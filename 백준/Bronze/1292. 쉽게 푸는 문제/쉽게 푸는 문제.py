import sys
input = sys.stdin.readline

x, y = map(int, input().split())

def func(x):
    if x <= 1: return x
    result = 0
    t = 1
    while x > 0:
        if x < t:
            result += t * x
            break
        result += t ** 2
        x -= t
        t += 1
    
    return result
    
print(func(y) - func(x - 1))