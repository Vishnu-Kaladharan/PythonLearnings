t = ['a', 'b', 'c']
n = [2,1,5,3, 9,1,3,5,2,4]

#Append function used to append an item to the list
t.append('d')
print(t)

# Insert method used to insert an item at an index
t.insert(3,'z')
print(t)

# Sorting a list in ascending
n.sort()
print(n)
# To sort in descending order. use reverse method after sorting
n.reverse()
print(n)

# Appending another list to a list
t.extend(t)
print(t)

# Delete the element & returns it
print(t.pop(3))
print(t)

# Delete operator to delete the element(s)
del t[3:]
print(t)


str = 'Hello World-It is me Vishnu-How you doing!'

print(list(str))

# Split operator converts a string to a list.

l = str.split()
#Use delimiter to split
m = str.split('-')
print(l)
print(m)
# Inverse of Split. converting a list to string
str2 = '-'.join(m)
print(str2)