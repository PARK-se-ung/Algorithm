import sys
input = sys.stdin.readline

# t일 후 금요일이면 t % 7 == 4여야 한다.
# 그러면 A_i들을 7로 나눈 나머지의 합이 4가 되는 경우가 있는지 체크

n = int(input())
arr = list(map(int, input().split()))

# residue는 조합가능한 나머지들의 집합 
residue = set()

# 각 A_i의 나머지 elem에 대하여
for elem in arr:

    # 새롭게 추가되는 나머지는
    new_residue = set()
    
    # 기존에 가능한 나머지 조합에 elem을 더해서 만들 수 있는 조합과 
    for r in residue:
        new_residue.add((r + elem) % 7)
    residue.update(new_residue)

    # elem으로 구성
    residue.add(elem % 7)

# 만들 수 있는 나머지 조합에 4가 있이면 YES, 없으면 NO
if 4 in residue: print('YES')
else: print('NO')