#calcular precio 
#preguntar la edad y mostrar el precio
#4> gratis
#4:18> 3.500
#18< 8.000
def calculo(entrada):
    mensaje = "Su entrada tiene un costo de: $"+str(entrada)
    return mensaje

def main():
    edad = int(input("Cuantos años tienes: "))

    if edad < 4:
        entrada = 0
        mensaje_1 = calculo(entrada)
        print(mensaje_1)  
    elif edad <18:
        entrada = 3500
        mensaje_2 = calculo(entrada)
        print(mensaje_2)
    else:
        entrada = 8000
        mensaje_3 = calculo(entrada)
        print(mensaje_3)
    
if __name__ == "__main__":
    main()
