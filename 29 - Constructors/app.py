class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def move(self):
    print("move")
  
  def draw(self):
    print("draw")

  def print(self):
    print(f'({self.x}, {self.y})')

point1 = Point(1,2)
point1.draw()
point1.print()
