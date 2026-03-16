import sys
input = sys.stdin.readline

n = int(input())
height = []
result = 0

for _ in range(n):
    x, y = map(int, input().split())

    while height and height[-1] > y:
        result += 1
        height.pop()
    
    if y == 0: continue

    if not height or y > height[-1]:
        height.append(y)
    elif y == height[-1]: continue

print(result + len(height))