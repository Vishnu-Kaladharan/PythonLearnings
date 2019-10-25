fhandle = open('sample_file.txt')

count_mail_address = dict()

for line in fhandle:
    list_mail_details = list()
    line = line.rstrip()
    if not line.startswith('From '):
        continue

    list_mail_details = line.split()
    count_mail_address[list_mail_details[1]] = count_mail_address.get(list_mail_details[1],0) + 1

maximum_mails = list()

for key,value in list(count_mail_address.items()):
    maximum_mails.append((value,key))


maximum_mails.sort(reverse=True)

(x,y) = maximum_mails[0]
print(f'{y} : {x}')

