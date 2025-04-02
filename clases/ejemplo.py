contraseña=input("dame una contraseña: ")

if(len(contraseña)>=8 and contraseña.isalnum()):
    print("todo piola")
    
else:
    print("no valido")
    

nombre=input("dame un nombre").upper()
nombre2=input("dame otro nombre").upper()

if(nombre==nombre2):
    print("nombre iguales")
else:
    print("nombres no iguales")
    
texto="aabcdef"
print(texto.count("a"))