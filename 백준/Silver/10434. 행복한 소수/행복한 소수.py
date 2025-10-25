import sys
input = sys.stdin.readline

def eratos(x):
    prime = [True] * (x + 1)
    prime[0], prime[1] = False, False
    for i in range(2, int(x ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, x + 1, i):
                prime[j] = False
    return prime

prime = eratos(10000)

def func(x):
    result = 0
    while x > 0:
        result += (x % 10) ** 2
        x //= 10
    return result

happy = set()

for _ in range(int(input())):
    idx, num = map(int, input().split())
    flag = 'NO'
    if prime[num]:
        prev = {num}
        next = func(num)
        while True:
            if next in prev: break
            if next == 1 or next in happy:
                flag = 'YES'
                happy.update(prev)
                break
            prev.add(next)
            next = func(next)
    print(f'{idx} {num} {flag}')