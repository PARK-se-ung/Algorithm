import sys
input = sys.stdin.readline

r, c = map(int, input().split())

t, b, s = 1, 2, 3

total = 0

def roll(t, s, residue):
    if residue == 0: 
        return s, 7 - t, 0
    if residue == 1: 
        return t, s, t
    if residue == 2: 
        return 7 - s, t, t + 7 - s
    return 7 - t, 7 - s, 14 - s


for _ in range(r):
    total += 14 * (c // 4)
    t, s, left = roll(t, s, c % 4)
    total += left
    t, b, s = 7 - b, t, 7 - s

print(total)