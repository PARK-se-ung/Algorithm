import sys
input = sys.stdin.read

A = ['a', 'i', 'y', 'e', 'o', 'u']
B = ['b', 'k', 'x', 'z', 'n', 'h', 
     'd', 'c', 'w', 'g', 'p', 'v', 
     'j', 'q', 't', 's', 'r', 'l', 'm', 'f']

dic = dict()
for i in range(len(A)):
    dic[A[i].capitalize()] = A[i - 3].capitalize()
    dic[A[i]] = A[i - 3]
for i in range(len(B)):
    dic[B[i].capitalize()] = B[i - 10].capitalize()
    dic[B[i]] = B[i - 10]

def convert(s):
    return dic[s] if s in dic else s

print(''.join(list(map(convert, list(input().rstrip())))))