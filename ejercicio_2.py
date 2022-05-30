#escribe una funcion que calcule el
#area de un circulo y
#otra que calcule el volumen de un cilindro usando la primera funcion
def calculo(area, altura):
    sol = "Su area es: "+str(area)+" cm^2 y su altura es: "+str(altura)+" cm^3"
    return sol
def main():
    
    radio = float(input("Ingrese un radio en cm: "))
    altura = float(input("Escriba una altura en cm: "))
    pi = 3.14
    calculo_area = pi*(radio**2)
    calculo_volumen = calculo_area*altura

    sol_a = calculo(calculo_area, calculo_volumen)
    print(sol_a)
    
if __name__ == "__main__":
    main()