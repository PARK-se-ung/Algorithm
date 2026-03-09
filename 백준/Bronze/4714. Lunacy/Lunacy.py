import sys
input = sys.stdin.readline
from decimal import Decimal, ROUND_HALF_UP

while True:
    w = float(input())
    if w == -1.0: break
    new_w = Decimal(w * 0.167).quantize(Decimal('0.01'), rounding = ROUND_HALF_UP)
    w = Decimal(w).quantize(Decimal('0.01'))
    print(f"Objects weighing {w} on Earth will weigh {new_w} on the moon.")