from random import choice

import string

password = ''

characters = string.ascii_lowercase + string.ascii_uppercase + string.ascii_letters + string.digits + string.punctuation

size = int(input('Qual o tamanho da senha a ser gerada? '))

for i in range(size):
	password += choice(characters)

print(password)
