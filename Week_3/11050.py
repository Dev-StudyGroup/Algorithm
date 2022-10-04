from itertools import combinations

#입력
n, k = map(int, input().split())

#요소가 n개인 리스트만들기
ls = []
for i in range(n):
    ls.append(i)

#출력
print(len(list(combinations(ls,k))))
