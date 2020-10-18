import string

def check_pangram(sentence):
    alphabet = string.ascii_uppercase
    for words in alphabet:
        if words not in sentence.upper():
            return False
    return True

def main():
    sentence = input('Input your sentence here to check:')
    if check_pangram(sentence) == True:
        print('The sentence is a pangram')
    else:
        print('The sentence is not a pangram')