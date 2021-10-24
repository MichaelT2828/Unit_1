def encoder(key:int, msg:str):
    '''
    Caesar cypher (key specifies how much the alphabet is shifted to the right)
    :param key: The shift value of the cypher
    :param msg: The message that needs to be encoded
    :return: Secret message
    '''
    secret_msg = ''
    for letter in msg:
        code = ord(letter) + key
        if 64 < ord(letter) < 91: # if the letter is within the ascii range for upper case letters
            if code > 90: # if code is past 'z' reset from a
                code -= 26
        elif 96 < ord(letter) < 123: # if the letter is within the ascii range for lower case letters
            if code > 122:
                code -= 26
        encoded = chr(code)
        secret_msg += encoded
    return secret_msg

# You can subtract key-1 to 26 as key to reverse the encryption
# encoder(3, "A") will give "C"
# encoder(24, "C") will give "A"
# print(encoder(2, 'C'))
