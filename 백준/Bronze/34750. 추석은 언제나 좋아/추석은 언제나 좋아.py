import sys
input = sys.stdin.readline

n = int(input()) // 100
if n >= 10000:
    print(f"{20 * n} {80 * n}")
elif n >= 5000:
    print(f"{15 * n} {85 * n}")
elif n >= 1000:
    print(f"{10 * n} {90 * n}")
else:
    print(f"{5 * n} {95 * n}")