print("Elige los numeros a comparar")

primer_numero = int(input("Introduce el primer numero: "))
segundo_numero = int(input("Introduce el segundo numero: "))

print("Los numeros a comprar son el ", primer_numero, " y el ", segundo_numero)


if primer_numero == segundo_numero:
    print("Los numeros son iguales")

if primer_numero != segundo_numero:
    print("los numeros no son iguales")

if primer_numero < segundo_numero:
    print("El primer numero es menor")

if primer_numero > segundo_numero:
    print ("El primer numero es mayor")

if primer_numero <= segundo_numero:
    print("el primer numero es menor o igual al segundo")
    
if primer_numero >= segundo_numero:
    print("El primer numero es mayor o igual")
