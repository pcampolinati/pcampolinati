#Criação de radar que aplique multa de acordo com nível: Leve/Grave/Gravíssimo

from time import sleep
from random import randint

print ('O veículo está se aproximando...')
sleep(5)
print ('O veículo passou no radar!')
sleep(2)
vmax = (80)
vveiculo = randint(65,120)
if vveiculo <= vmax:
  print(vveiculo,'Km/h! Você não levou Multa!')
elif vveiculo > vmax and vveiculo <= vmax + 10:
  print(vveiculo,'Km/h! Você levou Multa Leve!')
elif vveiculo > vmax + 10 and vveiculo <= vmax + 20:
  print(vveiculo,'Km/h!  Você levou Multa Grave!')
elif vveiculo > vmax +20:
  print(vveiculo,'Km/h! Você Levou Multa Gravíssima!')
