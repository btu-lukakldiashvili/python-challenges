import pickle

# open a file, where you stored the pickled data
file = open('banner.p', 'rb')

# dump information to that file
data = pickle.load(file, encoding="latin1")

file.close()


# print(data)

# print('Showing the pickled data:')

# print("\n".join(f'{k}: {v}' for k,v in data[0]))

# for item in data:
#     for tup in item:
#         ordin = tup[1]
#
#         # if tup[0] != ' ':
#         print(chr(ordin))

for line in data:
    tups = line

    output = ""

    for tup in tups:
        # print(tup)
        output += tup[0]*tup[1]

    print(output)

# pickle.dump(None, file, protocol=)