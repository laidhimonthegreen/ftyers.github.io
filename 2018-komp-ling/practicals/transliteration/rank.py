import sys

freq_dict = []

#извлечение слов и значений частоты из файла
fd = open('freq.txt', 'r')
for line in fd.readlines():
     f, w = line.split('\t')
     freq_dict.append((int(f), w.strip()))
fd.close()

#cортировка
freq_dict.sort(reverse=True)

#запись в новый файл отсортированного словаря
fd = open('freq_sorted.txt', 'w+')
for w in freq_dict:
    f, w = (list(w))
    fd.write(str(f) + "\t" + str(w) + "\n")
fd.close()