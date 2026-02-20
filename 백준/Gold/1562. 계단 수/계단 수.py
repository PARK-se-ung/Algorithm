import sys
input = sys.stdin.readline

DIV = 10 ** 9

def stair(n):
    if n <= 9:
        return 0    

    # t로 끝나고 경로가 m인 길이 l 수열의 개수
    dp = [[[-1] * (1 << 10) for _ in range(10)] for _ in range(n)]
    for i in range(1, 10):
        dp[0][i][1 << i] = 1
    

    for l in range(n - 1):
        for m in range(1 << 10):
            for t in range(10):
                if dp[l][t][m] >= 0:
                    if t > 0:
                        if dp[l + 1][t - 1][m | 1 << (t - 1)] == -1:
                            dp[l + 1][t - 1][m | 1 << (t - 1)] = dp[l][t][m] 
                        else:
                            dp[l + 1][t - 1][m | 1 << (t - 1)] += dp[l][t][m] 
                        dp[l + 1][t - 1][m | 1 << (t - 1)] %= DIV
                    if t < 9:
                        if dp[l + 1][t + 1][m | 1 << (t + 1)] == -1:
                            dp[l + 1][t + 1][m | 1 << (t + 1)] = dp[l][t][m] 
                        else:
                            dp[l + 1][t + 1][m | 1 << (t + 1)] += dp[l][t][m] 
                        dp[l + 1][t + 1][m | 1 << (t + 1)] %= DIV

    result = 0

    for m in range(1 << 10):
        for t in range(10):
            if dp[n - 1][t][m] > 0 and m.bit_count() == 10:
                result += dp[n - 1][t][m]
                result %= DIV
    
    return result

n = int(input())
print(stair(n))