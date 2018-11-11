import sys

#транслитератор
def transliteraptor (text):
	#составляем словарь для транслитерации
	cyr_lat = {}

	with open("alphabet", "r") as a:
		for line in a:
			k, n = line.split("\t")
			cyr_lat[k.strip()] = n.strip()
			#работаем с заглавными буквами
			if len(n.strip()) == 1:
				cyr_lat[k.upper().strip()] = n.upper().strip()
			if len (n.strip()) > 1:
				cyr_lat[k.upper().strip()] = n.strip().capitalize()

	#записываем текст
	tekst = ""
	with open(text, "r") as f:
		for line in f:
			for a in line:
				letters = [cyr_lat[a] if a in cyr_lat else a for a in line]
				line = ("".join(letters))
			tekst = tekst + "\n" + line
	with open("translite_text", "w") as t:
		t.write(tekst)


transliteraptor("game")