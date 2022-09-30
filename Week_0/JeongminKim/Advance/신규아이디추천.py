"""
    카카오 아이디의 규칙
    1. 3자 이상 15자 이하
    2. 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표 문자만 사용가능
    3. 마침표는 처음과 끝에 사용할 수 없음, 연속으로 사용 불가

    1. 모든 대문자를 대응되는 소문자로 치환
    2. 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    3. 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    4. 마침표(.)가 처음이나 끝에 위치한다면 제거
    5. new_id가 빈 문자열이라면, new_id에 "a"를 대입
    6. 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
        제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
    7. 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
"""

import re

def solution(new_id):
    new_id = new_id.lower()
    # 2단계
    m = re.compile('[^a-z0-9-._]+')
    new_id = m.sub('', new_id)
    # 3단계
    m = re.compile('[.]+')
    new_id = m.sub('.', new_id)
    # 4단계
    m = re.compile('^[.]')
    new_id = m.sub('', new_id)
    m = re.compile('[.]$')
    new_id = m.sub('', new_id)
    # 5단계
    if len(new_id) == 0:
        new_id = 'a'
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = m.sub('', new_id)
    # 7단계
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id

# print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))