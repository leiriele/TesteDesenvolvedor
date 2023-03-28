import json
import sys

with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

my_dict = {'total_faturamento': 0, 'dias': 0, 'media': 0.00, 'maior': 0.00, 'menor': sys.float_info.max}

for count_dias, data in enumerate(dados,1):
    my_dict['total_faturamento'] += data['valor']
    my_dict['dias'] = count_dias
    if data['valor'] > my_dict['maior']:
        my_dict['maior'] = data['valor']
    if 0 < data['valor'] < my_dict['menor']:
        my_dict['menor'] = data['valor']

my_dict['media'] = round(my_dict['total_faturamento'] / my_dict['dias'], 2)

print(my_dict)

