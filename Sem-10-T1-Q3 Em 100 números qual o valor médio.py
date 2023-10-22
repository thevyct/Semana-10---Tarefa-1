#Escreva um programa que leia um conjunto de 100 números inteiros e exiba o valor médio dos mesmos (com duas casas decimais).

valor = 0
for i in range(100):
    numeros = int(input())
    valor = numeros + valor
media = (valor / 100)
print(f'{media:.2f}')