


import xrenner

x = xrenner.Xrenner(model = "/home/laidhimonthegreen/udpipe/src/UD_Russian-SynTagRus/xrenner/xrenner/models/rus")

"""
#Часть один, про Новую Зеландию
res = x.analyze('example_in.conll10', "html")
#записываем результаты в html
open('coref.html', 'w+').write(res)
"""

#Часть два, про Пушкина.
res = x.analyze('pushkin.conllu', "html")
open('coref_pushkin.html', 'w+').write(res)
