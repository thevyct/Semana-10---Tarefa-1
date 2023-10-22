#Escreva um programa que leia um conjunto de 100 números inteiros positivos e determine o maior deles.

nota_melhor = 0

for i in range(100):
    nota = int(input())
    if nota > nota_melhor:
        nota_melhor = nota

print(nota_melhor)