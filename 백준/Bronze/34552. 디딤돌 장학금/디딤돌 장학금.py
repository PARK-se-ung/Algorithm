import sys
input = sys.stdin.readline

data = list(map(int, input().split()))

result = 0

for _ in range(int(input())):
    b, l, s = input().rstrip().split()
    if float(l) >= 2 and int(s) >= 17:
        result += data[int(b)]

print(result)