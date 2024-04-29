# Exercício 2:
# Verificador de Palíndromo:
# Escreva um programa que verifique se uma palavra fornecida pelo usuário é um palíndromo (ou seja, ela permanece a mesma 
# se lida de trás para frente).



class Palindromo():
    def __init__(self):

        self.palavra = str(input("Digite uma palavra: "))
        self.palavra = self.palavra.strip()
        self.palavra = self.palavra.replace(" ","")
        print(self.palavra)

        self.inverte = self.palavra[::-1]
        self.inverte = self.inverte.strip()
        self.inverte = self.inverte.replace(" ", "")
        print (self.inverte)

        if self.inverte == self.palavra:
            print("igual")
        else:
            print("errado")
        



a = Palindromo()

