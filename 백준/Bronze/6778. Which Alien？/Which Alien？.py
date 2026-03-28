import sys
input = sys.stdin.readline

ant, eye = int(input()), int(input())
result = []
if ant >= 3 and eye <= 4: result.append("TroyMartian")
if ant <= 6 and eye >= 2: result.append("VladSaturnian")
if ant <= 2 and eye <= 3: result.append("GraemeMercurian")

for elem in result:
    print(elem)