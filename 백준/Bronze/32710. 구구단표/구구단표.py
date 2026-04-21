import sys
input = sys.stdin.readline

n = int(input())
a, b = -1, -1
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        a, b = i, n // i
if 1 <= a <= 9 and 1 <= b <= 9:
    print(1)
else: print(0)