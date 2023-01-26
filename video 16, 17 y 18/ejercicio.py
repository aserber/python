print("============================")
print("Menú de opciones")
print("============================ \n")

nombre = str(input("Ingrese su nombre: "))
print("Hola, " + nombre)


print("Selecciona una opcion")
print("Ingrese su clave de trabajador, si eres de atencion al cliente elige 1, si eres de logistica ingrese 2, si eres de gerencia elige 3")

opcion = int(input("Que opcion quieres?: "))


if (opcion == 1):
    print("Eres de atencion al cliente")

    opcion_uno = int(input("Cuantos años llevas trabajando? "))
    
    if (opcion_uno == 1):
            print("Tienes 6 dias de vacaciones")

    if (opcion_uno >= 2 and opcion_uno <= 6):
            print("Tienes 14 dias de vacaciones")
            
    if (opcion_uno >= 7):
            print("Tienes 20 dias de vacaciones")

    if (opcion_uno == 0 or opcion_uno <= 0):
        print("No tienes vacaciones, fin.")
                     

elif (opcion == 2):
    print("Eres de Logistica")

    opcion_dos = int(input("Cuantos años llevas trabajando?: "))
    

    if (opcion_dos == 1):
            print("Tienes 7 dias de vacaciones")

    if (opcion_dos >= 2 and opcion_dos <= 6):
            print("Tienes 15 dias de vacaciones")

    if (opcion_dos >= 7):
            print("Tienes 22 dias de vacaciones")

    if (opcion_dos == 0 or opcion_dos <= 0):
        print("No tienes vacaciones, fin.")

elif (opcion == 3):
    print("Eres de gerencia")

    opcion_tres = int(input("Cuantos años llevas trabajando?: "))


    if (opcion_tres == 1):
            print("Tienes 10 dias de vacaciones")

    if (opcion_tres >= 2 and opcion_tres <= 6):
            print("Tienes 20 dias de vacacopmes")

    if (opcion_tres >= 7):
            print("Tienes 30 dias de vacaciones")

    if (opcion_tres == 0 or opcion_tres <= 0):
        print("No tienes vacaciones, fin.")

else: 
        print("Numero incorrecto")

print("Fin")





