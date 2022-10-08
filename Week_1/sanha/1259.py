while True:
    word = input()
    if word == '0':
        break
    reverse_word = word[::-1]
    if word == reverse_word:
        print("yes")
    else:
        print("no")
