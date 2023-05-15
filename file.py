## IMPORTANT NO FUNCIONA AMB CARACTERS LLETRES AMB TILDE 
import re
f = open("a.txt","r")
opcions = ["1. Per caracter","2. Per lletres"]

def menu():
    for o in opcions:
        print(f"{o}\n")





def per_caracter():
    paraula = {}
    for x in f:
        sin_p = re.sub(r'[^\w\s]','',x)
        for y in sin_p:
            if(y != ' ' and y != '\n'):
                if(existeix(y,paraula)):
                    paraula[y] += 1
                else:
                    paraula[y] = 1
    print(paraula)
    crear_arxiu(paraula)
                

def per_paraula():
    paraula = {}
    aux = ""
    for x in f:
        print(x)
        sin_p = re.sub(r'[^\w\s]','',x)
        

        for y in sin_p:
            if y != ' ' and y != '\n':
                aux += y
            else:
                    if(existeix(aux,paraula)):
                        paraula[aux] += 1
                        aux = ""
                    else:
                        paraula[aux] = 1
                        aux = ""
                    
                #print(paraula)
    #Al final pot no tenir espai
    if(existeix(aux,paraula)):
        paraula[aux] += 1
        aux = ""
    else:
        paraula[aux] = 1
        aux = ""
    
    crear_arxiu(paraula)

    print(paraula)
def main():

    menu()
    x = int(input())
    if x == 1:
        per_caracter()
    elif x == 2:
        per_paraula()

def crear_arxiu(paraula):
    w = open("output.txt", "w")
    
    for x in paraula:
        w.write("Paraula: {} Vegades: {}\n".format(x,paraula[x]))
    w.close()

def existeix(comparar,paraula):
    for x in paraula.keys():
        if(comparar == x): return True
    return False

main()