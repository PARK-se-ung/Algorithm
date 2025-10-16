import sys
input = sys.stdin.readline

# binary search
def search(n, u, d):
    start, end = 0, n

    while start <= end:
        mid = (start + end) // 2
        level = u * mid - d * (n - mid)

        if level <= 0:
            start = mid + 1
        else:
            end = mid - 1

    return u * start - d * (n - start)

n, m = map(int, input().split())
result = float('inf')

for _ in range(m):
    u, d = map(int, input().split())
    result = min(result, search(n, u, d))

print(result)