#calcule o percentual de representação que cada estado teve dentro 
#do valor total mensal da distribuidora
# dict dicionario
faturamentos = dict([('SP', 67836.43),('RJ', 36678.66),('MG', 29229.88),('ES', 27165.48),('Outros',  19849.53)])

def percentual(faturamentos):
    totalMensal = 0.00
    percentuais = []

    for i in faturamentos.values():
        totalMensal += i

    for i in faturamentos.values():
        percentuais.append(i*100/totalMensal)

    j = 0
    for i in faturamentos.keys():
        print(i, f'{percentuais[j]:.02f}','%')
        j += 1

percentual(faturamentos)