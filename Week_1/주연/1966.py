n = int(input())

for i in range(n):
    num, fileLine = map(int, input().split())
    impList = list(map(int, input().split()))
    idx = list(range(len(impList)))
    idx[fileLine] = 'x'

    order = 0

    while True:
        if impList[0] == max(impList):
            order += 1

            if idx[0] == 'x':
                print(order)
                break
            else:
                impList.pop(0)
                idx.pop(0)
        else:
            impList.append(impList.pop(0))
            idx.append(idx.pop(0))