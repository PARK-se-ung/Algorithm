import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
s, v = map(lambda x : 30 * int(x), input().split())
l = int(input())
rest = 100 * (250 - l)

result = 0
while rest > 0:
    result += 1
    if v > 0:
        v -= 1
        rest -= c
    elif s > 0:
        s -= 1
        rest -=b
    else:
        rest -= a

print(result)