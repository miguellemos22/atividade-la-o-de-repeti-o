import os 
import time
os.system("cls || clear ")

numero_negativo = 0

while True:
    numero = float(input("digte um numero:"))

    if numero > 0:
        break
numero_negativo += 1

print(f"quantidade de nemros negativos: {numero_negativo}")