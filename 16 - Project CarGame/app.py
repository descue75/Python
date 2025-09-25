command = ''
started = False
while True:
  command = input('> ').lower()
  if command == 'start':
    if started == False:
      print('Car started...Ready to go!')
      started = True
    else:
      print('Car is already started')
  elif command == 'stop':
    if started:
      print('Car stopped.')
      started = False
    else:
      print('Car is already stopped')
  elif command == 'help':
    print('''start - to start the car
stop - to stop the car
quit - to quit''')
  elif command == 'quit':
    break
  else:
    print("I don't understand that")