'''Jogo da Forca:
    Implemente o jogo da forca, onde o jogador tem que adivinhar uma palavra oculta.'''
import os
os.system('cls')

class JogodaForca():
    def __init__(self):
        self.palavra = "Python"
        self.tamanho_palavra = len(self.palavra)
        
        

        self.LIMITE = 3
        self.tentativas = 1
        self.letra_correta = []
        
        while True:
            
            
            self.palavra_mostrada = ""
            if self.tentativas >= 1 and self.tentativas <= self.LIMITE:
                self.letra = input(str("\nDigite uma palavra: "))
                if self.letra.lower() in self.palavra.lower():
                    self.letra_correta += self.letra.lower()
                    self.tamanho_palavra -= 1
                    print(f"\n Acertou! Letra: {self.letra} \n")
                    if self.tamanho_palavra == 0:
                        print(f"\n Parabéns, a palavra era {self.palavra.upper()}\n\n")
                        break
                    
                else:
                    self.tentativas += 1
                    print(f"\n Infelizmente você errou \n")

            else: 
                print("\nVocê chegou ao limite de suas tentativas!\n")
                break

            for self.letra in self.palavra.lower():
                if self.letra in self.letra_correta:
                    self.palavra_mostrada += self.letra
                else:
                    self.palavra_mostrada += "_"
            print("\n" + self.palavra_mostrada)
              
jogo_da_forca = JogodaForca()
