import forcaPOO
import re
import random
#Crie uma classe para o jogo de forca:
class Forca:
    #O construtor (__init__) dessa classe pode inicializar variáveis como a palavra a ser adivinhada, as letras corretas, as letras erradas e o número de tentativas restantes.
    #Defina métodos na classe:
    def __init__(self,palavra,letrasCor,letrasErr,chances):
        self.palavra = palavra
        self.letrasCor = letrasCor
        self.letrasErr = letrasErr
        self.chances = chances
#mostrar_palavra: Este método deve exibir a palavra oculta, mostrando as letras adivinhadas e substituindo as não adivinhadas por "_".
    def mostrar_palavra(self):
        palOculta = [i if  i in letrasCor or i == " " else "_" for i in self.palavra]
        for i in palOculta:
            if i == " ":
                print(" ",end=" ")
            else:
                print(i,end=" ")
            
#tentativa: Este método deve processar a tentativa do jogador, verificando se a letra está na palavra a ser adivinhada e atualizando as letras corretas ou erradas.
    def tentativa(self,letra):
        if letra in self.palavra:
            letrasCor.append(letra)
            
        else:
            letrasErr.append(letra)
            self.chances -=1
            forcaPOO.printForca(self.chances)
            

#jogo_terminado: Este método deve verificar se o jogo terminou, ou seja, se o jogador adivinhou todas as letras ou excedeu o número máximo de tentativas.
    def jogo_terminado(self):
        for i in self.palavra:
            if i in letrasCor:  
                continue
            else:
                if i == " ":
                    continue
                return False               
        return True

#Implemente a lógica do jogo:

letrasCor = []
letrasErr = []
chances = 6
palavras = [
    "1984",
    "NEUROMANCER",
    "FUNDACAO",
    "DUNA",
    "BLADE RUNNER",
    "FAHRENHEIT 451",
    "O GUIA DO MOCHILEIRO DAS GALAXIAS",
    "O TEMPO DESPEDACADO",
    "UMA DOBRA NO TEMPO",
    "A MAQUINA DO TEMPO",
    "O HOMEM DO CASTELO ALTO",
    "A CANTICLE FOR LEIBOWITZ",
    "SNOW CRASH",
    "ENDER'S GAME",
    "O FINITO NUMERO DE MUNDOS",
    "O MUNDO ASSOMBRADO PELOS DEMONIOS",
    "O HOMEM BICENTENARIO",
    "O HITCHHIKER'S GUIDE TO THE GALAXY",
    "RAGTIME",
    "THE WAR OF THE WORLDS",
    "READY PLAYER ONE",
    "THE MARTIAN",
    "STARSHIP TROOPERS",
    "O JOGO DO EXTERMINADOR",
    "THE LEFT HAND OF DARKNESS",
    "Rendezvous with Rama",
    "FOUNDATION AND EMPIRE"
]
if __name__=="__main__":
    palavra = palavras[random.randint(0,len(palavras)-1)]
    palavra = palavra.upper()
    f1 = Forca(palavra,letrasCor,letrasErr,chances)
    f1.mostrar_palavra()
    letra = input("\nDigite uma letra:")

    while(not(bool(re.search(r'[A-Z0-9]',letra)))):
        letra = input("\nDigite uma letra:")

    f1.tentativa(letra)
    f1.mostrar_palavra()
    print("\nLetras Corretas" , letrasCor)
    print("\nLetras Erradas" , letrasErr)

    while(chances ==0 or not(f1.jogo_terminado())):
        letra = input("\nDigite uma letra:")
        while(not(bool(re.search(r'[A-Z0-9]',letra)))):
            letra = input("\nDigite uma letra:")
        if letra in letrasCor:
            continue
        f1.tentativa(letra)
        print("\nLetras Corretas", letrasCor)
        print("\nLetras Erradas", letrasErr)
        f1.mostrar_palavra()

        if f1.jogo_terminado():
            print("PARABÉNS!!!!")
            break