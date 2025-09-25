customer = {
  'name': 'John Smith',
  'age': 30,
  'is_verified': True
}
print(customer['name'])
print(customer.get('birthdate'))
print(customer.get('birthdate', 'Jan 1 1980'))
customer['country'] = 'USA'
print(customer)

phone_number = '12345'
int_str_conversion = {
  1:'one',
  2:'two',
  3:'three',
  4:'four'
}

string = ''
for char in phone_number:
  value = int_str_conversion.get(int(char), '!')
  string += f"{value} "

string = string.rstrip()
print(string)

words = string.split(' ')
print(words)
