#입력
ls=list(map(int, input().split()))
#출력
asc=[1,2,3,4,5,6,7,8]
des=[8,7,6,5,4,3,2,1]

if ls==asc:
    print("ascending")
elif ls==des:
    print("descending")
else:
    print("mixed")
