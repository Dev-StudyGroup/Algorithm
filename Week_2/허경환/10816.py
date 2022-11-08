from bisect import bisect_left
#입력
n = int(input())
card_num = list(map(int, input().split()))
m = int(input())
tar_num = list(map(int, input().split()))
set_card_num = set(card_num)

#딕셔너리 - key : 숫자카드에 적혀있는 숫자, value : 해당 숫자의 카드 소유 개수
tmp = {}
for i in set_card_num:
    tmp[i]=0
for i in card_num:
    tmp[i]+=1

#딕셔너리 키 기준 오름차순 정렬
s_tmp = sorted(tmp.items())
key_tmp = list(i[0] for i in s_tmp)
value_tmp = list(i[1] for i in s_tmp)

#이진탐색으로 tar_num의 개수 찾기
for i in tar_num:
    if i in set_card_num:
        print(value_tmp[bisect_left(key_tmp, i)], end=' ')
        
    else:
        print(0, end=' ')
