# BOJ 20055
def checkDown():
    if robot[N-1] != 0:
        robot[N-1] = 0
    return
N, K = map(int, input().split())
# N : 벨트의 길이, K: 내구도가 0인 칸의 개수
Alist = list(map(int, input().split()))
step = 1; i = 0; robot = [0] * (2 * N)
leng = len(Alist)

while True:
    # step 1
    for i in range(leng-1, 0, -1):
        temp = Alist[i]
        Alist[i] = Alist[i-1]
        Alist[i-1] = temp

        temp = robot[i]
        robot[i] = robot[i-1]
        robot[i-1] = temp
    checkDown()
    # step 2
    for i in range(N-2, -1, -1):
        if robot[i] == 1 and robot[i+1] == 0 and Alist[i+1] > 0:
                robot[i] = 0
                robot[i+1] = 1
                Alist[i+1] -= 1
    checkDown()
    # step 3
    if Alist[0] != 0:
        robot[0] = 1
        Alist[0] -= 1
    
    if Alist.count(0) >= K:
        break
    step += 1

print(step)
