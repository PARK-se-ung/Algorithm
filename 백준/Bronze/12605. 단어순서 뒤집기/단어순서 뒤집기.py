import sys
input = sys.stdin.readline

for i in range(int(input())):
    current = list(input().split())
    print(f"Case #{i + 1}: {' '.join(current[::-1])}")
