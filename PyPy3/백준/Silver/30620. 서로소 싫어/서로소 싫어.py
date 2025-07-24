import sys
input = sys.stdin.readline
x, y = map(int, input().split(' '))
def gcd(x, y): 
    if x < y:
        x, y = y, x
    while y > 0:
        x, y = y, x % y
    return x

if x == y:
    print(0)
elif gcd(x , y) > 1:
    print(1)
    print(y - x)
else:
    print(2)
    print(x * (y - 1))
    print(y * (1 - x)) 