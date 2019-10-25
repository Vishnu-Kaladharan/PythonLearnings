import random

class Dice:
    def roll(self):
        return random.randint(1,6)


dice_1 = Dice()
dice_2 = Dice()
result = (dice_1.roll(), dice_2.roll())
print(result)