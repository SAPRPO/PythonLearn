from random import randint
class Die:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        result = randint(1,self.sides)
        return result



def play(play):
    for attempt in range(1,11):
        print(f"Your attempt {attempt}, your result: {play.roll_die()}")
    print(f"Number of sides: {play.sides}\n")
play6 = Die()
play10 = Die(10)
play20 = Die(20)

play(play6)
play(play10)
play(play20)



