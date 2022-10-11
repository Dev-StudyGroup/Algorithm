'''
단어 정렬

- 문제 요약
알파벳 소문자로 이루어진 N개의 단어가 들어오면
    1) 길이가 짧은 것부터
    2) 길이가 같으면 사전 순으로
정렬하는 프로그램

- 입력 조건
첫째 줄에 단어의 개수 N이 주어짐(1<= N <= 20000)
둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어짐.
주어진 문자열의 길이는 50을 넘지 않음

- 출력 조건
조건에 따라 정렬하여 단어들을 출력.
단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력
'''
n = int(input())
words = []

for _ in range(n):
    word = input()
    words.append([word, len(word)])
words.sort(key = lambda x:(x[1], x[0]))

new_list = []
for i in words: # 중복제거, 단어만 리스트에 넣기
    if i[0] not in new_list:
        new_list.append(i[0])

for x in new_list:
    print(x)
