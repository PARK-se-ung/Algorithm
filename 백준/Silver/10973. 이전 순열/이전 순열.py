import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

current = seq[-1]
idx = -1

for i in range(n - 1, -1, -1):
    if seq[i] <= current:
        current = seq[i]
    else:
        idx = i
        break

if idx == -1:
    print(-1)
else:
    result = seq[:idx]
    tails = seq[idx:]
    tails.sort(key = lambda x : -x)

    for i in range(n - idx):
        if tails[i] == seq[idx]:
            result.append(tails[i + 1])
            break
    
    head = result[-1]
    for t in tails:
        if t != head:
            result.append(t)

    print(' '.join(map(str, result)))