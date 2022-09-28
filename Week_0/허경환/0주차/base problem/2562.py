#입력
num=[0]
for i in range(9):
    num.append(int(input()))
#최댓값 찾기
m_num=max(num)
#최댓값의 인덱스 찾기
m_index=num.index(m_num)
#출력
print(m_num)
print(m_index)
