import sys
input = sys.stdin.readline
from decimal import Decimal, ROUND_HALF_UP

while True:
    n = float(input())
    if n == 0: break
    result = 1 + n + n ** 2 + n ** 3 + n ** 4
    print(Decimal(result).quantize(Decimal('0.01'), ROUND_HALF_UP))
