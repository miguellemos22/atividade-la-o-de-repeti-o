import os 
import time
os.system("cls || clear ")

orcamento = 1200
soma = 0
contador = 0
while True:
     for i in range(1):
          gasto = float(input("digite um valor"))
          contador += 1

          soma = gasto + soma    

          if soma > orcamento:
            break