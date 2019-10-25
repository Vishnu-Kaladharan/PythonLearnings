price_house = 1000000
has_good_credit = True
has_criminal_record = True


if has_good_credit and not has_criminal_record:
    credit = 10
else:
    credit = 20

offer_price = round(price_house-((credit/100) * price_house))
print(f"The Offer Price is ${offer_price}")

name = input("Please type your name: ")

if len(name) < 3:
    print('Please enter at least 3 characters')
elif len(name) > 50:
    print('Entered name exceeds 50 characters')
else:
    print('Name is good')