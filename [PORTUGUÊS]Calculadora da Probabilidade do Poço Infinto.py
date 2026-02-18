#As medidas são exigidas em metros.

import math
print('Calculadora de probabilidades do Poço Infinito')
qtd = int(input('\nDigite a quantidade de probabilidades que deseja calcular: '))
for i in range(qtd):
    print('\nProbabilidade ', i+1)
    
    l = float(input("\nDigite o comprimento do Poço Infinito sem potência de 10: "))
    ul = int(input(f'{l}x10^'))
    l = l*10**ul
    print(f'\nO valor de L é: {l}m')
    
    n = int(input('\nDigite o valor de n: '))
    
    a = float(input("\nDigite o valor da extremidade A sem potência de 10: "))
    ua = int(input(f'{a}x10^'))
    a = a*10**ua
    print(f'\nO valor de A é: {a}m')
    
    b = float(input("\nDigite o valor da extremidade B sem potência de 10: "))
    ub = int(input(f'{b}x10^'))
    b = b*10**ub
    print(f'\nO valor de B é: {b}m')
    
    p = (1/l)*((b-a)-(l/(2*n*math.pi))*(math.sin(2*n*math.pi*b/l)-math.sin(2*n*math.pi*a/l)))
    
    print("\nO valor da probabilidade é: ",f'{p:.5f}')