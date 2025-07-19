#Variáveis
valor_produto = float(input('Informe o valor do produto: '))
desconto = float(input('Informe o percentual de desconto: '))
#Funções e Métodos

#Processamento
valor_desconto = (valor_produto * desconto / 100)
valor_final = (valor_produto - valor_desconto)

#Visualização
print(f'Valor do produto com o desconto: R$ {valor_final:.2f}')







