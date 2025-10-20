import sys
input = sys.stdin.readline

S = input().rstrip()
result = [0] * 26

for s in S:
    result[ord(s) - ord('a')] += 1

print(' '.join(map(str, result)))