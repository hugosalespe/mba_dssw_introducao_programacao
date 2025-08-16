from datetime import datetime

hora = int(datetime.now().timestamp())


with open('ling_prog.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Eu amo programar em Python!\n')
    arquivo.write('Eu amo programar em PySpark!\n')
    arquivo.write('Eu amo programar em SQL!\n')
