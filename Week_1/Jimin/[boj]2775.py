'''
'부녀회장이 될테야'
'''
T = int(input())
t_list = []
maxK = 0
maxN = 0
for i in range(T):
    k = int(input())
    n = int(input())
    t_list.append([k, n])
    maxK = max(maxK, n)
    maxN = max(maxN, n)

people = [[i for i in range(1, maxN+1)] for j in range(maxK+1)]
for i in range(1, maxK+1):
    for j in range(1, maxN):
        people[i][j] = people[i-1][j] + people[i][j-1]

for i in t_list:
    x = i[0]
    y = i[1]-1
    print(people[x][y])