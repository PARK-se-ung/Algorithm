import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

distinct = []
prev = set()
second = set()
for elem in arr:
    if elem not in prev:
        distinct.append(elem)
        prev.add(elem)
    elif elem not in second:
        distinct.append(elem)
        second.add(elem)

def func(x, y):
    current = x * y
    value = 0
    while current > 0:
        value += current % 10
        current //= 10
    return value

result = -1
for i in range(len(distinct)):
    for j in range(i + 1, len(distinct)):
        result = max(result, func(distinct[i], distinct[j]))

print(result)