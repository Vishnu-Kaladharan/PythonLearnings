import string
fhandle = open('words.txt')

count_words = dict()

for line in fhandle:
    words = list()
    line = line.rstrip()
    line = line.lower()
    line = line.translate(str.maketrans('', '', string.punctuation))
    words = line.split()
    for word in words:
        count_words[word] = count_words.get(word, 0) + 1

list_count_words = list()
for key,value in list(count_words.items()):
    list_count_words.append((value, key))


list_count_words.sort(reverse=True)
print(list_count_words)
print(list_count_words[:10])