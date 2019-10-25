
age = 0
try:
    age = int(input('Enter age'))

except ValueError:
    print('Invalid integer entered')

print(age)