import sys
input = sys.stdin.readline

n = int(input())
S = []
for _ in range(n):
	S.append(list(input().rstrip()))
init = S[0]
l = len(S[0])
result = []
for i in range(l):
	current = init[i]
	for j in range(1, n):
		if S[j][i] != current:
			current = '?'
			break
	result.append(current)

print(''.join(result))