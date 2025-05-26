from random import randint
class Die:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        self.sides = randint(1,6)
        return self.sides

play=Die()

for attempt in range(1,10):
    print(f"Your attempt {attempt}, your result: {play.roll_die()}")



