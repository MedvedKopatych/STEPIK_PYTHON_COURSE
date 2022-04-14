import simplecrypt


with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open("passwords.txt", "r") as pss:
    pss_lst = pss.readlines()
    for password in pss_lst:
        password = password[:-1]
        print(password)
        try:
            print(simplecrypt.decrypt(password, encrypted).decode('utf8'))

        except simplecrypt.DecryptionException:
            print(password, 'is wrong')

        else:
            print(password, 'is correct')

import simplecrypt
import urllib.request as urllib

passwords = urllib.urlopen('https://stepik.org/media/attachments/lesson/24466/passwords.txt')

with open('encrypted.bin', 'rb') as inp:
    encrypted = inp.read()

for password in passwords:
    password = password[:-1]
    try:
        print(simplecrypt.decrypt(password, encrypted).decode('utf8'))
    except simplecrypt.DecryptionException:
        print(password, 'is wrong')
    else:
        print(password, 'is correct')

