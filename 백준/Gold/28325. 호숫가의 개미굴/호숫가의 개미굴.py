import sys
input = sys.stdin.readline

# i번째 방에 쪽방이 존재하는 경우, 반드시 모든 쪽방에 개미를 배치 == i번째 방은 개미 존재 x
# i - 1번째 방과 i + 1번째 방에 개미가 없는 경우 i번째방에 개미 배치(당연히 원형으로 배치)

# 쪽방이 있는 방부터 순회를 돌아야 최대한 차지 가능
# ㄴ 이걸 무시하고 for문 돌리면 반례
# TC
# 5
# 0 0 2 2 0
# answer = 6

n = int(input())
arr = list(map(int, input().split()))

# 쪽방이 있는 방 찾기, 없으면 처음부터
start = 0
for i in range(n):
    if arr[i] > 0:
        start = i
        break

# i번째 방을 개미가 차지했는지 기록
occupy = [0] * n
result = 0

for i in range(start, start + n):
    if i >= n: i -= n


    # 쪽방이 있으면 쪽방에 배치, i번째 방은 차지 x
    if arr[i] > 0:
        result += arr[i]

    # 쪽방이 없는 경우, 양 옆이 비어있으면 차지
    elif occupy[i - 1] == occupy[(i + 1) % n] == 0:
        result += 1
        occupy[i] = 1

print(result)