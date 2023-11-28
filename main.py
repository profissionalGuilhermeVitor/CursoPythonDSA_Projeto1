import random
import re
import forca

print("-----------------------------------------JOGO DA FORCA------------------------------------------")
#Algoritmo e passos
# 1. Gerar palavra aleatoria das que eu colocar na lista


listaPal = ["COMIDA","EMPREGO","STAR WARS","BLEACH","O PODEROSO CHEFÃO","GHOSTBUSTERS"]
letraCerta = []
letraErrada =[]
chances = 6
letrasFaltantes = 0
forca.desenha_forca(chances)

palavra =listaPal[random.randint(0,len(listaPal)-1)]

# 2. Pedir uma letra maíuscula de A-Z
letra = input("Digite uma letra: ")
f = re.search(r'[A-Z]',letra)


while(len(letra) > 1 or bool(f) == False):
    letra = input("Não está correto!!\nDigite uma letra Maíuscula[A-Z]: ")
    f = re.search(r'[A-Z]',letra)

while(chances!=0 or letrasFaltantes !=0):
    letra = input("Digite uma letra: ")
    if(bool(f) and (letra in palavra)):
        letraCerta.append(letra)
        for i in palavra:
            if(i == letra):
                print(i,end="")
                if(letrasFaltantes!=0):
                    letrasFaltantes -=1
            else:
                print("_",end="")
                letrasFaltantes +=1
    else:
        letraErrada.append(letra)
        print("LETRA ERRADA!")
        chances -=1
        print("Faltam r'{chances}'")
        forca.desenha_forca(chances)


