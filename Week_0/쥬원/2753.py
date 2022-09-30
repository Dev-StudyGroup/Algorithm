i = int(input())
if (i%4 == 0 and i%100 != 0) or i%400 == 0:
    print(1)
else:
    print(0)
