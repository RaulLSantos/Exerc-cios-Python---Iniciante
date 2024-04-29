'''
Classificador de Triângulos:
Escreva um programa que classifique um triângulo (equilátero, isósceles ou escaleno) com base nos comprimentos de seus lados fornecidos pelo usuário.
'''

# Escaleno "as medidas dos lados são todas diferentes"
# Isósceles é quando possui pelo menos dois lados congruentes, ou seja, com a mesma medida.
# Equilátero é quando possui os três lados com as mesmas medidas
import os
os.system('cls')


class ValidaTiposDeTriangulo:
    def __init__(self):

        self.medidas_digitadas = 1
        self.medidas = list()

        while True:
            if self.medidas_digitadas <= 3:
                if self.medidas_digitadas == 1:
                    self.solicita_medidas = input("Informe a primeira medida do seu triângulo para ver qual seu tipo.\n=> ")
                elif self.medidas_digitadas == 2:
                    self.solicita_medidas = input("Informe a segunda medida do seu triângulo para ver qual seu tipo.\n=> ")
                elif self.medidas_digitadas == 3:
                    self.solicita_medidas = input("Informe a terceira medida do seu triângulo para ver qual seu tipo.\n=> ")
            
                self.medidas.append(self.solicita_medidas)
                self.medidas_digitadas += 1
            else:
                break

        
        if self.medidas[0] != self.medidas[1] and self.medidas[0] != self.medidas[2] and self.medidas[1] != self.medidas[2]:
            print(f'''
                Suas medidas são todas diferentes. {self.medidas}
                Portanto, seu triângulo é o Escaleno
                  ''')
        elif self.medidas[0] == self.medidas[1] and self.medidas[0] == self.medidas[1] and self.medidas[1] == self.medidas[2]:
            print(f'''
                Suas medidas possui todos os lados iguais. {self.medidas}
                Portanto, seu triângulo é o Equilátero
                  ''')
        elif self.medidas[0] == self.medidas[1] or self.medidas[0] == self.medidas[2] or self.medidas[1] == self.medidas[2]:
            print(f'''
                Suas medidas possui dois lados iguais. {self.medidas}
                Portanto, seu triângulo é o Isósceles
                  ''')
        
        else:
            print("Failed")
        

a = ValidaTiposDeTriangulo()



