class ZeroNum(Exception):
    def __init__(self):
        super().__init__()

while True:
    try:
        A, B= map(int,input().split())
        if A == 0 & B == 0:
            raise ZeroNum
        print(A+B)
    except ZeroNum:
        break
