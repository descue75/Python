class Mammal:
  def walk(self):
    print('walk')
  def talk(self):
    print('grr')


class Dog(Mammal):
  def talk(self):
    print('bark')


class Cat(Mammal):
  def talk(self):
    print('meow')


class Monster(Mammal):
  pass


dog = Dog()
cat = Cat()
monster = Monster()

dog.walk()

dog.talk()
cat.talk()
monster.talk()
