'''
'팰린드롬수'
'''
while True:
    answer = 'yes'
    word = input()

    if word == '0':
        break

    for i in range(len(word)//2):
        if word[i] != word[-1-i]:
            answer = 'no'
            break

    print(answer)