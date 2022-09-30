'''
'신규 아이디 추천'
'''
def solution(new_id):
    answer = new_id

    # 1단계
    answer = answer.lower()

    # 2, 3단계
    temp = ''
    isOne = True
    for i in answer:
        if i != '.' and ((ord(i) >= 97 and ord(i) <= 122) or (i.isdigit() == True) or i == '-' or i == '_'):
            isOne = True
        if (ord(i) >= 97 and ord(i) <= 122) or (i.isdigit() == True) or i == '-' or i == '_' or i == '.':
            if isOne:
                temp += i
            if i == '.':
                isOne = False
            else:
                isOne = True
    answer = temp

    # 4, 5단계
    if len(answer) == 0:
        answer = 'a'
    if answer[0] == '.':
        answer = answer[1:]

    if len(answer) == 0:
        answer = 'a'
    if answer[-1] == '.':
        answer = answer[:-1]

    # 5단계
    if len(answer) == 0:
        answer = 'a'

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]

    # 7단계
    if len(answer) <= 2:
        answer = answer + answer[-1] * (3-len(answer))

    return answer
print(solution("...!@BaT#*..y.abcdefghijklm"))
