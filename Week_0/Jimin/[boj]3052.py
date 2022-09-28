'''
'나머지'
'''
num_dic = {}
for i in range(10):
    num = int(input())
    de_result = num % 42
    if de_result in num_dic:
        num_dic[de_result] += 1
    else:
        num_dic[de_result] = 1

print(len(num_dic))