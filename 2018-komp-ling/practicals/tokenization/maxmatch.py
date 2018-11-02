#для работы с алгоритмом нужно передать ему следующие параметры:
#wordlist -- последовательность слов языка, которые ищутся в предложениях
#seq -- анализируемая последовательность слов без разделителей



def max_match(seq, wordlist):
    if not seq:
        return []
    # поиск самого длинного слова из существующих в словаре
    for i in range(len(seq) - 1, -1, -1):
        first_word = (seq[0:i + 1])
        remainder = seq[i + 1:len(seq)]
        print (remainder)
        if first_word in wordlist:
            return [first_word] + max_match(remainder, wordlist)

    # если слово не найдено, создается однобуквенное слово
    first_word = seq[0]
    remainder = seq[1:len(seq)]

    return [first_word] + max_match(remainder, wordlist)

"""
простейший пример работы: 

max_match("xaaababbbaa", ["aaa", "aa", "bab", "b", "x"])
"""



"""
построчный вывод алгоритма maxmatch для файла со списком предложений
wordlist -- уже сформированный словарь

with open("sentences200.txt", "r", encoding="utf-8") as f:
    for l in f.readlines():
        l = max_match(l.strip(), wordlist)
        print (l)
"""



