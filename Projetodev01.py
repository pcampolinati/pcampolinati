#Escreva um programa que, ao iniciar gera um valor aletório de 1 a 10.
# Permita que o usuario chute um número até que o valor aleatório gerado no inicio do programa seja chutad corretamente.
# O programa deve informar se o chute foi acima, abaixo ou igual ao valor aletório gerado no inicio do programa.

import random

numero_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
  palpite_usuario = int(input('Escolha um número de 1 a 10: '))
  if palpite_usuario < numero_aleatorio:
    print('O seu palpite é Menor que o Número! Tente Novamente! ')
  elif palpite_usuario > numero_aleatorio:
    print(' O seu palpite é Maior que o Número! Tente Novamente!')
  elif palpite_usuario == numero_aleatorio:
    acertou = True
    print(' Parabéns! Você acertou o seu palpite!')
  