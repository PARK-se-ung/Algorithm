import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dp = [0] * 10001
dp[1], dp[2] = 1, 2

def match(n):
    if dp[n] > 0: return dp[n]
    dp[n] = match(n - 1) + match(n - 2)
    return dp[n]

while True:
    try:
        n = int(input())
        print(match(n) + match(n - 2))
    except: 
        break