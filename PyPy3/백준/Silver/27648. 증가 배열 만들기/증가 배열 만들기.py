import sys
input = sys.stdin.readline

n, m, k = map(int, input().split(' '))


if k >= n + m - 1:
    print("YES")
    for r in range(n):
        print(' '.join(map(str, [r + c + 1 for c in range(m)])))    
else:
    print("NO")