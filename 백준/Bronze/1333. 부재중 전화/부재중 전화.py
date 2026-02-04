import sys
input = sys.stdin.readline

n, l, d = map(int, input().split())

time = 0
while True:
    if l <= time % (l + 5) < l + 5 or time > (n - 1) * (l + 5) + l:
        print(time)
        break
    time += d