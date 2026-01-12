import sys
input = sys.stdin.readline

n = int(input())

if n == 2 or n % 2 == 1: 
    print("NIE")
    sys.exit(0)

k = n // 2
last = n - (3 * ((k - 2) // 2)) - (k % 2)

coord = [(0, 0)]

for i in range(k - 2):
    coord.append((i, 1 + i % 2))
    coord.append((i + 1, 1 + i % 2))

coord.append((k - 2, last))
coord.append((k - 1, last))
coord.append((k - 1, 0))

for elem in coord:
    print(' '.join(map(str, elem)))