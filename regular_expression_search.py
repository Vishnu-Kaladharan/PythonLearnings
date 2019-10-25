import re

txt_1 = 'Vishnu: Hi my name is Vishnu. My Email ID is vishnukaladhar@gmail.com'

txt_2 = 'Sonia: Hi my name is Sonia. My Email ID is soniasingh124@gmail.com'

txt_3 = 'Vishnu: Nice to Meet you!'

if re.search('^Vishnu:.+@.+',txt_1):
    print('Match Found')
else:
    print('Match not found')