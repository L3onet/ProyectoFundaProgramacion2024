class NumeroRomano:
    __numeroArabigo = 0
    __numeroRomano = ""
    __listaNumeros = [0, 0, 0, 0]
    __numeroRomanoValido = False

    def convertirNumeroArabigoARomano(self, numero):
        self.__numeroArabigo = numero
        """
        10 // 1000 = 0
        """
        self.__listaNumeros[0] = self.__numeroArabigo // 1000
        resto = self.__numeroArabigo % 1000
        self.__listaNumeros[1] = resto // 100
        resto = resto % 100
        self.__listaNumeros[2] = resto // 10
        resto = resto % 10
        self.__listaNumeros[3] = resto // 1
        return self.__listaNumeros


if __name__ == "__main__":
    numeroRomano = NumeroRomano()
    numero = numeroRomano.convertirNumeroArabigoARomano(7645)
    print(numero)