# Exercício 1:
# Calculadora Simples:
# Crie um programa que permita ao usuário realizar operações básicas de uma calculadora (adição, subtração, multiplicação, divisão)
# com dois números fornecidos como entrada.


class Calculadora():
    def __init__(self):

        self.valor1 = int(input("Informe o primeiro número:"))    
        self.operador = input("Informe o operador:")
        self.valor2 = int(input("Informe o segundo número:"))
        
        self.operadores = ["+", "-", "/", "*"]

        self.soma = self.valor1 + self.valor2
        self.subtracao = self.valor1 - self.valor2
        self.divisao = self.valor1 / self.valor2
        self.multiplicacao = self.valor1 * self.valor2


    def executa(self):
        

        if self.operador == self.operadores[0]:
            print("\nResultado: " + str(self.soma)+'\n')
        elif self.operador == self.operadores[1]:
            print("\nResultado: " + str(self.subtracao)+'\n')
        elif self.operador == self.operadores[2]:
            print("\nResultado: " + str(self.divisao)+'\n')
        elif self.operador == self.operadores[3]:
            print("\nResultado: " + str(self.multiplicacao)+'\n')
        else:
            print("Err")


calcula = Calculadora()
calcula.executa()