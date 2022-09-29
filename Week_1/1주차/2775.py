#테스트케이스 개수 입력
t = int(input())

for i in range(t):
    #층수입력
    k = int(input())
    #호수입력
    n = int(input())
    
    #문제풀이방법
    #for문으로 층수를 증가시키며 파악하기
    #크기가 n인 리스트를 2개 만들어 현재층과 이전층의 각 호 인원 저장
    
    #현재층의 인원 저장할 리스트
    this_floor=[0]*(n+1)
    #아래층의 인원 저장할 리스트 - 처음에는 0층의 인원으로 초기화
    down_floor=[i for i in range(n+1)]
    #구현
    for i in range(1, k+1):
        for j in range(n+1):
            this_floor[j]=sum(down_floor[:j+1])
        for j in range(n+1):
            down_floor[j]=this_floor[j]
        
    #출력
    print(this_floor[n])
