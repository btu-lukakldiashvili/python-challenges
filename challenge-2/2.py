import string

dict_cyp = {
  "!": '1',
  "@": '2',
  "#": '3',
  "$": '4',
  "%": '5',
  "^": '6',
  "&": '7',
  "*": '8',
  "(": '9',
  ")": '0',
}

# in_txt = "123456789"
# in_txt = "!@#$%^&*()_-+={}|:,./';[]"
in_cyp = open('2.txt', 'r').read()

output = ''

for i in in_cyp:
    if ord('a') <= ord(i) <= ord('z'):
        output += i

print(output)