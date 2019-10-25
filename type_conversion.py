# type conversion of variable- int() float() str()

weight_in_pound = input('Type your weight in Pounds: ')
print(type(weight_in_pound))
weight_in_pound = float(weight_in_pound)
print(type(weight_in_pound))
weight_in_kg = weight_in_pound * 0.453592

print("Your weight in Kg: " + str(weight_in_kg))
