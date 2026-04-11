import sys
input = sys.stdin.readline

result = int(input())
for _ in range(int(input())):
    sym, val = input().rstrip(), int(input())
    if sym == '+': result += val
    else: result -= val

print(result)