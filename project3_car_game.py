is_started = False
while True:
    value = input('>').lower()
    if value == 'help':
        print('''start - to start the car
stop - to stop the car
quit - to exit''')
    elif value == 'start':
        if is_started:
            print('The car is already started')
        else:
            print('Car started... Ready to go!')
            is_started = True
    elif value == 'stop':
        if not is_started:
            print('The car is already stopped')
        else:
            print('Car is stopped!')
            is_started = False
    elif value == 'quit':

        exit()
    else:
        print("I don't understand that...")
