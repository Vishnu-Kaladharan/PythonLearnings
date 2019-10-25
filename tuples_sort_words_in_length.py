txt = 'Hello My Name is Vishnu and I am 26 years old'

words = list(txt.split())
lst = list()

for word in words:
    lst.append((len(word), word))

lst.sort(reverse=True)
result = list()

for length, word in lst:
    result.append(word)
print(result)