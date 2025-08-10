import sys
input = sys.stdin.readline

mush = [int(input()) for _ in range(10)]
for i in range(1, 10):
    mush[i] += mush[i - 1]

mush.sort(key = lambda x : (abs(x - 100), 100 - x))
print(mush[0])