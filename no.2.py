#def translate(text):
    #consonants = 'bcdfghjklmnpqrstwxyz'
    #final = ' '
    #for l in text:
        #if l in consonants:
            #final +=
x=input('Please input a word or a sentence to translate: ')
def trans(x):
    string = ""
    for l in x:
        string += l
        if l in "bcdfghjklmnpqrstvwxz":
            string += 'o' + l
    return string
print(trans(x))