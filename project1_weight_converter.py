input_weight = int(input("Weight: "))
input_unit_type = input("(L)bs or (K)g: ")

if input_unit_type in ('l', 'L'):
    weight = input_weight * 0.453592
    unit_type = 'kilos'
elif input_unit_type in ('k', 'K'):
    weight = input_weight / 0.453592
    unit_type = 'pounds'
else:
    print('Invalid input')

print(f'You are {weight} {unit_type}')
