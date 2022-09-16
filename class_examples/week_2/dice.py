import random

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):  # every method needs self as the first argument
        return random.randint(1, self.sides)

dice = Dice(6)
for roll in range(100):
    print(dice.roll())

# Dice default is 6 sided
dice2 = Dice(14)
print(dice2.roll())
