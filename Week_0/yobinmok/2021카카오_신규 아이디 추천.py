import re

def solution(new_id):
    answer = new_id
    answer = new_id.lower() # step 1
    answer = re.sub(r"[^a-zA-Z0-9-_.]","", answer) # step 2
    answer = re.sub("\.+",".", answer) # step 3
    answer = answer.strip(".") # step 4
    if answer == "":  # step 5
        answer = "a"
    if len(answer) >= 16: # step 6
        if answer[14] == ".":
            answer = answer[0:14]
        else:
            answer = answer[0:15]
    if len(answer) <= 2: # step 7
        while len(answer) != 3:
            answer = answer + answer[-1]

    return answer