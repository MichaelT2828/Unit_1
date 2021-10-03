def hbox1(word, n):
    times = 0
    for i in word:
        o = i.lower()
        if ord(o) - 96 == n:
            times += 1
    return times

print(hbox1('jofaaa', 1))