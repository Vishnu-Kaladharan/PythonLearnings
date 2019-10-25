import re
fhandle = open('sample_file.txt')

result = list()

for line in fhandle:
    list_emails = list()
    line = line.rstrip()
    list_emails = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]',line)

    result.extend(list_emails)


print(result)