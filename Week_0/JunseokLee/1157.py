ss = input()
ss = ss.upper()
arr = []
alpha = set()

for s in ss:
    if s not in alpha:
        alpha.add(s)
        arr.append([s,1])
    elif s in alpha:
        for i in range(len(arr)):
            if arr[i][0] == s:
                arr[i][1] += 1
arr.sort(key=lambda x:-x[1])

if len(arr)>1:
    if arr[0][1] == arr[1][1]:
        print('?')
    else:
        print(arr[0][0])
else:
    print(arr[0][0])