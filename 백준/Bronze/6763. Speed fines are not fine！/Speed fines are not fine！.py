import sys
input = sys.stdin.readline
a, b = int(input()), int(input())
x = b - a
if x <= 0: print("Congratulations, you are within the speed limit!")
elif x <= 20: print("You are speeding and your fine is $100.")
elif x <= 30: print("You are speeding and your fine is $270.")
else: print("You are speeding and your fine is $500.")