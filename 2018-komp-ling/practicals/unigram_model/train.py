import sys

columns = ["# P", "count", "tag", "form", "lemma"]

#основные категории
words = []
lemmas = []
tags = []

#создаём списки слов, лемм, тегов
with open("inpt.txt", "r", encoding="utf-8") as f:
    for i in f.readlines():
        if i.split():
            #избавляемся от строчек с send_id и text
            if len(i.split("\t"))>2:
                #добавляем словоформы из файла
                #все слова приводятся к нижнему регистру
                words.append(i.split("\t")[1].lower())
                #добавляем леммы из файла
                lemmas.append(i.split("\t")[2])
                #добавляем теги из файла
                tags.append(i.split("\t")[3])
                #общее количество слов
                total_tokens = len(words)

#создаём список формата [[слово1, лемма1, тег1],...[словоN, леммаN, тегN]]
words_lemmas_tags = []
c = 0
while c < len(lemmas):
    words_lemmas_tags.append([words[c], lemmas[c], tags[c]])
    c += 1

#функция, удаляющая из строки повторяющиеся элементы
def str_uniq(stroka):
    str_uniq = []
    for st in stroka:
        if st not in str_uniq:
            str_uniq.append(st)
    return (str_uniq)

#короткое название для уникальных наборов слово-форма-тег
trinuq = str_uniq(words_lemmas_tags)

#функция, которая считает количество тех или иных тегов для словоформы
def all_tag(word):
    all_tags = []
    freq = []
    for i in words_lemmas_tags:
        if word in i:
            all_tags.append(i[2])
    for i in str_uniq(all_tags):
        freq.append([i, all_tags.count(i)])
    #возвращаем количество тегов по отдельности и вместе
    return freq, len(all_tags)

#считаем P для словоформ
def P_word(word, tag):
    for i in all_tag(word)[0]:
        if i[0] == tag:
            return str(round(i[1]/all_tag(word)[1], 2))

#записываем таблицу
def table():
    try:
        f = open(sys.argv[1], 'w')
        #печатаем названия столбцов таблицы
        for column in columns:
            f.write (column + "\t")
        f.write ("\n")

        #печатаем данные для тегов
        for tag in str_uniq(tags):
            f.write(str(round(tags.count(tag)/total_tokens, 2)) + "\t" + str(tags.count(tag)) + "\t" + tag + "\t" + "_" + "\t" + "_" + "\t" + "\n")

        #печатаем данные для словоформ
        cnter = 0
        while cnter < len(trinuq):
            f.write (P_word(trinuq[cnter][0], trinuq[cnter][2]) + "\t" + str(words.count(trinuq[cnter][0])) + "\t" + trinuq[cnter][2]
                  + "\t" + trinuq[cnter][0] + "\t" + trinuq[cnter][1] + "\t" + "\n")
            cnter += 1
        f.close()

    #предупреждаем ошибку при запуске без аргумента
    except IndexError as e:
        print ("Запустите команду из командной строки и задайте аргумент-документ")

table()



