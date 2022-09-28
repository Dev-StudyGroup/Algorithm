'''
단어 공부

- 문제 요약
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램.
단, 대문자와 소문자를 구분하지 않음.

- 입력 조건
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어짐.
주어지는 단어의 길이는 1,000,000을 넘지 않음.

- 출력 조건
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력.
단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력.
'''
word = input().upper()
alphabet_list = list(set(word))
cnt = []
for i in alphabet_list:
    cnt.append(word.count(i))
if (cnt.count(max(cnt))>=2):
    print('?')
else:
    print(alphabet_list[cnt.index(max(cnt))])