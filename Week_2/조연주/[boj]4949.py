"""
균형잡힌 세상
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
while 1:
    string = list(input())
    if string == ['.']:
        break
    bracket = ['0']
    result = "yes"
    for s in string:
        if s in ['(', '[']:
            bracket.append(s)
        elif s == ')':
            if bracket[-1] == '(':
                bracket.pop()
            else:
                result = 'no'
                break
        elif s == ']':
            if bracket[-1] == '[':
                bracket.pop()
            else:
                result = 'no'
                break
        else:
            continue
    
    if bracket != ['0']:
        result = 'no'
    
    print(result)
