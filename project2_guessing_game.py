secret_number = 9
guess_count = 1
flag = False
while guess_count <= 3:
    guess = int(input(f"Guess {guess_count}: "))
    if guess == 9:
        flag = True
        break
    guess_count += 1

if flag:
    print('You won!!!')
else:
    print('Sorry You lost!!!')