# def print_words_upper (list):
# #takes in a list of words and returns each word in all uppercase
#     for word in list:
#         print(word.upper())
    
# wordlist = ['Bear','Beats','Battlestar Galactica','Eggs','Espresso','Enron']

# print_words_upper(wordlist)


# def print_words_upper (list):
# #prints only words that start with 'e' (upper or lower case)
#     for word in list:
#         if word.startswith('e') or word.startswith('E'):
#             print(word)
        
    
# wordlist = ['Bear','Beats','Battlestar Galactica','Eggs','Espresso','enron']

# print_words_upper(wordlist)


# def print_words_upper (list,starts_with):
# #prints only words that start with 'e' (upper or lower case)
#     for word in list:
#         if word.startswith(starts_with):
#             print(word.upper())
    
# wordlist = ['Bear','Beats','Battlestar Galactica','Eggs','Espresso','enron']

# print_words_upper(wordlist,'b')


def print_upper_words3(words, must_start_with):
    """Print each word on sep line, uppercased, if starts with one of given

        >>> print_upper_words3(["eagle", "Edward", "Alfred", "zope"],
        ...                   must_start_with=["A", "E"])
        EDWARD
        ALFRED
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
    
wordlist = ['Bear','Beats','Battlestar Galactica','Eggs','Espresso','enron']

print_upper_words3(wordlist,'b')