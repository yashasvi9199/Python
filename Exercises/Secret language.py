import secrets
import string
import logging

# TODO """ Secret Language tool model """.

# TODO ##Encode
# TODO if word has 3 or less chars -> reverse the word
# TODO otherwise, trim first letter and append it at the last of the word. In addition, add three random characters at end and beginning of the word

# TODO ##Decode
# TODO if word has 3 or less chars -> reverse the word
# TODO otherwise, remove first and last three chars from beginning and end. Trim the last char of new word and append it at the beginning of word.


# * Function to encode a word
def encode(sentence) -> str:  # ? Returns string
    sentence = sentence.upper().split()  # ? Convert to uppercase and Split into words
    code = []  # ? initialising output list
    for word in sentence:
        if len(word) <= 3:
            res = word[::-1]
        else:
            res = (
                "".join(
                    secrets.choice(string.ascii_uppercase + string.digits)
                    for _ in range(3)  # ? The first chars include capital letters
                )
                + word[1:]
                + word[0]
                + "".join(
                    secrets.choice(string.ascii_letters)
                    for _ in range(3)  # ? The last chars include small letters
                )
            )
        # print(res)
        code.append(res)
    return " ".join(code)  # ? returns string with space in encoded words

def decode(sentence) -> str:
    sentence = sentence.upper().split()
    code = []
    for words in sentence:
        if len(words) <=3:
            res = words[::-1]
        else:
            word = words[3:-3]
            l = len(word)
            res = word[l-1] + word[:l-1]
        code.append(res)
    return " ".join(code)    

choice = input("Do you want to encode or decode? ")
match choice.lower():
    case "encode":
        sentence = input("Enter sentence to encode : ")
        print(encode(sentence))
    case "decode":
        sentence = input("Enter sentence to decode : ")
        print(decode(sentence))
    case _:
        print("Please enter valid option!")
