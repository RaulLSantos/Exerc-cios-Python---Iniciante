'''Jogo da Forca:
    Implemente o jogo da forca, onde o jogador tem que adivinhar uma palavra oculta.4'''

class JogodaForca():
    def __init__(self):

        self.palavra = "PyTHon"
        self.palavra = self.palavra.lower()

        self.letras_corretas = tuple()

        for letra in self.palavra:
            if letra in self.palavra:
