'''
Soma dos Números Pares:
    Escreva um programa que calcule a soma de todos os números pares em uma lista fornecida pelo usuário.
'''
import os
import random

os.system('cls')

class SomaNumerosPares:
    def __init__(self):
        
        self.input_by_user = list([1,3,5,6,78,52,47,69,33,26,14,11,28])

        self.numeros_pares = list()
        
        self.soma = 0

        for numero in self.input_by_user:
            if numero % 2 == 0:
                self.numeros_pares.append(numero)
                self.soma += numero
        print(f'''\t\tNúmeros pares: {self.numeros_pares}
                A soma deles é: {self.soma}\n''')

a = SomaNumerosPares()

