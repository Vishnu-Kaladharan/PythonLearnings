dict_one = dict()

print(dict_one)

dict_one['one'] = 'onnu'
print(dict_one)

dict_two = {'one': 'onnu',
            'two': 'randu',
            'three': 'moonu'}
print(dict_two)

flag_1 = 'one' in dict_two
flag_2 = 'onnu' in dict_two
print(f'Whether key in the dictionary: {flag_1}')
print(f'wrong way of searching a value in dictionary {flag_2}')

list_values = dict_two.values()
print(list_values)
print(type(list_values))

flag_3 = 'onnu' in list_values
print(f'Way to check if a value is there in the list {flag_3}')