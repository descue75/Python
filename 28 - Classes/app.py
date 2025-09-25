class Point:
  def move(self):
    print("move")
  
  def draw(self):
    print("draw")


point1 = Point()
point1.draw()
point1.x = 1
point1.y = 2
print(f'({point1.x}, {point1.y})')