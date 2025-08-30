import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split(' ')))
seq.sort()
prev = 0
for i in range(n):
    if seq[i] > prev + 1: break
    else: prev += seq[i]

print(prev + 1)