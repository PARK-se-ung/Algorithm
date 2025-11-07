import sys
input = sys.stdin.readline

n, m = map(int, input().split())
product = list(map(int, input().split()))
company = list(map(int, input().split()))

product.sort(key = lambda x : -x)
company.sort()

p, c = 0, 0
result = 0

while p < n and c < m:
    if product[p] > company[c]:
        result += product[p] - company[c]
        p += 1
        c += 1
    else:
        break

print(result)