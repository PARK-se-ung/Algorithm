import sys
input=sys.stdin.readline
dp=[0 for _ in range(41)]
dp[0],dp[1]=0,1
for i in range(2,41):
    dp[i]=dp[i-1]+dp[i-2]

n=int(input().rstrip())
for _ in range(n):
    temp=int(input().rstrip())
    if temp==0:
        print("1 0")
    else:
        print(f"{dp[temp-1]} {dp[temp]}")
