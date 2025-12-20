import sys
input = sys.stdin.readline

# 기댓값을 최대로 하기 위해선 (만족도 / 인기도)가 가장 높은 과목부터 마일리지를 투자
# 단, 투자하는 마일리지는 과목별 최대 마일리지, 남은 마일리지, 인기도를 넘어서는 안된다.

n, m, s = map(int, input().split())
A, B = list(map(int, input().split())), list(map(int, input().split()))

# i번째 과목 정보를 인덱스, 인기도, 만족도로 묶어서 리스트로
arr = []
for i in range(n):
    arr.append((i, A[i], B[i]))

# 만족도 / 인기도 기준 내림차순 정렬
arr.sort(key = lambda x : - x[2] / x[1])

# 이제 정렬한대로 마일리지 투자
idx = 0
result = [0] * n

while s > 0 and idx < n:
    # 현재 투자가능한 최대 마일리지
    mile = min(s, m, arr[idx][1])

    # 투자한 마일리지/소모한 마일리지 기록
    result[arr[idx][0]] += mile
    s -= mile
    idx += 1

print(' '.join(map(str, result)))