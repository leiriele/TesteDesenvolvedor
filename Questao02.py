def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2) 
    
n = int(input('Qual termo deseja encontrar? '))
lista = [(fibonacci(i)) for i in range(0,n+1)] 
print('Sequencia Fibonacci: ', lista)

if n in lista:
    print(n, 'Pertence a sequência de Fibonacci')
else:
    print(n, 'Não pertence a sequência de Fibonacci')