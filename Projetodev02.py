#Crie um programa que recebe um número e imprime o fatorial daquele número;


numero = int(input('Digite um número: '))
if numero > 0:
  fatorial=1
  for item in range(1,numero + 1):
    fatorial = fatorial * item
  print(fatorial)


