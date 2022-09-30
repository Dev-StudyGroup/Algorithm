"""

    수 10개를 입력 받은 뒤, 이를 42로 나눈 나머지를 구한다.

"""
i=1
ls = []
while 1:
    if i > 10:
        break

    num = int(input()) % 42
    if num not in ls:
        ls.append(num)
    i += 1
print(len(ls))