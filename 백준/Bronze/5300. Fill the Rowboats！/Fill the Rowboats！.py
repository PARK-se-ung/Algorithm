import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    print(i + 1, sep =' ')
    if i == n - 1:
        print("Go!")
    elif i % 6 == 5:
        print("Go!", sep = ' ')
