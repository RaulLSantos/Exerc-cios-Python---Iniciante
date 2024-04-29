# Jogo da Forca:
#     Implemente o clássico jogo da forca, onde o jogador tem que adivinhar uma palavra oculta, uma letra de cada vez.
import os
os.system('cls')

class JogoDaForca:
    def __init__(self):

        # Pede a palavra
        self.palavra = input("Qual é a palavra?\nR: ").upper()

        # Conta a quantidade de caracteres na palavra informada
        self.quantidade_caracteres_palavra = len(self.palavra)
        
        # Constante que define a quantidade de tentativas
        self.TENTATIVAS_LIMITE = 6

        # Variável que recebe o valor da Constante de tentativas limite e 
        # grava as tentativas efetuadas, diminuindo a cada erro
        self.tentativas_efetuadas = self.TENTATIVAS_LIMITE

        # Variável para guardar as letras acertadas durante as tentativas
        self.letras_corretas = []
        

        while True:
            # Pede a palavra
            self.letra = input(str("Digite uma letra: ")).upper()
          
            # Valida se o valor informado para a variável letra contém apenas 1 caracter
            if len(self.letra) > 1:
                print("Digite apenas uma letra!")
                continue
            # Valida se o valor informado para a variável letra contém qualquer caracter
            elif len(self.letra) <= 0:
                continue

            # Se a quantidade de tentativa efetuada for maior que zero e menor que as tentativas limite, entra na condicional. 
            # Se não, para
            if self.tentativas_efetuadas > 0 and self.tentativas_efetuadas <= self.TENTATIVAS_LIMITE:
                
                # se a letra informada estiver dentro da palavra, entrão entra na condicional
                if (self.letra.upper()) in (self.palavra.upper()):
                    
                    print(f"\nAcertou a letra {self.letra.upper()}\n")
                    
                    # Variável para apresentar as letras de acordo com os acertos
                    self.palavra_mostrada = ""

                    # Adiciona as letras acertadas a lista
                    self.letras_corretas.append(self.letra.upper())

                    # Aqui é descontado da variável de quantidade de caracteres na palavra a quantidade 
                    # de letras encontradas dentro da palavra                      
                    self.quantidade_caracteres_palavra -= self.palavra.count(self.letra)

                    # Passa por todas as letras da palavra. Caso exista a letra informada na lista letras_corretas
                    # então é adicionado a letra à variável palavra_mostrada.
                    # Se a letra não estiver na lista letras_corretas então é adicionado o caracter "_"
                    for self.letra in self.palavra:
                        if (self.letra.upper()) in (self.letras_corretas):
                            self.palavra_mostrada += self.letra + " "
                        else:
                            self.palavra_mostrada += "_ "
                    print(self.palavra_mostrada + "\n\n")

                    
                    # Caso a quantidade de caracteres da palavra zere, significa que o usuário
                    # acertou todas as letras contidas na palavra.
                    if self.quantidade_caracteres_palavra == 0:
                        print(f"\nPARABÉNS! A palavra era {self.palavra.upper()}\n")
                        break
                    

                else:
                    # Se o usuário errou a letra, será descontado da quantidade de tentativas efetuadas
                    self.tentativas_efetuadas -= 1

                    # Variável para apresentar as letras de acordo com os acertos
                    self.palavra_mostrada = ""

                    # Passa por todas as letras da palavra. Caso exista a letra informada na lista letras_corretas
                    # então é adicionado a letra à variável palavra_mostrada.
                    # Se a letra não estiver na lista letras_corretas então é adicionado o caracter "_"
                    for self.letra in self.palavra:
                        if (self.letra.upper()) in (self.letras_corretas):
                            self.palavra_mostrada += self.letra + " "
                        else:
                            self.palavra_mostrada += "_ "
                    

                    # Se a quantidade de tentativas efetuadas chegar a zero, interrompe a execução
                    if self.tentativas_efetuadas == 0:
                        print("\nQue pena! Você perdeu!\n")
                        break
                    
                    # Informa ao usuário caso a quantidade de tentativas seja igual a 1
                    # Se não, informa a quantidade de tentativas restantes e a variável palavra_mostrada
                    print(f"\n\n\nATENÇÃO! É sua última tentativa.\n\n" if self.tentativas_efetuadas == 1 else f"\nTente novamente.\nTentativas restantes {self.tentativas_efetuadas}\n{self.palavra_mostrada}\n")
     
            else:              
                break
            
                
a = JogoDaForca()

