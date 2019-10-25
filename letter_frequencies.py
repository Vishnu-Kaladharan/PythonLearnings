import string
fhandle = open('words.txt')

letter_frequency = dict()
list_letter_frequency = list()

for line in fhandle:

    line = line.lower()
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', string.whitespace))
    line = line.translate(str.maketrans('', '', string.digits))
    for item in line:
        letter_frequency[item] = letter_frequency.get(item,0) + 1

for key,value in list(letter_frequency.items()):
    list_letter_frequency.append((value, key))

list_letter_frequency.sort(reverse=True)
print(list_letter_frequency)