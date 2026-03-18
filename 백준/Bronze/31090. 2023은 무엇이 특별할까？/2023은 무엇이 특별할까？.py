import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    print("Good") if (n + 1) % (n % 100) == 0 else print("Bye")