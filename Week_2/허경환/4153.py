while True:
    ls = list(map(int, input().split()))
    ls.sort()
    if ls[0]==0 and ls[1]==0 and ls[2]==0:
        break
    else:
        if ls[0]**2+ls[1]**2==ls[2]**2:
            print("right")
        else:
            print("wrong")
