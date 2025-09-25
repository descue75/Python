weight = int(input('Weight: '))
conversion_factor = 0.45

while True:
  lbs_or_kg = input('(L)bs or (K)g: ')
  if lbs_or_kg.upper() == 'L' or lbs_or_kg.upper() == 'K':
    break
  print('invalid input')

if lbs_or_kg.upper() == 'L':
  print(f'you weigh {weight * 0.45} kgs')
else:
  print(f'you weigh {weight / 0.45} lbs')