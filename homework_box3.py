def hbox3(a, b):
    similar = ''
    if len(b) > len(a):
        b, a = a, b #a is biggest

    for i in b:
        if i in a:
            similar += i
    return similar

print(hbox3('abcdefgh', 'abcdefg'))