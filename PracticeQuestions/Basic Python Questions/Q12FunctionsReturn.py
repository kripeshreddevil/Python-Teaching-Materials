def emojiConverter(message):
    emoji = {
        ":)": "😁",
        ":(": "🥺",
        ":/": "🙂"
    }

    words = message.split()
    converted_message = ""
    for word in words:
        converted_message += emoji.get(word, word) + " "
    return converted_message


print(emojiConverter("I am sad :( "))