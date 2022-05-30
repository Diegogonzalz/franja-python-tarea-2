#preguntar al usuario por una frase y una letra,
#y mostrar por pantalla el numero de veces que aparece la letra en la frase 

def main():
    
    frase = input("Ingrese un texto: ")
    letra = input("Escriba una letra: ") 
    contador = 0
    for i in frase:
        if i in letra:
            contador += 1
    print("Esta frase tiene: "+str(contador)+" letras")
    
if __name__ == "__main__":
    main()