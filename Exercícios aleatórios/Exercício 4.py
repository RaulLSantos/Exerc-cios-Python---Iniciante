# Exercício 4:
# Conversor de Temperatura:
# Escreva um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
import os
os.system('cls')

class ConvertTemperature:
    def __init__(self):

        self.validatefromTemp = False
        while not self.validatefromTemp:
            self.fromTemp = input(str("Informe a Temperatura que deseja converter: \n 1 - Celsius\n 2 - Fahrenheit\n 3 - Kelvin \n R: "))
            try:
                self.fromTemp = int(self.fromTemp)
                if self.fromTemp == 1 or self.fromTemp == 2 or self.fromTemp == 3:
                    self.validatefromTemp = True
                    if self.fromTemp == 1:
                        self.celsius = 1
                        self.fahrenheit = None
                        self.kelvin = None
                    elif self.fromTemp == 2:
                        self.fahrenheit = 2
                        self.celsius = None
                        self.kelvin = None
                    else:
                        self.kelvin = 3
                        self.celsius = None
                        self.fahrenheit = None

                else:
                    print("Digite um valor válido\n\n")
            except:
                print("Deve ser um valor válido\n\n")

        self.quantidade = input(str("Quantos graus?\n R: "))

        self.validatetoTemp = False
        while not self.validatetoTemp:
            self.toTemp = input(str("Para qual Temperatura deseja converter? \n 1 - Celsius\n 2 - Fahrenheit\n 3 - Kelvin \n R: "))
            try:
                self.toTemp = int(self.toTemp)
                if self.toTemp == 1 or self.toTemp == 2 or self.toTemp == 3:
                    self.validatetoTemp = True
                    if self.toTemp == 1:
                        self.celsius = 1
                    elif self.toTemp == 2:
                        self.fahrenheit = 2
                    else:
                        self.kelvin = 3
                else:
                    print("Digite um valor válido")
            except:
                print("Deve ser um valor válido")
            

    def convertCelsiusToFahrenheit(self):
        # F = 1,8C + 32
        self.multiplicadorfahrenheit = (1.8)
        self.quantidade = float(self.quantidade)
        self.fahrenheit = (self.multiplicadorfahrenheit * self.quantidade)
        
        self.fahrenheit = self.fahrenheit + 32
        
        print("\n\n Celsius convertido para Fahrenheit: " + str(round(self.fahrenheit,2)) +" F\n\n")
    
    def convertCelsiusToKelvin(self):
        # K = C + 273

        self.quantidade = int(self.quantidade)
        self.kelvin = self.quantidade + 273
        print("\n\n Celsius convertido para Kelvin: " + str(round(self.kelvin,2)) +" K\n\n")
    
    def convertFahrenheitToCelsius(self):
        # Ex.: Converta 95°F para a escala Celsius:
        # C=95−32/1,8
        self.divisorfahrenheit = (1.8)
        self.celsius = int(self.quantidade) - 32
        self.celsius = float(self.celsius) / self.divisorfahrenheit
        print("\n\n Fahrenheit convertido para Celsius: " + str(round(self.celsius,2)) +" ºC\n\n")

    def convertFahrenheitToKelvin(self):
        # K = (°F + 459.67) × 5/9

        self.kelvin = float(self.quantidade) + (459.69)
        self.kelvin = ((self.kelvin * 5)/ 9)
        
        print("\n\n Fahrenheit convertido para Kelvin: " + str(round(self.kelvin,2)) +" K\n\n")

    def convertKelvinToCelsius(self):
        # C = K - 273,15
        
        self.celsius = float(self.quantidade) - (273.15)
        print("\n\n Kelvin convertido para Celsius: " + str(round(self.celsius,2)) +" ºC\n\n")

    def convertKelvinToFahrenheit(self):
       # °F = (K − 273) × 1.8 + 32
    
        self.fahrenheit = int(self.quantidade) - 273
        self.fahrenheit = (float(self.fahrenheit) * (1.8)) + 32
        
        print("\n\n Kelvin convertido para Fahrenheit: " + str(round(self.fahrenheit,2)) +" F\n\n")



    def verificaConversao(self):

        if self.fromTemp == self.celsius and self.toTemp == self.fahrenheit:
            self.convertCelsiusToFahrenheit()
        elif self.fromTemp == self.celsius and self.toTemp == self.kelvin:
            self.convertCelsiusToKelvin()
        elif self.fromTemp == self.fahrenheit and self.toTemp == self.celsius:
            self.convertFahrenheitToCelsius()
        elif self.fromTemp == self.fahrenheit and self.toTemp == self.kelvin:
            self.convertFahrenheitToKelvin()
        elif self.fromTemp == self.kelvin and self.toTemp == self.celsius:
            self.convertKelvinToCelsius()
        elif self.fromTemp == self.kelvin and self.toTemp == self.fahrenheit:
            self.convertKelvinToFahrenheit()
        else:
            print("aaaa")

 


convert = ConvertTemperature()
convert.verificaConversao()