"""

    나이와 이름이 가입한 순서대로 주어진다.

    나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬

"""
N = int(input())
ls = []
for i in range(0, N):
    age, name = input().split()
    age = int(age)

    ls.append([age, name, i])

ls.sort(key=lambda x:[x[0],x[2]])

for age, name, i in ls:
    print(f'{age} {name}')