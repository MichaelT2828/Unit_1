def hbox2(a, b):
   number = a + b
   lst = ''
   for i in range(number):
       lst += chr(i+97)
   return lst

print(hbox2(1, 7))