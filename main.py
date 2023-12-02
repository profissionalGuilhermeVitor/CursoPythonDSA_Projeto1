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
for i in palavra:#Imprimir espaços de palavra
    if(i == " "):
        print(" ",end=" ")
    else:
        print("_",end=" ")
    
# 2. Pedir uma letra maíuscula de A-Z
letra = input("\nDigite uma letra: ") #Pede uma letra para o usuário
f = re.search(r'[A-Z]',letra)#Verifica se a letra está em um padrão específico


while(len(letra) > 1 or bool(f) == False):#Enquanto o usuário digitar mais de 2 caracteres ou fora do padrão pedido,repete
    letra = input("Não está correto!!\nDigite uma letra Maíuscula[A-Z]: ")
    f = re.search(r'[A-Z]',letra)
    
letrasFaltantes = len(palavra.replace(" ",""))# Conta letras da palavra sem o espaço

while(chances != 0 or letrasFaltantes == 0):
    while(len(letra) > 1 or bool(f) == False):#Enquanto o usuário digitar mais de 2 caracteres ou fora do padrão pedido,repete
        letra = input("Não está correto!!\nDigite uma letra Maíuscula[A-Z]: ")
        f = re.search(r'[A-Z]',letra)
    cont=0
    for t in palavra:#Faz busca na palavra em cada letra
        if(letra == t):#Se a letra for igual ao index
            cont +=1#Se passar desse if, conte a letra
            print(t,end=" ")#Imprime a letra
            if(t in letraCerta):# Se a letra repetir
                print(t,end=" ")#Imprime a letra
                continue
            else:#Se não adicione a letra nas certas
                letraCerta.append(t)
        elif(t == " "):
            print(" ", end=" ")
        else:
            if(t in letraCerta):
                print(t,end=" ")#Imprime a letra
                continue
            else:
                print("_",end=" ")
    print("\nLetras Certas",letraCerta)
    if(cont ==0):#Caso chegue o final da busca e não tiver a letra
        chances -=1
        forca.desenha_forca(chances)
        letraErrada.append(letra)
        print("Você errou!!\nChances: {}".format(chances))
        print("Letras Erradas: ",letraErrada)
        
    else:
        letrasFaltantes -= cont
        if(letrasFaltantes==0):
            print("PARABÉNS!!!!")
            break
    letra = input("\nDigite uma letra: ")
    
