import sys
input = sys.stdin.readline

n = int(input())
DNA = list(input().rstrip())
result = str()
table = [
    ['A', 'C', 'A', 'G'],
    ['C', 'G', 'T', 'A'],
    ['A', 'T', 'C', 'G'],
    ['G', 'A', 'G', 'T']
]
def func(x):
    if x == 'A': return 0
    if x == 'G': return 1
    if x == 'C': return 2
    if x == 'T': return 3

for i in range(n - 1, 0, -1):
    DNA[i - 1] = table[func(DNA[i - 1])][func(DNA[i])]
print(DNA[0])