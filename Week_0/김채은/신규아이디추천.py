# [Programmers] 72410 신규 아이디 추천
# Time Taken: 32m

import re

def solution(new_id):
    answer = new_id[:]
    answer = answer.lower()
    answer = re.sub('[^a-z0-9-_.]', '', answer)
    answer = re.sub('[.]+', '.', answer)
    answer = answer[1:] if answer and answer[0] == '.' else answer
    answer = answer[0:-1] if answer and answer[-1] == '.' else answer
    answer = 'a' if not answer else answer
    answer = answer[0:15] if len(answer) > 15 else answer
    answer = answer[0:-1] if answer[-1] == '.' else answer
    answer = answer + answer[-1]*(3-len(answer)) if len(answer)<=2 else answer
    return answer
