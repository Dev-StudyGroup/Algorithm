#입력
year = int(input())
#구현
if year%400==0:
    print(1)
elif year%100!=0 and year%4==0:
    print(1)
else:
    print(0)
