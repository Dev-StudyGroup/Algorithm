T = int(input())
for t in range(T):
    s = input()
    arr = [0]*len(s)
    if s[0] == 'O':
        arr[0]=1
    for i in range(1,len(s)):
        if s[i]=='O' and s[i-1]=='O':
            arr[i] = arr[i-1]+1
        elif s[i]=='O':
            arr[i]+=1
    print(sum(arr))