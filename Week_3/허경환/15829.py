#입력
l = int(input())
string = input()

M=1234567891
r=31

#해시함수 구현
def hash_func(x):
    sum_num=0
    for i in range(len(x)):
        sum_num+=x[i]*(r**i)
    return sum_num

#영어 소문자로 이루어진 문자열을 숫자문자열로 변환
num_str=[]
for i in string:
    num_str.append(ord(i)-96)

#해시값 출력
print(hash_func(num_str)%M)
