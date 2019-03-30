import sys

#создаём словарь вида: {слово: самая частая часть речи}

#разбиваем файл на списки нужного формата
def lines(model):
    lines_lists = []
    with open(model, "r") as f:
        for line in f.readlines():
            if line.strip():
                if not line.startswith("#"):
                    line_elements = (line.strip().split("\t"))
                    lines_lists.append(line_elements)
    return lines_lists

#находим самую частую часть речи
def get_most_common_tag(lines_lists):
    tags = []
    for i in lines_lists:
        if i[3] == "_" and i[2] != "_":
            tags.append(i)
    count = 0
    for tag in tags:
        if float(tag[0]) > count:
            count = float(tag[0])
            most_common_tag = tag[2]
    return most_common_tag

#составляем для каждого слова словарь вида {слово: самая вероятная для него часть речи}

#создаём список всех слов
def all_words(lines_lists):
    words = []
    for i in lines_lists:
        if i[3] != "_" or i[2] == "_":
            words.append(i[4])
    return (set(words))

#создаём словарь
def freq_dict(words, lines_lists):
    freq_dict = {}
    for word in words:
        #сначала просто все заполняем пустышкой
        freq_dict[word] = "no info"
        for line in lines_lists:
            number = 0
            if line[4] == word:
                if float(line[0]) > number:
                    number = float(line[0])
                    freq_dict[word] = line[2]
    return freq_dict


# анализируем полученный для разметки текст
def text_annotation(text, freq_dict, file_to_write, model):
    with open(text, "r") as f:
        annotated_text = ""
        for line in f.readlines():
            if line.strip() and not line.startswith("#"):
                list_line = line.strip().split("\t")
                if (list_line[2]) in freq_dict:
                    new_line = list_line[0:3] + [freq_dict[list_line[2]]] + list_line[4:]
                else:
                    new_line = list_line[0:3] + [get_most_common_tag(lines(model))] + list_line[4:]
                new_str_line = "\t".join(new_line)
                annotated_text += new_str_line + "\n"
            else:
                annotated_text += line.strip() + "\n"
    with open(file_to_write, "w") as f:
        f.write(annotated_text)

def final_function():
    try:
        text_annotation(sys.argv[1], freq_dict(all_words(lines(sys.argv[3])), lines(sys.argv[3])), sys.argv[2], sys.argv[3])
    #предупреждаем ошибку при запуске без аргумента
    except IndexError:
        print ("Запустите команду из командной строки и задайте файл ввода, файл вывода, модель")

final_function()