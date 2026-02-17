import sys
input = sys.stdin.readline
from functools import cmp_to_key

def to_decimal(x):
    if ord(x) >= ord('A'):
        return ord(x) - ord('A') + 10
    return int(x)

def to_36(arr):
    result = str()
    for elem in arr:
        if elem <= 9:
            result += str(elem)
        else:
            result += chr(ord('A') + elem - 10)
    return result

def plus(x, y):
    if len(x) < len(y):
        x, y = y, x
    
    result = []
    bias = 0
    for i in range(len(x)):
        dx = x[-i - 1]
        dy = y[-i - 1] if i < len(y) else '0'
        digit = to_decimal(dx) + to_decimal(dy) + bias
        bias = 0
        if digit >= 36:
            bias = 1
            digit = digit % 36
        result.append(digit)
    if bias == 1:
        result.append(1)
    return to_36(result[::-1])

def plus_arr(arr):
    result = str()
    for elem in arr:
        result = plus(result, elem)
    
    return result

def substract(x, y):
    result = []
    for i in range(len(x)):
        dx = x[-i - 1]
        dy = y[-i - 1]
        result.append(to_decimal(dx) - to_decimal(dy))
    while result[-1] == 0 and len(result) > 1:
        result.pop()

    return to_36(result[::-1])

def compare(x, y):
    if len(x) != len(y):
        return len(y) - len(x)
    for i in range(len(x)):
        flag = to_decimal(y[i]) - to_decimal(x[i])
        if flag != 0:
            return flag
    return 0

n = int(input())
arr = [input().rstrip() for _ in range(n)]
k = int(input())

diff = []

for i in range(36):
    result = '0'
    change = to_36([i])
    for elem in arr:
        x = str()
        for j in range(len(elem)):
            x += 'Z' if elem[j] == change else elem[j]
        result = plus(result, substract(x, elem))
    diff.append(result)


diff.sort(key = cmp_to_key(compare))

result = plus_arr(arr)

for i in range(k):
    result = plus(result, diff[i])

print(result)