def word_mixer(word_list):
    words = "She could hear him in the shower singing with a joy she hoped he'd retain after she delivered the news."
    words = input("enter random words: ")
    word_list = words.split()
    word_length = len(word_list)
for n in range(word_length):
    if len(word_list[n]) <=3:
        word_list[n] = word_list[n].lower()
    elif len(word_list[n]) >= 5:
        word_list[n] = word_list[n].upper()

     print(word_list)      