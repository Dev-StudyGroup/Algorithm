'''
스택 수열

- 문제 요약
스택(stack)은 자료를 넣는(push) 입구와 자료를 뽑는(pop) 입구가 같아 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out)특성을 가지고 있다.
1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓아 하나의 수열을 만든다고 하자. 
이때 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다.
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들수 있는지, 있다면 어떤 순서로 push, pop을 수행해야 하는지를 계산하는 프로그램

- 입력 조건
첫째 줄에 n(1<=n<=100,000)이 주어짐.
둘째 줄부터 n개의 줄에는 수열을 이루는 1 이상 n 이하의 정수가 하나씩 순서대로 주어짐(같은 정수가 두 번 나오는 일은 없다.)

- 출력 조건
입력된 수열을 만들기 위해 필요한 연산을 한 줄에 하나씩 출력.
push 연산은 +로, pop 연산은 -로 표현하도록 한다.
불가능한 경우 NO를 출력
'''
n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

curr = 1
stack = []
calc = []

for x in array:
    while x >= curr:
        stack.append(curr)
        calc.append('+')
        curr += 1
    
    if x == stack[-1]:
        stack.pop()
        calc.append('-')
    else:
        calc = []
        break

if calc:
    for i in calc:
        print(i)
else:
    print('NO')
