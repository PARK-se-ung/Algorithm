import sys
input = sys.stdin.readline

while True:
    try:
        equation = input().rstrip()
        if not equation: break
        print(equation)
    except EOFError:
        break