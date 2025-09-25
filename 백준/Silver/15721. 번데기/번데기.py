import sys
input = sys.stdin.readline

a = int(input())
t = int(input())
flag = int(input())

start = 4
total = 0
while total + start < t:
    total += start
    start += 1

t -= total
total *= 2

if t <= 2:
    total += 2 * t - 1 + flag
else:
    total += t + 2 + flag * (start - 2)

print((total - 1) % a)