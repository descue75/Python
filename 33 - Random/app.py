import random

for i in range(3):
  print(random.random())

for i in range(3):
  print(random.randint(10, 20))

members = ['John', 'Mary', 'Bob']
print(random.choice(members))


class Dice:
  def roll(self):
    self.first = random.randint(1, 6)
    self.second = random.randint(1, 6)
    return self.first, self.second
  def print(self):
    print(f'({self.first}, {self.second})')


dice = Dice()
die1, die2 = dice.roll()
print(f'{die1}, {die2}')
dice.print()