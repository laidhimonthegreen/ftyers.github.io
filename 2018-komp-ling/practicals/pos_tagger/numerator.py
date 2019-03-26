with open('freq_sorted.txt', 'r') as fd:
    with open ("ranks.txt", "w") as rank:
        counter = 1
        for n in fd.readlines():
            rank.write (str(counter) + "\t" + n)
            counter += 1
            print (n)
