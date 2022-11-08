"""
1463: 1로 만들기
* 동적계획법(DP) 문제
  전의 결과를 다음 결과에 이용하게 되는 점화식을 활용
  앞에서 구한 결과값을 저장했다가 후에 사용

정수 X에 사용할 수 있는 연산
 - x가 3으로 나누어 떨어지면 3으로 나눈다
 - x가 2으로 나누어 떨어지면 2로 나눈다
 - 1을 뺀다
"""

N = int(input())
result = [0] * (N+1) # 인덱스 수가 1이 되는데 필요한 연산횟수 저장
    
for i in range(2, N+1):
    result[i] = result[i-1] + 1
    if i % 3 == 0:
        result[i] = min(result[i], result[i//3] + 1)
    if i % 2 == 0:
        result[i] = min(result[i], result[i//2] + 1)

print(result[N])

