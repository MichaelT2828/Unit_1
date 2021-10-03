def hbox1(word, n):
    times = 0
    for i in word:
        o = i.lower()
        if ord(o) - 96 == n:
            times += 1
    return times

def hbox2(a, b):
   number = a + b
   lst = ''
   for i in range(number):
       lst += chr(i+97)
   return lst

def hbox3(a, b):
    similar = ''
    if len(b) > len(a):
        b, a = a, b  # a is biggest

    for i in b:
        if i in a:
            similar += i
    return similar

print(hbox2(hbox1('asdghwsdsa', 1), hbox1('fdgffadffv', 6)))
print(hbox3(hbox2(hbox1('asdghwsdsa', 1), hbox1('fdgffadffv', 6)),hbox2(hbox1('asdjghjjkmn', 7), hbox1('qwertyuiii', 9))))