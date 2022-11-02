import sys
#입력
n = int(sys.stdin.readline())
dot=[]
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    dot.append((x,y))
    
#정렬
dot.sort()

#출력
for x, y in dot:
    print(x, y)
