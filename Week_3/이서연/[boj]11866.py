'''
요세푸스 문제 0

- 문제 요약
1번부터 N번까지 N명의 사람이 원을 이루며 앉아있고, 양의 정수 K(<=N)가 주어진다.
이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 N명의 사람이 모두 제거될때까지 계속한다. 
원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.

ex) (7,3)-요세푸스 순열
    <3,6,2,7,5,1,4>
N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램

- 입력 조건
첫째 줄에 N과 K가 빈칸을 사이에 두고 주어진다.
(1 <= K <= N <= 1000)

- 출력 조건
요세푸스 순열을 출력
'''
n, k = map(int, input().split())
circle = [i for i in range(1, n+1)]
index = 0
order = []
for _ in range(n):
    index = index + k - 1
    if index >= len(circle):
        index = index % len(circle)
    delete = circle.pop(index)
    order.append(delete)

print('<'+', '.join(map(str, order))+'>')
