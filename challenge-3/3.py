in_txt = open('3.txt', 'r').read()

index = 0
saved_char = ''
output = ""

min = 4
max = 5

for c in in_txt:
    if c.islower():
        print(c)
        if index - min < 0:
            continue

        context = in_txt[index - 4 : index + max]

        if context[0].islower() and context[4].islower() and context[-1].islower():
            if context[1:4].isupper() and context[5:8].isupper():
                print(context)
                output += c

    index += 1

print(output)