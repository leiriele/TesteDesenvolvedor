# Escreva um programa que inverta os caracteres de um string.
# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

frase = input('Digite uma frase: ')
invertida = ' '.join(palavra[::-1] for palavra in frase.split())
print('Frase invertida: {}'.format(invertida))

# outra forma
print('Outra forma')
txt = "Inverter String"[::-1]
print(txt)
