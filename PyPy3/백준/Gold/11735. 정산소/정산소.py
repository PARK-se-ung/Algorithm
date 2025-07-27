import sys
input = sys.stdin.readline

n, q = map(int, input().split(' '))
R, C = set(), set()
r_cnt, c_cnt, r_total, c_total = 0, 0, 0, 0
for _ in range(q):
    query, num = input().rstrip().split(' ')
    num = int(num)
    if query == "R":
        if num not in R:
            result = (n - c_cnt) * num + n * (n + 1) // 2 - c_total
            print(result)
            r_cnt += 1
            r_total += num
            R.add(num)
        else:
            print(0)
    else:
        if num not in C:
            result = (n - r_cnt) * num + n * (n + 1) // 2 - r_total
            print(result)
            c_cnt += 1
            c_total += num
            C.add(num)
        else:
            print(0)