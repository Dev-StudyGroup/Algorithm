"""

    팰린드롬 수: 121 1221 12421

    주어진 수의 자릿 수가 홀수일 경우
    [:len(number)//2] , [len(number)//2+1::-1]가 같을 경우 팰린드롬 수이다.

    주어진 수의 자릿수가 짝수일경우
    [:len(number)/2] , [len(number)//2::-1] 가 같을 경우 팰린드롬 수이다.

"""

class ZeroNum(Exception):
    def __init__(self):
        super().__init__()

result = []
while True:
    number = input()
    if number == '0':
        break
    mid = len(number) // 2
    if len(number) % 2 != 0:
        left = number[:mid]
        left = left[::-1]
        right = number[mid+1:]
        if left == right:
            result.append('yes')
        else:
            result.append('no')
    else:
        left = number[:mid]
        left = left[::-1]
        right = number[mid:]
        if left == right:
            result.append('yes')
        else:
            result.append('no')

for i in range(len(result)):
    print(result[i])
