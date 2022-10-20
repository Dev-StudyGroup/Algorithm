import sys
input = sys.stdin.readline
# n줄에 'x y' 입력 받기
arr = [input() for _ in range(int(input()))]
# x좌표 정렬 후 y좌표를 정렬한 결과를 arr에 저장
# 한 줄을 나누어 리스트로 저장후 정수형으로 변환
arr = sorted(arr, key = lambda x: (int(x.split()[0]), int(x.split()[1])))
# arr은 한 줄에 (x y)가 있으므로..
print(''.join(arr))

