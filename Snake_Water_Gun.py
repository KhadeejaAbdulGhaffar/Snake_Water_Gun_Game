import random

win_conditions = {
    "snake": "water",
    "water": "gun",
    "gun": "snake"
}

options = list(win_conditions.keys())
computer = random.choice(options)

player = input("Enter (snake/water/gun): ").lower()
print(f"Computer chose: {computer}")

"""
Snake vs. Water:  Snake wins.
Water vs. Gun  :  Water wins.
Gun vs. Snake  :  Gun wins
"""

if player not in win_conditions:
    print("INVALID INPUT")
elif player == computer:
    print("TIE")
elif win_conditions[player] == computer:
    print("PLAYER WINS")
else:
    print("COMPUTER WINS")
