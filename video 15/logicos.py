print("Elija un numero para comparar")

numero_uno = int(input("Elija un numero: "))

if numero_uno == 5 and numero_uno >= 5:
    print("El numero ", numero_uno, " es igual a 5 y es menor o igual a 5")

else:
    print("El numero ", numero_uno, " no es igual a 5 y no es menor o igual a 5")

if numero_uno >= 5 and numero_uno <= 10:
    print("El numero ", numero_uno, " es mayor o igual a 5 y menor o igual a 10")

else:
    print ("El numero ", numero_uno, " no es menor o igual 5 y no es mayor o igual a 10")

if numero_uno == 6 or numero_uno < 10:
    print ("El numero ", numero_uno, " es igual a 6 o menor que 10")
    
else:
    print("El numero ", numero_uno, " no es igual a 6 o menor o igual a 10")


