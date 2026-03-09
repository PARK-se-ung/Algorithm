import sys
input = sys.stdin.readline

n, d = map(int, input().split())
stack = []

move_a = "R"

if n < 0:
    n = -n
    move_a = "L"

def gcd(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    return gcd(y, x % y)

g = gcd(n, d)
n, d = n // g, d // g

if d.bit_count() != 1:
    print(-1)
    sys.exit(0)

new_n, new_d = n, d

while new_d != 1:
    stack.append("D")
    new_d //= 2

while new_n > 0:
    if new_n % 2 == 1:
        stack.append(move_a)
    new_n //= 2
    if new_n > 0:
        stack.append("U")

print(len(stack))
print(''.join(stack))