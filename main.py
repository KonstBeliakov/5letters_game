# five letters game

def word_check(word):
    global prev_attempt
    global banned_letters
    global prev_attempt
    global sample
    global wrong_place
    for i in range(5):
        match sample[i]:
            case '0':
                banned_letters.add(prev_attempt[i])
            case '1':
                wrong_place[i].add(prev_attempt[i])
                if prev_attempt[i] not in word or word[i] == prev_attempt[i]:
                    return False
            case '2':
                if prev_attempt[i] != word[i]:
                    return False
    for i in banned_letters:
        if i in word:
            if sample[word.find(i)] != '2':
                return False
    for i in range(5):
        if word[i] in wrong_place[i]:
            return False
    return True


def generate_sample(word, right_word):
    sample = ''
    for i in range(len(word)):
        if word[i] == right_word[i]:
            sample += '2'
        elif word[i] in right_word:
            sample += '1'
        else:
            sample += '0'
    return sample


letter_frequency = {'а': 7998, 'б': 1592, 'в': 4533, 'г': 1687, 'д': 2977, 'е': 8483, 'ж': 940, 'з': 1641, 'и': 7367,
                    'й': 1208, 'к': 3486,
                    'л': 4343, 'м': 3203, 'н': 6700, 'о': 10983, 'п': 2804, 'р': 4746, 'с': 5473, 'т': 6318, 'у': 2615,
                    'ф': 267, 'х': 966,
                    'ц': 486, 'ч': 1450, 'ш': 718, 'щ': 361, 'ъ': 37, 'ы': 1898, 'ь': 1735, 'э': 331, 'ю': 638,
                    'я': 2001}

with open('singular.txt', 'r', encoding='utf-8') as file:
    words = list(filter(lambda x: len(x) == 5, file.read().split()))
    words_sorted = sorted(words, key=lambda s: sum([letter_frequency.get(i, 0) for i in set(s)]))
    banned_letters = set()
    wrong_place = [set(), set(), set(), set(), set()]
    # print(list(filter(lambda x: "р" in x and 'е' in x and 'а' in x and 'н' in x, words_sorted)))
while True:
    word = words_sorted[-1]
    print(word)
    print('0 for letter not in the word, 1 for letter not on the right position, 2 for right letter')
    sample = input()
    prev_attempt = word
    words_sorted = list(filter(word_check, words_sorted[:-1]))
'''
d = [0] * 8
m = len(words)
for i in range(m):
     right_word = words[i]
     attempt = 0
     words_sorted = sorted(words, key=lambda s: sum([letter_frequency.get(i, 0) for i in set(s)]))
     banned_letters = set()
     wrong_place = [set(), set(), set(), set(), set()]
     #print()
     #print(right_word)
     while len(words_sorted) != 0 and attempt < 7:
         word = words_sorted[-1]
         #print(word)
         sample = generate_sample(word, right_word)
         prev_attempt = word
         words_sorted = list(filter(word_check, words_sorted[:-1]))
         attempt += 1
     #print(attempt)
     #print(banned_letters)
     #print(wrong_place)

     d[attempt] += 1
     if i % 100 == 0:
         print(f"{100 * i // m}%")

for i in range(6):
    print(f'Угадано за {i} попыток: {d[i]} раз ({d[i] * 100 // len(words)}%)')
print(f"Провалов: {d[7]} ({d[7] * 100 // len(words)}%)")'''

