def email_split(email):
    name = ''
    mail = ''
    digit = 0
    list = []
    for i in email:
        digit += 1
        if i in '@':
           mail = email[digit:]
           name = email[0:digit-1]
        fullname = name.replace('.', ' ')
        fullname1 = fullname.title()
    list.append(fullname1)
    list.append(mail)
    return list

print(email_split('john.doe@gmail.com'))

