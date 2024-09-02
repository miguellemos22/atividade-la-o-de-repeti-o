import os 
import time
os.system("cls || clear ")

numero = 10
contador = 0
while True:
    for i in range(1):
        fator = int(input("digite um numero: "))
        multiplicacao = numero * fator
        contador += 1

    if multiplicacao > 100:
        break

print(f"produto final: {multiplicacao}")
print(f"contador: {contador}")  
    