import random
import re
import forca

print("-----------------------------------------JOGO DA FORCA------------------------------------------")
#Algoritmo e passos
# 1. Gerar palavra aleatoria das que eu colocar na lista


listaPal = ["COMIDA FODA","EMPREGO BOM","STAR WARS","BLEACH","O PODEROSO CHEFAO","GHOSTBUSTERS","SOCIEDADE DO ANEL","MATRIX"]
letraCerta = []
letraErrada =[]
chances = 6
letrasFaltantes = 0
cont =0
forca.desenha_forca(chances)

palavra =listaPal[random.randint(0,len(listaPal)-1)]

# 2. Pedir uma letra maíuscula de A-Z
letra = input("Digite uma letra: ") #Pede uma letra para o usuário
f = re.search(r'[A-Z]',letra)#Verifica se a letra está em um padrão específico


while(len(letra) > 1 or bool(f) == False):#Enquanto o usuário digitar mais de 2 caracteres ou fora do padrão pedido,repete
    letra = input("Não está correto!!\nDigite uma letra Maíuscula[A-Z]: ")
    f = re.search(r'[A-Z]',letra)
    
letrasFaltantes = len(palavra.replace(" ",""))# Conta letras da palavra sem o espaço

while(chances != 0 or letrasFaltantes == 0):
    cont=0
    for t in palavra:#Faz busca na palavra em cada letra
        if t in letraCerta:#Se tem t nas letras que já foram certas
            print(t,end=" ")#Imprima
            continue#continue
        if(letra == t):#Se a letra for igual ao index
            cont +=1#Se passar desse if, conte a letra
            print(t,end=" ")
            letraCerta.append(t)

        elif(t == " "):
            print(t,end=" ")
            continue
        else:
            print("_",end=" ")
            letraErrada.append(t)
        print(cont)
    if(cont==0):
        chances -=1
        forca.desenha_forca(chances)
    if(letrasFaltantes==0):
        print("Parabéns!!!!! VOCÊ GANHOU !!!!!!!")
    print(cont)
    letra = input("\nDigite uma letra: ")
    

