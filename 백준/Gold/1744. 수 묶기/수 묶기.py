import sys
input = sys.stdin.readline

n = int(input())
positive, zero, negative = [], [], []

for _ in range(n):
    t = int(input())
    if t > 0: positive.append(t)
    elif t < 0: negative.append(t)
    else: zero.append(t)

positive.sort(key = lambda x : -x)
negative.sort()

result = 0

a, b = len(positive), len(negative)

for i in range(a // 2):
    first, second = positive[2 * i], positive[2 * i + 1]
    if first == 1 or second == 1:
        result += first + second
        continue
    result += first * second
if a % 2 == 1: result += positive[-1]

for i in range(b // 2):
    result += negative[2 * i] * negative[2 * i + 1]
if len(zero) == 0 and b % 2 == 1: result += negative[-1]

print(result)