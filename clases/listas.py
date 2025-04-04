list=[1,2,3,4,5,6,7,8,9,10]
print(list[0])
#range(1,10)
def Range(inicio,fin):
    if inicio< fin:
        print(inicio, end= ' ')
        Range(inicio + 1, fin)
    else:
        print('\n')
Range(1,10)

def recorrer_lista(lista, index):
    if index < len(lista):
        print(lista[index], end=' ')
        recorrer_lista(lista,index + 1)
    else:
        print('\n')
recorrer_lista(list,0)

cadena= 'hola'

def recorrer_cadena(cadena, index):
    if index < len(cadena):
        print(cadena[index], end=' ')
        recorrer_lista(cadena,index + 1)
    else:
        print('\n')
recorrer_lista(cadena,0)

#def mi_break(lista,valor_detener,index):
   # if index < len(lista):
        #if lista []
       # return 

num=[]
def cuentareg(lista,index):
    if index > -(len(lista)+1) :
        print(lista[index], end = ' ')
        cuentareg(lista, index -1)
    else:
        print("Despeje...")
        print('\n') 
lista = [1,2,3,4,5] 
cuentareg(lista,-1)

nombre_ordenados= []
generos_ordenados=[]
edades_ordenados=[]
enfermedades_ordenadas = []

def encuentra_indice(edades_actuales, edad_menor,index):
    if index < len (edades_actuales):
        

        
    
