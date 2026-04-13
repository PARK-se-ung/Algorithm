import sys
input = sys.stdin.readline

radius, interval = float(input()), float(input())
n = int(input())
print("YES") if interval * n <= radius * 3.14159 else print("NO")