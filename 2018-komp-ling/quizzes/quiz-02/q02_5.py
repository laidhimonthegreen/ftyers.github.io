while True:
    a = input()
    if a.isalpha():
        if a.endswith(("ch", "sh", "tz", "s", "x")):
            print (a+"es")
        else:
            print (a+"s")