import sys
input = sys.stdin.readline

m = int(input())

def combi(n, r):
    num = 1
    for i in range(r):
        num *= n - i
        num //= i + 1
    return num

def binary_search(r):
    left, right = 2 * r, m + 1
    while left <= right:
        mid = (left + right) // 2
        c = combi(mid, r)
        if c == m:
            return mid
        if c < m:
            left = mid + 1
        else:
            right = mid - 1
    return -1

result = set()
for r in range(1, 31):
    n = binary_search(r)
    if n != -1:
        result.add((n, r))
        if n - r != r:
            result.add((n, n - r))

result = list(result)
result.sort(key = lambda x : (x[0], x[1]))

print(len(result))
for x, y in result:
    print(f'{x} {y}')