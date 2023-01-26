# Messy message
message = ' This IS JUST A lOng text, with some. -- extra Functions. to test the functions in this file. '


# convert text to lowercase
def lowercase(text):
    return text.lower()


# remove special characters
def removePunctuation(text):
    punctuations = [',', '.', ';', ':', '!', '?', '--', '  ']
    for p in punctuations:
        text = text.replace(p, '')
    return text


# remove extra spaces
def removeNewLines(text):
    text = text.replace('\n', '')
    return text


# create an array of functionms
processingFunctions = [lowercase, removePunctuation, removeNewLines]

# for every function in the array, apply it to the message
for func in processingFunctions:
    message = func(message)

print(message)
