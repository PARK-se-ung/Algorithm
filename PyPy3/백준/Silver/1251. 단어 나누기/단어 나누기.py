import sys
input = sys.stdin.readline

S = list(input().rstrip())
n = len(S)
result = []
for i in range(1, n - 1):
    first = S[:i]
    first.reverse()
    for j in range(i + 1, n):
        second, third = S[i:j], S[j:]
        second.reverse()
        third.reverse()
        result.append(str(''.join(first + second + third)))
        result.sort()
        result = [result[0]]
print(result[0])