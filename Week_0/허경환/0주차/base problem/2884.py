#입력
h, m = map(int, input().split())

#구현
if m>=45:
    print(h, end=' ')
    print(m-45)
elif h==0:
    print(23, end=' ')
    print(60-(45-m))
else:
    print(h-1, end=' ')
    print(60-(45-m))
