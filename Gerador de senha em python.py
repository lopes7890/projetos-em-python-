#gerador de senha em python
import string
from random import random, choice

valores = string.ascii_letters
valores += string.digits
valores += string.punctuation
tamanho = 5
senha = ''

for i in range(tamanho):
    senha += choice(valores)

print(senha)
