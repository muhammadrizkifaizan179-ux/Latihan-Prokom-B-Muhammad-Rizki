from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))
        
d6 = Die()
d10 = Die(10)
d20 = Die(20)

print("Dadu 6 sisi:")
for _ in range(10):
    d6.roll_die()

print("Dadu 10 sisi:")
for _ in range(10):
    d10.roll_die()

print("Dadu 20 sisi:")
for _ in range(10):
    d20.roll_die()