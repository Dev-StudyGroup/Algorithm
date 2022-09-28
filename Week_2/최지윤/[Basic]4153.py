result = []

while 1:
    abc = list(map(int, input().split()))

    if abc == [0, 0, 0]:
        break

    abc.sort()
    if abc[0]**2 + abc[1]**2 == abc[2]**2:
        result.append('right')
    else:
        result.append('wrong')

for r in result:
    print(r)