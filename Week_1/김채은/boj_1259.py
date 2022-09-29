# [BOJ] 1259 팰린드롬수

def isPalindrome(num):
    for i in range(len(num)//2):
        if num[i] != num[-(i+1)]:
            return False
    return True

while True:
    num = input()
    if num == '0':
        break
    
    if isPalindrome(num):
        print('yes')
    else:
        print('no')
            