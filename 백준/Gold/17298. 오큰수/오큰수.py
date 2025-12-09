import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split(' ')))
result = [-1] * n
stack = [(-1, float('inf'))]
for i in range(n):
    if stack[-1][1] < seq[i]:
        while stack[-1][1] < seq[i] and len(stack) > 1:
            idx, v = stack.pop()
            result[idx] = seq[i]
    stack.append((i, seq[i]))

print(' '.join(map(str, result)))