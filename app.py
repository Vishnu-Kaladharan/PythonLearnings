def count_occurence(letter,string):
    count = 0
    for item in string:
        if item == letter:
            count += 1
    return count


inp1 = input('>')
inp1 = inp1.lower()
inp2 = input('>')
inp2 = inp2.lower()

print(count_occurence(inp1,inp2))