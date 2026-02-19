import sys
input = sys.stdin.readline

n = int(input())
result = 0
remain = 30
for _ in range(n):
    current = int(input())
    if current < remain:
        remain -= current
        result += 1
    else: # current >= remain
        if remain * 2 >= current:
            result += 1
        remain = 30

print(result)