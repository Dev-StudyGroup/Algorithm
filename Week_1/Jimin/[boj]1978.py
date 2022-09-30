'''
'소수 찾기'
'''
N = int(input())
n_list = list(map(int, input().split()))

end = max(n_list)

a = [False, False] + [True] * end
prime = []
for i in range(2, end+1):
    if a[i]:
        prime.append(i)
        for j in range(2*i, end+1, i):
            a[j] = False

answer = 0
for i in n_list:
    if i in prime:
        answer += 1

print(answer)