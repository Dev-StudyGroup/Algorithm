#팰린드롬 체크함수
def check_p(n):
    while True:
        if len(n)==1:
            return True
        elif len(n)==2:
            if n[0]==n[-1]:
                return True
            else:
                return False
        else:
            if n[0]==n[-1]:
                n=n[1:-1]
            else:
                return False


#입력
while True:
    num = input()
    if num=='0':
        break
    if check_p(num):
        print("yes")
    else:
        print("no")
