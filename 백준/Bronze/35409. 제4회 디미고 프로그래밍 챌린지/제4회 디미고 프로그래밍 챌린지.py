import sys
input = sys.stdin.readline

h, m = map(int, input().split())

def convert(h, m):
    return 60 * h + m

current = convert(h, m)

if convert(6, 30) <= current <= convert(9, 0): print("Yes")
elif convert(9, 50) <= current <= convert(10, 0): print("Yes")
elif convert(10, 50) <= current <= convert(11, 0): print("Yes")
elif convert(11, 50) <= current <= convert(12, 0): print("Yes")
elif convert(12, 50) <= current <= convert(13, 50): print("Yes")
elif convert(14, 40) <= current <= convert(14, 50): print("Yes")
elif convert(15, 40) <= current <= convert(15, 50): print("Yes")
elif convert(16, 40) <= current <= convert(22, 50): print("Yes")
else: print("No")
