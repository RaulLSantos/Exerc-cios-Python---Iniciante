# Fatorial de um Número:
#     Escreva uma função para calcular o fatorial de um número fornecido pelo usuário.
# n! = n . (n – 1)
import os
os.system('cls')


def main():

    numero = input(str("Informe um número: "))
    numero = int(numero)
    limite = numero
    multiplicador = None

    for i in range(1, (numero+1)):
        
        if limite == numero:
            multiplicador = numero
            numero = numero - 1
        else:
            multiplicador = (multiplicador * numero)
            numero = numero - 1

    print(multiplicador)
        
    

    
main()


