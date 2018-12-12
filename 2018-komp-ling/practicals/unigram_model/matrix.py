import sys

rus = ['бы', 'вас', 'видит', 'всего', 'вы']
eng = ['a', 'absorbed', 'all', 'and', 'another']

m = {}

for w1 in rus:
	if w1 not in m:
		m[w1] = {}
	for w2 in eng:
		m[w1][w2] = 0

print (m)

print('\t' + '\t'.join(eng))
for w1 in m:
    print('%s\t' % (w1), end='')
    for w2 in m[w1]:
        print('%d\t' % (m[w1][w2]), end='')
    print('')





"""
#здесь были попытки создать матрицу, которая проставляет единицы, а не только нули
#пока что они были безуспешны, но может быть, что-то улучшится в будущем
rus, eng = [], []

with open("rus_eng_tagor.txt", "r", encoding="utf-8") as f:
    for i in f.readlines():
        if i:
            #добавляем словоформы из файла
            rus.append(i.split("\t")[0])
            #добавляем словоформы из файла
            eng.append(i.strip("\n").split("\t")[1])


def bag_sentence(sentences):
    sentences2 = []
    for i in sentences:
        sentences2.append(i.lower().split())
    sentences3 = []
    for i in sentences2:
        i2 = []
        for word in i:
            clword = word.strip(".,–")
            if clword:
                i2.append(clword)
        if i2:
            sentences3.append(i2)
    return sentences3

bag_rus = (bag_sentence(rus))
bag_eng = (bag_sentence(eng))

dict = {}
i = 0
while i < len(bag_rus):
    for slovo in bag_rus[i]:
        if slovo not in dict:
            dict[slovo] = bag_eng[i]
    i += 1

print (dict)
"""
