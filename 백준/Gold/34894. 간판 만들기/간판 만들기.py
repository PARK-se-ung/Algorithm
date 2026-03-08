import sys
input = sys.stdin.readline

n = int(input())
S = list(input().rstrip())
arr = list(map(int, input().split()))

memo = {
    'U':float('inf'),
    'O':float('inf'),
    'S':float('inf'),
    'P':float('inf'),
    'C':float('inf')
}

prev = {
    'O':'U',
    'S':'O',
    'P':'S',
    'C':'P'
}

for i in range(n):
    if S[i] == 'U':
        memo['U'] = min(memo['U'], arr[i])
    else:
        memo[S[i]] = min(memo[S[i]], memo[prev[S[i]]] + arr[i])

print(-1) if memo['C'] == float('inf') else print(memo['C'])