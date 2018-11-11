from nltk.tokenize import word_tokenize

#разбивает текст на слова
def tokenizer(text):
	with open(text, "r") as f:
		for line in f:
			print (word_tokenize(line))

tokenizer("game")