def emoji_converter(input_string):
    emojis = {
        ":)": "\U0001F642",

        ":D": "\U0001F601",

        ":(": "\U0001F642"
    }
    message = ""
    words = input_string.split()
    for word in words:
        message = message + emojis.get(word,word) + " "

    return message


inp = input('> ')
output = emoji_converter(inp)
print(output)

