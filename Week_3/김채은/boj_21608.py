# [BOJ] 21608 상어 초등학교
# Time Taken: 51m

n = int(input())

students = []
preference = [[0]*(n**2 + 1) for _ in range(n**2 + 1)]

for _ in range(n**2):

    preferred_list = list(map(int, input().split()))

    student = preferred_list[0]

    students.append(student)

    for preferred in preferred_list[1:]:
        preference[student][preferred] = 1

def inRange(y, x):

    if 0 <= y < n and 0 <= x < n:
        return True
    else:
        return False

def isLike(student, other):

    return preference[student][other]

classroom = [[0] * n for _ in range(n)]
    
def sit(student):

    dys, dxs = [1, 0, -1, 0], [0, 1, 0, -1]

    seats = []

    for i in range(n):

        for j in range(n):

            if classroom[i][j]:
                continue

            seat = [0, 0, i, j]

            for dy, dx in zip(dys, dxs):
                y, x = i + dy, j + dx

                if inRange(y, x):
                    preferred = classroom[y][x]

                    if not preferred:
                        seat[1] += 1
                    elif isLike(student, preferred):
                        seat[0] += 1

            seats.append(seat)

    seats.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    
    result = seats[0]

    return (result[2], result[3])

def satisfy():

    dys, dxs = [1, 0, -1, 0], [0, 1, 0, -1]

    satisfaction = 0

    for i in range(n):

        for j in range(n):

            count = 0

            for dy, dx in zip(dys, dxs):
                y, x = i + dy, j + dx

                student, preferred = classroom[i][j], classroom[y][x]

                if inRange(y, x) and isLike(student, preferred):
                    count += 1

            if count:
                satisfaction += 10 ** (count - 1)
    
    return satisfaction

for student in students:
    y, x = sit(student)     
    classroom[y][x] = student

print(satisfy())
