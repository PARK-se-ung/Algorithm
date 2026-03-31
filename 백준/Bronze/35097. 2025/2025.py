import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0: break
    result = 0
    for i in range(n):
        for j in range(n):
            result += (i + 1) * (j + 1)
    print(result)
