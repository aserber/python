num_uno = 10
if num_uno == 5:
    print("El numero es ", num_uno)

print("fin")

# ----------- Condicional if - else

nombre = input("Cual es tu nombre? ")
print("Hola " + nombre)

numero_uno = int(input("Por favor introduce tu calificacion en matematica: "))
numero_dos = int(input("Por favor introduce tu calificacion en ingles: "))
numero_tres = int(input("Por favor introduce tu calificacion en lengua: "))

promedio = int(numero_uno + numero_dos + numero_tres) / 3
promedio = int(promedio)

if (promedio >= 7):
    print ("Felicitaciones, ", nombre ," aprobaste", " con un promedio de ", promedio)

else:
    print("ha - ha")


# ----------- Condicional if - else con numeros decimales

nombre = input("Cual es tu nombre? ")
print("Hola " + nombre)

numero_uno = float(input("Por favor introduce tu calificacion en matematica: "))
numero_dos = float(input("Por favor introduce tu calificacion en ingles: "))
numero_tres = float(input("Por favor introduce tu calificacion en lengua: "))

promedio = float(numero_uno + numero_dos + numero_tres) / 3
promedio = float(promedio)

if (promedio >= 7):
    print ("Felicitaciones, ", nombre ," aprobaste", " con un promedio sin redondear de ", float(promedio))
    print ("Felicitaciones, ", nombre ," aprobaste", " con un promedio de ", float(round(promedio,2)))

else:
    print("ha - ha,  tu promedio sin redondear es de ", float(promedio))
    print("ha - ha,  tu promedio es de ", float(round(promedio,2)))
    

    
