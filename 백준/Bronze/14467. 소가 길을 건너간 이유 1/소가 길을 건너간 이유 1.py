import sys
input = sys.stdin.readline

n = int(input())
cow = dict()
result = 0
for _ in range(n):
    c, p = map(int, input().split())
    if c not in cow:
        cow[c] = p
    elif cow[c] != p:
        result += 1
        cow[c] = p
    
print(result)