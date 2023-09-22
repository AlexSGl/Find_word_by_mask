# Подготовка файла со списком слов
my_file_word = open('russian_nouns.txt', "r", encoding='utf-8')
data_read = my_file_word.read()
list_noun = data_read.replace("\n", " ").split(" ")

mask = input(
    'Легенда: * - любая буква, g - любая гласная, s - любая согласная, а-я - точное соответствие.\nВведите маску:')

# Создание списка слов длиной = длине маски
list_noun_len = []
for word in list_noun:
    if len(mask) == len(word):
        list_noun_len.append(word)

# Поиск слова по маске
count = 0
list_noun_len_word = []

for word in list_noun_len:
    word_new = []
    for i in range(len(word)):
        if mask[i] == '*' or mask[i] == word[i]:
            word_new.append(word[i])
        else:
            word_new = []
            break
    if word_new:
        list_noun_len_word.append(''.join(word_new))
        count += 1

print('Найдено', count, 'слов:', list_noun_len_word)

# Поиск слов с буквами, которые ЕСТЬ в слове
char_str_yes = input('Какие буквы ЕСТЬ в слове, введите через пробел:')
if char_str_yes != '':
    char_arr_yes = char_str_yes.split()
    print(char_arr_yes)
    list_noun_len_word_yes = []
    for word in list_noun_len_word:
        count = 0
        for char in char_arr_yes:
            if char in word:
                count += 1
                if count == len(char_arr_yes):
                    list_noun_len_word_yes.append(word)
else:
    list_noun_len_word_yes = list_noun_len_word

print('Найдено', len(list_noun_len_word_yes), 'слов:', list_noun_len_word_yes)

# Поиск слов с буквами, которых НЕТ в слове
char_str_no = input('Каких букв НЕТ в слове, введите через пробел:')
if char_str_no != '':
    char_arr_no = char_str_no.split()
    list_noun_len_word_yes_no = []
    for word in list_noun_len_word_yes:
        count = 0
        for char in char_arr_no:
            if char not in word:
                count += 1
                if count == len(char_arr_no):
                    list_noun_len_word_yes_no.append(word)
else:
    list_noun_len_word_yes_no = list_noun_len_word_yes

print('Найдено', len(list_noun_len_word_yes_no), 'слов:', list_noun_len_word_yes_no)

my_file_word.close()