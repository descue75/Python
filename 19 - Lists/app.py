values = [1,2,3,4,5]
print(values)
print(values[0])
print(values[-1])
print(values[2:])
print(values[2:4])

max = values[0]
for i in values:
  if i > max:
    max = i
print(max)