# Exercício 3:
# Contador de Vogais:
#     Faça um programa que conte o número de vogais em uma string fornecida pelo usuário.
import os
os.system('cls')

def VerificaVogais(c):
    vogais = "aeiou"
    if (c in vogais):
        return True
    else:
        return False
    

def contavogal(s):
    s = s.lower()
    soma = 0
    for c in s:
        if VerificaVogais(c) == True:
            soma += 1
    print(soma)
    return soma
    

contavogal("Olá, quero vogais")
    
    



            


