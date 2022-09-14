def solution(new_id):
    n_id = []
    for i in range(len(new_id)):
        if new_id[i].isalpha() or new_id[i].isdigit() or new_id[i] in ('-', '_', '.'):
            if new_id[i].isalpha():
                n_id.append(new_id[i].lower())
            else:
                n_id.append(new_id[i])
    n_id1 = []
    tmp = -1
    for i in range(len(n_id)):
        if i > tmp and n_id[i] == '.':
            for j in range(i, len(n_id)):
                if n_id[j] == '.':
                    tmp = j
                else:
                    break
            n_id1.append('.')
        elif n_id[i] != '.':
            n_id1.append(n_id[i])
    if n_id1 and n_id1[0] == '.':
        n_id1.pop(0)
    if n_id1 and n_id1[-1] == '.':
        n_id1.pop()
    if not n_id1:
        n_id1.append('a')
    if len(n_id1) >= 16:
        n_id1 = n_id1[:15]
        if n_id1[-1] == '.':
            n_id1.pop()
    if len(n_id1) <= 2:
        n_id1.extend([n_id1[-1] for _ in range(3-len(n_id1))])
    answer = ''.join(n_id1)
    return answer