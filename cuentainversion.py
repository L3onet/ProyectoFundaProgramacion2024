class CuentaInversion:
    # Atributos
    __cantidadDinero = 0.0
    __aniosInversion = 0.0
    __tasaInteres = 0.0
    __montoAcumulado = 0.0

    # Metodos constructores

    # Metodos setter

    # Metodos getter

    def calcularMontoAcumulado(self, cantidadDinero, aniosInversion, tasaInteres):
        self.__cantidadDinero = cantidadDinero
        self.__aniosInversion = aniosInversion
        self.__tasaInteres = tasaInteres
        self.__montoAcumulado = self.__cantidadDinero * ((1 + self.__tasaInteres / 100) ** self.__aniosInversion)
        return self.__montoAcumulado

if __name__ == "__main__":
    miCuenta = CuentaInversion()
    cuentaJennifer = CuentaInversion()
    cuentaNery = CuentaInversion()
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
    
    while True:
        try:
            anios = float(input("Introduce la cantidad de años de inversion: "))
            if anios > 0:
                break
            elif anios == 0:
                print("Vuelve a introducir un valor mayor que 0")
            elif anios < 0:
                print("Vuelve a introducir un valor positivo")
        except ValueError as ve:
            print("Vuelve a introducir un valor numerico")
    while True:
        try:
            tasa = float(input("Introduce la tasa de interes: "))
            if tasa > 0:
                break
            elif tasa == 0:
                print("Vuelve a introducir un valor mayor que 0")
            elif tasa < 0:
                print("Vuelve a introducir un valor positivo")
        except ValueError as ve:
            print("Vuelve a introducir un valor numerico")
   
    print("El monto acumulado es: ", miCuenta.calcularMontoAcumulado(dinero, anios, tasa))

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
    
    while True:
        try:
            anios = float(input("Introduce la cantidad de años de inversion: "))
            if anios > 0:
                break
            elif anios == 0:
                print("Vuelve a introducir un valor mayor que 0")
            elif anios < 0:
                print("Vuelve a introducir un valor positivo")
        except ValueError as ve:
            print("Vuelve a introducir un valor numerico")
    while True:
        try:
            tasa = float(input("Introduce la tasa de interes: "))
            if tasa > 0:
                break
            elif tasa == 0:
                print("Vuelve a introducir un valor mayor que 0")
            elif tasa < 0:
                print("Vuelve a introducir un valor positivo")
        except ValueError as ve:
            print("Vuelve a introducir un valor numerico")
    
    print("El monto acumulado es: ", cuentaJennifer.calcularMontoAcumulado(dinero, anios, tasa))

