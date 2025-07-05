PI = 3.14
altura = float(input('Digite o valor da altura: '))
raio = float(input('Digite o valor do raio: '))

area_lateral = 2 * altura * raio
base = PI * raio ** 2
area_cilindro = area_lateral + base
quantidade_litros = area_cilindro / 3
quantidade_latas = quantidade_litros / 5
custo_total = quantidade_latas * 50

print(f'O custo total da pintura é R$ {custo_total:.2f}')
