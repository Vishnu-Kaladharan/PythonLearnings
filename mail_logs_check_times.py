fhandle = open('sample_file.txt')

count_mails_as_per_hour = dict()
result = list()

for line in fhandle:
    list_mail_details = list()
    time = list()
    line.rstrip()
    if not line.startswith('From '):
        continue
    list_mail_details = line.split()
    time = list_mail_details[5].split(':')
    count_mails_as_per_hour[time[0]] = count_mails_as_per_hour.get(time[0],0) + 1

for key,value in list(count_mails_as_per_hour.items()):
    result.append((key, value))

result.sort()

for x,y in result:
    print(f'{x} {y}')
