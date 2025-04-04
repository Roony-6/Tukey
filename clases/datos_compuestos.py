'''
Listas:
 lista=[]
 

e=["a",[1,2,3],4,]
print(len(e), e)
print(e[1])

lista_enteros=[1,6,9,7,6,8,6,7,8]
print(max(lista_enteros))

#slice (rangos)

print(lista_enteros[2:6]) #imprime desde la posicion 2 de la lista hasta la 5 intervalo [)
print(lista_enteros[2:]) #imprime desde el elemento de la posicion 2 hasta el ultimo

#suma de listas

l3=[]
l3.append(5)
print(l3)
l3=l3.append(4)


l1=["do"]
l2=["mi"]
l3=["re"]
l4=["si"]

list1=l1+l2+l3
list2=l3+l2
list1[2]=l1[0]
list1.append(l3[0])
print(list1)
 
list2[0]=l4[0]
list2[1]=l3[0]
list2=None
list2=[l4[0],l3[0],l4[0],l1[0]]
print(list2)
'''

#list
#split
#sort 
#reverse
edades=['18','18','21','19','19']
edades.sort()
print(edades)