def pick_colour(num):

    if num == 0:
        colour = 'Red'

    elif num == 1:
        colour = 'Green'

    else:
        colour = 'Orange'
    return colour


def pick_lane(selection):
    selection = selection.lower()
    if selection == 'right':
        return 'Right'
    elif selection == 'left':
        return 'Left'
    else:
        return 'Invalid entry'




