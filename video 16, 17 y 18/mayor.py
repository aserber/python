print("=============================")
print("Programa para saber que numero es mayor")
print("=============================")

nombre = input("Hola, por favor ingrese su nombre: ")
print("Hola, " + nombre)

numero_uno = int(input("Elija el primer numero: "))
numero_dos = int(input("Elija el segundo numero: "))
numero_tres = int(input("Elija el tercer numero: "))

if (numero_uno > numero_dos and numero_uno > numero_tres):
    print("El ", numero_uno, "es mayor que el numero dos y el numero tres")

if (numero_dos > numero_uno and numero_dos > numero_tres):
    print("El ", numero_dos, "es mayor que el numero uno y el numero tres")

if (numero_tres > numero_uno and numero_tres > numero_dos):
    print("El ", numero_tres, "es mayor que el numero uno y el numero dos")

if (numero_uno == numero_dos and numero_uno == numero_tres and numero_dos == numero_tres):
    print("Los numeros son iguales")

if (numero_uno == numero_dos and numero_tres > numero_uno):
    print("El numero ", numero_tres, "es mayor al numero uno y numero dos")

if (numero_uno == numero_dos and numero_tres < numero_uno):
    print("los numeros ", numero_uno, "y ", numero_dos, "Son iguales y mayores que el numero dos")

if (numero_dos == numero_tres and numero_uno > numero_dos):
    print("El numero ", numero_uno, "Es mayor que el numero dos y tres")

if (numero_dos == numero_tres and numero_uno < numero_dos):
    print("los numeros ", numero_dos, "y ", numero_tres, "son iguales y mayores que el numero 1")

if (numero_tres == numero_uno and numero_dos > numero_uno):
    print("El numero ", numero_dos, "Es mayor que el numero uno y el numero tres")

if (numero_tres == numero_uno and numero_dos < numero_uno):
    print("El numero ", numero_uno, "y ", numero_tres, "Son iguales y mayores que el numero dos")

print("Fin")


    
    

