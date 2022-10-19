"""
괄호
@Author : yeonjoo cho
@contact : wormjoo@naver.com
"""
t = int(input())

for _ in range(t):
    string = list(input())
    bracket = ['0']
    result = 'YES'
    for s in string:
        if s == '(':
            bracket.append(s)
        elif s == ')':
            if bracket[-1] == '(':
                bracket.pop()
            else:
                result = 'NO'
                break
    
    if bracket != ['0']:
        result = 'NO'
    
    print(result)
