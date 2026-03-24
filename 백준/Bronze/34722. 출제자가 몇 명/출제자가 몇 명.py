import sys
input = sys.stdin.readline

result = 0
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if a >= 1000 or b >= 1600 or c >= 1500 or (1 <= d <= 30):
        result += 1
print(result)