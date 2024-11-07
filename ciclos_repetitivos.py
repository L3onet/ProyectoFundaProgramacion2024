dinero = 0.0
while True:
    try:
        dinero = float(input("Introduce la cantidad de dinero: "))
        if dinero > 0:
            break
        elif dinero == 0:
            print("Vuelve a introducir un valor mayor que 0")
        elif dinero < 0:
            print("Vuelve a introducir un valor positivo")
    except ValueError as ve:
        print("Vuelve a introducir un valor numerico")
    
    

print("La cantidad de dinero es: ", dinero)