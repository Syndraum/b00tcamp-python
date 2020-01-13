import string


def text_analyzer(str=None):
    if str is None:
        print("What is the text to analyse?")
        str = input(">> ")
    upper = 0
    lower = 0
    ponct = 0
    space = 0
    for i in str:
        if string.ascii_uppercase.find(i) != -1:
            upper += 1
        elif string.ascii_lowercase.find(i) != -1:
            lower += 1
        elif string.punctuation.find(i) != -1:
            ponct += 1
        elif i == ' ':
            space += 1
    print("The text contains", len(str), "characters:")
    print("-", upper, "upper letters")
    print("-", lower, "lower letters")
    print("-", ponct, "lower punctuation marks")
    print("-", space, "lower spaces")
