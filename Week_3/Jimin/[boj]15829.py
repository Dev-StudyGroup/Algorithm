'''
'Hashing'
'''
L = int(input())
string = input()
M = 1234567891

temp = 0
for i in range(L):
    a = ord(string[i]) - 96
    temp += a * 31**i

print(temp % M)
