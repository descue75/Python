for x in range(4):
  for y in range(3):
    print(f'({x}, {y})')

numbers = [5, 2, 5, 2, 2]
y = 0
for x in numbers:
  buffer = ''
  for y in range(x):
    buffer += 'x'
  print(buffer)