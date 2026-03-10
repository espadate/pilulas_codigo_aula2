import math
#leituras
assinante = int(input('Digite quantidade de assinantes atuais: '))
mensalidade = float(input('Digite valor da mensalidade: '))
taxa = float(input('Digite a taxa de crescimento mensal %: '))
meses = int(input('Digite a quantidade de meses da projeção: '))
#processamento
assinantes_finais = assinante * math.pow((1 + taxa/100), meses)
receita_final = assinantes_finais * mensalidade
#saída
print(f'Assinantes estimados: {assinantes_finais:.0f}')
print(f'Receita estimada: R$ {receita_final:.2f}')