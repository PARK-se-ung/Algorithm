import sys
input = sys.stdin.readline
n, w = int(input()), int(input())
result = 10 * n
if n >= 3: result += 20
if n >= 5: result += 50
if w > 1000: result -= 15
print(max(0, result))