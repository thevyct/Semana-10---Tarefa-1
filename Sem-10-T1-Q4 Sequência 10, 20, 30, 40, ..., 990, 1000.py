#Escreva um programa que gere a seguinte sequência: 10, 20, 30, 40, ..., 990, 1000. Considere a separação dos números por vírgula seguido de espaço em brando e o pontos no final da sequência.

sequencia = ''
for i in range(10 , 1010, 10):
    sequencia += str(i) + ',' + ' '  
sequencia = sequencia.strip()
sequencia = sequencia[:-1]
print(f'{sequencia}.')