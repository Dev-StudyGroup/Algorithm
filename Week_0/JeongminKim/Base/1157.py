def find_max(count_alpha):
    max_num = -1
    max_letter = []
    for key, value in count_alpha:
        if value > max_num:
            max_num = value
            max_letter = []
            max_letter.append(key)
        elif value == max_num:
            max_letter.append(key)
    return max_letter, max_num

word = input()
count_alpha = dict()

for i in word:
    letter = i.lower()
    if letter not in count_alpha.keys():
        count_alpha[letter] = 1
    else:
        count_alpha[letter] += 1

count_alpha = sorted(count_alpha.items(), key = lambda item: item[1])

max_letter, max_num = find_max(count_alpha)

if len(max_letter) == 1:
    print(max_letter[0].upper())
else:
    print('?')