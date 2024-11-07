class CuentaInversionCetes:
    # Atributos
    __cantidadDinero = 0.0
    __aniosInversion = 0
    __tasaInteres = 0.0
    __montoAcumulado = 0.0
    __aporteExtra = 0.0

    def calcularMontoAcumulado(self, cantidadDinero, aniosInversion, tasaInteres, aporteExtra):
        self.__cantidadDinero = cantidadDinero
        self.__aniosInversion = aniosInversion
        self.__tasaInteres = tasaInteres
        self.__aporteExtra = aporteExtra
        tasaInteresMensual = 1 + ((self.__tasaInteres / 100) / 12)
        calculoMensual = self.__cantidadDinero
        totalanios = self.__aniosInversion + 1
        for a in range(1, totalanios,1):
            for i in range(1, 13, 1):
                calculoMensual *= tasaInteresMensual
                #print(f'Año: {a} mes: {i} Total: {calculoMensual}')
                calculoMensual += self.__cantidadDinero
            calculoMensual += self.__aporteExtra
        self.__montoAcumulado = calculoMensual
        return self.__montoAcumulado
    
if __name__ == "__main__":
    miCuenta = CuentaInversionCetes()
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
            aporteExtra = float(input("Introduce la cantidad de aporte extra: "))
            if aporteExtra > 0:
                break
            elif aporteExtra < 0:
                print("Vuelve a introducir un valor positivo")
        except ValueError as ve:
            print("Vuelve a introducir un valor numerico")
    
    while True:
        try:
            anios = int(input("Introduce la cantidad de años de inversion: "))
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

    montoAcumulado = round(miCuenta.calcularMontoAcumulado(dinero, anios, tasa, aporteExtra),2)
    print(f'El monto acumulado es: {montoAcumulado}')