import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, p = input().rstrip().split(' ')
    n = int(n)
    if n == 1:
        print("9 3")
        continue
    p = list(map(int, p))
    bias = sum(p) % 3 
    bias = bias if bias > 0 else 3
    for i in range(n):
        if p[i] > 3:
            p[i] -= bias
            print(f"{''.join(map(str, p))} 3")
            p[i] += bias
        else: 
            p[i] += 6 - bias
            print(f"{''.join(map(str, p))} 3")
            p[i] -= 6 - bias