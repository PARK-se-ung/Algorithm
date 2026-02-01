import sys
input = sys.stdin.readline


n, atk = map(int, input().split())
health = 0
result = 0

for _ in range(n):
    t, a, h = map(int, input().split())
    if t == 1:
        health -= ((h - 1) // atk) * a
    else: # t == 2 
        result = max(result, 1 - health)
        health = min(health + h, 0)
        atk += a

print(max(result, 1 - health))