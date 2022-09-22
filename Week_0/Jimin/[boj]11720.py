'''
'숫자의 합'
'''
n = int(input())
num_str = input()
answer = 0
for i in num_str:
    answer += int(i)

print(answer)