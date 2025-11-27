import sys
input = sys.stdin.readline

n, m = map(int, input().split())

balls = [-1] * n
for i in range(m):
    l, r = map(int, input().split())
    for j in range(l - 1, r):
        balls[j] = i

result = set(balls)

if -1 in result:
    print(2 ** (len(result) - 1))
else:
    print(2 ** len(result))