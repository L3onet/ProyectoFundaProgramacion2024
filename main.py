# Sintaxis básica

# Identación

if 5 > 2:
    print("cinco es mayor que dos")
    if 7 > 3:
        print("Siete es mayor que tres")

# Comentarios de una linea
'''
Comentarios de
varias lineas en
Python
'''

# Atributos (variables) --- Tipos de datos
# Python utiliza un tipado dinámico
catetoOpuesto = 12   # tipos de datos enteros
catetoAdyacente = 14.3   # Tipo de datos de punto flotante o reales
mensaje = "Hola mundo"   # Tipo de dato Cadena de caracteres
esValido = True          # Tipo de dato booleano
esValido = "Verdadero"   # Tipo de dato cadena de caracteres
hipotenusa = catetoOpuesto * catetoAdyacente

# Operadores de asignacion

c = 10
c += 5   # c = c + 5
c -= 5   # c = c - 5
c *= 5   # c = c * 5
c /= 5   # c = c / 5
c %= 5   # c = c % 5
c //= 5  # c = c // 5
c **= 5  # c = c ** 5

contador = 1
contador += 3

'''
Jerarquía de operadores

1. Parentesis ( )
2. Exponenciación **
3. Multiplicación * y la división /, %, //
4. Suma + y resta -
5. ==, !=, <, >, <=, >=
6. not
7. and
8. or
9. =, +=, -=, *=, /=
'''

'''
Nombres de los atributos

1. No usar espacios en blanco en los nombres
2. Se recomienda usar la notación camello (Camel Case) --> esValidoHacerEsto
3. Pueden usar los guiones bajos --> es_valido_hacer_esto
4. No iniciar con un número

Encapsulación de los atributos

1. públicos     ----> base
2. protegidos   ----> _base
3. privados     ----> __base

Asignación multiple

a, b, c = 5, 10, 15
a = b = c = 0
'''


'''
Desplazamiento

3      ---->    011
3 << 1 ---->    110
'''

'''
Estructuras de control

Selectivas

if .. else
if .. else if .. else

if condicion:
    # codigo si se cumple la condicion
else:
    # codigo si no se cumple la condicion

    >, <, >=, <=, ==, !=, and, or, not
'''
edad = int(input("Escribe tu edad: "))

# Convertir tipos de datos

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

if edad < 2:
    print("Eres un bebe")
elif edad >= 2 and edad <= 12:
    print("Eres un niño")
elif edad > 12 and edad <= 16:
    print("Eres un adolescente")
elif edad > 16 and edad < 24:
    print("Eres un jove")
elif edad >= 24 and edad < 60:
    print("Eres un adulto")
elif edad >=60:
    print("Eres un adulto mayor")