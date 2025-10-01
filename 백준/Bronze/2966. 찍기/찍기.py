import sys
input = sys.stdin.readline

n = int(input())
answers = list(input().rstrip())

X, Y, Z = ['A', 'B', 'C'], ['B', 'A', 'B', 'C'], ['C', 'C', 'A', 'A', 'B', 'B']
x, y, z = 0, 0, 0


for i in range(n):
    if answers[i] == X[i % 3]: x += 1
    if answers[i] == Y[i % 4]: y += 1
    if answers[i] == Z[i % 6]: z += 1

m = max(x, y, z)
print(m)
if m == x: print('Adrian')
if m == y: print('Bruno')
if m == z: print('Goran')