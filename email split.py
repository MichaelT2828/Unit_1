def email_split(email):
    name = ''
    mail = ''
    digit = 0
    list = []
    for i in email: #goes through each character of email
        digit += 1
        if i in '@': #checks each character if its "@", if it is:
           mail = email[digit:] #mail becomes the everything after the "@", using index of digit
           name = email[0:digit-1] #name becomes everything before "@"
        fullname = name.replace('.', ' ') #replace the . in between the name with a space
        fullname1 = fullname.title() #replace the first letter in each word with capital
    list.append(fullname1)
    list.append(mail) #add fullname and mail into a list, so you can return them both at once
    return list

print(email_split('john.doe@gmail.com')) #need to print John Doe and gmail.com

