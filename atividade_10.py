from random import randint

import time

numero_oculto = randint(1, 100)
parada = True

while parada:

    meu_numero = int(input('Digite um número entre 1 e 100:'))

    if meu_numero == numero_oculto:
        print('Parabéns, você acertou')
        parada = False

    elif meu_numero < numero_oculto:
        print('Seu número é MENOR')

    elif meu_numero > numero_oculto:
        print('Seu número é MAIOR')

    time.sleep(1)

print('Programa encerrado')



