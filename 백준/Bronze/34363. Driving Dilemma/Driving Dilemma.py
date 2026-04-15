import sys
input = sys.stdin.readline

s, d, t = int(input()), float(input()), float(input())
print("MADE IT") if s * 5280 * t / 3600 > d else print("FAILED TEST")