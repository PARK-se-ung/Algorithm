import sys
input = sys.stdin.readline

while True:
    a, b, c, d = map(int, input().split())
    if a == b == c == d == 0: break

    result = 0
    while not (a == b == c == d):
        a, b, c, d = abs(a - b), abs(b - c), abs(c - d), abs(d - a)
        result += 1
    
    print(result)