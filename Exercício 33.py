#Exercício 33 (Recebe entrada de 3 números e informa o maior e menor)
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
maior = max(n1, n2, n3)
menor = min(n1, n2, n3)
print('O maior número é {}' .format(maior))
print('O maior número é {}' .format(menor))