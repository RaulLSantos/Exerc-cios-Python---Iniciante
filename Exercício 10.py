'''
Crie um programa que determine se duas palavras fornecidas pelo usuário são anagramas uma da outra 
(ou seja, elas contêm exatamente as mesmas letras, mas em ordem diferente).
'''
import os
os.system('cls')

class Anagrama:
    def __init__(self):

        primeira_palavra = "Virginia"   #input("Informe a primeira palavra\n=> ")
        primeira_palavra = primeira_palavra.strip()
        primeira_palavra = primeira_palavra.lower()
        
        segunda_palavra =  "virginia"  #input("Informe a segunda palavra\n=> ")
        segunda_palavra = segunda_palavra.strip()
        segunda_palavra = segunda_palavra.lower()

        lista_segunda_palavra = list(segunda_palavra)
        # print(lista_segunda_palavra)

        valida_qtd_primeira_palavra = len(primeira_palavra)

        for letra in primeira_palavra:
            # print("Primeira: " + letra)
            
            for letrasegunda in lista_segunda_palavra:
                
                # print("Seg: " +letrasegunda)

                if letrasegunda == letra:
                    valida_qtd_primeira_palavra -= 1
                    lista_segunda_palavra.remove(letrasegunda)
                    print(valida_qtd_primeira_palavra)
                    
                    
        if valida_qtd_primeira_palavra == 0:
            print(f'''As palavras são Anagramas.\n
                {primeira_palavra}
                {segunda_palavra}
                 ''')
        else:
            print(f'''As palavras não são Anagramas.\n
                {primeira_palavra}
                {segunda_palavra}
                 ''')


a = Anagrama()