import sys
input = sys.stdin.readline

n, time = map(int, input().split())

direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]
idx = 0

x, y = 0, 0

prev = 0
for _ in range(n):
    current, direct = input().rstrip().split()
    current = int(current)

    x += direction[idx][0] * (current - prev)
    y += direction[idx][1] * (current - prev)
    prev = current

    if direct == 'right': 
        idx += 1
        if idx == 4:
            idx = 0
    else:
        idx -= 1
        if idx == -1:
            idx = 3

x += direction[idx][0] * (time - prev)
y += direction[idx][1] * (time - prev)

print(f'{x} {y}')
