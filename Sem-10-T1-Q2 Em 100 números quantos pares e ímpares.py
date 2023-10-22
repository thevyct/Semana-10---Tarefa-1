#Escreva um programa que leia o um conjunto de 100 números inteiros positivos e determine a quantidade de números pares e números ímpares contidos no mesmo.

pares = 0
impares = 0
for i in range(100):
    numero = int(input())
    if (numero % 2 ==0):
            pares = pares +1
    else: 
            impares = impares + 1

print(pares)
print(impares)