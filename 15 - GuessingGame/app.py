number = 9
guesses = 0
guessed_number = 0

while guesses < 3:
  guessed_number = int(input('Guess: '))
  guesses += 1
  if guessed_number == number:
    print('You win!')
    break
else:
  print('You lose')