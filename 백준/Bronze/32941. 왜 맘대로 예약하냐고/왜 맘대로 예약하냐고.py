import sys
input = sys.stdin.readline

t, x = map(int, input().split())
result = "YES"
for _ in range(int(input())):
    n = int(input())
    if x not in set(map(int, input().split())):
        result = "NO"

print(result)