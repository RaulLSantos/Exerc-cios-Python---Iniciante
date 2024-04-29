'''
Gerador de Números Primos:
    Crie uma função que gere os primeiros n números primos.
'''
import os
import random
os.system('cls')

class GeraNumerosPrimos:
    def __init__(self):
        
        self.pede_numero_limite = int(input("Até qual número deseja que seja gerado os números pares?\n=> "))

        self.armazena_pares = list()

        for numero in range(0,self.pede_numero_limite):
            if numero % 2 == 0:
                self.armazena_pares.append(numero)
        print(f"Os números primos gerados até o número limite informado são: {self.armazena_pares}")

a = GeraNumerosPrimos()