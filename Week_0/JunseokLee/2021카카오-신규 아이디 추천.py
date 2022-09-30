def solution(new_id):
    new_id = new_id.lower()  # stage1
    remove = []
    dot = []
    for n in range(len(new_id)):  # stage2
        if 'a' <= new_id[n] <= 'z':
            continue
        if '0' <= new_id[n] <= '9':
            continue
        if new_id[n] == '-' or new_id[n] == '_' or new_id[n] == '.':
            continue
        remove.append(n)
    for i in range(len(remove) - 1, -1, -1):
        new_id = new_id[:remove[i]] + new_id[remove[i] + 1:]
    index = 0

    while index < len(new_id):  # stage3
        index2 = index
        while index2<len(new_id) and new_id[index2] == '.':
            index2 += 1
        if index2-index > 1:
            dot.append([index, index2])
            index=index2
        index+=1
    dot.sort(key=lambda x: -x[0])
    for s, e in dot:
        new_id = new_id[:s]+'.' + new_id[e:]
    if new_id[len(new_id)-1] =='.':  # stage 4
        new_id=new_id[:len(new_id)-1]
    if len(new_id)>0 and new_id[0] == '.':
        new_id=new_id[1:]
    if len(new_id) == 0:  # stage5
        new_id+='a'
    if len(new_id) >= 16:  # stage6
        new_id = new_id[:15]
        if new_id[14] == '.':
            new_id = new_id[:14]
    if len(new_id) <= 2:  # stage7
        last = new_id[len(new_id) - 1]
        while len(new_id) < 3:
            new_id = new_id + last
    return new_id