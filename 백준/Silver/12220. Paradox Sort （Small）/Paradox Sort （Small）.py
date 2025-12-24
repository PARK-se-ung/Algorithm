import sys
input = sys.stdin.readline
from itertools import permutations


for i in range(int(input())):
    n, a = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(n)]

    if n == 1:
        print(f"Case #{i + 1}: {a}")
        continue

    result = None
    for elem in permutations(range(n)):
        current = elem[0]
        for j in range(1, n):
            current = current if grid[current][elem[j]] == 'Y' else elem[j]
        if current == a:
            result = elem
            break

    if result is None:
        print(f"Case #{i + 1}: IMPOSSIBLE")
    else:
        print(f"Case #{i + 1}: {' '.join(map(str, result))}")