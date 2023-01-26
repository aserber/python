print("=======================")
print("Programa para saber si un numero es par o impar")
print("=======================")

nombre = input("Hola, escriba su nombre por favor: ")
print("Hola, " + nombre)

numero = int(input("Elija un numero por favor:"))

if (numero == 0):
        print("El numero 0 no es par ni impar")

elif (numero % 2 != 0):
        print("Su numero es", numero, "es impar")

else:
    print("Su numero es", numero, "es par")

print("Fin")


