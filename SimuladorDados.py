import random
import time

print('-=-' * 20)
print('BEM VINDO AO SIMULADOR DE DADO!!')
print("DADOS: \n1 = (d4) \n2 = (d6) \n3 = (d8) \n4 = (d10 unidade) \n5 = (d10 dezena) \n6 = (d100) \n7 = (d12) \n8 = (d20)")

escolha_dado = int(input("Qual o dado você quer? "))
quant = int(input('Quantidade de dados? '))

dados = [4, 6, 8, 10, 0, 100, 12, 20]

def escolhaDado(num):
    print('Rodando o dado...')
    if num == 5:
        time.sleep(2)
        print(random.randrange(0, 100, 10) * quant)
    else:
        time.sleep(2)
        print(random.randrange(dados[num - 1]) * quant)

escolhaDado(escolha_dado)

print('FIM DO SIMULADOR!')
print('-=-' * 20)