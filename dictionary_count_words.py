import string
fhandle = open('words.txt')

words = {}

for line in fhandle:
    line = line.rstrip()
    line = line.upper()
    line = line.translate(str.maketrans('','',string.punctuation))
    list_word = line.split()
    for word in list_word:
        words[word] = words.get(word,0) + 1

# for key in words:
#     print(f'The word "{key}" occured "{words[key]}" times')

for key in words:
    if words[key] > 5:
        print(f'{key} : {words[key]}')

print('Get the words in alphabetical order')
words_in_alph_order = list(words.keys())
words_in_alph_order.sort()
for item in words_in_alph_order:
    print(f'{item} : {words[item]}')
