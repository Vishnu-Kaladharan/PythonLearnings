def open_file(file_name):
    try:
        fhand = open(file_name)
    except:
        print('Invalid File Name')
        exit()
    return fhand


# file_handle = open_file(input('Enter File Name: '))
# spam_value = []
#
# for line in file_handle:
#     line = line.rstrip()
#     if line.startswith('X-DSPAM-Confidence:'):
#         position = line.find(': ')
#         value = float(line[position + 1:])
#         spam_value.append(value)
#
# print(f'The average of spam value is {sum(spam_value)/len(spam_value)}')
