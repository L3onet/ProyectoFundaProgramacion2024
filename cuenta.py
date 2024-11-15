dinero = float(input("Introduce la cantidad de dinero: "))
anios = float(input("Introduce la cantidad de años de inversion: "))
tasa = float(input("Introduce la tasa de interes: "))

montoAcumulado = dinero * ((1 + tasa / 100) ** anios)
print("El monto acumulado es: ", montoAcumulado)

class CuentaInversion:
    # Precondiciones + Postcondiciones de los casos de uso
    # Atributos: Encapsulación
    __dinero = 0.0
    __anios = 0
    __tasa = 0.0
    __montoAcumulado = 0.0

    # Metodos: 1 metodo por cada caso de uso
    # def nombreCasoUso(self, parametros (precondiciones separadas con ',')):
    def calcularMontoAcumulado(self, dinero, anios, tasa):
        self.__dinero = dinero
        self.__anios = anios
        self.__tasa = tasa
        self.__montoAcumulado = self.__dinero * ((1 + self.__tasa / 100) ** self.__anios)
        return self.__montoAcumulado
