import sys
input = sys.stdin.readline

s = list(input().rstrip())
def weight(i):
    return 1 + (i % 2) * 2

result, idx = int(s[-1]), -1
for i in range(12):
    if s[i] != '*': result += int(s[i]) * weight(i)
    else: idx = i
for i in range(10):
    if (result + i * weight(idx)) % 10 == 0:
        print(i)
        break