import numbers
import random

print('Password Generator Intialised')

passChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!£$%&@?\/#'

passQuan = input('Number of Passwords to Generate: ')
passQuan = int(passQuan)

passLength = input('Please Specify Password Length: ')
passLength = int(passLength)

print('\nPasswords Generated: ')

for pwd in range(passQuan):
    passwords = ''
    for c in range(passLength):
        passwords += random.choice(passChars)
    print(passwords)
