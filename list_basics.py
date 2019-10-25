# List of string
names = ['John', 'Mary', 'Jacob', 'Liam', 'Kalyani']

print(len(names))
print(names[0])
print(names[-2])
print(names[1:3])

names[0] = 'Jon'
print(names)

numbers = [23,22,56,9,2,12,83,73,44,32]
largest = numbers[0]
for item in numbers:
    if item > largest:
        largest = item

print(f"The largest number in the list is {largest}")
new = []
for items in range(4):
    new.append(items)

for items in new:
    print(items)