#  Esse codigo foi feito em janeiro de 2020 qdo comecei a estudar programacao!


#  -- coding: utf-8 --
# '''
# 1. Considere um input do usuário como sendo o valor base para o cálculo, 
# sobre esse valor aplique um desconto de 10%, e como saída deverá apresentar o 
# valor final com desconto em duas diferentes formatações de moeda - REAL e DOLAR.'''

# import requests
# import json
# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR')

# def leiadinheiro(msg):
#     valido = False
#     while not False:
#         entrada = str(input(msg)).strip()
#         if entrada.isalpha() or entrada == "":
#             print('\033[0;31mErro: Valor inválido!\033[m')
      
#         else:
#             válido = True
#             return float(entrada)

# valor = leiadinheiro('Informe um valor em real para calculo: R$ ')

# requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
# cotacao = json.loads(requisicao.text)
# cot = float(cotacao['USD']['high'])

# valor_com_desconto_real = valor - (valor * 10 / 100)
# valor_com_desconto_dolar = (valor / cot) - (valor / cot) * 10 / 100

# print('-' * 40)
# print('A cotação do dólar no momento é ' + locale.currency(cot, grouping=True))
# print('O valor com desconto em real é ' + locale.currency(valor_com_desconto_real, grouping=True))
# print('O valor com desconto em dólar é $ {:,.2f}'.format(valor_com_desconto_dolar))
# print('-' * 40)


# Esse codigo foi feito em Julho 2021, depois de estudar os APIs

'''
1. Considere um input do usuário como sendo o valor base para o cálculo, 
sobre esse valor aplique um desconto de 10%, e como saída deverá apresentar o 
valor final com desconto em duas diferentes formatações de moeda - REAL e DOLAR.'''

import requests

def leiadinheiro(msg):
    valido = False
    while not False:
        entrada = str(input(msg)).strip()
        if entrada.isalpha() or entrada == "":
            print('\033[0;31mErro: Valor inválido!\033[m')

        else:
            válido = True
            return float(entrada)


valor = leiadinheiro('Informe um valor em real para calculo: R$ ')

requisicao = requests.get('https://api.exchangerate-api.com/v6/latest')
cotacao = requisicao.json()
cot = cotacao['rates']['BRL']

valor_com_desconto_real = valor - (valor * 10 / 100)
valor_com_desconto_dolar = (valor / cot) - (valor / cot) * 10 / 100

print('-' * 40)
print(f'A cotação do dólar no momento é US$ {cot}')
print(f'O valor com desconto em real é {valor_com_desconto_real}')
print(f'O valor com desconto em dólar é $ {valor_com_desconto_dolar:.2f}')
print('-' * 40)
