
num = int(input()) # 테스트 케이스의 수

for i in range(num):
    count = 0
    n, m = map(int, input().split()) # 문서의 개수, 몇 번째로 인쇄되었는지 궁금한 문서의 위치
    score = list(map(int, input().split())) # 문서 별 중요도
    idx = list(range(len(score)))
    idx[m] = 'target'
    while True:
        if score[0] == max(score):
            count += 1
            if idx[0] == 'target':
                print(count)
                break
            else:
                score.pop(0)
                idx.pop(0)
        else:
            score.append(score.pop(0))
            idx.append(idx.pop(0))


        

        
