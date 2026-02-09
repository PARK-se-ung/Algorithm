import sys
input = sys.stdin.readline

# 1이 소수개이고 n이하인 수들로 포함-배제

# 1이 소수개이고 n이하인 수들의 집합 건설
n = int(input())
digit = len(str(n))

prime = []
for i in range(2, digit + 1):
    flag = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            flag = False
            break
    if flag:
        prime.append(int('1' * i))

# 포함-배제를 위한 집합 생성
include_exclude = [set() for _ in range(len(prime))]
for p in prime:
    for i in range(1, len(prime)):
        for s in include_exclude[i]:
            if s * p <= n:
                include_exclude[i - 1].add(s * p)
    include_exclude[-1].add(p)

# 결과 생성
result = 0
for i in range(len(prime)):
    for s in include_exclude[i]:
        result += (n // s) * ((-1) ** (len(prime) - i - 1))

print(result)