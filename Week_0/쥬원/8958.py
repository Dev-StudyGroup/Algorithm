import sys
input = sys.stdin.readline
for _ in range(int(input())):
    t,s = 0,0
    for i in input():
        if i == "O":
            t+=1
            s+=t
        else:
            t=0
    print(s)
