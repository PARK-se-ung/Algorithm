import sys
input = sys.stdin.readline

def score(x, y):
    dist_square = x ** 2 + y ** 2
    if dist_square <= 9: return 100
    if dist_square <= 36: return 80
    if dist_square <= 81: return 60
    if dist_square <= 144: return 40
    if dist_square <= 225: return 20
    return 0

for _ in range(int(input())):
    arr = list(map(float, input().split()))
    player1, player2 = 0, 0
    for i in range(6):
        if i < 3:
            player1 += score(arr[2 * i], arr[2 * i + 1])
        else:
            player2 += score(arr[2 * i], arr[2 * i + 1])
    
    result = str()
    if player1 > player2: result = "PLAYER 1 WINS."
    elif player1 == player2: result = "TIE."
    else: result = "PLAYER 2 WINS."

    print(f"SCORE: {player1} to {player2}, {result}")