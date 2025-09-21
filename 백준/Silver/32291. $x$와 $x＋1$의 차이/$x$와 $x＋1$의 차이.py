import sys
import math
input = sys.stdin.readline

x = int(input())

def divisors(x):
    result = [1]

    for i in range(2, math.isqrt(x) + 1):
        if x % i == 0:
            result.append(i)
            if x // i != i:
                result.append(x // i)

    return result

answer = divisors(x + 1)
answer.sort()

print(' '.join(map(str, answer)))