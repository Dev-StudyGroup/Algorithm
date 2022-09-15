"""
2021-카카오기출: 신규 아이디 추천
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
import re
p = re.compile('[a-z0-9-_.]')

def solution(new_id):
    answer = ''
    temp = []
    dot_flag = True

    new_id = new_id.lower()
    for x in p.findall(new_id):
        if x == '.' and dot_flag:
            temp.append(x)
            dot_flag = False
        elif x != '.':
                dot_flag = True
                temp.append(x)

    if len(temp) > 0:
        if temp[0] == '.':
            del temp[0]
            
    if len(temp) > 0:
        if temp[-1] == '.':
            del temp[-1]

    if len(temp) == 0:
        temp.append('a')
    
    if len(temp) >= 16:
        temp = temp[:15]
        if temp[-1] == '.':
            del temp[-1]
    elif len(temp) <= 2:
        while len(temp) < 3:
            temp.append(temp[-1])

    for x in temp:
        answer += x

    return answer
