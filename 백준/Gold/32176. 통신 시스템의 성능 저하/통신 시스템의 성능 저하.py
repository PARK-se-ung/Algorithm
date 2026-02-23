import sys
input = sys.stdin.readline

n, m, k1, k2 = map(int, input().split())
grid = []
broad = tuple()
node = []
for r in range(n):
    temp = list(input().rstrip())
    for c in range(n):
        if temp[c] == 'B':
            broad = (r, c)
        elif temp[c] == 'N':
            node.append((r, c))
    grid.append(temp)

def path(nd):
    return abs(broad[0] - nd[0]) + abs(broad[1] - nd[1])

def build(rect, nd):
    return (min(rect[0], nd[0]), max(rect[1], nd[0]), min(rect[2], nd[1]), max(rect[3], nd[1]))

def area(rect):
    return (rect[1] - rect[0] + 1) * (rect[3] - rect[2] + 1)

def cost(remove):
    p = 0
    rect = (n, -1, n, -1)
    for i in range(m):
        if i not in remove:
            p += path(node[i])
            rect = build(rect, node[i])
    return max(0, p - area(rect))

def func(n, m, k1, k2):
    
    def back1(idx, remove, rect):
        if len(remove) == m - k1:
            return cost(remove)
        
        if idx == m:
            return 0
        
        c = 0
        for i in range(idx, m):
            remove.add(i)
            c = max(c, back1(i + 1, remove, build(rect, node[i])))
            remove.remove(i)

        return c

    def back2(idx, cnt, rect, p):
        if cnt == k2:
            return max(0, p - area(rect))

        if idx == m:
            return 0

        c = 0
        for i in range(idx, m):
            c = max(c, back2(i + 1, cnt + 1, build(rect, node[i]), p + path(node[i])))
    
        return c
    
    return [back1(0, set(), (n, -1, n, -1)), back2(0, 0, (n, -1, n, -1), 0)]

print('\n'.join(map(str, func(n, m, k1, k2))))