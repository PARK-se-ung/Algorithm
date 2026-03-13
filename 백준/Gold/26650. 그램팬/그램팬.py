import sys
input = sys.stdin.readline

result = 0
arr = list(input().rstrip())
stack = []

head, tail = 0, 0

for elem in arr:
    if ord(elem) == len(stack) + ord('A'):
        stack.append(elem)
        if elem == 'A': head += 1
        elif elem == 'Z': tail += 1
    elif stack and elem == stack[-1]:
        if elem == 'A': head += 1
        elif elem == 'Z': tail += 1
    else:
        result += head * tail
        if elem == 'A':
            stack = ['A']
            head = 1
            tail = 0
        else:
            stack = []
            head, tail = 0, 0

print(result + head * tail)