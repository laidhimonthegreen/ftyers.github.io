import sys
from nltk.tokenize import word_tokenize

#токенизация текста
def tokenizer(text):
    tokenized_text = []
    with open(text, "r") as f:
        for line in f:
            tokenized_text = tokenized_text + (word_tokenize(line))
    return (tokenized_text)


#составление словаря
freq_dict = {}
for slovo in tokenizer("text.txt"):
    # капитализация не важна ("Первый" и "первый" -- одно слово)
    slovo = slovo.lower()
    #проверяем, есть ли слово в словаре, обновляем "счетчик"
    if slovo in freq_dict:
        freq_dict[slovo] = freq_dict[slovo] + 1
    else:
        freq_dict[slovo] = 1

#составление упорядоченного словаря
freq = []

for w in freq_dict:
	freq.append((freq_dict[w], w))

freq.sort(reverse=True) #если значение false, то наименее частотные слова будут в начале

#записываем частотный словарь в файл
fd = open('freq.txt', 'w+')
for w in freq_dict:
    fd.write(str(freq_dict[w])+"\t"+w+"\n")
fd.close()

#функция-палиндром
def is_palindrome(s):
	"""Return True if the given string is a palindrome."""
	rev = ''
	if len(s) == 1:
		return False
	for j in range(1, len(s) + 1):
		rev = rev + s[-j]
	if s == rev:
		return True
	return False

#проверка на палиндромы
for i in freq:
	if is_palindrome(i[1]):
		print('%d\t%s' % (i[0], i[1]))