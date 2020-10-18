def find_longest_word(lwords):
    word = []
    for i in lwords:
        word.append(len(i))
    return max(word)
    print(find_longest_word())