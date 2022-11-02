# this is an emoji converter file that creates a function with a positional parameter that contains the input from the user

def emoji_converter(message):
    words = message.split(" ")
    emoji = {
        ":)": "Smiley",
        ":(": "Sady"
    }
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output


line = "Hi I am happy to be here :)"
result = emoji_converter(line)
print(result)
