#def filter_long_words(lwords, n):
    #new_list = []
   # for i in lwords:
        #if len(i) > n:
            #newlist.append(i)
        #else :
            #pass
    #return new_list
def filterlongword(lwords,n):

    for i in range(len(lwords)):
        new_list = []
        if len(lwords[i]) > n:
            new_list.append(lwords[i])

        return new_list


def main():
    words = input("Please input the list of words: ")
    integer = eval(input("Please input an integer: "))

    words1 = filterlongword(words,integer)

    print("The list of words greater than the integer is",words1)

main()
