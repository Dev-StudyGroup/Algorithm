#입력
n1, n2, n3, n4, n5 = map(int, input().split())
#검증수 구하기
result=(n1**2+n2**2+n3**2+n4**2+n5**2)%10
#출력
print(result)

