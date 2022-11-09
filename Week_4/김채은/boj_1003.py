from typing import Final

def getNumberOf(case):
    for i in range(2, LIMIT):
        case[i] = case[i-1] + case[i-2]

    return case

if __name__ == "__main__":
    t = int(input())
    
    LIMIT: Final = 41

    zero = [0 for _ in range(LIMIT)]
    one = [0 for _ in range(LIMIT)]

    zero[0] = 1
    one[1] = 1

    zero = getNumberOf(zero)
    one = getNumberOf(one)

    for _ in range(t):
        n = int(input())

        print(zero[n], one[n])
