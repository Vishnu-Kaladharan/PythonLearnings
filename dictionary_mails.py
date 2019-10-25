import files
# file_name = input('Enter File name')
fhandle = open('sample_file.txt')
#print(fhandle)
mail_day_wise = {}
mail_email_wise = {}

for line in fhandle:
    list_words = []
    line = line.rstrip()
    if line.startswith('From '):
        list_words = line.split()
        mail_day_wise[list_words[2]] = mail_day_wise.get(list_words[2],0) + 1
        mail_email_wise[list_words[1]] = mail_email_wise.get(list_words[1],0) + 1
    #print(mail_day_wise)

# print(list_words)

print(mail_day_wise)
print(mail_email_wise)

list_emails = list(mail_email_wise.values())
max_value = max(list_emails)

for key in mail_email_wise:
    if mail_email_wise[key] == max_value:
        print(f'{key} : {mail_email_wise[key]}')

