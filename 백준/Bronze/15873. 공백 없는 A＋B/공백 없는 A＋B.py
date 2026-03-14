import sys
input = sys.stdin.readline

n = input().rstrip()
if len(n) == 4: print(20)
elif len(n) == 2: print(int(n[0]) + int(n[1]))
elif n[1] == '0': print(int(n[:2]) + int(n[2:]))
else: print(int(n[:1]) + int(n[1:]))