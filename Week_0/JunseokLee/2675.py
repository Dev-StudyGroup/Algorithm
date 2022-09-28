T = int(input())
for _ in range(T):
    R, S = input().split()
    for i in range(len(S)):
        for j in range(int(R)):
            print(S[i],end='')
    print()