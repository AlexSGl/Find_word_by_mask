# Подготовка файла со списком слов
my_file_word = open('russian_nouns.txt', "r", encoding='utf-8')
data_read = my_file_word.read()
list_noun = data_read.replace("\n", " ").split(" ")

mask = input('Легенда: * - любая буква, g - любая гласная, s - любая согласная, а-я - точное соответствие.\nВведите маску:')


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
    if word_new != []:
        list_noun_len_word.append(''.join(word_new))
        count += 1

print('Найдено', count, 'слов:', list_noun_len_word)


my_file_word.close()