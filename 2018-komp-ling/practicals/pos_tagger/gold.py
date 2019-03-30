
#разметка файла на списки
def lines(text):
    lines_lists = []
    with open(text, "r") as f:
        for line in f.readlines():
            if line.strip():
                if not line.startswith("#"):
                    line_elements = (line.strip().split("\t"))
                    lines_lists.append(line_elements)
    return lines_lists

def match(gold, annotated):
    count_all = 0
    count_true = 0
    for i, line in enumerate(lines(gold)):
        count_all += 1
        if line[3] == lines(annotated)[i][3]:
            count_true +=1
    return (count_true/count_all)

print (match("standard.txt", "annotated.txt"))

