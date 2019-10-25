input_list = [1,2,1,2,3,4,3,5,6,11,23,25,2,2,1,11,23,25]
print(len(input_list))

result = []

for item in input_list:
    if item not in result:
        result.append(item)


print(result)
print(len(result))