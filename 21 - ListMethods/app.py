numbers = [5,2,1,2,7,4,7]
numbers.append(20)
print(numbers)
numbers.insert(2,12)
print(numbers)
numbers.remove(5)
print(numbers)
value = numbers.pop()
print(numbers)
print(value)
print(numbers.index(2))
print(5 in numbers)
print(numbers.count(2))

numbers.sort()
numbers.reverse()
print(numbers)

uniques = []
for num in numbers:
  if num not in uniques:
    uniques.append(num)

print(uniques)

numbers.clear()
print(numbers)