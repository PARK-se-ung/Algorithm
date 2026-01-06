import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    print("PREMIADO") if n % 42 == 0 else print("TENTE NOVAMENTE")