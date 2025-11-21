import sys
from datetime import datetime
input = sys.stdin.readline 

n = int(input())

if n == 0:
    print(0)
    sys.exit()

submit = []

for _ in range(n):
    date, time, weight = input().rstrip().split()
    dt = datetime.strptime(f"{date} {time}", "%Y/%m/%d %H:%M:%S")
    submit.append((dt, int(weight)))

upper, lower = 0, 0
for i in range(n):
    diff = (submit[-1][0] - submit[i][0]).total_seconds() / 86400
    p = max(0.5 ** (diff / 365), 0.9 ** (n - 1 - i))

    upper += p * submit[i][1]
    lower += p

print(int(upper / lower + 0.5))