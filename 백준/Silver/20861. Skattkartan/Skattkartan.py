import sys
input = sys.stdin.readline

row, column = int(input()), int(input())
grid = [list(input().rstrip()) for _ in range(row)]
visited = [[False] * column for _ in range(row)]
current = [(0, 0)]

direct = {">": (0, 1), "<":(0, -1), "v": (1, 0), "^": (-1, 0)}

result = str()

while current:
    r, c = current.pop()

    if visited[r][c]:
        result = "cykel"
        break

    if grid[r][c] == "A":
        result = "sushi"
        break

    if grid[r][c] == "B":
        result = "samuraj"
        break

    bias = direct[grid[r][c]]
    dr, dc = r + bias[0], c + bias[1]
    current.append((dr, dc))
    visited[r][c] = True

print(result)