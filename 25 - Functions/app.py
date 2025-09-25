phone_number = '12345'
int_str_conversion = {
  1:'one',
  2:'two',
  3:'three',
  4:'four'
}

def convert_phone_number(phone_number):
  output = ''
  for char in phone_number:
    value = int_str_conversion.get(int(char), '!')
    output += f"{value} "
  output = output.rstrip()
  return output


string = convert_phone_number(phone_number)
print(string)
