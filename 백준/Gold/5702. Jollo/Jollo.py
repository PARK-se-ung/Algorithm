import sys
input = sys.stdin.readline

def func(m, chosen):
    for i in range(m, 53):
        if i not in chosen:
            return i    
    return -1

while True:
    a, b, c, x, y = map(int, input().split())
    if a == b == c == x == y == 0:
        break

    chosen = {a, b, c, x, y}
    princess, prince = [a, b, c], [x, y]
    princess.sort(reverse = True)
    prince.sort(reverse = True)

    result = -1

    if prince[0] > princess[0]:
        if prince[1] > princess[0]:
            result = func(1, chosen)
        elif prince[1] > princess[1]:
            result = func(princess[1] + 1, chosen)
        else:
            result = func(princess[0] + 1, chosen)

    elif prince[0] > princess[1]:
        if prince[1] > princess[1]:
            result = func(princess[1] + 1, chosen)
    
    print(result)