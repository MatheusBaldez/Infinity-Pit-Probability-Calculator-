#The mesuares are meant to be in meters.

import math
print('Infinity Pit Probability Calculator')
qtd = int(input('\nType how many probabilities you are going to calculate: '))
for i in range(qtd):
    print('\nProbability ', i+1)
    
    l = float(input("\nType the lenght of the Infinity Pit without the power of 10: "))
    ul = int(input(f'{l}x10^'))
    l = l*10**ul
    print(f'\nThe value of L is: {l}m')
    
    n = int(input('\nType the value of n: '))
    
    a = float(input("\nType the value of the end A without the power of 10: "))
    ua = int(input(f'{a}x10^'))
    a = a*10**ua
    print(f'\nThe value of A is: {a}m')
    
    b = float(input("\nType the value of the end B without the power of 10: "))
    ub = int(input(f'{b}x10^'))
    b = b*10**ub
    print(f'\nThe value of B is: {b}m')
    
    p = (1/l)*((b-a)-(l/(2*n*math.pi))*(math.sin(2*n*math.pi*b/l)-math.sin(2*n*math.pi*a/l)))
    
    print("\nThe probability's value is': ",f'{p:.5f}')