quote = input("Enter a 1 sentence quote, non-alpha separate words: ")
word = ''
for letter in quote:
    if letter.isalpha():
        word += letter
        print("letter is: ", word)
    elif word.lower() >= 'h' :
        print(word.upper())
        word = ''
    else:
        word = ''
    if word.lower() >= 'h' :
        print(word.upper())           