sample_string = 'Hello World! This is me Vishnu Kaladharan.'

# len() generic to other data types also to find the total number of characters in a string
print(len(sample_string))

# Case Conversions
print(sample_string.upper())
print(sample_string.lower())
print(sample_string.title())

# Find method to get index of the character/string
print(sample_string.find('!'))
print(sample_string.find('Hello'))

# Replacing method
print(sample_string.replace('Vishnu','Varun'))

# in operator to check if the string has a particular sub string
print('Vishnu' in sample_string)