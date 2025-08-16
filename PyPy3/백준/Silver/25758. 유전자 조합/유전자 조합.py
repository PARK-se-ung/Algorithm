import sys
input = sys.stdin.readline

n = int(input())
dna = list(map(list, input().rstrip().split(' ')))
child = set()

dna.sort(key = lambda x : x[0])
for i in range(1, n):
    if ord(dna[i][1]) >= ord(dna[0][0]):
        child.add(dna[i][1])
    if ord(dna[0][1]) >= ord(dna[i][0]):
        child.add(dna[0][1])

dna.sort(key = lambda x : x[1])
for i in range(1, n):
    if ord(dna[i][0]) >= ord(dna[0][1]):
        child.add(dna[i][0])
    if ord(dna[0][0]) >= ord(dna[i][1]):
        child.add(dna[0][0])

child = list(child)
child.sort()
print(len(child))
print(' '.join(child))
