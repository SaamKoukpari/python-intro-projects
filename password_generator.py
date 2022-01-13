import random

print('Password Generator!')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number = input('Number of passwords to generate: ')
number = int(number)

length = input('Password length: ')
length = int(length)

print('\nYour password list: ')

for pwd in range(number):
  passwords = ''
  for c in range(length):
    passwords += random.choice(chars)
print(passwords)
