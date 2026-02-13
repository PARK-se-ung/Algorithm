import sys
input = sys.stdin.readline

n, t = map(int, input().split())
nums = list(map(lambda x : int(x) - 1, input().split()))
ops = [list(input().split()) for _ in range(t)][::-1]
player = [[] for _ in range(n)]
occupied = set()

op = list()
for i in range(t):
    if not player[nums[i]]:
        op = ops.pop()
        if op[1] == 'acquire':
            if op[2] in occupied:
                player[nums[i]].append(op)
            else:
                occupied.add(op[2])
        elif op[1] == 'release':
            occupied.remove(op[2])
    else:
        op = player[nums[i]][0]
        if op[2] not in occupied:
            occupied.add(op[2])
            player[nums[i]].pop()
    print(op[0])